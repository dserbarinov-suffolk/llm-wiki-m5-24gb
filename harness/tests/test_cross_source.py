"""Cross-source synthesis tests: relationship classification, topic planning,
rendering, quality, and the end-to-end synthesize operation.

These prove the DDD's cross-source invariants: positions from different sources
stay separate, relationships use the controlled vocabulary, only shared
distinctive concepts become pages, and a page draws on at least two sources.
"""

import json

from fakes import FakeClient
from forge.context import ContextManager, NoCompact

from llmwiki.config import WikiPaths
from llmwiki.domain.ledger.concepts import concept_topic_keys
from llmwiki.domain.ledger.cross_source import (
    CrossSourceRelationship,
    CrossSourceTopic,
    SourceBackedPosition,
    SourcePosition,
    classify_relationship,
    plan_cross_source_topics,
)
from llmwiki.domain.ledger.cross_source_quality import build_cross_source_quality_report
from llmwiki.domain.ledger.cross_source_render import render_cross_source_page
from llmwiki.domain.ledger.pointers import quality_check_catalog_pointer
from llmwiki.domain.ledger.quality import page_write_decision
from llmwiki.domain.ledger.quality_catalog import (
    default_quality_check_catalog,
    default_severity_policy,
)
from llmwiki.runtime.cross_source_load import load_source_positions
from llmwiki.runtime.cross_source_pipeline import build_cross_source_pages
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-06-12"
_CATALOG = default_quality_check_catalog()
_SEVERITY = default_severity_policy()
_POINTER = quality_check_catalog_pointer("qcc", "fp")


def _pos(
    source: str,
    *,
    kind: str = "concept",
    subject: str = "A closure",
    predicate: str = "is",
    polarity: str = "affirmative",
    has_scope: bool = False,
    text: str = "A closure is a function plus its environment.",
    facets: tuple[str, ...] = ("closure",),
    entry: str = "",
) -> SourcePosition:
    return SourcePosition(
        source_locator=source,
        source_hash=source[:8].ljust(8, "0"),
        projection_source_support_id=f"pss-{source}",
        ledger_entry_id=entry or f"ledger-entry-{source}-1",
        ledger_entry_kind=kind,
        subject=subject,
        predicate=predicate,
        polarity=polarity,
        claim_force="asserted",
        condition_scope="conditional" if has_scope else "unconditional",
        has_scope=has_scope,
        normalized_text=text,
        concept_facets=facets,
        topic_keys=concept_topic_keys(facets) if kind == "concept" else (),
        evidence_ids=(f"ev-{source}",),
        citation_label=f"{source} (sr-1)",
    )


class TestClassifyRelationship:
    def test_same_predicate_same_polarity_agrees(self) -> None:
        assert classify_relationship(_pos("a.pdf"), _pos("b.pdf")) == "agrees-with"

    def test_topic_key_without_shared_predicate_is_not_a_relationship(self) -> None:
        a = _pos("a.pdf", predicate="contains")
        b = _pos("b.pdf", predicate="requires")
        assert classify_relationship(a, b) is None

    def test_shared_predicate_without_comparable_statement_terms_is_not_a_relationship(
        self,
    ) -> None:
        a = _pos("a.pdf", text="A character is ready.")
        b = _pos("b.pdf", text="A character is green.")
        assert classify_relationship(a, b) is None

    def test_opposite_polarity_conflicts(self) -> None:
        a = _pos("a.pdf", polarity="affirmative")
        b = _pos("b.pdf", polarity="negative")
        assert classify_relationship(a, b) == "conflicts-with"

    def test_scope_difference_qualifies(self) -> None:
        a = _pos("a.pdf", has_scope=False)
        b = _pos("b.pdf", has_scope=True)
        assert classify_relationship(a, b) == "qualifies"

    def test_succession_wording_supersedes(self) -> None:
        a = _pos("a.pdf", text="This edition supersedes the earlier closure model.")
        assert classify_relationship(a, _pos("b.pdf")) == "supersedes"


class TestTopicPlanning:
    def test_shared_concept_across_two_sources_becomes_topic(self) -> None:
        positions = (_pos("a.pdf"), _pos("b.pdf"))
        topics = plan_cross_source_topics(positions)
        assert len(topics) == 1
        topic = topics[0]
        assert topic.topic_key == "closure"
        assert topic.page_kind == "concept"
        # One position per source, kept separate; one relationship between them.
        assert {p.source_locator for p in topic.positions} == {"a.pdf", "b.pdf"}
        assert len(topic.relationships) == 1

    def test_single_source_term_is_not_a_topic(self) -> None:
        positions = (_pos("a.pdf"), _pos("a.pdf", entry="ledger-entry-a-2"))
        assert plan_cross_source_topics(positions) == ()

    def test_shared_concept_in_every_source_remains_topic(self) -> None:
        positions = tuple(_pos(f"s{i}.pdf") for i in range(3))
        # Cross-source planning trusts explicit concept topic keys instead of
        # dropping a topic because it is shared by all sources.
        assert len(plan_cross_source_topics(positions)) == 1

    def test_only_concept_entries_anchor_topics(self) -> None:
        # Claim entries (not concepts) do not contribute candidate vocabulary.
        positions = (_pos("a.pdf", kind="claim"), _pos("b.pdf", kind="claim"))
        assert plan_cross_source_topics(positions) == ()

    def test_positions_without_topic_keys_are_ignored(self) -> None:
        positions = (
            _pos("a.pdf", facets=()),
            _pos("b.pdf", facets=()),
        )
        assert plan_cross_source_topics(positions) == ()


