"""AssociationGraph edge mining rules."""

from __future__ import annotations

from itertools import combinations

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.association_graph_text import canonical_label
from llmwiki.domain.assertion_graph import (
    AssociationEdge,
    AssociationEdgeKind,
    AssociationNode,
    AssociationNodeKind,
)
from llmwiki.domain.ledger.canonical import short_digest

_MAX_PAIRWISE_UNIT_RECORDS = 32


def association_edges(
    graph: AssertionGraphArtifact,
    nodes: tuple[AssociationNode, ...],
    node_id_by_record: dict[str, str],
) -> tuple[AssociationEdge, ...]:
    edges: list[AssociationEdge] = []
    _append_source_edges(edges, graph, node_id_by_record)
    _append_assertion_edges(edges, graph, nodes, node_id_by_record)
    _append_atom_edges(edges, graph, node_id_by_record)
    _append_relationship_edges(edges, graph, node_id_by_record)
    _append_source_unit_edges(edges, graph, node_id_by_record)
    by_id = {edge.id: edge for edge in edges}
    return tuple(by_id[key] for key in sorted(by_id))


def _append_source_edges(
    edges: list[AssociationEdge], graph: AssertionGraphArtifact, node_id_by_record: dict[str, str]
) -> None:
    for span in graph.evidence_spans:
        if span.id not in node_id_by_record:
            continue
        for unit_id in span.source_unit_ids:
            _add_edge(
                edges,
                AssociationEdgeKind.SOURCE_CONTAINS_EVIDENCE,
                unit_id,
                span.id,
                0.95,
                "source unit contains evidence span",
                (span.id,),
                node_id_by_record,
            )
    for unit in graph.source_units:
        if unit.parent_id:
            _add_edge(
                edges,
                AssociationEdgeKind.HEADING_ANCESTRY,
                unit.parent_id,
                unit.id,
                0.4,
                "source-derived parent/child structure",
                (unit.id,),
                node_id_by_record,
            )


def _append_assertion_edges(
    edges: list[AssociationEdge],
    graph: AssertionGraphArtifact,
    nodes: tuple[AssociationNode, ...],
    node_id_by_record: dict[str, str],
) -> None:
    concept_ids = {
        node.label: node.id for node in nodes if node.node_kind == AssociationNodeKind.CONCEPT_LABEL
    }
    for assertion in graph.assertions:
        for span_id in assertion.evidence_span_ids:
            _add_edge(
                edges,
                AssociationEdgeKind.ASSERTION_HAS_EVIDENCE,
                assertion.id,
                span_id,
                0.95,
                "assertion cites exact evidence span",
                (assertion.id, span_id),
                node_id_by_record,
            )
        for atom_id in assertion.technical_atom_ids:
            _add_edge(
                edges,
                AssociationEdgeKind.ASSERTION_USES_ATOM,
                assertion.id,
                atom_id,
                0.92,
                "assertion directly references technical atom",
                (assertion.id, atom_id),
                node_id_by_record,
            )
        _append_subject_edge(edges, assertion.id, assertion.subject, concept_ids, node_id_by_record)


def _append_subject_edge(
    edges: list[AssociationEdge],
    assertion_id: str,
    subject: str,
    concept_ids: dict[str, str],
    node_id_by_record: dict[str, str],
) -> None:
    concept_id = concept_ids.get(canonical_label(subject))
    assertion_node = node_id_by_record.get(assertion_id)
    if concept_id and assertion_node:
        edges.append(
            _edge(
                AssociationEdgeKind.SHARED_SUBJECT,
                assertion_node,
                concept_id,
                0.5,
                "assertion shares normalized subject label",
                (assertion_id,),
            )
        )


def _append_atom_edges(
    edges: list[AssociationEdge], graph: AssertionGraphArtifact, node_id_by_record: dict[str, str]
) -> None:
    for atom in graph.technical_atoms:
        for span_id in atom.evidence_span_ids:
            _add_edge(
                edges,
                AssociationEdgeKind.ATOM_HAS_EVIDENCE,
                atom.id,
                span_id,
                0.95,
                "technical atom cites exact evidence span",
                (atom.id, span_id),
                node_id_by_record,
            )


def _append_relationship_edges(
    edges: list[AssociationEdge], graph: AssertionGraphArtifact, node_id_by_record: dict[str, str]
) -> None:
    for relation in graph.relationships:
        _add_edge(
            edges,
            AssociationEdgeKind.EXPLICIT_RELATIONSHIP,
            relation.subject_id,
            relation.object_id,
            0.9,
            relation.predicate.value.replace("_", " "),
            (relation.id, *relation.assertion_ids),
            node_id_by_record,
        )
    for edge in graph.argument_edges:
        _add_edge(
            edges,
            AssociationEdgeKind.ARGUMENT_EDGE,
            edge.from_assertion_id,
            edge.to_assertion_id,
            0.6,
            edge.rationale,
            (edge.id, edge.from_assertion_id, edge.to_assertion_id),
            node_id_by_record,
        )


def _append_source_unit_edges(
    edges: list[AssociationEdge], graph: AssertionGraphArtifact, node_id_by_record: dict[str, str]
) -> None:
    records_by_unit = _records_by_source_unit(graph)
    for unit_id, record_ids in records_by_unit.items():
        unique = tuple(dict.fromkeys(record_ids))
        if len(unique) > _MAX_PAIRWISE_UNIT_RECORDS:
            continue
        for first, second in combinations(unique, 2):
            _add_edge(
                edges,
                AssociationEdgeKind.SHARED_SOURCE_UNIT,
                first,
                second,
                0.72,
                "records share the same source unit",
                (unit_id, first, second),
                node_id_by_record,
            )


def _records_by_source_unit(graph: AssertionGraphArtifact) -> dict[str, list[str]]:
    records_by_unit: dict[str, list[str]] = {}
    for assertion in graph.assertions:
        for unit_id in assertion.source_unit_ids:
            records_by_unit.setdefault(unit_id, []).append(assertion.id)
    span_unit_ids = {span.id: span.source_unit_ids for span in graph.evidence_spans}
    for atom in graph.technical_atoms:
        for span_id in atom.evidence_span_ids:
            for unit_id in span_unit_ids.get(span_id, ()):
                records_by_unit.setdefault(unit_id, []).append(atom.id)
    return records_by_unit


def _add_edge(
    edges: list[AssociationEdge],
    kind: AssociationEdgeKind,
    first_record_id: str,
    second_record_id: str,
    weight: float,
    rationale: str,
    support: tuple[str, ...],
    node_id_by_record: dict[str, str],
) -> None:
    first = node_id_by_record.get(first_record_id)
    second = node_id_by_record.get(second_record_id)
    if first and second:
        edges.append(_edge(kind, first, second, weight, rationale, support))


def _edge(
    kind: AssociationEdgeKind,
    first: str,
    second: str,
    weight: float,
    rationale: str,
    support: tuple[str, ...],
) -> AssociationEdge:
    ordered = tuple(sorted((first, second)))
    return AssociationEdge(
        id=f"ase_{short_digest(kind.value + '|' + '|'.join(ordered) + '|' + '|'.join(support))}",
        edge_kind=kind,
        from_node_id=ordered[0],
        to_node_id=ordered[1],
        weight=round(weight, 3),
        rationale=rationale,
        support_record_ids=support,
    )
