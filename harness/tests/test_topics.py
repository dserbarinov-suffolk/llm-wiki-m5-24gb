"""Per-source topic-index tests: heading + key-term topic planning and the
topic page renderer.

These prove the searchable-topic projection: the author's headings and salient
recurring subject terms become concept topics that aggregate the source's
claims and atoms, run-on/contents-list statements are excluded, common English
words never anchor a topic, and rendered pages leak no internal ids.
"""

from llmwiki.domain.ledger.atoms import atom_raw_text
from llmwiki.domain.ledger.builder import (
    LedgerBuildResult,
    SegmentInput,
    build_claim_ledger,
    default_schema_bundle,
)
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_render import render_topic_page
from llmwiki.domain.ledger.topics import SourceTopic, plan_source_topics

_HASH = "abcdef0123456789"
# Usable (has a pivot verb "provides") but a run-on of > 45 words.
_LONG = "A function provides " + " ".join(f"detail{i}" for i in range(60)) + "."


def _build(specs: list[tuple[str, str, list[str]]]) -> LedgerBuildResult:
    inputs: list[SegmentInput] = []
    profiles = {}
    for order, (kind, text, claims) in enumerate(specs, start=1):
        seg = SourceSegment(
            segment_id=f"seg-{order:03d}",
            source_range_id=f"sr-{order:03d}",
            source_locator="book.pdf",
            source_hash=_HASH,
            heading_path="H",
            structure_node_id="",
            source_order=order,
            text=text,
            segment_kind=kind,
            evidence_ids=(f"ev-{order:03d}",),
        )
        claim_records = tuple(
            SegmentClaim(f"c-{order}-{i}", statement, (), "eligible", "supported", seg.evidence_ids)
            for i, statement in enumerate(claims)
        )
        inputs.append(SegmentInput(seg, claim_records))
        profiles[seg.segment_id] = profile_unit(
            extracted_unit_id=seg.segment_id,
            source_range_id=seg.source_range_id,
            text=text,
            evidence_ids=seg.evidence_ids,
        )
    return build_claim_ledger(
        source_locator="book.pdf",
        source_hash=_HASH,
        evidence_registry_hash="er",
        segments=tuple(inputs),
        profiles=profiles,
        schema=default_schema_bundle(),
    )


_SPECS = [
    ("heading", "# Functions", []),
    ("paragraph", "A function provides a result.", ["A function provides a result."]),
    ("paragraph", "A function uses arguments.", ["A function uses arguments."]),
    ("paragraph", "A function holds local state.", ["A function holds local state."]),
    ("paragraph", "A function becomes a value.", ["A function becomes a value."]),
    ("paragraph", _LONG, [_LONG]),
    ("paragraph", "The compiler uses passes.", ["The compiler uses passes."]),
    ("code-fence", "```go\nfunc add(a, b int) int {\n    return a + b\n}\n```", []),
]


def _topic(result: LedgerBuildResult, key: str) -> SourceTopic | None:
    return next(
        (
            t
            for t in plan_source_topics(result.ledger, result.document_structure)
            if t.topic_key == key
        ),
        None,
    )


def _topic_texts(result: LedgerBuildResult, entry_ids: tuple[str, ...]) -> list[str]:
    texts: list[str] = []
    for entry_id in entry_ids:
        entry = result.ledger.entry(entry_id)
        assert entry is not None
        texts.append(entry.normalized_text)
    return texts


