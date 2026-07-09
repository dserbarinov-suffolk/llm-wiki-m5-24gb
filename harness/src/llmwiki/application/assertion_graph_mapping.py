"""Map accepted ledger state into assertion graph domain records."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.application.source_artifacts import CanonicalSourceArtifact
from llmwiki.domain.assertion_graph import (
    Assertion,
    AssertionKind,
    AssertionStatus,
    EvidenceSpan,
    ParseStatus,
    SourceUnit,
    TechnicalAtom,
    TechnicalAtomKind,
)
from llmwiki.domain.ledger.atoms import TechnicalAtom as LedgerTechnicalAtom
from llmwiki.domain.ledger.atoms import atom_raw_text
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger


@dataclass(frozen=True)
class SourceIndex:
    unit_by_range: dict[str, SourceUnit]
    span_by_range: dict[str, EvidenceSpan]
    unit_by_id: dict[str, SourceUnit]
    span_by_unit: dict[str, EvidenceSpan]
    span_by_id: dict[str, EvidenceSpan]


def build_source_index(
    source_artifact: CanonicalSourceArtifact, ledger: ClaimLedger
) -> SourceIndex:
    unit_by_order = {unit.source_order: unit for unit in source_artifact.source_units}
    unit_by_range: dict[str, SourceUnit] = {}
    for entry in ledger.entries:
        if entry.source_range_id not in unit_by_range and (
            unit := unit_by_order.get(_source_order(entry))
        ):
            unit_by_range[entry.source_range_id] = unit
    span_by_unit = {
        span.source_unit_ids[0]: span
        for span in source_artifact.evidence_spans
        if len(span.source_unit_ids) == 1
    }
    span_by_range = {
        source_range_id: span_by_unit[unit.id]
        for source_range_id, unit in unit_by_range.items()
        if unit.id in span_by_unit
    }
    return SourceIndex(
        unit_by_range=unit_by_range,
        span_by_range=span_by_range,
        unit_by_id={unit.id: unit for unit in source_artifact.source_units},
        span_by_unit=span_by_unit,
        span_by_id={span.id: span for span in source_artifact.evidence_spans},
    )


def accepted_assertions(ledger: ClaimLedger, index: SourceIndex) -> tuple[Assertion, ...]:
    provenance_id = assertion_activity_id(ledger)
    return tuple(
        _assertion(entry, index.span_by_range[entry.source_range_id], provenance_id)
        for entry in ledger.entries
        if _assertion_eligible(entry, index)
    )


def accepted_technical_atoms(ledger: ClaimLedger, index: SourceIndex) -> tuple[TechnicalAtom, ...]:
    provenance_id = assertion_activity_id(ledger)
    return tuple(
        _technical_atom(atom, index, provenance_id)
        for atom in ledger.technical_atoms
        if atom.source_range_id in index.span_by_range
    )


def unit_for_span(span_id: str, index: SourceIndex) -> SourceUnit:
    span = index.span_by_id[span_id]
    return index.unit_by_id[span.source_unit_ids[0]]


def same_parent_or_unit(first_id: str, second_id: str, index: SourceIndex) -> bool:
    first = index.unit_by_id[first_id]
    second = index.unit_by_id[second_id]
    return first.id == second.id or first.parent_id == second.parent_id


def unit_order(unit_id: str, index: SourceIndex) -> int:
    return index.unit_by_id[unit_id].source_order


def graph_record_id(prefix: str, *parts: str) -> str:
    return f"{prefix}_{short_digest('|'.join(parts))}"


def assertion_activity_id(ledger: ClaimLedger) -> str:
    return graph_record_id("prv", ledger.source_hash, "assertion-graph-build")


def assertion_source_span_ids(assertions: tuple[Assertion, ...]) -> frozenset[str]:
    return frozenset(span_id for assertion in assertions for span_id in assertion.evidence_span_ids)


def technical_atom_span_ids(atoms: tuple[TechnicalAtom, ...]) -> frozenset[str]:
    return frozenset(span_id for atom in atoms for span_id in atom.evidence_span_ids)


def _source_order(entry: LedgerEntry) -> int:
    return int(entry.source_range_id.rsplit("-", 1)[-1]) if "-" in entry.source_range_id else 0


def _assertion_eligible(entry: LedgerEntry, index: SourceIndex) -> bool:
    return (
        entry.ledger_entry_status == "usable"
        and entry.ledger_entry_kind in {"claim", "event", "concept"}
        and entry.source_range_id in index.span_by_range
    )


def _assertion(entry: LedgerEntry, span: EvidenceSpan, provenance_id: str) -> Assertion:
    return Assertion(
        id=graph_record_id("ast", entry.ledger_entry_id),
        kind=_assertion_kind(entry),
        subject=entry.subject or "source statement",
        predicate=entry.predicate or "states",
        object_value=entry.object_value or entry.normalized_text or entry.source_text,
        status=AssertionStatus.ACCEPTED,
        confidence=_confidence(entry.extraction_confidence),
        source_unit_ids=span.source_unit_ids,
        evidence_span_ids=(span.id,),
        provenance_activity_ids=(provenance_id,),
    )


def _assertion_kind(entry: LedgerEntry) -> AssertionKind:
    if entry.ledger_entry_kind == "concept":
        return AssertionKind.DEFINITION
    if entry.ledger_entry_kind == "event":
        return AssertionKind.EVENT_STATEMENT
    if entry.claim_force in {"required", "forbidden", "permitted", "recommended"}:
        return AssertionKind.RULE_STATEMENT
    if "example" in entry.claim_role_tags:
        return AssertionKind.EXAMPLE_STATEMENT
    return AssertionKind.SOURCE_CLAIM


def _technical_atom(
    atom: LedgerTechnicalAtom, index: SourceIndex, provenance_id: str
) -> TechnicalAtom:
    span = index.span_by_range[atom.source_range_id]
    return TechnicalAtom(
        id=graph_record_id("tat", atom.technical_atom_id),
        atom_kind=_technical_atom_kind(atom.technical_atom_kind),
        evidence_span_ids=(span.id,),
        exact_payload=atom_raw_text(atom.payload),
        normalized_payload=atom_raw_text(atom.payload),
        parse_status=_parse_status(atom.parse_status),
        context_span_ids=_context_span_ids(span, index),
        source_order=index.unit_by_range[atom.source_range_id].source_order,
        provenance_activity_ids=(provenance_id,),
    )


def _technical_atom_kind(kind: str) -> TechnicalAtomKind:
    return {
        "code-block": TechnicalAtomKind.CODE_BLOCK,
        "worked-example": TechnicalAtomKind.EXAMPLE,
        "table": TechnicalAtomKind.TABLE,
        "formula": TechnicalAtomKind.FORMULA,
        "rule": TechnicalAtomKind.RULE,
        "procedure": TechnicalAtomKind.PROCEDURE,
        "figure": TechnicalAtomKind.DIAGRAM,
    }.get(kind, TechnicalAtomKind.STRUCTURED_RECORD)


def _parse_status(status: str) -> ParseStatus:
    return {
        "parsed": ParseStatus.PARSED,
        "partially-parsed": ParseStatus.PARTIAL,
        "unparsed": ParseStatus.UNPARSED,
    }.get(status, ParseStatus.PARTIAL)


def _context_span_ids(span: EvidenceSpan, index: SourceIndex) -> tuple[str, ...]:
    unit = unit_for_span(span.id, index)
    if unit.parent_id and unit.parent_id in index.span_by_unit:
        return (index.span_by_unit[unit.parent_id].id,)
    return ()


def _confidence(value: str) -> float:
    return {"high": 0.9, "medium": 0.65, "low": 0.35}.get(value, 0.35)
