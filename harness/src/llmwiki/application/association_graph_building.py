"""Pure AssociationGraph construction from assertion graph records."""

from __future__ import annotations

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.association_graph_clustering import association_clusters
from llmwiki.application.association_graph_edges import association_edges
from llmwiki.application.association_graph_text import canonical_label
from llmwiki.domain.assertion_graph import (
    Assertion,
    AssociationGraph,
    AssociationNode,
    AssociationNodeKind,
)
from llmwiki.domain.ledger.canonical import short_digest


def build_association_graph(assertion_graph: AssertionGraphArtifact) -> AssociationGraph:
    nodes = association_nodes(assertion_graph)
    node_id_by_record = {node.record_id: node.id for node in nodes if node.record_id}
    edges = association_edges(assertion_graph, nodes, node_id_by_record)
    clusters = association_clusters(assertion_graph, nodes, edges)
    return AssociationGraph(
        source_locator=assertion_graph.source_locator,
        source_hash=assertion_graph.source_hash,
        nodes=nodes,
        edges=edges,
        clusters=clusters,
    )


def association_nodes(graph: AssertionGraphArtifact) -> tuple[AssociationNode, ...]:
    nodes: list[AssociationNode] = []
    order_by_unit = {unit.id: unit.source_order for unit in graph.source_units}
    nodes.extend(
        _node(unit.id, AssociationNodeKind.SOURCE_UNIT, unit.text, unit.source_order)
        for unit in graph.source_units
    )
    nodes.extend(
        _node(
            span.id,
            AssociationNodeKind.EVIDENCE_SPAN,
            span.exact_text,
            min((order_by_unit.get(unit_id, 0) for unit_id in span.source_unit_ids), default=0),
        )
        for span in graph.evidence_spans
    )
    nodes.extend(
        _node(
            assertion.id,
            AssociationNodeKind.ASSERTION,
            assertion.subject,
            _record_order(assertion, order_by_unit),
        )
        for assertion in graph.assertions
    )
    nodes.extend(
        _node(atom.id, AssociationNodeKind.TECHNICAL_ATOM, atom.atom_kind.value, atom.source_order)
        for atom in graph.technical_atoms
    )
    nodes.extend(_concept_nodes(graph.assertions, order_by_unit))
    return tuple(sorted(nodes, key=lambda item: (item.source_order, item.node_kind.value, item.id)))


def _concept_nodes(
    assertions: tuple[Assertion, ...], order_by_unit: dict[str, int]
) -> tuple[AssociationNode, ...]:
    nodes: list[AssociationNode] = []
    seen_labels: set[str] = set()
    for assertion in assertions:
        label = canonical_label(assertion.subject)
        if label and label not in seen_labels:
            seen_labels.add(label)
            nodes.append(
                _node(
                    f"concept:{label}",
                    AssociationNodeKind.CONCEPT_LABEL,
                    label,
                    _record_order(assertion, order_by_unit),
                )
            )
    return tuple(nodes)


def _node(record_id: str, kind: AssociationNodeKind, label: str, order: int) -> AssociationNode:
    clean = " ".join(label.split()) or record_id
    return AssociationNode(
        id=f"asn_{short_digest(kind.value + '|' + record_id)}",
        node_kind=kind,
        record_id=record_id if not record_id.startswith("concept:") else "",
        label=clean[:180],
        source_order=max(order, 0),
    )


def _record_order(assertion: Assertion, order_by_unit: dict[str, int]) -> int:
    return min((order_by_unit.get(unit_id, 0) for unit_id in assertion.source_unit_ids), default=0)
