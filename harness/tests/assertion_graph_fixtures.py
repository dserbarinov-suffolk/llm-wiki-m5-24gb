from __future__ import annotations

from llmwiki.domain.assertion_graph import (
    Assertion,
    AssertionKind,
    AssertionStatus,
    EvidenceSpan,
    ParseStatus,
    ProvenanceActivity,
    ProvenanceActivityKind,
    SourceUnit,
    SourceUnitKind,
    TechnicalAtom,
    TechnicalAtomKind,
)

SOURCE_HASH = "a" * 64


def provenance_activity() -> ProvenanceActivity:
    return ProvenanceActivity(
        id="prv_ingest_1",
        activity_kind=ProvenanceActivityKind.SOURCE_UNIT_EXTRACTION,
        actor="unit-test",
        output_record_ids=("su_intro",),
        source_locator="raw/source.pdf",
    )


def source_unit() -> SourceUnit:
    return SourceUnit(
        id="su_intro",
        source_locator="raw/source.pdf",
        source_hash=SOURCE_HASH,
        source_order=0,
        kind=SourceUnitKind.PARAGRAPH,
        text="A precise source sentence.",
        page_span=(1, 1),
    )


def evidence_span() -> EvidenceSpan:
    return EvidenceSpan(
        id="evs_sentence",
        source_locator="raw/source.pdf",
        source_hash=SOURCE_HASH,
        source_unit_ids=("su_intro",),
        exact_text="A precise source sentence.",
        page_span=(1, 1),
        text_fingerprint="fingerprint-1",
        confidence=1.0,
        provenance_activity_ids=("prv_ingest_1",),
    )


def technical_atom() -> TechnicalAtom:
    return TechnicalAtom(
        id="tat_table_1",
        atom_kind=TechnicalAtomKind.TABLE,
        evidence_span_ids=("evs_sentence",),
        exact_payload="| Name | Value |\n| A | 1 |",
        parse_status=ParseStatus.PARSED,
        source_order=1,
        provenance_activity_ids=("prv_ingest_1",),
    )


def accepted_assertion() -> Assertion:
    return Assertion(
        id="ast_claim_1",
        kind=AssertionKind.SOURCE_CLAIM,
        subject="Character creation",
        predicate="uses",
        object_entity_id="tat_table_1",
        status=AssertionStatus.ACCEPTED,
        confidence=0.9,
        source_unit_ids=("su_intro",),
        evidence_span_ids=("evs_sentence",),
        technical_atom_ids=("tat_table_1",),
        provenance_activity_ids=("prv_ingest_1",),
    )
