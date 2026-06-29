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
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink
from llmwiki.domain.ledger.walkability import audit_related_links, related_link_markdown
from llmwiki.runtime.ledger_pages import build_topic_pages


def test_walkability_accepts_and_explains_shared_source_evidence() -> None:
    ledger = _ledger(
        entries=(
            _claim(
                "entry-calibration",
                "statement-calibration",
                "range-calibration",
                "Only the operator can calibrate the meter.",
            ),
        ),
        statements=(
            SourceStatement(
                "statement-calibration",
                "range-calibration",
                "The operator controls the meter. Only the operator can calibrate it.",
                ("entry-calibration",),
            ),
        ),
    )
    context = build_projection_context(ledger, _structure())

    report = audit_related_links(
        "source-meter",
        (
            RelatedTopicLink(
                "source-operator",
                "Operator",
                "shared statements",
                shared_entry_ids=("entry-calibration",),
            ),
        ),
        ledger,
        projection_context=context,
    )

    assert report.rejected_links == ()
    assert report.accepted_count == 1
    line = related_link_markdown(report.accepted_links[0])
    assert "[[source-operator]] - shared statements: Operator shares source evidence" in line
    assert "The operator controls the meter." in line
    assert "(1 shared statement(s))" in line


def test_walkability_rejects_links_without_support() -> None:
    report = audit_related_links(
        "source-meter",
        (RelatedTopicLink("source-ghost", "Ghost", "shared statements"),),
        _ledger(),
    )

    assert report.accepted_links == ()
    assert report.rejected_count == 1
    assert report.findings[0].finding_type == "unsupported-link"


def test_walkability_rejects_missing_support_ids() -> None:
    report = audit_related_links(
        "source-meter",
        (
            RelatedTopicLink(
                "source-operator",
                "Operator",
                "shared statements",
                shared_entry_ids=("missing-entry",),
            ),
        ),
        _ledger(),
    )

    assert report.accepted_links == ()
    assert report.rejected_count == 1
    assert report.findings[0].finding_type == "missing-support"


def test_walkability_accepts_source_structure_links() -> None:
    report = audit_related_links(
        "source-section-child",
        (
            RelatedTopicLink(
                "source-section-parent",
                "Chapter 1 / Meter Setup",
                "broader source section",
            ),
        ),
        _ledger(),
    )

    assert report.rejected_links == ()
    assert related_link_markdown(report.accepted_links[0]) == (
        "- [[source-section-parent]] - broader source section: Chapter 1 / Meter Setup"
    )


def test_topic_pages_render_bidirectional_related_links() -> None:
    pages = build_topic_pages(
        (
            SourceTopic(
                topic_key="sequence",
                label="Sequence",
                page_kind="concept",
                match_terms=("sequence",),
                entry_ids=(),
                atom_ids=("atom-code",),
                from_heading=False,
                salience=3.0,
            ),
            SourceTopic(
                topic_key="ordered-sequence",
                label="Ordered Sequence",
                page_kind="concept",
                match_terms=("ordered", "sequence"),
                entry_ids=(),
                atom_ids=("atom-code",),
                from_heading=False,
                salience=2.0,
            ),
        ),
        _ledger(atoms=(_code_atom(),)),
        source_page_id="source",
        source_locator="source.md",
        today="2026-06-29",
    )

    by_id = {page.page_id: page.page_body for page in pages}
    assert (
        "[[source-ordered-sequence]] - narrower topic: Ordered Sequence shares technical "
        "code-block: item => item + 1 (1 shared atom(s))"
    ) in by_id["source-sequence"]
    assert (
        "[[source-sequence]] - broader topic: Sequence shares technical code-block: "
        "item => item + 1 (1 shared atom(s))"
    ) in by_id["source-ordered-sequence"]


def _structure() -> DocumentStructure:
    return DocumentStructure(
        "root",
        (
            StructureNode("root", "root", "source.pdf", "root", "source.pdf", 0),
            StructureNode(
                "node-meter",
                "section",
                "Meter",
                "range-heading",
                "source.pdf",
                1,
                parent_structure_node_id="root",
            ),
        ),
        (
            ExtractedUnitDispositionRecord("unit-heading", "range-heading", "structural", 1),
            ExtractedUnitDispositionRecord("unit-calibration", "range-calibration", "accepted", 2),
        ),
    )


def _claim(entry_id: str, statement_id: str, range_id: str, text: str) -> LedgerEntry:
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
        structure_node_ids=("node-meter",),
        normalized_text=text,
        subject="Meter",
        predicate="has calibration rule",
        object_value=text,
        polarity="positive",
        claim_force="asserted",
    )


def _code_atom() -> TechnicalAtom:
    return TechnicalAtom(
        technical_atom_id="atom-code",
        technical_atom_kind="code-block",
        payload=CodeBlockPayload(
            raw_code_text="item => item + 1",
            parse_status="parsed",
            source_locator="source.md",
            language_tag="javascript",
        ),
        source_locator="source.md",
        source_range_id="source-range-code",
        evidence_ids=("evidence-code",),
    )


def _ledger(
    entries: tuple[LedgerEntry, ...] = (),
    statements: tuple[SourceStatement, ...] = (),
    atoms: tuple[TechnicalAtom, ...] = (),
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
            claim_count=len(entries),
            event_count=0,
            concept_count=0,
            relationship_count=0,
            atom_kind_counts={"code-block": len(atoms)},
            feature_signal_means={},
        ),
        source_family_assignment=SourceFamilyAssignment(
            labels=(FamilyLabelScore("general-prose", 1.0),),
            assignment_confidence=1.0,
        ),
        entries=entries,
        technical_atoms=atoms,
        technical_atom_contexts=(),
        source_statements=statements,
        extractor_decisions=(),
        rejected_candidates=(),
    )
