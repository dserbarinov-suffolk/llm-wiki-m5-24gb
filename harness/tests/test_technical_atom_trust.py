from llmwiki.domain.ledger.atoms import (
    AtomPayload,
    CodeBlockPayload,
    TableCell,
    TableColumn,
    TablePayload,
    TableRow,
    TechnicalAtom,
)
from llmwiki.domain.ledger.builder import SegmentInput, build_claim_ledger, default_schema_bundle
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.pointers import claim_ledger_pointer, document_structure_pointer
from llmwiki.domain.ledger.projection import ProjectionSourceSupport, plan_source_page
from llmwiki.domain.ledger.renderer import render_source_page
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.technical_atom_trust import (
    REVIEW_ONLY,
    TRUSTED,
    assess_technical_atom_trust,
)

_HASH = "a" * 64


def test_clean_table_atom_is_trusted() -> None:
    atom = _atom(
        "table",
        TablePayload(
            raw_table_text="| Name | Cost |\n| --- | --- |\n| Rope | 5 |\n| Torch | 1 |",
            parse_status="parsed",
            source_locator="source.pdf",
            columns=(TableColumn(0, "Name"), TableColumn(1, "Cost")),
            rows=(TableRow(0), TableRow(1)),
            cells=(
                TableCell(0, 0, "Rope"),
                TableCell(0, 1, "5"),
                TableCell(1, 0, "Torch"),
                TableCell(1, 1, "1"),
            ),
        ),
    )

    decision = assess_technical_atom_trust(atom)

    assert decision.trust_status == TRUSTED
    assert decision.projection_policy == "authoritative"


def test_table_with_interleaved_prose_is_review_only() -> None:
    atom = _atom(
        "table",
        TablePayload(
            raw_table_text=(
                "Table 1 Example\n"
                "This paragraph explains something in a full sentence.\n"
                "Another narrative line continues outside the tabular grid.\n"
                "| been | determined, | to |\n"
                "| --- | --- | --- |\n"
                "| another sentence with many words. | A | 1 |\n"
                "| stable row | B | 2 |"
            ),
            parse_status="parsed",
            source_locator="source.pdf",
            columns=(TableColumn(0, "been"), TableColumn(1, "determined,"), TableColumn(2, "to")),
            rows=(TableRow(0), TableRow(1)),
            cells=(
                TableCell(0, 0, "another sentence with many words."),
                TableCell(0, 1, "A"),
                TableCell(0, 2, "1"),
                TableCell(1, 0, "stable row"),
                TableCell(1, 1, "B"),
                TableCell(1, 2, "2"),
            ),
        ),
    )

    decision = assess_technical_atom_trust(atom)

    assert decision.trust_status == REVIEW_ONLY
    assert "table-raw-text-contaminated-by-prose" in decision.trust_reasons
    assert decision.projection_policy == "raw-review-only"


def test_partially_parsed_table_is_review_only() -> None:
    atom = _atom(
        "table",
        TablePayload(
            raw_table_text="10 for 12\n10 for 12\n5 for 20",
            parse_status="partially-parsed",
            source_locator="source.pdf",
            columns=(TableColumn(0, "entry"), TableColumn(1, "content")),
            rows=(TableRow(0), TableRow(1), TableRow(2)),
            cells=(
                TableCell(0, 0, "10"),
                TableCell(0, 1, "for 12"),
                TableCell(1, 0, "10"),
                TableCell(1, 1, "for 12"),
                TableCell(2, 0, "5"),
                TableCell(2, 1, "for 20"),
            ),
        ),
    )

    decision = assess_technical_atom_trust(atom)

    assert decision.trust_status == REVIEW_ONLY
    assert "table-parse-incomplete" in decision.trust_reasons


def test_high_confidence_aligned_partial_table_is_trusted() -> None:
    atom = _atom(
        "table",
        TablePayload(
            raw_table_text=(
                "Table- Alpha 1000 Series\n"
                "Model   Voltage   Rating\n"
                "A1001   12V       Standard\n"
                "A1002   24V       Fire"
            ),
            parse_status="partially-parsed",
            source_locator="source.pdf",
            columns=(
                TableColumn(0, "Model"),
                TableColumn(1, "Voltage"),
                TableColumn(2, "Rating"),
            ),
            rows=(TableRow(0), TableRow(1)),
            cells=(
                TableCell(0, 0, "A1001"),
                TableCell(0, 1, "12V"),
                TableCell(0, 2, "Standard"),
                TableCell(1, 0, "A1002"),
                TableCell(1, 1, "24V"),
                TableCell(1, 2, "Fire"),
            ),
        ),
    )

    decision = assess_technical_atom_trust(atom)

    assert decision.trust_status == TRUSTED
    assert decision.projection_policy == "authoritative"


