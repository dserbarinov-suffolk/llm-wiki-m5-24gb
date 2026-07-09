"""End-to-end operation tests: real store + domain, fake/absent LLM.

Ingest is the claim-ledger-first flow: a source page is a deterministic
projection of the source's ledger, so it runs with no model. Query, lint, and
claim-support still drive the real WorkflowRunner with a scripted fake client.
"""

import json

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import ToolCall

from llmwiki.config import WikiPaths
from llmwiki.domain.claim_support import ClaimSupportCandidate, ClaimSupportSelection
from llmwiki.domain.objects import IngestRun, QueryRun
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-06-10"


def _session(store: WikiStore, script: list, paths: WikiPaths) -> Session:
    return Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="test-run",
    )


def _wiki_page(
    page_id: str,
    page_kind: str,
    summary: str,
    page_body: str,
    *,
    updated: str = TODAY,
) -> WikiPage:
    return WikiPage.from_metadata(
        PageMetadata(page_id=page_id, page_kind=page_kind, summary=summary, updated=updated),
        page_body,
    )


_WIDGETS_MD = """# Widget Protocol

A widget contains three slots.

A widget contains a name.

The handler must validate every request.

```python
def add(a, b):
    return a + b
```

Glossary of core terminology plus notation.
"""


@pytest.fixture
def source(paths: WikiPaths) -> str:
    (paths.raw_dir / "widgets.md").write_text(_WIDGETS_MD, encoding="utf-8")
    return "widgets.md"


def _ledger(store: WikiStore, source_locator: str) -> dict:
    text = store.read_claim_ledger_artifact(source_locator)
    assert text is not None
    return json.loads(text)["ledger"]


def _page_containing(store: WikiStore, text: str, required_text: str = "") -> str:
    for page_id in store.list_pages():
        body = store.read_page(page_id)
        if text in body and (not required_text or required_text in body):
            return body
    raise AssertionError(f"No page contains {text!r}.")


