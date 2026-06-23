"""End-to-end operation tests: real WorkflowRunner + real store, fake LLM.

These map to the design doc's key interactions — ingest, query, lint —
and exercise the guardrail wiring (required steps, prerequisites) that the
harness declares on each workflow.
"""

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import TextResponse, ToolCall

from llmwiki.config import WikiPaths
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


def _source_summary_args(
    target_page_id: str,
    citation: str,
    *,
    uncertainty: str = "",
    claim_ids: tuple[str, ...] = ("source-claim-unit-0001-0001",),
) -> dict:
    uncertainty_sentence = f" {uncertainty}" if uncertainty else ""
    covered = list(claim_ids)
    return {
        "source_record_text": (
            f"Source record for [[{target_page_id}]] using ({citation}).{uncertainty_sentence}"
        ),
        "claim_bullets": [
            {
                "bullet_text": (
                    f"The source supports a focused note about [[{target_page_id}]]. ({citation})"
                ),
                "covered_source_claims": covered,
            },
            {
                "bullet_text": (
                    f"The source should be used as cited evidence, not copied wholesale. "
                    f"({citation})"
                ),
                "covered_source_claims": covered,
            },
            {
                "bullet_text": (
                    f"The source leaves detailed interpretation to the target page. ({citation})"
                ),
                "covered_source_claims": covered,
            },
        ],
    }


def _entity_body(source_page_id: str, citation: str, claim: str) -> str:
    return f"{claim} See [[{source_page_id}]]. ({citation})"


@pytest.fixture
def source(paths: WikiPaths) -> str:
    (paths.raw_dir / "moon.md").write_text(
        "The Moon formed ~4.5 billion years ago from a giant impact.", encoding="utf-8"
    )
    return "moon.md"


