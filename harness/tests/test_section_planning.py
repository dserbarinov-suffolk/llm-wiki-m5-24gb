"""Section-grounded planning tests.

These prove authored sections, not table rows or lexical mentions alone, drive
page targets. The examples are synthetic so the invariant is source-neutral.
"""

from llmwiki.domain.ledger.atoms import atom_raw_text
from llmwiki.domain.ledger.builder import (
    LedgerBuildResult,
    SegmentInput,
    build_claim_ledger,
    default_schema_bundle,
)
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.section_planning import build_section_grounded_plan
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.topics import plan_source_topics

_HASH = "1234567890abcdef"


def _build(specs: list[tuple[str, str, list[str]]]) -> LedgerBuildResult:
    inputs: list[SegmentInput] = []
    profiles = {}
    for order, (kind, text, claims) in enumerate(specs, start=1):
        segment = SourceSegment(
            segment_id=f"seg-{order:03d}",
            source_range_id=f"sr-{order:03d}",
            source_locator="synthetic.pdf",
            source_hash=_HASH,
            heading_path="H",
            structure_node_id="",
            source_order=order,
            text=text,
            segment_kind=kind,
            evidence_ids=(f"ev-{order:03d}",),
        )
        claim_records = tuple(
            SegmentClaim(
                f"c-{order}-{index}", claim, (), "eligible", "supported", segment.evidence_ids
            )
            for index, claim in enumerate(claims)
        )
        inputs.append(SegmentInput(segment, claim_records))
        profiles[segment.segment_id] = profile_unit(
            extracted_unit_id=segment.segment_id,
            source_range_id=segment.source_range_id,
            text=text,
            evidence_ids=segment.evidence_ids,
        )
    return build_claim_ledger(
        source_locator="synthetic.pdf",
        source_hash=_HASH,
        evidence_registry_hash="er",
        segments=tuple(inputs),
        profiles=profiles,
        schema=default_schema_bundle(),
    )