def test_implicit_header_partial_table_is_trusted() -> None:
    atom = _atom(
        "table",
        TablePayload(
            raw_table_text=(
                "Shared Matrix\n"
                "Value Meaning\n"
                "1 First branch value\n"
                "2 First branch option"
            ),
            parse_status="partially-parsed",
            source_locator="source.pdf",
            columns=(TableColumn(0, "entry"), TableColumn(1, "content")),
            rows=(TableRow(0), TableRow(1)),
            cells=(
                TableCell(0, 0, "1"),
                TableCell(0, 1, "First branch value"),
                TableCell(1, 0, "2"),
                TableCell(1, 1, "First branch option"),
            ),
        ),
    )

    decision = assess_technical_atom_trust(atom)

    assert decision.trust_status == TRUSTED
    assert decision.projection_policy == "authoritative"


def test_partial_table_with_low_raw_row_coverage_is_review_only() -> None:
    atom = _atom(
        "table",
        TablePayload(
            raw_table_text=(
                "Table 4: Mixed Layout   Next Column\n"
                "record the selected options.\n"
                "                      Header A   Header B\n"
                "the surrounding paragraph continues.\n"
                "                      value 1    value 2\n"
                "another non-row line appears.\n"
                "                      value 3    value 4"
            ),
            parse_status="partially-parsed",
            source_locator="source.pdf",
            columns=(TableColumn(0, "Table 4: Mixed Layout"), TableColumn(1, "Next Column")),
            rows=(TableRow(0), TableRow(1)),
            cells=(
                TableCell(0, 0, "Header A"),
                TableCell(0, 1, "Header B"),
                TableCell(1, 0, "value 1"),
                TableCell(1, 1, "value 2"),
            ),
        ),
    )

    decision = assess_technical_atom_trust(atom)

    assert decision.trust_status == REVIEW_ONLY
    assert "table-parse-incomplete" in decision.trust_reasons


def test_code_block_with_prose_leakage_is_review_only() -> None:
    atom = _atom(
        "code-block",
        CodeBlockPayload(
            raw_code_text=(
                "const wrap = (value) => [value];\n"
                "Now expand it into a block form:\n"
                "const wrap = (value) => {\n"
                "return [value];\n"
                "}"
            ),
            parse_status="parsed",
            source_locator="source.pdf",
            line_count=5,
        ),
    )

    decision = assess_technical_atom_trust(atom)

    assert decision.trust_status == REVIEW_ONLY
    assert "code-block-contaminated-by-prose" in decision.trust_reasons


def test_review_only_atom_does_not_render_as_authoritative_projection() -> None:
    text = (
        "Table 2 Mixed Results\n"
        "This paragraph is narrative prose and not a table row.\n"
        "Another prose sentence should keep the grid from being authoritative.\n"
        "| been | determined, | to |\n"
        "| --- | --- | --- |\n"
        "| another sentence with many words. | A | 1 |\n"
        "| stable row | B | 2 |"
    )
    result = _build_ledger((("table-block", text),))
    atom = result.ledger.technical_atoms[0]
    atom_entry = next(
        entry for entry in result.ledger.entries if entry.ledger_entry_kind == "technical-atom"
    )

    assert atom.trust_status == REVIEW_ONLY
    assert atom_entry.ledger_entry_status == "needs-review"
    assert not result.ledger.usable_entries
    assert result.document_structure.dispositions[0].disposition == "needs-review"

    support = ProjectionSourceSupport(
        "support",
        _HASH,
        "source.pdf",
        claim_ledger_pointer("claim-ledger", "fingerprint"),
        document_structure_pointer("document-structure", "fingerprint"),
    )
    plan = plan_source_page(
        result.ledger,
        result.document_structure,
        wiki_page_locator="source",
        title="Source",
        source_support=support,
    )
    rendered = render_source_page(plan, result.ledger)

    assert "## Source review" in rendered.page_body
    assert "technical-atom-trust" in rendered.page_body
    assert "rendered-technical-atom-block" not in {
        entry.projection_coverage_unit_kind for entry in rendered.coverage.entries
    }


def _atom(kind: str, payload: AtomPayload) -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id=f"technical-atom-{kind}",
        technical_atom_kind=kind,
        payload=payload,
        source_locator="source.pdf",
        source_range_id="source-range-001",
        evidence_ids=("evidence-001",),
    )


def _build_ledger(specs: tuple[tuple[str, str], ...]):
    segments: list[SegmentInput] = []
    profiles = {}
    for order, (kind, text) in enumerate(specs, start=1):
        segment = SourceSegment(
            segment_id=f"segment-{order:03d}",
            source_range_id=f"source-range-{order:03d}",
            source_locator="source.pdf",
            source_hash=_HASH,
            heading_path="Document",
            structure_node_id="",
            source_order=order,
            text=text,
            segment_kind=kind,
            evidence_ids=(f"evidence-{order:03d}",),
        )
        segments.append(SegmentInput(segment))
        profiles[segment.segment_id] = profile_unit(
            extracted_unit_id=segment.segment_id,
            source_range_id=segment.source_range_id,
            text=text,
            evidence_ids=segment.evidence_ids,
        )
    return build_claim_ledger(
        source_locator="source.pdf",
        source_hash=_HASH,
        evidence_registry_hash="registry",
        segments=tuple(segments),
        profiles=profiles,
        schema=default_schema_bundle(),
    )
