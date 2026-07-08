"""Source-neutral hierarchy reconciliation for numbered document headings."""

from __future__ import annotations

from dataclasses import replace

from llmwiki.domain.ledger import structure_numbers
from llmwiki.domain.ledger.structure import StructureNode


def reconcile_numbered_hierarchy(
    nodes: tuple[StructureNode, ...], *, root_node_id: str
) -> tuple[StructureNode, ...]:
    ordered = sorted(nodes, key=lambda item: item.source_order)
    by_id = {node.structure_node_id: node for node in ordered}
    open_numbered: list[StructureNode] = []
    reconciled: list[StructureNode] = []

    for node in ordered:
        if node.structure_node_id == root_node_id or node.structure_node_kind == "root":
            reconciled.append(node)
            continue
        number_path = _number_path(node)
        if not number_path:
            reconciled.append(node)
            continue
        open_numbered = [
            candidate
            for candidate in open_numbered
            if structure_numbers.number_parent(_number_path(candidate), number_path)
        ]
        parent = _nearest_numbered_parent(open_numbered, number_path)
        if parent is not None and _can_reparent(node, parent, by_id):
            node = replace(node, parent_structure_node_id=parent.structure_node_id)
        reconciled.append(node)
        open_numbered.append(node)

    return tuple(sorted(reconciled, key=lambda item: item.source_order))


def _nearest_numbered_parent(
    open_numbered: list[StructureNode], number_path: tuple[int, ...]
) -> StructureNode | None:
    parents = tuple(
        candidate
        for candidate in open_numbered
        if structure_numbers.number_parent(_number_path(candidate), number_path)
    )
    if not parents:
        return None
    return max(parents, key=lambda item: len(_number_path(item)))


def _can_reparent(
    node: StructureNode, parent: StructureNode, by_id: dict[str, StructureNode]
) -> bool:
    if node.structure_node_id == parent.structure_node_id:
        return False
    current_parent = by_id.get(node.parent_structure_node_id)
    if current_parent is None or current_parent.structure_node_kind == "root":
        return True
    current_path = _number_path(current_parent)
    parent_path = _number_path(parent)
    if not current_path:
        return True
    node_path = _number_path(node)
    if not structure_numbers.number_parent(current_path, node_path):
        return True
    return len(parent_path) > len(current_path)


def _number_path(node: StructureNode) -> tuple[int, ...]:
    return structure_numbers.heading_number_path(
        structure_numbers.canonical_heading_label(node.heading_text)
    )
