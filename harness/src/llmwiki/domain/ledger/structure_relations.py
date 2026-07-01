"""Derived relations between source structure nodes."""

from __future__ import annotations

from llmwiki.domain.ledger.structure import StructureNode, StructureRelation


def sibling_relations(nodes: tuple[StructureNode, ...]) -> tuple[StructureRelation, ...]:
    by_parent: dict[str, list[StructureNode]] = {}
    for node in nodes:
        if node.structure_node_kind == "root":
            continue
        by_parent.setdefault(node.parent_structure_node_id, []).append(node)
    relations: list[StructureRelation] = []
    for siblings in by_parent.values():
        ordered = sorted(siblings, key=lambda item: item.source_order)
        for left, right in zip(ordered, ordered[1:], strict=False):
            relations.append(
                StructureRelation(left.structure_node_id, right.structure_node_id, "next-sibling")
            )
            relations.append(
                StructureRelation(
                    right.structure_node_id, left.structure_node_id, "previous-sibling"
                )
            )
    return tuple(relations)