class TestIngest:
    async def test_markdown_ingest_projects_source_page_from_ledger(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        result = await _session(store, [], paths).ingest(source)

        assert "Claim-ledger ingest" in result.output
        assert "[[widgets]]" in result.output
        body = store.read_page("widgets")
        assert "## Page Families" in body
        assert "## Concept Entry Points" in body
        assert "A widget contains three slots." not in body
        section_body = _page_containing(
            store, "A widget contains three slots.", "page_family: topic-concept"
        )
        assert "## Statements" in section_body
        assert "(widgets.md document)" in section_body  # source-facing citation label
        assert isinstance(result.run, IngestRun)
        log = paths.log_path.read_text(encoding="utf-8")
        assert f"## [{TODAY}] ingest | widgets.md" in log
        assert "- [[widgets]]" in store.read_index()

    async def test_deontic_sentence_becomes_rule_atom_not_duplicate_claim(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        await _session(store, [], paths).ingest(source)
        ledger = _ledger(store, source)
        atom_kinds = {atom["technical_atom_kind"] for atom in ledger["technical_atoms"]}
        assert "rule" in atom_kinds
        assert "code-block" in atom_kinds
        # The deontic sentence is preserved once, by the rule atom — not also as
        # a standalone claim.
        rule_texts = [
            atom["payload"]["rule_text"]
            for atom in ledger["technical_atoms"]
            if atom["technical_atom_kind"] == "rule"
        ]
        assert any("must validate every request" in text for text in rule_texts)
        claim_statements = [
            entry["normalized_text"]
            for entry in ledger["entries"]
            if entry["ledger_entry_kind"] in ("claim", "event")
        ]
        assert not any("must validate every request" in text for text in claim_statements)

    async def test_fragmentary_statement_routed_to_review_not_asserted(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        await _session(store, [], paths).ingest(source)
        body = store.read_page("widgets")
        review_index = body.index("## Source review")
        fragment = "Glossary of core terminology"
        # The verbless fragment appears under review, never as an asserted claim.
        assert fragment in body[review_index:]
        assert fragment not in body[:review_index]

    async def test_page_body_has_no_internal_ids(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        await _session(store, [], paths).ingest(source)
        body = store.read_page("widgets")
        for prefix in ("ledger-entry-", "projection-coverage-entry-", "atom-candidate-"):
            assert prefix not in body
        # The coverage pointer lives in metadata, not the visible body.
        assert "projection_coverage:" in body.split("---")[1]

    async def test_ledger_artifacts_and_evidence_registry_written(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        await _session(store, [], paths).ingest(source)
        artifact_dir = store.page_plan_artifact_dir(source)
        ledger_dir = artifact_dir / "ledger"
        for name in (
            "claim-ledger.json",
            "document-structure.json",
            "projection-coverage.json",
            "ledger-quality-report.json",
            "projection-quality-report.json",
            "quality-check-catalog.json",
            "portable-artifact-set.json",
            "proposed-change-review.json",
            "assertion-graph.json",
            "topic-states.json",
            "page-projections.json",
            "ingestion-trace.json",
        ):
            assert (ledger_dir / name).is_file(), name
        for retired_name in (
            "projection-context.json",
            "section-plan.json",
            "knowledge-shapes.json",
            "topics.json",
        ):
            assert not (ledger_dir / retired_name).exists(), retired_name
        # The evidence registry remains the prior link in the authority chain.
        assert (artifact_dir / "evidence-registry.json").is_file()
        manifest = json.loads((ledger_dir / "portable-artifact-set.json").read_text())
        kinds = {member["portable_artifact_kind"] for member in manifest["members"]}
        assert "claim-ledger-artifact" in kinds
        assert "document-structure-artifact" in kinds
        assert "proposed-change-review-artifact" in kinds
        assert "assertion-graph-artifact" in kinds
        assert "topic-state-artifact" in kinds
        assert "page-projection-artifact" in kinds
        assert "ingestion-trace-artifact" in kinds
        assert "portable-artifact-set" not in kinds
        assert "projection-context-artifact" not in kinds
        assert "section-grounded-plan-artifact" not in kinds
        assert "knowledge-shape-catalog-artifact" not in kinds
        trace = json.loads((ledger_dir / "ingestion-trace.json").read_text())
        stage_ids = {stage["stage_id"] for stage in trace["stages"]}
        assert {"topic-state", "page-projection", "graph-export"} <= stage_ids

    async def test_ledger_artifact_write_replaces_stale_files(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        ledger_dir = store.page_plan_artifact_dir(source) / "ledger"
        ledger_dir.mkdir(parents=True, exist_ok=True)
        (ledger_dir / "projection-context.json").write_text("stale", encoding="utf-8")

        await _session(store, [], paths).ingest(source)

        assert not (ledger_dir / "projection-context.json").exists()
        assert (ledger_dir / "page-projections.json").is_file()

    async def test_claim_ledger_references_document_structure_and_has_entries(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        await _session(store, [], paths).ingest(source)
        artifact = json.loads(
            (store.page_plan_artifact_dir(source) / "ledger" / "claim-ledger.json").read_text()
        )
        pointer = artifact["document_structure_pointer"]
        assert pointer["target_artifact_kind"] == "document-structure-artifact"
        assert pointer["target_artifact_id"]
        assert artifact["ledger"]["entries"]


class TestClaimSupport:
    async def test_claim_support_records_verdict_and_files_report(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            _wiki_page(
                "javascriptallonge-value-types",
                "concept",
                "Value type notes.",
                "Same-type cups can still be distinguished. (raw/javascriptallonge.pdf p.22)",
            )
        )
        candidate = ClaimSupportCandidate(
            candidate_id="claim-support-prose-javascriptallonge-value-types-1",
            page_id="javascriptallonge-value-types",
            claim_text="Same-type cups can still be distinguished.",
            page_context=(
                "Same-type cups can still be distinguished. (raw/javascriptallonge.pdf p.22)"
            ),
            citation_texts=("raw/javascriptallonge.pdf p.22",),
            source_claim_ids=(),
            evidence_ids=("evidence-value-cups",),
            evidence_excerpts=(
                "evidence-value-cups: Value cups with the same value are undistinguishable.",
            ),
        )
        selection = ClaimSupportSelection(
            candidates=(candidate,),
            blocked_candidates=(),
            deterministic_findings=(),
            candidate_count=1,
            max_claims=1,
            sample_strategy="ordered",
        )
        script = [
            [
                ToolCall(
                    tool="record_claim_support_verdict",
                    args={
                        "candidate_id": candidate.candidate_id,
                        "verdict": "not_supported",
                        "rationale": "The excerpt says equal value cups are undistinguishable.",
                        "recommended_action": "Move this distinction to the reference-types page.",
                    },
                )
            ],
            [ToolCall(tool="finish_claim_support", args={"report": "audited one claim"})],
        ]

        result = await _session(store, script, paths).claim_support(
            selection,
            subject="raw/javascriptallonge.pdf pages=javascriptallonge-value-types",
            source_locator="javascriptallonge.pdf",
        )

        assert result.op == "claim-support"
        assert "- not_supported: 1" in result.output
        assert "Move this distinction" in store.read_page("wiki-claim-support")
        artifact = store.page_plan_artifact_dir("javascriptallonge.pdf") / "claim-support-report.md"
        assert artifact.is_file()
        log = paths.log_path.read_text(encoding="utf-8")
        assert f"## [{TODAY}] claim-support | raw/javascriptallonge.pdf" in log
        assert "Model-raised issues: 1" in log


class TestQuery:
    async def test_search_then_respond_and_logged(self, store: WikiStore, paths: WikiPaths) -> None:
        store.write_page(
            _wiki_page("moon", "source", "Lunar notes.", "Giant impact formed the Moon.")
        )
        script = [
            [ToolCall(tool="search_wiki", args={"query": "moon formation"})],
            [ToolCall(tool="respond", args={"message": "A giant impact — see [[moon]]."})],
        ]
        result = await _session(store, script, paths).query("How did the Moon form?")
        assert result.output == "A giant impact — see [[moon]]."
        assert f"## [{TODAY}] query | How did the Moon form?" in paths.log_path.read_text()
        assert isinstance(result.run, QueryRun)
        assert result.run.user_question == "How did the Moon form?"


class TestLint:
    async def test_empty_wiki_short_circuits_without_llm(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        result = await _session(store, [], paths).lint()
        assert "empty" in result.output.lower()
        assert f"## [{TODAY}] lint | empty wiki" in paths.log_path.read_text()

    async def test_lint_files_report_page_and_log(self, store: WikiStore, paths: WikiPaths) -> None:
        store.write_page(_wiki_page("alpha", "concept", "A.", "Links to [[ghost]]."))
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="finish_lint", args={"report": "ghost link is broken."})],
        ]
        session = _session(store, script, paths)
        result = await session.lint()
        assert result.output == "ghost link is broken."
        assert "wiki-health" in store.list_pages()
        assert f"## [{TODAY}] lint | wiki health" in paths.log_path.read_text()
        fake: FakeClient = session.client
        first_turn = fake.sent[0]
        user_msgs = [m["content"] for m in first_turn if m.get("role") == "user"]
        assert any("ghost" in content for content in user_msgs)

    async def test_health_page_is_not_reported_as_orphan(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(_wiki_page("alpha", "concept", "A.", "[[beta]]"))
        store.write_page(_wiki_page("beta", "concept", "B.", "[[alpha]]"))
        store.write_page(_wiki_page("wiki-health", "synthesis", "Old report.", "All clean."))
        session = _session(store, [], paths)
        result = await session.lint()
        fake: FakeClient = session.client
        assert fake.sent == []
        assert "No deterministic issues" in result.output

    async def test_large_lint_finding_set_files_deterministic_report_without_llm(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        for index in range(55):
            store.write_page(
                _wiki_page(
                    f"orphan-{index:02d}",
                    "concept",
                    f"Orphan {index}.",
                    "No inbound links.",
                )
            )
        session = _session(store, [], paths)

        result = await session.lint()

        fake: FakeClient = session.client
        assert fake.sent == []
        assert "Model repair loop skipped" in result.output
        assert "55 issue(s)" in result.output
        assert "wiki-health" in store.list_pages()
