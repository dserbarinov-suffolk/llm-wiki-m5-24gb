"""Per-source topic-index tests.

Authored headings are projected as section-reference pages. Topic pages are for
repeated or emergent concepts that aggregate source-backed claims and atoms.
"""

from llmwiki.domain.ledger.builder import (
    LedgerBuildResult,
    SegmentInput,
    build_claim_ledger,
    default_schema_bundle,
)
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.section_pages import build_section_pages
from llmwiki.domain.ledger.section_planning import build_section_grounded_plan
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_render import render_topic_page
from llmwiki.domain.ledger.topics import (
    SourceTopic,
    build_topic_index,
    plan_source_topic_result,
    plan_source_topics,
)

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
    def test_repeated_subject_term_with_source_heading_anchor_creates_topic(self) -> None:
        topic = _topic(_build(_SPECS), "function")
        assert topic is not None
        assert not topic.from_heading
        assert topic.label == "Function"
        assert len(topic.entry_ids) >= 4
        assert topic.candidate_origin == "subject-term"
        assert topic.admission_reason == "source-heading-anchor"

    def test_repeated_subject_term_without_semantic_anchor_is_rejected(self) -> None:
        specs = [
            (
                "paragraph",
                f"A glimmer provides signal {index}.",
                [f"A glimmer provides signal {index}."],
            )
            for index in range(1, 6)
        ]
        result = _build(specs)
        plan = plan_source_topic_result(result.ledger, result.document_structure)

        assert "glimmer" not in {topic.topic_key for topic in plan.topics}
        rejected = {candidate.topic_key: candidate for candidate in plan.rejected_candidates}
        assert rejected["glimmer"].rejection_reason == "lexical-subject-frequency-only"

    def test_repeated_adverbial_operator_never_becomes_topic(self) -> None:
        specs = [
            (
                "paragraph",
                f"Always provide viable options for sample {index}.",
                [f"Always provide viable options for sample {index}."],
            )
            for index in range(1, 6)
        ]
        result = _build(specs)
        plan = plan_source_topic_result(result.ledger, result.document_structure)
        keys = {topic.topic_key for topic in plan.topics}
        rejected = {candidate.topic_key for candidate in plan.rejected_candidates}

        assert "always" not in keys
        assert "alway" not in keys
        assert "always" not in rejected
        assert "alway" not in rejected

    def test_technical_atom_does_not_admit_bare_subject_token_page(self) -> None:
        result = _build(
            [
                (
                    "paragraph",
                    f"A helper provides utility {index}.",
                    [f"A helper provides utility {index}."],
                )
                for index in range(1, 6)
            ]
            + [
                ("paragraph", "The helper can be used like this:", []),
                ("code-fence", "```go\nhelper()\n```", []),
            ]
        )
        plan = plan_source_topic_result(result.ledger, result.document_structure)

        assert "helper" not in {topic.topic_key for topic in plan.topics}
        rejected = {candidate.topic_key: candidate for candidate in plan.rejected_candidates}
        assert rejected["helper"].rejection_reason == "technical-atom-without-semantic-anchor"

    def test_exact_section_target_does_not_create_duplicate_topic(self) -> None:
        result = _build(
            [
                ("heading", "# Alpha", []),
                (
                    "paragraph",
                    "Alpha has source-local evidence.",
                    ["Alpha has source-local evidence."],
                ),
            ]
        )
        section_plan = build_section_grounded_plan(result.ledger, result.document_structure)
        topics = plan_source_topics(
            result.ledger, result.document_structure, section_plan=section_plan
        )

        assert "alpha" not in {topic.topic_key for topic in topics}

    def test_section_page_includes_only_context_supported_atoms(self) -> None:
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

        pages = build_section_pages(
            result.ledger,
            result.document_structure,
            section_plan=build_section_grounded_plan(result.ledger, result.document_structure),
            source_page_id="book",
            source_locator="book.pdf",
            today="2026-06-26",
        )
        page = next(page for page in pages if page.page_body.startswith("# Arrays"))

        assert "scores := [4]int{9001, 9333}" in page.page_body
        assert "arrayBuffer" not in page.page_body

    def test_section_page_includes_table_with_matching_source_caption(self) -> None:
        result = _build(
            [
                ("heading", "# Armor", []),
                (
                    "paragraph",
                    "The Armor table shows key values.",
                    ["The Armor table shows key values."],
                ),
                ("heading", "# Heavy Armor", []),
                (
                    "table-block",
                    "Table- Armor\n"
                    "Name        Cost       Weight\n"
                    "Alpha       10         Light\n"
                    "Beta        20         Heavy",
                    [],
                ),
            ]
        )

        pages = build_section_pages(
            result.ledger,
            result.document_structure,
            section_plan=build_section_grounded_plan(result.ledger, result.document_structure),
            source_page_id="book",
            source_locator="book.pdf",
            today="2026-06-26",
        )
        page = next(page for page in pages if page.page_body.startswith("# Armor"))

        assert "Table- Armor" in page.page_body

    def test_section_page_includes_table_named_by_generic_forward_cue(self) -> None:
        filler = [
            ("paragraph", f"Intervening source line {index} separates cue and table.", [])
            for index in range(10)
        ]
        result = _build(
            [
                ("heading", "# Sample Outcomes", []),
                (
                    "paragraph",
                    "The Sample Outcomes table shows generated results.",
                    ["The Sample Outcomes table shows generated results."],
                ),
                ("heading", "# Roll on the table below.", []),
                *filler,
                ("heading", "# Follow-up Notes", []),
                (
                    "table-block",
                    "| Roll | Result |\n| --- | --- |\n| 1 | Alpha |\n| 2 | Beta |",
                    [],
                ),
            ]
        )

        pages = build_section_pages(
            result.ledger,
            result.document_structure,
            section_plan=build_section_grounded_plan(result.ledger, result.document_structure),
            source_page_id="sample-source",
            source_locator="book.pdf",
            today="2026-06-26",
        )
        page = next(page for page in pages if page.page_body.startswith("# Sample Outcomes"))

        assert "## Technical atoms" in page.page_body
        assert "Alpha" in page.page_body

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

    def test_topic_index_persists_admission_and_rejection_provenance(self) -> None:
        result = _build(
            [
                *_SPECS,
                *[
                    (
                        "paragraph",
                        f"A glimmer provides signal {index}.",
                        [f"A glimmer provides signal {index}."],
                    )
                    for index in range(1, 6)
                ],
            ]
        )
        plan = plan_source_topic_result(result.ledger, result.document_structure)
        topic_index = build_topic_index(
            result.ledger,
            plan.topics,
            source_locator="book.pdf",
            source_hash=_HASH,
            projection_source_support_id="pss",
            rejected_candidates=plan.rejected_candidates,
        )

        topic = next(item for item in topic_index.topics if item.topic_key == "function")
        assert topic.candidate_origin == "subject-term"
        assert topic.admission_reason == "source-heading-anchor"
        rejected = {candidate.topic_key: candidate for candidate in topic_index.rejected_candidates}
        assert rejected["glimmer"].rejection_reason == "lexical-subject-frequency-only"

    def test_topics_are_capped_and_ranked(self) -> None:
        topics = plan_source_topics(*_unpack(_build(_SPECS)), max_topics=32)
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
        assert "# Function" in page.page_body
        assert "[[book]]" in page.page_body  # back-link to source
        assert "A function provides a result." in page.page_body
        assert "ledger-entry-" not in page.page_body
        assert "projection-coverage-entry-" not in page.page_body
        kinds = {e.projection_coverage_unit_kind for e in page.coverage.entries}
        assert "generated-page-claim" in kinds

    def test_section_page_renders_atom_context_before_atom(self) -> None:
        result = _build(
            [
                ("heading", "# Arrays", []),
                ("paragraph", "Arrays are fixed values.", ["Arrays are fixed values."]),
                ("paragraph", "We can initialize the array with values:", []),
                ("code-fence", "```go\nscores := [4]int{9001, 9333}\n```", []),
            ]
        )
        pages = build_section_pages(
            result.ledger,
            result.document_structure,
            section_plan=build_section_grounded_plan(result.ledger, result.document_structure),
            source_page_id="book",
            source_locator="book.pdf",
            today="2026-06-26",
        )
        page = next(page for page in pages if page.page_body.startswith("# Arrays"))

        assert "We can initialize the array with values:" in page.page_body
        assert "scores := [4]int{9001, 9333}" in page.page_body

    def test_section_page_renders_context_supported_structured_rule_atom(self) -> None:
        result = _build(
            [
                ("heading", "# Combat", []),
                ("paragraph", "Combat uses required rolls.", ["Combat uses required rolls."]),
                ("paragraph", "Combat rules specify required rolls:", []),
                ("paragraph", "A combatant must roll a die.", ["A combatant must roll a die."]),
            ]
        )
        pages = build_section_pages(
            result.ledger,
            result.document_structure,
            section_plan=build_section_grounded_plan(result.ledger, result.document_structure),
            source_page_id="book",
            source_locator="book.pdf",
            today="2026-06-26",
        )
        page = next(page for page in pages if page.page_body.startswith("# Combat"))

        assert "Combat rules specify required rolls:" in page.page_body
        assert "A combatant must roll a die." in page.page_body
