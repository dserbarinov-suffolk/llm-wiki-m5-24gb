"""AssociationGraph deterministic clustering."""

from __future__ import annotations

from collections import Counter

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.domain.assertion_graph import (
    Assertion,
    AssertionKind,
    AssociationCluster,
    AssociationClusterShape,
    AssociationEdge,
    AssociationNode,
    AssociationNodeKind,
    SourceUnit,
    TechnicalAtom,
    TechnicalAtomKind,
)
from llmwiki.domain.ledger.canonical import short_digest

_CLUSTER_EDGE_MIN = 0.65
_OVERSIZED_ASSERTION_MIN = 48
_OVERSIZED_MEMBER_MIN = 120


def association_clusters(
    graph: AssertionGraphArtifact,
    nodes: tuple[AssociationNode, ...],
    edges: tuple[AssociationEdge, ...],
) -> tuple[AssociationCluster, ...]:
    parent = {node.id: node.id for node in nodes}
    for edge in edges:
        if edge.weight >= _CLUSTER_EDGE_MIN:
            _union(parent, edge.from_node_id, edge.to_node_id)
    grouped: dict[str, list[AssociationNode]] = {}
    for node in nodes:
        grouped.setdefault(_find(parent, node.id), []).append(node)
    assertions = {assertion.id: assertion for assertion in graph.assertions}
    atoms = {atom.id: atom for atom in graph.technical_atoms}
    units = {unit.id: unit for unit in graph.source_units}
    clusters = [
        _cluster(group, assertions, atoms, units, edges)
        for group in grouped.values()
        if _has_cluster_content(group)
    ]
    return tuple(
        sorted(clusters, key=lambda item: (min(item.source_unit_ids or ("",)), item.label, item.id))
    )


def _has_cluster_content(nodes: list[AssociationNode]) -> bool:
    content_kinds = {AssociationNodeKind.ASSERTION, AssociationNodeKind.TECHNICAL_ATOM}
    return any(node.node_kind in content_kinds for node in nodes)


def _cluster(
    nodes: list[AssociationNode],
    assertions: dict[str, Assertion],
    atoms: dict[str, TechnicalAtom],
    units: dict[str, SourceUnit],
    edges: tuple[AssociationEdge, ...],
) -> AssociationCluster:
    node_ids = {node.id for node in nodes}
    assertion_ids = tuple(node.record_id for node in nodes if node.record_id in assertions)
    atom_ids = tuple(node.record_id for node in nodes if node.record_id in atoms)
    source_unit_ids = tuple(node.record_id for node in nodes if node.record_id in units)
    internal = [
        edge.weight
        for edge in edges
        if edge.from_node_id in node_ids and edge.to_node_id in node_ids
    ]
    external = [
        edge.weight
        for edge in edges
        if (edge.from_node_id in node_ids) != (edge.to_node_id in node_ids)
    ]
    member_ids = tuple(sorted(node_ids))
    return AssociationCluster(
        id=f"asc_{short_digest('|'.join(member_ids))}",
        label=_cluster_label(assertion_ids, atom_ids, assertions, atoms),
        member_node_ids=member_ids,
        assertion_ids=assertion_ids,
        technical_atom_ids=atom_ids,
        source_unit_ids=source_unit_ids,
        dominant_shape=_dominant_shape(assertion_ids, atom_ids, assertions, atoms),
        cohesion_score=_average(internal),
        separation_score=round(1.0 - max(external, default=0.0), 3),
        ambiguous=bool(external and max(external) >= _CLUSTER_EDGE_MIN),
        oversized=len(assertion_ids) >= _OVERSIZED_ASSERTION_MIN
        or len(member_ids) >= _OVERSIZED_MEMBER_MIN,
    )


def _dominant_shape(
    assertion_ids: tuple[str, ...],
    atom_ids: tuple[str, ...],
    assertions: dict[str, Assertion],
    atoms: dict[str, TechnicalAtom],
) -> AssociationClusterShape:
    kinds = Counter(assertions[item].kind for item in assertion_ids)
    atom_kinds = Counter(atoms[item].atom_kind for item in atom_ids)
    if kinds[AssertionKind.PROCEDURE_STEP] > max(1, len(assertion_ids) * 0.6):
        return AssociationClusterShape.PROCEDURE
    if kinds[AssertionKind.RULE_STATEMENT] > max(1, len(assertion_ids) * 0.5):
        return AssociationClusterShape.RULE_SET
    catalog_atoms = (
        atom_kinds[TechnicalAtomKind.TABLE] + atom_kinds[TechnicalAtomKind.STRUCTURED_RECORD]
    )
    if atom_ids and catalog_atoms >= max(1, len(atom_ids) * 0.6):
        return AssociationClusterShape.CATALOG_RECORD
    if atom_ids and len(atom_ids) > len(assertion_ids):
        return AssociationClusterShape.TECHNICAL_ATOM_SET
    if assertion_ids:
        return AssociationClusterShape.CONCEPT
    return AssociationClusterShape.MIXED


def _cluster_label(
    assertion_ids: tuple[str, ...],
    atom_ids: tuple[str, ...],
    assertions: dict[str, Assertion],
    atoms: dict[str, TechnicalAtom],
) -> str:
    subjects = [assertions[item].subject for item in assertion_ids]
    if subjects:
        return Counter(subjects).most_common(1)[0][0]
    if atom_ids:
        return atoms[atom_ids[0]].atom_kind.value.replace("_", " ")
    return "association cluster"


def _average(values: list[float]) -> float:
    return round(sum(values) / len(values), 3) if values else 0.0


def _find(parent: dict[str, str], node_id: str) -> str:
    while parent[node_id] != node_id:
        node_id = parent[node_id]
    return node_id


def _union(parent: dict[str, str], first: str, second: str) -> None:
    first_root = _find(parent, first)
    second_root = _find(parent, second)
    if first_root != second_root:
        parent[second_root] = first_root
