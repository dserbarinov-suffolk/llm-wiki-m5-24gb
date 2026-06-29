from llmwiki.domain.ledger.atoms import TablePayload, TechnicalAtom
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


def test_table_frame_prefers_table_caption_and_omits_unrelated_nearby_context() -> None:
    ledger = _ledger(
        entries=(
            _claim("entry-prose", "statement-prose", "range-prose"),
            _table_entry("entry-table", "atom-table", "range-table"),
        ),
        atoms=(_table_atom("atom-table", "range-table", "Table- Calibration Results\nA B\n1 2"),),
        statements=(
            SourceStatement(
                "statement-prose",
                "range-prose",
                "Operators record ordinary notes before the appendix.",
                ("entry-prose",),
            ),
        ),
    )

    context = build_projection_context(ledger, _structure())

    frame = context.frames_for_atoms(("atom-table",))[0]
    assert frame.label == "Calibration Results"
    assert frame.context_block_id == ""


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
            ExtractedUnitDispositionRecord("unit-prose", "range-prose", "accepted", 2),
            ExtractedUnitDispositionRecord("unit-table", "range-table", "accepted", 3),
        ),
    )


def _claim(entry_id: str, statement_id: str, range_id: str) -> LedgerEntry:
    text = "Operators record ordinary notes before the appendix."
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
        structure_node_ids=("node-widget",),
        normalized_text=text,
        subject="Widget",
        predicate="has detail",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
    )


def _table_entry(entry_id: str, atom_id: str, range_id: str) -> LedgerEntry:
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
        technical_atom_kind="table",
        technical_atom_id=atom_id,
    )


def _table_atom(atom_id: str, range_id: str, text: str) -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id=atom_id,
        technical_atom_kind="table",
        payload=TablePayload(
            raw_table_text=text,
            parse_status="parsed",
            source_locator="source.pdf",
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
            claim_count=1,
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={"table": len(atoms)},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("reference", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=entries,
        technical_atoms=atoms,
        technical_atom_contexts=(),
        source_statements=statements,
        extractor_decisions=(),
        rejected_candidates=(),
    )
