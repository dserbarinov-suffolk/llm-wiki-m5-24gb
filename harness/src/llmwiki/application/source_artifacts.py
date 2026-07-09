"""Canonical source artifacts for the KoteKomi ingest flow."""

from __future__ import annotations

import json
from dataclasses import dataclass

from pydantic import BaseModel, ConfigDict

from llmwiki.domain.assertion_graph import (
    EvidenceSelector,
    EvidenceSpan,
    ParseStatus,
    ProvenanceActivity,
    ProvenanceActivityKind,
    SelectorType,
    SourceUnit,
    SourceUnitKind,
    TechnicalAtom,
    TechnicalAtomKind,
)
from llmwiki.domain.ledger.builder import SegmentInput
from llmwiki.domain.ledger.canonical import artifact_fingerprint, short_digest
from llmwiki.domain.ledger.extraction import ExtractedUnitProfile
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT


class CanonicalSourceArtifact(BaseModel):
    """Source-derived records consumed before ledger assembly."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    source_artifact_id: str
    source_artifact_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    provenance_activities: tuple[ProvenanceActivity, ...]
    source_units: tuple[SourceUnit, ...]
    evidence_spans: tuple[EvidenceSpan, ...]
    technical_atoms: tuple[TechnicalAtom, ...]
    segment_ids: tuple[str, ...]


@dataclass(frozen=True)
class CanonicalLedgerSource:
    artifact: CanonicalSourceArtifact
    segment_inputs: tuple[SegmentInput, ...]
    profiles: dict[str, ExtractedUnitProfile]


def build_canonical_ledger_source(
    *,
    source_locator: str,
    source_hash: str,
    segment_inputs: tuple[SegmentInput, ...],
    profiles: dict[str, ExtractedUnitProfile],
) -> CanonicalLedgerSource:
    """Build the canonical source artifact and retain ledger segment inputs."""

    if not segment_inputs:
        raise ValueError("canonical source artifact requires at least one segment")
    provenance = _provenance(source_locator, source_hash, segment_inputs)
    unit_drafts = [_source_unit(source_hash, item) for item in segment_inputs]
    source_units = _with_structure(tuple(unit_drafts))
    evidence_spans = tuple(
        _evidence_span(source_locator, source_hash, unit, provenance.id)
        for unit in source_units
    )
    span_by_unit = {
        unit.id: span for unit, span in zip(source_units, evidence_spans, strict=True)
    }
    technical_atoms = tuple(
        atom
        for unit, item in zip(source_units, segment_inputs, strict=True)
        if (atom := _technical_atom(source_hash, unit, item, span_by_unit, provenance.id))
        is not None
    )
    artifact = _artifact(
        source_locator=source_locator,
        source_hash=source_hash,
        provenance=provenance,
        source_units=source_units,
        evidence_spans=evidence_spans,
        technical_atoms=technical_atoms,
        segment_inputs=segment_inputs,
    )
    return CanonicalLedgerSource(artifact, segment_inputs, profiles)


def canonical_source_artifact_to_json(artifact: CanonicalSourceArtifact) -> str:
    """Serialize a canonical source artifact deterministically."""

    return json.dumps(
        artifact.model_dump(mode="json"),
        sort_keys=True,
        ensure_ascii=False,
        indent=2,
        separators=(",", ": "),
    )


def canonical_source_artifact_from_json(text: str) -> CanonicalSourceArtifact:
    """Parse a canonical source artifact from JSON."""

    return CanonicalSourceArtifact.model_validate_json(text)


def _provenance(
    source_locator: str, source_hash: str, segment_inputs: tuple[SegmentInput, ...]
) -> ProvenanceActivity:
    output_ids = tuple(
        _source_unit_id(source_hash, item.segment.source_order) for item in segment_inputs
    )
    return ProvenanceActivity(
        id=f"prv_{short_digest(source_hash + source_locator)}",
        activity_kind=ProvenanceActivityKind.SOURCE_UNIT_EXTRACTION,
        actor="llmwiki-source-artifact-builder",
        output_record_ids=output_ids,
        source_locator=source_locator,
    )


def _source_unit(source_hash: str, item: SegmentInput) -> SourceUnit:
    seg = item.segment
    return SourceUnit(
        id=_source_unit_id(source_hash, seg.source_order),
        source_locator=seg.source_locator,
        source_hash=seg.source_hash,
        source_order=seg.source_order,
        kind=_source_unit_kind(seg.segment_kind),
        text=seg.text,
        page_span=_page_span(seg.source_page_start, seg.source_page_end),
    )


def _with_structure(units: tuple[SourceUnit, ...]) -> tuple[SourceUnit, ...]:
    parent_by_id: dict[str, str | None] = {}
    heading_stack: list[tuple[int, str]] = []
    for unit in units:
        level = _heading_level(unit)
        if level > 0:
            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()
            parent_by_id[unit.id] = heading_stack[-1][1] if heading_stack else None
            heading_stack.append((level, unit.id))
        else:
            parent_by_id[unit.id] = heading_stack[-1][1] if heading_stack else None

    children_by_parent: dict[str | None, list[str]] = {}
    for unit_id, parent_id in parent_by_id.items():
        children_by_parent.setdefault(parent_id, []).append(unit_id)

    structured = []
    for unit in units:
        parent_id = parent_by_id[unit.id]
        siblings = tuple(item for item in children_by_parent[parent_id] if item != unit.id)
        structured.append(
            unit.model_copy(
                update={
                    "parent_id": parent_id,
                    "child_ids": tuple(children_by_parent.get(unit.id, ())),
                    "sibling_ids": siblings,
                }
            )
        )
    return tuple(structured)


def _evidence_span(
    source_locator: str, source_hash: str, unit: SourceUnit, provenance_id: str
) -> EvidenceSpan:
    selector_value = _page_locator(unit.page_span)
    return EvidenceSpan(
        id=_evidence_id(source_hash, unit.source_order),
        source_locator=source_locator,
        source_hash=source_hash,
        source_unit_ids=(unit.id,),
        exact_text=unit.text.strip(),
        page_span=unit.page_span,
        selectors=(EvidenceSelector(selector_type=SelectorType.PAGE, value=selector_value),),
        text_fingerprint=short_digest(unit.text),
        confidence=1.0,
        provenance_activity_ids=(provenance_id,),
    )


def _technical_atom(
    source_hash: str,
    unit: SourceUnit,
    item: SegmentInput,
    span_by_unit: dict[str, EvidenceSpan],
    provenance_id: str,
) -> TechnicalAtom | None:
    atom_kind = _atom_kind(item.segment.segment_kind)
    if atom_kind is None:
        return None
    context_span_ids: tuple[str, ...] = ()
    if unit.parent_id is not None and unit.parent_id in span_by_unit:
        context_span_ids = (span_by_unit[unit.parent_id].id,)
    return TechnicalAtom(
        id=f"tat_{short_digest(source_hash + item.segment.source_range_id)}",
        atom_kind=atom_kind,
        evidence_span_ids=(span_by_unit[unit.id].id,),
        exact_payload=_atom_payload(item),
        normalized_payload=item.segment.text,
        parse_status=ParseStatus.PARSED,
        context_span_ids=context_span_ids,
        source_order=unit.source_order,
        provenance_activity_ids=(provenance_id,),
    )


def _artifact(
    *,
    source_locator: str,
    source_hash: str,
    provenance: ProvenanceActivity,
    source_units: tuple[SourceUnit, ...],
    evidence_spans: tuple[EvidenceSpan, ...],
    technical_atoms: tuple[TechnicalAtom, ...],
    segment_inputs: tuple[SegmentInput, ...],
) -> CanonicalSourceArtifact:
    draft = CanonicalSourceArtifact(
        source_artifact_id="pending",
        source_artifact_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_locator=source_locator,
        source_hash=source_hash,
        provenance_activities=(provenance,),
        source_units=source_units,
        evidence_spans=evidence_spans,
        technical_atoms=technical_atoms,
        segment_ids=tuple(item.segment.segment_id for item in segment_inputs),
    )
    fingerprint = artifact_fingerprint(
        draft.model_dump(mode="json"),
        exclude=("source_artifact_id", "source_artifact_fingerprint"),
    )
    return draft.model_copy(
        update={
            "source_artifact_id": f"assertion-graph-source-{fingerprint}",
            "source_artifact_fingerprint": fingerprint,
        }
    )


def _source_unit_id(source_hash: str, source_order: int) -> str:
    return f"su_{source_hash[:8]}_{source_order:05d}"


def _evidence_id(source_hash: str, source_order: int) -> str:
    return f"evs_{source_hash[:8]}_{source_order:05d}"


def _source_unit_kind(segment_kind: str) -> SourceUnitKind:
    return {
        "heading": SourceUnitKind.HEADING,
        "code-fence": SourceUnitKind.CODE,
        "table-block": SourceUnitKind.TABLE,
        "formula": SourceUnitKind.FORMULA,
        "figure": SourceUnitKind.FIGURE,
        "list": SourceUnitKind.LIST,
    }.get(segment_kind, SourceUnitKind.PARAGRAPH)


def _atom_kind(segment_kind: str) -> TechnicalAtomKind | None:
    return {
        "code-fence": TechnicalAtomKind.CODE_BLOCK,
        "table-block": TechnicalAtomKind.TABLE,
        "formula": TechnicalAtomKind.FORMULA,
    }.get(segment_kind)


def _atom_payload(item: SegmentInput) -> str:
    seg = item.segment
    return seg.code_text or seg.table_text or seg.formula_text or seg.text


def _heading_level(unit: SourceUnit) -> int:
    if unit.kind != SourceUnitKind.HEADING:
        return 0
    stripped = unit.text.lstrip()
    return len(stripped) - len(stripped.lstrip("#"))


def _page_span(start: int, end: int) -> tuple[int, int]:
    if start <= 0 or end <= 0:
        return (0, 0)
    return (min(start, end), max(start, end))


def _page_locator(page_span: tuple[int, int]) -> str:
    start, end = page_span
    if start <= 0 or end <= 0:
        return "document"
    return f"p.{start}" if start == end else f"p.{start}-{end}"
