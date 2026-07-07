"""Build a DocumentStructure from ordered source segments.

Heading segments become structure nodes. Depth comes first from extracted
heading level, then from source-authored numbering when a PDF extractor flattens
or splits numbered headings. Both are reusable structural signals rather than
source-specific shims.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from llmwiki.domain.ledger import structure_numbers, structure_relations
from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.structure import StructureNode, StructureRelation

_DEPTH_KIND = {1: "chapter", 2: "section"}
_PENDING_NUMBER_MARKER_WINDOW = 24


@dataclass(frozen=True)
class StructurePlan:
    root_node_id: str
    nodes: tuple[StructureNode, ...]
    node_for_segment: dict[str, str]
    relations: tuple[StructureRelation, ...] = ()


@dataclass(frozen=True)
class _OpenHeading:
    depth: int
    node_id: str
    canonical_label: str
    number_path: tuple[int, ...]
    is_number_marker: bool
    title_bound: bool = True


@dataclass(frozen=True)
class _PendingNumberMarker:
    heading: _OpenHeading
    stack: tuple[_OpenHeading, ...]
    previous_node_id: str
    source_order: int


def build_structure(
    source_hash: str, source_locator: str, segments: tuple[SourceSegment, ...]
) -> StructurePlan:
    root_id = deterministic_id("structure-node", source_hash, "root", "root")
    root = StructureNode(
        structure_node_id=root_id,
        structure_node_kind="root",
        heading_text=source_locator,
        source_range_id="root",
        source_locator=source_locator,
        source_order=0,
    )
    nodes: list[StructureNode] = [root]
    node_for_segment: dict[str, str] = {}
    open_headings: list[_OpenHeading] = []
    pending_markers: dict[tuple[int, ...], _PendingNumberMarker] = {}
    for index, segment in enumerate(segments):
        order = index + 1
        if segment.segment_kind == "heading":
            _add_heading(
                source_hash,
                root_id,
                segment,
                tuple(segments),
                index,
                order,
                nodes,
                node_for_segment,
                open_headings,
                pending_markers,
            )
            continue
        node_for_segment[segment.segment_id] = _node_for_non_heading(
            open_headings, pending_markers, segment, root_id
        )
    structure_nodes = tuple(nodes)
    return StructurePlan(
        root_id,
        structure_nodes,
        node_for_segment,
        structure_relations.sibling_relations(structure_nodes),
    )


def _add_heading(
    source_hash: str,
    root_id: str,
    segment: SourceSegment,
    segments: tuple[SourceSegment, ...],
    index: int,
    order: int,
    nodes: list[StructureNode],
    node_for_segment: dict[str, str],
    open_headings: list[_OpenHeading],
    pending_markers: dict[tuple[int, ...], _PendingNumberMarker],
) -> None:
    depth = _heading_depth(segment)
    heading_text = structure_numbers.heading_text(segment.text)
    canonical_label = structure_numbers.canonical_heading_label(heading_text)
    number_path = structure_numbers.heading_number_path(canonical_label)
    is_number_marker = structure_numbers.is_number_marker(canonical_label, number_path)
    previous_node_id = _previous_node_id(open_headings, root_id)
    pending = _pending_marker_for_title(pending_markers, canonical_label, segments, index, order)
    if pending is not None:
        _bind_pending_marker(pending, heading_text, segment, nodes, node_for_segment, open_headings)
        pending_markers.pop(pending.heading.number_path, None)
        return
    _pop_closed_headings(open_headings, depth, number_path)
    if _same_unbound_number_marker(open_headings, number_path, is_number_marker):
        node_for_segment[segment.segment_id] = open_headings[-1].node_id
        return
    while open_headings and structure_numbers.number_conflicts(
        open_headings[-1].number_path, number_path
    ):
        open_headings.pop()
    _bind_top_level_unnumbered_container(open_headings, number_path)
    if (
        open_headings
        and canonical_label
        and structure_numbers.same_heading(open_headings[-1].canonical_label, canonical_label)
    ):
        node_for_segment[segment.segment_id] = open_headings[-1].node_id
        return
    parent_id = open_headings[-1].node_id if open_headings else root_id
    node_id = deterministic_id(
        "structure-node",
        source_hash,
        segment.source_range_id,
        _DEPTH_KIND.get(depth, "heading"),
        short_digest(heading_text.lower()),
    )
    nodes.append(
        StructureNode(
            structure_node_id=node_id,
            structure_node_kind=_DEPTH_KIND.get(depth, "heading"),
            heading_text=heading_text,
            source_range_id=segment.source_range_id,
            source_locator=segment.source_locator,
            source_order=order,
            depth=depth,
            parent_structure_node_id=parent_id,
            evidence_ids=segment.evidence_ids,
        )
    )
    heading = _OpenHeading(
        depth,
        node_id,
        canonical_label,
        number_path,
        is_number_marker,
        title_bound=not is_number_marker,
    )
    open_headings.append(heading)
    if is_number_marker:
        pending_markers[number_path] = _PendingNumberMarker(
            heading=heading,
            stack=tuple(open_headings),
            previous_node_id=previous_node_id,
            source_order=order,
        )
    node_for_segment[segment.segment_id] = node_id


def _bind_top_level_unnumbered_container(
    open_headings: list[_OpenHeading], number_path: tuple[int, ...]
) -> None:
    if not open_headings or len(number_path) < 3:
        return
    current = open_headings[-1]
    if current.number_path or current.depth != 1 or current.is_number_marker:
        return
    inferred_parent = number_path[:-1]
    open_headings[-1] = replace(current, number_path=inferred_parent)


def _heading_depth(segment: SourceSegment) -> int:
    for block in segment.source_blocks:
        level = getattr(block, "heading_level", 0)
        if isinstance(level, int) and level > 0:
            return level
    stripped = segment.text.lstrip()
    depth = len(stripped) - len(stripped.lstrip("#"))
    return depth if depth > 0 else 1


def _pop_closed_headings(
    open_headings: list[_OpenHeading], depth: int, number_path: tuple[int, ...]
) -> None:
    while open_headings and open_headings[-1].depth >= depth:
        if structure_numbers.number_parent(open_headings[-1].number_path, number_path):
            break
        if open_headings[-1].is_number_marker and open_headings[-1].title_bound and not number_path:
            break
        open_headings.pop()


def _same_unbound_number_marker(
    open_headings: list[_OpenHeading], number_path: tuple[int, ...], is_number_marker: bool
) -> bool:
    return bool(
        open_headings
        and number_path
        and open_headings[-1].number_path == number_path
        and is_number_marker
    )


def _pending_marker_for_title(
    pending_markers: dict[tuple[int, ...], _PendingNumberMarker],
    canonical_label: str,
    segments: tuple[SourceSegment, ...],
    index: int,
    order: int,
) -> _PendingNumberMarker | None:
    for pending in sorted(pending_markers.values(), key=lambda item: -item.source_order):
        if order - pending.source_order > _PENDING_NUMBER_MARKER_WINDOW:
            continue
        if order - pending.source_order == 1:
            return pending
        if _nearby_numbered_title(pending.heading.number_path, canonical_label, segments, index):
            return pending
    return None


def _nearby_numbered_title(
    number_path: tuple[int, ...],
    canonical_label: str,
    segments: tuple[SourceSegment, ...],
    index: int,
) -> bool:
    for segment in segments[index : index + 4]:
        candidate = structure_numbers.canonical_heading_label(
            structure_numbers.heading_text(segment.text)
        )
        if structure_numbers.heading_number_path(candidate) == number_path and (
            structure_numbers.same_heading(candidate, canonical_label)
        ):
            return True
    return False


def _bind_pending_marker(
    pending: _PendingNumberMarker,
    heading_text: str,
    segment: SourceSegment,
    nodes: list[StructureNode],
    node_for_segment: dict[str, str],
    open_headings: list[_OpenHeading],
) -> None:
    bound_text = structure_numbers.numbered_title(pending.heading.number_path, heading_text)
    canonical_label = structure_numbers.canonical_heading_label(bound_text)
    bound = replace(pending.heading, canonical_label=canonical_label, title_bound=True)
    _replace_node_heading(nodes, bound.node_id, bound_text, segment.evidence_ids)
    open_headings[:] = [*pending.stack[:-1], bound]
    node_for_segment[segment.segment_id] = bound.node_id


def _replace_node_heading(
    nodes: list[StructureNode], node_id: str, heading_text: str, evidence_ids: tuple[str, ...]
) -> None:
    for index, node in enumerate(nodes):
        if node.structure_node_id != node_id:
            continue
        nodes[index] = replace(
            node,
            heading_text=heading_text,
            evidence_ids=tuple(dict.fromkeys((*node.evidence_ids, *evidence_ids))),
        )
        return


def _previous_node_id(open_headings: list[_OpenHeading], root_id: str) -> str:
    for heading in reversed(open_headings):
        if heading.title_bound or not heading.is_number_marker:
            return heading.node_id
    return root_id


def _node_for_non_heading(
    open_headings: list[_OpenHeading],
    pending_markers: dict[tuple[int, ...], _PendingNumberMarker],
    segment: SourceSegment,
    root_id: str,
) -> str:
    if not open_headings:
        return root_id
    current = open_headings[-1]
    if not current.is_number_marker or current.title_bound:
        return current.node_id
    pending = pending_markers.get(current.number_path)
    if pending is None:
        return current.node_id
    if (
        structure_numbers.heading_number_path(
            structure_numbers.canonical_heading_label(segment.text)
        )
        == current.number_path
    ):
        return current.node_id
    return pending.previous_node_id