def _topic() -> CrossSourceTopic:
    positions = (
        SourceBackedPosition(
            "p-a", "a.pdf", "pss-a", "le-a", "A closure binds scope.", "a.pdf (sr-1)"
        ),
        SourceBackedPosition(
            "p-b", "b.pdf", "pss-b", "le-b", "Closures capture environment.", "b.pdf (sr-1)"
        ),
    )
    relationship = CrossSourceRelationship("rel-1", "agrees-with", ("p-a", "p-b"), ("le-a", "le-b"))
    return CrossSourceTopic(
        "closure", "Closure", "concept", positions, (relationship,), ("pss-a", "pss-b")
    )


class TestRenderAndQuality:
    def test_render_keeps_positions_separate_and_covers_each_unit(self) -> None:
        page = render_cross_source_page(_topic(), "closure")
        assert "A closure binds scope." in page.page_body
        assert "Closures capture environment." in page.page_body
        assert "agrees-with" in page.page_body
        kinds = [e.projection_coverage_unit_kind for e in page.coverage.entries]
        assert kinds.count("generated-page-claim") == 2
        assert kinds.count("cross-source-relationship") == 1
        assert "ledger-entry-" not in page.page_body

    def test_valid_cross_source_page_is_not_blocked(self) -> None:
        page = render_cross_source_page(_topic(), "closure")
        report = build_cross_source_quality_report(
            _topic(), page.page_body, catalog=_CATALOG, severity=_SEVERITY, catalog_pointer=_POINTER
        )
        assert not report.has_severity("blocking")
        assert page_write_decision(report) == "write-authoritative-page"

    def test_single_support_topic_is_blocked(self) -> None:
        positions = (
            SourceBackedPosition(
                "p-a", "a.pdf", "pss-a", "le-a", "Only one source.", "a.pdf (sr-1)"
            ),
        )
        topic = CrossSourceTopic("closure", "Closure", "concept", positions, (), ("pss-a",))
        report = build_cross_source_quality_report(
            topic, "body", catalog=_CATALOG, severity=_SEVERITY, catalog_pointer=_POINTER
        )
        assert report.has_severity("blocking")


def _representative(entry_id: str, text: str, source: str) -> dict:
    return {
        "ledger_entry_id": entry_id,
        "subject": "Subject",
        "predicate": "is",
        "polarity": "affirmative",
        "claim_force": "asserted",
        "condition_scope": "unconditional",
        "has_scope": False,
        "normalized_text": text,
        "citation_label": f"{source} (sr-1)",
    }


def _topic_index(source: str, topics: list[tuple[str, str, str]]) -> str:
    """Build a per-source topics.json artifact (key, label, statement)."""
    return json.dumps(
        {
            "source_locator": source,
            "source_hash": source[:8].ljust(8, "0"),
            "projection_source_support_id": f"pss-{source}",
            "topics": [
                {
                    "topic_key": key,
                    "label": label,
                    "page_kind": "concept",
                    "entry_count": 1,
                    "atom_count": 0,
                    "representative": _representative(f"le-{source}-{key}", text, source),
                }
                for key, label, text in topics
            ],
        }
    )


class TestSynthesizePipeline:
    def test_loader_reads_one_position_per_topic(self) -> None:
        loaded = load_source_positions(
            _topic_index("alpha.pdf", [("binding", "Binding", "A binding names a value.")])
        )
        assert loaded.source_locator == "alpha.pdf"
        assert len(loaded.positions) == 1
        assert loaded.positions[0].topic_keys == ("binding",)

    def test_build_cross_source_pages_from_two_topic_indexes(self) -> None:
        a = _topic_index("alpha.pdf", [("binding", "Binding", "A binding names a value.")])
        b = _topic_index("beta.pdf", [("binding", "Binding", "Bindings attach names.")])
        result = build_cross_source_pages((a, b), today=TODAY)
        concept_pages = [p for p in result.pages if p.page_kind == "concept"]
        assert any(p.page_id == "binding" for p in concept_pages)
        assert any(p.page_kind == "synthesis" for p in result.pages)
        assert result.blocked == ()

    async def test_session_synthesize_writes_concept_pages(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        for source in ("alpha.pdf", "beta.pdf"):
            store.write_ledger_artifacts(
                source,
                {
                    "topics.json": _topic_index(
                        source, [("monad", "Monad", "A monad wraps a value.")]
                    )
                },
            )
        session = Session(
            store=store,
            client=FakeClient([]),
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
            today=TODAY,
            runs_dir=paths.root / "runs",
            run_id="synth-test",
        )
        result = await session.synthesize()
        assert "Cross-source synthesis over 2 source(s)" in result.output
        assert "monad" in store.list_pages()
        assert "cross-source-synthesis" in store.list_pages()
        body = store.read_page("monad")
        assert "[[alpha]]" in body and "[[beta]]" in body
        assert f"## [{TODAY}] synthesize" in paths.log_path.read_text(encoding="utf-8")
