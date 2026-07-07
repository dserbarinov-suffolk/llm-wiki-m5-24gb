"""Source-neutral record boundaries inside authored document structure.

Records are repeated, bounded source units that are not always emitted as
headings by PDF extractors: catalog entries, reference entries, list members,
or item cards. They are structural ownership boundaries, not claims.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger import structure_relations
from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.structure import StructureNode
from llmwiki.domain.ledger.structure_build import StructurePlan

_FIELD_ASSIGNMENT = re.compile(r"(?<!\S)[A-Z][A-Za-z0-9 /()-]{0,36}=")
_BRACKET_GROUP = re.compile(r"(\[|\u300a|\u3010)\s*([^\]\u300b\u3011]{1,96}?)\s*(\]|\u300b|\u3011)")
_DOTTED_IDENTIFIER = re.compile(r"[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)+")
_LABEL_WORD_LIMIT = 10
_MIN_REPEATED_BOUNDARIES = 2


@dataclass(frozen=True)
class SourceRecordBoundary:
    segment_id: str
    source_range_id: str
    source_order: int
    label: str
    parent_node_id: str
    evidence_ids: tuple[str, ...]
    reason_codes: tuple[str, ...]


@dataclass(frozen=True)
class SourceRecord:
    record_node_id: str
    label: str
    parent_node_id: str
    depth: int
    first_source_order: int
    last_source_order: int
    source_range_id: str
    source_locator: str
    evidence_ids: tuple[str, ...]
    field_names: tuple[str, ...]
    reason_codes: tuple[str, ...]


@dataclass(frozen=True)
class SourceRecordPlan:
    records: tuple[SourceRecord, ...]
    node_for_segment: dict[str, str]


def add_source_records_to_structure(
    source_hash: str,
    source_locator: str,
    segments: tuple[SourceSegment, ...],
    structure_plan: StructurePlan,
) -> StructurePlan:
    """Return a structure plan with supported source records inserted."""

    record_plan = build_source_record_plan(source_hash, source_locator, segments, structure_plan)
    if not record_plan.records:
        return structure_plan
    record_nodes = tuple(_record_node(record) for record in record_plan.records)
    nodes = tuple(
        sorted((*structure_plan.nodes, *record_nodes), key=lambda item: item.source_order)
    )
    node_for_segment = dict(structure_plan.node_for_segment)
    node_for_segment.update(record_plan.node_for_segment)
    return StructurePlan(
        structure_plan.root_node_id,
        nodes,
        node_for_segment,
        structure_relations.sibling_relations(nodes),
    )


def build_source_record_plan(
    source_hash: str,
    source_locator: str,
    segments: tuple[SourceSegment, ...],
    structure_plan: StructurePlan,
) -> SourceRecordPlan:
    boundaries = tuple(
        boundary
        for segment in segments
        if (
            boundary := _boundary_for_segment(
                segment, structure_plan.node_for_segment.get(segment.segment_id, "")
            )
        )
        is not None
    )
    supported = _supported_boundaries(boundaries, segments)
    if not supported:
        return SourceRecordPlan((), {})
    node_by_id = {node.structure_node_id: node for node in structure_plan.nodes}
    records = tuple(
        _record_for_boundary(
            source_hash, source_locator, boundary, supported, segments, index, node_by_id
        )
        for index, boundary in enumerate(supported)
    )
    ownership: dict[str, str] = {}
    for record in records:
        for segment in segments:
            if record.first_source_order <= segment.source_order <= record.last_source_order:
                ownership[segment.segment_id] = record.record_node_id
    return SourceRecordPlan(records, ownership)


def _boundary_for_segment(
    segment: SourceSegment, parent_node_id: str
) -> SourceRecordBoundary | None:
    if segment.segment_kind not in {"heading", "paragraph", "list"}:
        return None
    label, reasons = _record_label(segment.text)
    if not label or not parent_node_id:
        return None
    return SourceRecordBoundary(
        segment.segment_id,
        segment.source_range_id,
        segment.source_order,
        label,
        parent_node_id,
        segment.evidence_ids,
        reasons,
    )


def _record_label(text: str) -> tuple[str, tuple[str, ...]]:
    plain = _plain(text)
    groups = _bracket_groups(plain)
    if groups:
        opener, label = groups[-1]
        if opener in ("[", "\u3010") and _short_label(label):
            reasons = ["bracket-record-label"]
            if len(groups) > 1:
                reasons.append("container-plus-record-label")
            return label, tuple(reasons)
    if _field_density(plain) >= 2:
        label = _leading_field_label(plain)
        if label and _short_label(label):
            return label, ("field-dense-record-label",)
    return "", ()


def _supported_boundaries(
    boundaries: tuple[SourceRecordBoundary, ...], segments: tuple[SourceSegment, ...]
) -> tuple[SourceRecordBoundary, ...]:
    counts: dict[str, int] = {}
    for boundary in boundaries:
        counts[boundary.parent_node_id] = counts.get(boundary.parent_node_id, 0) + 1
    supported: list[SourceRecordBoundary] = []
    for index, boundary in enumerate(boundaries):
        has_repeated_peer = counts.get(boundary.parent_node_id, 0) >= _MIN_REPEATED_BOUNDARIES
        has_record_shape = _record_shaped_span(boundary, boundaries, segments, index)
        if has_repeated_peer and has_record_shape:
            supported.append(boundary)
            continue
        if "field-dense-record-label" in boundary.reason_codes and has_record_shape:
            supported.append(boundary)
    return tuple(supported)


def _record_for_boundary(
    source_hash: str,
    source_locator: str,
    boundary: SourceRecordBoundary,
    boundaries: tuple[SourceRecordBoundary, ...],
    segments: tuple[SourceSegment, ...],
    index: int,
    node_by_id: dict[str, StructureNode],
) -> SourceRecord:
    next_order = _next_boundary_order(boundary, boundaries, index)
    last_order = _last_order_before(segments, boundary.source_order, next_order)
    field_names = _field_names(segments, boundary.source_order, last_order)
    record_id = deterministic_id(
        "structure-node",
        source_hash,
        boundary.source_range_id,
        "record",
        short_digest(boundary.label.lower()),
    )
    return SourceRecord(
        record_id,
        boundary.label,
        boundary.parent_node_id,
        node_by_id.get(boundary.parent_node_id, StructureNode("", "", "", "", "", 0)).depth + 1,
        boundary.source_order,
        last_order,
        boundary.source_range_id,
        source_locator,
        boundary.evidence_ids,
        field_names,
        boundary.reason_codes,
    )


def _record_node(record: SourceRecord) -> StructureNode:
    return StructureNode(
        record.record_node_id,
        "record",
        record.label,
        record.source_range_id,
        record.source_locator,
        record.first_source_order,
        record.depth,
        record.parent_node_id,
        record.evidence_ids,
    )


def _record_shaped_span(
    boundary: SourceRecordBoundary,
    boundaries: tuple[SourceRecordBoundary, ...],
    segments: tuple[SourceSegment, ...],
    index: int,
) -> bool:
    next_order = _next_boundary_order(boundary, boundaries, index)
    last_order = _last_order_before(segments, boundary.source_order, next_order)
    return len(_field_names(segments, boundary.source_order, last_order)) >= 2


def _next_boundary_order(
    boundary: SourceRecordBoundary, boundaries: tuple[SourceRecordBoundary, ...], index: int
) -> int:
    for candidate in boundaries[index + 1 :]:
        if candidate.source_order > boundary.source_order:
            return candidate.source_order
    return 0


def _last_order_before(
    segments: tuple[SourceSegment, ...], start_order: int, next_boundary_order: int
) -> int:
    last_order = start_order
    for segment in segments:
        if segment.source_order < start_order:
            continue
        if next_boundary_order and segment.source_order >= next_boundary_order:
            break
        if segment.source_order > start_order and segment.segment_kind == "heading":
            break
        last_order = segment.source_order
    return last_order


def _field_names(
    segments: tuple[SourceSegment, ...], start_order: int, last_order: int
) -> tuple[str, ...]:
    names: list[str] = []
    for segment in segments:
        if not start_order <= segment.source_order <= last_order:
            continue
        for match in _FIELD_ASSIGNMENT.finditer(segment.text):
            name = match.group(0).split("=", 1)[0].strip()
            if name:
                names.append(name)
    return tuple(dict.fromkeys(names))


def _bracket_groups(text: str) -> tuple[tuple[str, str], ...]:
    return tuple(
        (match.group(1), match.group(2).strip()) for match in _BRACKET_GROUP.finditer(text)
    )


def _field_density(text: str) -> int:
    return len(_FIELD_ASSIGNMENT.findall(text))


def _leading_field_label(text: str) -> str:
    first = _FIELD_ASSIGNMENT.search(text)
    return text[: first.start()].strip(" :-") if first else ""


def _plain(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"^\s{0,3}#{1,6}\s*", "", text)).strip()


def _short_label(text: str) -> bool:
    stripped = text.strip()
    return (
        bool(stripped)
        and any(char.isalpha() for char in stripped)
        and not _DOTTED_IDENTIFIER.fullmatch(stripped)
        and len(stripped.split()) <= _LABEL_WORD_LIMIT
        and len(stripped) <= 96
    )