def test_product_family_section_collects_table_as_evidence_without_row_pages() -> None:
    result = _build(
        [
            ("heading", "# Alpha 1000 Series", []),
            (
                "paragraph",
                "Alpha 1000 Series provides field-rated assemblies.",
                ["Alpha 1000 Series provides field-rated assemblies."],
            ),
            (
                "table-block",
                "Table- Alpha 1000 Series\n"
                "Model   Voltage   Rating\n"
                "A1001   12V       Standard\n"
                "A1002   24V       Fire",
                [],
            ),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)

    target = next(item for item in plan.page_targets if item.topic_key == "alpha-1000-series")
    assert target.entry_ids
    assert len(target.atom_ids) == 1
    assert any(e.evidence_role == "structured-table" for e in target.attached_evidence)
    assert "a1001" not in {item.topic_key for item in plan.page_targets}


def test_coding_section_attaches_code_example_to_section_target() -> None:
    result = _build(
        [
            ("heading", "# Widgets", []),
            ("paragraph", "Widgets provide ordered values.", ["Widgets provide ordered values."]),
            ("paragraph", "We can initialize widgets with values:", []),
            ("code-fence", "```go\nwidgets := [2]int{1, 2}\n```", []),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)

    target = next(item for item in plan.page_targets if item.topic_key == "widget")
    assert len(target.atom_ids) == 1
    atom = result.ledger.atom(target.atom_ids[0])
    assert atom is not None
    assert "widgets :=" in atom_raw_text(atom.payload)


def test_generic_table_instruction_heading_does_not_create_page_target() -> None:
    result = _build(
        [
            ("heading", "# Outcomes", []),
            ("paragraph", "Outcomes provide play results.", ["Outcomes provide play results."]),
            ("heading", "# Roll on the table below.", []),
            ("table-block", "| Roll | Result |\n| --- | --- |\n| 1 | Quiet |\n| 2 | Loud |", []),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)

    keys = {item.topic_key for item in plan.page_targets}
    assert "outcome" in keys
    assert "roll-table" not in keys


def test_record_shaped_structure_node_does_not_create_page_target() -> None:
    result = _build(
        [
            ("heading", "# Reference Catalog", []),
            (
                "paragraph",
                "Reference catalog provides reusable entries.",
                ["Reference catalog provides reusable entries."],
            ),
            ("heading", "# [ Luma ] Rate=2 Cost=4 Range=near", []),
            ("paragraph", "Luma provides a reusable entry.", ["Luma provides a reusable entry."]),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)

    keys = {item.topic_key for item in plan.page_targets}
    assert "reference-catalog" in keys
    assert "luma-rate-cost-range" not in keys


def test_section_label_keeps_non_plural_suffix_terms() -> None:
    result = _build(
        [
            ("heading", "# Proficiency Bonus", []),
            (
                "paragraph",
                "A proficiency bonus applies to supported checks.",
                ["A proficiency bonus applies to supported checks."],
            ),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)

    assert "proficiency-bonus" in {item.topic_key for item in plan.page_targets}
    assert "proficiency-bonu" not in {item.topic_key for item in plan.page_targets}


def test_coordinated_section_labels_seed_component_concepts() -> None:
    result = _build(
        [
            ("heading", "# Arrays and slices", []),
            (
                "paragraph",
                "Arrays and slices provide collections.",
                ["Arrays and slices provide collections."],
            ),
            ("heading", "# Arrays and their type", []),
            (
                "paragraph",
                "Array type provides length constraints.",
                ["Array type provides length constraints."],
            ),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)
    topics = plan_source_topics(result.ledger, result.document_structure, section_plan=plan)

    target = next(item for item in plan.page_targets if item.topic_key == "array-slice")
    assert target.concept_keys == ("array", "slice")
    topic = next(item for item in topics if item.topic_key == "array")
    assert len(topic.entry_ids) == 2


def test_section_topic_does_not_import_later_table_by_lexical_match() -> None:
    result = _build(
        [
            ("heading", "# Proficiency Bonus", []),
            (
                "paragraph",
                "A proficiency bonus provides a rule modifier.",
                ["A proficiency bonus provides a rule modifier."],
            ),
            ("heading", "# Exhaustion Effects", []),
            (
                "table-block",
                "A creature cannot benefit from any bonus to speed.\n"
                "Table- Exhaustion Effects\n"
                "Level Effect\n"
                "1 Disadvantage on checks",
                [],
            ),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)

    target = next(item for item in plan.page_targets if item.topic_key == "proficiency-bonus")
    assert target.atom_ids == ()


def test_same_named_table_only_attaches_to_source_ancestry_section() -> None:
    result = _build(
        [
            ("heading", "# First Branch", []),
            ("heading", "## Shared Matrix", []),
            (
                "table-block",
                "Shared Matrix\nValue Meaning\n1 First branch value\n2 First branch option",
                [],
            ),
            ("heading", "# Second Branch", []),
            ("heading", "## Shared Matrix", []),
            (
                "paragraph",
                "The second branch describes a separate matrix.",
                ["The second branch describes a separate matrix."],
            ),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)

    by_path = {
        result.document_structure.label_path(target.structure_node_id): target
        for target in plan.page_targets
    }
    assert by_path[("First Branch", "Shared Matrix")].atom_ids
    second = by_path.get(("Second Branch", "Shared Matrix"))
    assert second is None or second.atom_ids == ()


def test_comma_label_does_not_seed_component_concepts() -> None:
    result = _build(
        [
            ("heading", "# Widget, advanced", []),
            ("paragraph", "Widget advanced provides output.", ["Widget advanced provides output."]),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)

    target = next(item for item in plan.page_targets if item.topic_key == "widget-advanced")
    assert target.concept_keys == ()


def test_discourse_heading_without_section_evidence_does_not_create_page_target() -> None:
    result = _build(
        [
            ("heading", "# But in our case", []),
            (
                "paragraph",
                "Widget has a Draw method so it satisfies the Shape interface.",
                ["Widget has a Draw method so it satisfies the Shape interface."],
            ),
        ]
    )

    plan = build_section_grounded_plan(result.ledger, result.document_structure)

    assert "case" not in {item.topic_key for item in plan.page_targets}
