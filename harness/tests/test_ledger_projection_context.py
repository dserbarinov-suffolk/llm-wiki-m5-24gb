from llmwiki.domain.ledger.atoms import CodeBlockPayload, TechnicalAtom
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry, SourceStatement
from llmwiki.domain.ledger.ledger import (
    ClaimLedger,
    FamilyLabelScore,
    SourceFamilyAssignment,
    SourceProfile,
)
from llmwiki.domain.ledger.projection_context import build_projection_context
from llmwiki.domain.ledger.structure import (
    DocumentStructure,
    ExtractedUnitDispositionRecord,
    StructureNode,
)
from llmwiki.domain.ledger.topic_render import render_topic_page
from llmwiki.domain.ledger.topics import SourceTopic


def test_topic_projection_renders_source_blocks_and_atom_frames() -> None:
    ledger = _ledger(
        entries=(
            _claim("entry-widget-one", "statement-widget", "range-widget", "A widget stores pins."),
            _claim(
                "entry-widget-two",
                "statement-widget",
                "range-widget",
                "A widget exposes pin order.",
            ),
            _atom_entry("entry-code", "atom-code", "range-code"),
        ),
        atoms=(_code_atom("atom-code", "range-code", "pins := [2]int{7, 9}"),),
        statements=(
            SourceStatement(
                "statement-widget",
                "range-widget",
                "A widget stores pins. A widget exposes pin order.",
                ("entry-widget-one", "entry-widget-two"),
            ),
        ),
    )
    context = build_projection_context(ledger, _structure())
    topic = SourceTopic(
        topic_key="widget",
        label="Widgets",
        page_kind="concept",
        match_terms=("widget",),
        entry_ids=("entry-widget-one", "entry-widget-two"),
        atom_ids=("atom-code",),
        from_heading=True,
        salience=10,
    )

    rendered = render_topic_page(
        topic,
        ledger,
        wiki_page_locator="source-widget",
        source_page_id="source",
        projection_context=context,
    )

    body = rendered.page_body
    assert "- A widget stores pins. A widget exposes pin order." in body
    assert "- A widget exposes pin order." not in body
    assert "### Widgets" in body
    assert "### Technical frame 1: Widgets" in body
    assert "**Context:** _(source.pdf (range-widget))_" in body
    assert "pins := [2]int{7, 9}" in body
    kinds = {entry.projection_coverage_unit_kind for entry in rendered.coverage.entries}
    assert "projected-evidence-block" in kinds
    assert "technical-atom-frame" in kinds


def test_topic_projection_groups_ambiguous_claims_by_source_section() -> None:
    ledger = _ledger(
        entries=(
            _claim(
                "entry-limitation",
                "statement-limitation",
                "range-limitation",
                "This applies only after the meter is armed.",
                node_id="node-calibration",
                subject="This",
            ),
        ),
        atoms=(),
        statements=(
            SourceStatement(
                "statement-limitation",
                "range-limitation",
                "This applies only after the meter is armed.",
                ("entry-limitation",),
            ),
        ),
    )
    context = build_projection_context(ledger, _nested_structure())
    topic = SourceTopic(
        topic_key="meter",
        label="Meter",
        page_kind="concept",
        match_terms=("meter",),
        entry_ids=("entry-limitation",),
        atom_ids=(),
        from_heading=True,
        salience=3,
    )

    rendered = render_topic_page(
        topic,
        ledger,
        wiki_page_locator="source-meter",
        source_page_id="source",
        projection_context=context,
    )

    assert "### Instruments / Calibration" in rendered.page_body
    assert (
        "- This applies only after the meter is armed. _(source.pdf (range-limitation))_"
        in rendered.page_body
    )


def _structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-widget",
                "section",
                "Widgets",
                "range-heading",
                "source.pdf",
                1,
                parent_structure_node_id="root",
            ),
        ),
        (
            ExtractedUnitDispositionRecord("unit-heading", "range-heading", "structural", 1),
            ExtractedUnitDispositionRecord("unit-widget", "range-widget", "accepted", 2),
            ExtractedUnitDispositionRecord("unit-code", "range-code", "accepted", 3),
        ),
    )


def _nested_structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-instruments",
                "chapter",
                "Instruments",
                "range-instruments",
                "source.pdf",
                1,
                parent_structure_node_id="root",
            ),
            StructureNode(
                "node-calibration",
                "section",
                "Calibration",
                "range-calibration",
                "source.pdf",
                2,
                parent_structure_node_id="node-instruments",
            ),
        ),
        (
            ExtractedUnitDispositionRecord(
                "unit-instruments", "range-instruments", "structural", 1
            ),
            ExtractedUnitDispositionRecord(
                "unit-calibration", "range-calibration", "structural", 2
            ),
            ExtractedUnitDispositionRecord("unit-limitation", "range-limitation", "accepted", 3),
        ),
    )


def _claim(
    entry_id: str,
    statement_id: str,
    range_id: str,
    text: str,
    *,
    node_id: str = "node-widget",
    subject: str = "Widget",
) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=statement_id,
        ledger_entry_kind="claim",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="source.pdf",
        source_hash="sourcehash",
        source_range_id=range_id,
        evidence_ids=(range_id,),
        source_text=text,
        structure_node_ids=(node_id,),
        normalized_text=text,
        subject=subject,
        predicate="has detail",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
    )


def _atom_entry(entry_id: str, atom_id: str, range_id: str) -> LedgerEntry:
    return LedgerEntry(
        ledger_entry_id=entry_id,
        source_statement_id=f"statement-{entry_id}",
        ledger_entry_kind="technical-atom",
        ledger_entry_status="usable",
        extraction_confidence="high",
        confidence_basis=ConfidenceBasis("test"),
        source_locator="source.pdf",
        source_hash="sourcehash",
        source_range_id=range_id,
        evidence_ids=(range_id,),
        source_text="",
        structure_node_ids=("node-widget",),
        technical_atom_kind="code-block",
        technical_atom_id=atom_id,
    )


def _code_atom(atom_id: str, range_id: str, text: str) -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id=atom_id,
        technical_atom_kind="code-block",
        payload=CodeBlockPayload(
            raw_code_text=text,
            parse_status="parsed",
            source_locator="source.pdf",
            language_tag="go",
        ),
        source_locator="source.pdf",
        source_range_id=range_id,
        evidence_ids=(range_id,),
    )


def _ledger(
    *,
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
    statements: tuple[SourceStatement, ...],
) -> ClaimLedger:
    return ClaimLedger(
        claim_ledger_id="ledger",
        source_locator="source.pdf",
        source_hash="sourcehash",
        evidence_registry_hash="registry",
        source_profile=SourceProfile(
            source_locator="source.pdf",
            unit_count=len(entries),
            accepted_entry_count=len(entries),
            claim_count=len([entry for entry in entries if entry.ledger_entry_kind == "claim"]),
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={"code-block": len(atoms)},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("coding", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=entries,
        technical_atoms=atoms,
        technical_atom_contexts=(),
        source_statements=statements,
        extractor_decisions=(),
        rejected_candidates=(),
    )