class TestTopicPlanning:
    def test_heading_and_term_merge_into_one_topic(self) -> None:
        topic = _topic(_build(_SPECS), "function")
        assert topic is not None
        assert topic.from_heading  # the "Functions" heading anchors it
        assert topic.label == "Functions"
        assert len(topic.entry_ids) >= 4

    def test_heading_topic_does_not_import_sibling_lexical_mentions(self) -> None:
        result = _build(
            [
                ("heading", "# Vessel Failure", []),
                (
                    "paragraph",
                    "A vessel failure requires immediate venting.",
                    ["A vessel failure requires immediate venting."],
                ),
                (
                    "paragraph",
                    "A cracked vessel loses pressure.",
                    ["A cracked vessel loses pressure."],
                ),
                (
                    "paragraph",
                    "Repair crews can seal a failed vessel.",
                    ["Repair crews can seal a failed vessel."],
                ),
                ("heading", "# Vessel Painting", []),
                (
                    "paragraph",
                    "A vessel painting crew uses blue primer.",
                    ["A vessel painting crew uses blue primer."],
                ),
                (
                    "paragraph",
                    "A vessel painting crew uses rollers.",
                    ["A vessel painting crew uses rollers."],
                ),
            ]
        )
        topic = _topic(result, "vessel-failure")
        assert topic is not None
        texts = _topic_texts(result, topic.entry_ids)
        assert any("immediate venting" in text for text in texts)
        assert any("failed vessel" in text for text in texts)
        assert not any("blue primer" in text for text in texts)

    def test_heading_topic_includes_only_context_supported_atoms(self) -> None:
        result = _build(
            [
                ("heading", "# Arrays", []),
                ("paragraph", "Arrays are fixed values.", ["Arrays are fixed values."]),
                ("paragraph", "We can initialize the array with values:", []),
                ("code-fence", "```go\nscores := [4]int{9001, 9333}\n```", []),
                ("paragraph", "Logging uses a buffer for output:", []),
                ("code-fence", "```go\narrayBuffer := make([]byte, 10)\n```", []),
            ]
        )

        topic = _topic(result, "array")

        assert topic is not None
        assert len(topic.atom_ids) == 1
        atom = result.ledger.atom(topic.atom_ids[0])
        assert atom is not None
        assert "scores" in atom_raw_text(atom.payload)

    def test_generic_reflexive_pronouns_never_anchor_topics(self) -> None:
        specs = [
            (
                "paragraph",
                f"Himself provides signal {index}.",
                [f"Himself provides signal {index}."],
            )
            for index in range(1, 6)
        ]
        keys = {t.topic_key for t in plan_source_topics(*_unpack(_build(specs)))}
        assert "himself" not in keys

    def test_runon_statement_is_excluded(self) -> None:
        result = _build(_SPECS)
        topic = _topic(result, "function")
        assert topic is not None
        texts = _topic_texts(result, topic.entry_ids)
        assert all(len(text.split()) <= 45 for text in texts)
        assert not any("detail59" in text for text in texts)

    def test_common_words_never_anchor_a_topic(self) -> None:
        keys = {t.topic_key for t in plan_source_topics(*_unpack(_build(_SPECS)))}
        # "compiler" recurs only once, below the frequency gate; generic words
        # are stopworded — none of these anchor a topic.
        for term in ("compiler", "time", "value", "once", "thing", "first"):
            assert term not in keys

    def test_topics_are_capped_and_ranked(self) -> None:
        topics = plan_source_topics(*_unpack(_build(_SPECS)))
        assert len(topics) <= 32
        saliences = [t.salience for t in topics]
        assert saliences == sorted(saliences, reverse=True)


def _unpack(result: LedgerBuildResult) -> tuple[ClaimLedger, DocumentStructure]:
    return result.ledger, result.document_structure


class TestTopicRender:
    def test_topic_page_aggregates_statements_and_links_source(self) -> None:
        result = _build(_SPECS)
        topic = _topic(result, "function")
        assert topic is not None
        page = render_topic_page(
            topic, result.ledger, wiki_page_locator="book-function", source_page_id="book"
        )
        assert "# Functions" in page.page_body
        assert "[[book]]" in page.page_body  # back-link to source
        assert "A function provides a result." in page.page_body
        assert "ledger-entry-" not in page.page_body
        assert "projection-coverage-entry-" not in page.page_body
        kinds = {e.projection_coverage_unit_kind for e in page.coverage.entries}
        assert "generated-page-claim" in kinds

    def test_topic_page_renders_atom_context_before_atom(self) -> None:
        result = _build(
            [
                ("heading", "# Arrays", []),
                ("paragraph", "Arrays are fixed values.", ["Arrays are fixed values."]),
                ("paragraph", "We can initialize the array with values:", []),
                ("code-fence", "```go\nscores := [4]int{9001, 9333}\n```", []),
            ]
        )
        topic = _topic(result, "array")
        assert topic is not None

        page = render_topic_page(
            topic, result.ledger, wiki_page_locator="book-array", source_page_id="book"
        )

        assert "Context: We can initialize the array with values:" in page.page_body
        assert "scores := [4]int{9001, 9333}" in page.page_body
        kinds = {e.projection_coverage_unit_kind for e in page.coverage.entries}
        assert "technical-atom-context" in kinds

    def test_topic_page_renders_context_supported_structured_rule_atom(self) -> None:
        result = _build(
            [
                ("heading", "# Combat", []),
                ("paragraph", "Combat uses required rolls.", ["Combat uses required rolls."]),
                ("paragraph", "Combat rules specify required rolls:", []),
                ("paragraph", "A combatant must roll a die.", ["A combatant must roll a die."]),
            ]
        )
        topic = _topic(result, "combat")
        assert topic is not None

        page = render_topic_page(
            topic, result.ledger, wiki_page_locator="book-combat", source_page_id="book"
        )

        assert "Context: Combat rules specify required rolls:" in page.page_body
        assert "A combatant must roll a die." in page.page_body