class TestIngest:
    async def test_markdown_ingest_uses_planned_source_and_subject_pages(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_args("moon", "raw/moon.md"),
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "source written"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_body": _entity_body(
                            "moon-source",
                            "raw/moon.md",
                            "The Moon has a giant-impact formation account.",
                        ),
                    },
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "entity written"})],
        ]
        result = await _session(store, script, paths).ingest(source)

        assert "Planned ingest completed" in result.output
        assert "Written pages: [[moon-source]], [[moon]]" in result.output
        assert "Ingest confidence:" in result.output
        assert "Source record for [[moon]]" in store.read_page("moon-source")
        assert "giant-impact formation account" in store.read_page("moon")
        assert "Ingest Confidence Report" in store.read_page("wiki-ingest-confidence")
        artifact_dir = store.page_plan_artifact_dir(source)
        assert (artifact_dir / "page-plan.json").is_file()
        assert (artifact_dir / "evidence-registry.json").is_file()
        assert (artifact_dir / "evidence-locators.json").is_file()
        assert (artifact_dir / "artifact-fingerprint.json").is_file()
        assert "- [[moon-source]] — Source summary for moon." in store.read_index()
        assert "- [[moon]] — Facts about moon from an ingested RawSource." in store.read_index()
        log = paths.log_path.read_text(encoding="utf-8")
        assert f"## [{TODAY}] ingest | moon.md" in log
        assert "Written pages: [[moon-source]], [[moon]]" in log
        assert result.transcript_path is not None and result.transcript_path.exists()
        assert isinstance(result.run, IngestRun)
        assert result.run.source_bundle.raw_sources[0].source_locator == "moon.md"
        assert result.run.page_plan is not None
        assert result.run.source_plans[0].planned_page_write_ids == ("write-moon-source",)
        assert result.run.source_plans[1].planned_page_write_ids == ("write-moon",)

    async def test_model_report_cannot_claim_unwritten_pages(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_args("moon", "raw/moon.md"),
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "also wrote [[ghost]]"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_body": _entity_body(
                            "moon-source",
                            "raw/moon.md",
                            "Moon notes retain the cited source.",
                        )
                    },
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "also wrote [[ghost]]"})],
        ]
        result = await _session(store, script, paths).ingest(source)
        assert "ghost" not in result.output
        assert "ghost" not in paths.log_path.read_text(encoding="utf-8")
        assert set(store.list_pages()) == {"moon-source", "moon", "wiki-ingest-confidence"}

    async def test_required_links_and_citations_are_checked_before_write(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args={"page_body": "Body without the planned link or citation."},
                )
            ],
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_args("moon", "raw/moon.md"),
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "source written"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_body": _entity_body(
                            "moon-source",
                            "raw/moon.md",
                            "Moon notes retain the cited source.",
                        )
                    },
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "entity written"})],
        ]
        await _session(store, script, paths).ingest(source)
        assert "Body without" not in store.read_page("moon-source")
        assert "Key supported claims" in store.read_page("moon-source")

    async def test_uncertainty_terms_are_checked_before_write(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "origin.md").write_text(
            "# Origin\n\nThe device may have originated in Corinth, possibly near Syracuse.",
            encoding="utf-8",
        )
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_args(
                        "origin",
                        "raw/origin.md",
                        uncertainty="The source may place the origin near Corinth.",
                    ),
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "source written"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_body": (
                            "The device originated in Corinth. "
                            "See [[origin-source]]. (raw/origin.md)"
                        ),
                    },
                )
            ],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_body": (
                            _entity_body(
                                "origin-source",
                                "raw/origin.md",
                                "The source says the device may have a Corinthian origin.",
                            )
                        ),
                    },
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "entity written"})],
        ]
        await _session(store, script, paths).ingest("origin.md")
        assert "The device originated in Corinth." not in store.read_page("origin")
        assert "may have a Corinthian origin" in store.read_page("origin")

    async def test_rewrite_without_read_is_blocked_then_recovers(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # write_page replaces the whole page; rewriting one the model never
        # read this run must fail with a corrective error (open question #10),
        # and succeed after read_page.
        store.write_page(
            _wiki_page("moon", "entity", "Original.", "Original rich body with [[links]].")
        )
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_args("moon", "raw/moon.md"),
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "source written"})],
            [
                ToolCall(  # blind rewrite — must be rejected
                    tool="write_page",
                    args={"page_body": "Thin rewrite with [[moon-source]]. (raw/moon.md)"},
                )
            ],
            [ToolCall(tool="read_page", args={"page_id": "moon"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_body": (
                            "Original rich body with [[links]]. Plus new facts. "
                            "See [[moon-source]]. (raw/moon.md)"
                        ),
                    },
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "updated moon"})],
        ]
        result = await _session(store, script, paths).ingest(source)
        assert "Written pages: [[moon-source]], [[moon]]" in result.output
        body = store.read_page("moon")
        assert "Plus new facts" in body
        # The blind rewrite never landed:
        assert "thin" not in store.read_index()

    async def test_pipeline_markers_stripped_from_written_pages(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # The OCR caveat tag is extraction plumbing; observed quoted verbatim
        # into a wiki page despite the schema — stripped at the boundary now.
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "source_record_text": (
                            "Real claim for [[moon]]. (raw/moon.md)\n"
                            "[figure text (OCR, unverified): NOISE ON A MUG]"
                        ),
                        "claim_bullets": [
                            {
                                "bullet_text": "First compact claim. (raw/moon.md)",
                                "covered_source_claims": ["source-claim-unit-0001-0001"],
                            },
                            {
                                "bullet_text": "Another claim. (raw/moon.md)",
                                "covered_source_claims": ["source-claim-unit-0001-0001"],
                            },
                            {
                                "bullet_text": "Third compact claim. (raw/moon.md)",
                                "covered_source_claims": ["source-claim-unit-0001-0001"],
                            },
                        ],
                    },
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "source written"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_body": _entity_body(
                            "moon-source",
                            "raw/moon.md",
                            "Moon notes retain the cited source.",
                        )
                    },
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "entity written"})],
        ]
        await _session(store, script, paths).ingest(source)
        body = store.read_page("moon-source")
        assert "Real claim for [[moon]]." in body and "Another claim." in body
        assert "OCR" not in body and "NOISE" not in body

    async def test_source_framing_source_summary_rejection_is_recoverable(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        bad_args = _source_summary_args("moon", "raw/moon.md")
        bad_args["claim_bullets"][0]["bullet_text"] = (
            "The source discusses a compact claim. (raw/moon.md)"
        )
        good_args = _source_summary_args("moon", "raw/moon.md")
        script = [
            [ToolCall(tool="write_page", args=bad_args)],
            [ToolCall(tool="write_page", args=good_args)],
            [ToolCall(tool="finish_planned_write", args={"report": "source written"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_body": _entity_body(
                            "moon-source",
                            "raw/moon.md",
                            "The Moon has a giant-impact formation account.",
                        )
                    },
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "entity written"})],
        ]

        await _session(store, script, paths).ingest(source)

        body = store.read_page("moon-source")
        assert "The source discusses" not in body
        assert "The source supports a focused note" in body

    async def test_bare_text_after_work_nudged_to_terminal_tool(
        self, store: WikiStore, paths: WikiPaths, source: str
    ) -> None:
        # The observed live failure mode: the model finishes its page writes,
        # then "reports" in bare text instead of calling finish_planned_write. The
        # retry nudge must name the terminal tool and the run must recover.
        script = [
            [
                ToolCall(
                    tool="write_page",
                    args=_source_summary_args("moon", "raw/moon.md"),
                )
            ],
            TextResponse(content="I have finished ingesting the source."),
            [ToolCall(tool="finish_planned_write", args={"report": "source written"})],
            [
                ToolCall(
                    tool="write_page",
                    args={
                        "page_body": _entity_body(
                            "moon-source",
                            "raw/moon.md",
                            "Moon notes retain the cited source.",
                        )
                    },
                )
            ],
            [ToolCall(tool="finish_planned_write", args={"report": "entity written"})],
        ]
        session = _session(store, script, paths)
        result = await session.ingest(source)
        assert "Written pages: [[moon-source]], [[moon]]" in result.output
        fake: FakeClient = session.client
        # The turn after the bare text must carry the terminal-tool hint.
        nudges = [m["content"] for turn in fake.sent for m in turn if m.get("role") == "user"]
        assert any("finish_planned_write" in content for content in nudges)


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
        # The deterministic findings reached the model in the user message.
        fake: FakeClient = session.client
        first_turn = fake.sent[0]
        user_msgs = [m["content"] for m in first_turn if m.get("role") == "user"]
        assert any("ghost" in content for content in user_msgs)

    async def test_health_page_is_not_reported_as_orphan(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        # A prior lint filed wiki-health; the next lint must not flag it.
        store.write_page(_wiki_page("alpha", "concept", "A.", "[[beta]]"))
        store.write_page(_wiki_page("beta", "concept", "B.", "[[alpha]]"))
        store.write_page(_wiki_page("wiki-health", "synthesis", "Old report.", "All clean."))
        script = [
            [ToolCall(tool="read_page", args={"page_id": "alpha"})],
            [ToolCall(tool="finish_lint", args={"report": "Still clean."})],
        ]
        session = _session(store, script, paths)
        await session.lint()
        fake: FakeClient = session.client
        user_msgs = [m["content"] for m in fake.sent[0] if m.get("role") == "user"]
        assert not any("Orphan" in content for content in user_msgs)
