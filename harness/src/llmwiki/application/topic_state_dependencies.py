"""Source-neutral topic dependency derivation."""

from __future__ import annotations

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.domain.assertion_graph import (
    Assertion,
    DependencyStatus,
    RelationshipKind,
    SourceUnit,
    TopicDependency,
    TopicKind,
    TopicState,
)
from llmwiki.domain.ledger.canonical import short_digest


def topic_dependencies(
    graph: AssertionGraphArtifact, topics: tuple[TopicState, ...]
) -> tuple[TopicDependency, ...]:
    dependencies = [
        *_record_dependencies(graph, topics),
        *_structure_dependencies(graph, topics),
    ]
    by_id = {dependency.id: dependency for dependency in dependencies}
    return tuple(by_id[key] for key in sorted(by_id))


def attach_dependencies(
    topics: tuple[TopicState, ...], dependencies: tuple[TopicDependency, ...]
) -> tuple[TopicState, ...]:
    by_topic: dict[str, list[str]] = {}
    for dependency in dependencies:
        by_topic.setdefault(dependency.from_topic_state_id, []).append(dependency.id)
    return tuple(
        topic.model_copy(update={"required_dependency_ids": tuple(by_topic.get(topic.id, ()))})
        for topic in topics
    )


def _record_dependencies(
    graph: AssertionGraphArtifact, topics: tuple[TopicState, ...]
) -> tuple[TopicDependency, ...]:
    owner_by_record = _owner_by_record(topics)
    assertion_by_id = {assertion.id: assertion for assertion in graph.assertions}
    dependencies: list[TopicDependency] = []
    for relationship in graph.relationships:
        from_topic = owner_by_record.get(relationship.subject_id)
        to_topic = owner_by_record.get(relationship.object_id)
        if not from_topic or not to_topic or from_topic == to_topic:
            continue
        dependencies.append(
            TopicDependency(
                id=_dependency_id(relationship.id, from_topic, to_topic),
                from_topic_state_id=from_topic,
                to_topic_state_id=to_topic,
                relation=relationship.predicate,
                required_status=DependencyStatus.REQUIRED,
                rationale_assertion_ids=relationship.assertion_ids,
                source_order=_source_order(relationship.assertion_ids, assertion_by_id),
            )
        )
    for edge in graph.argument_edges:
        from_topic = owner_by_record.get(edge.from_assertion_id)
        to_topic = owner_by_record.get(edge.to_assertion_id)
        if not from_topic or not to_topic or from_topic == to_topic:
            continue
        dependencies.append(
            TopicDependency(
                id=_dependency_id(edge.id, from_topic, to_topic),
                from_topic_state_id=from_topic,
                to_topic_state_id=to_topic,
                relation=edge.relation,
                required_status=DependencyStatus.REQUIRED,
                rationale_assertion_ids=(edge.from_assertion_id, edge.to_assertion_id),
                source_order=_source_order(
                    (edge.from_assertion_id, edge.to_assertion_id), assertion_by_id
                ),
            )
        )
    return tuple(dependencies)


def _structure_dependencies(
    graph: AssertionGraphArtifact, topics: tuple[TopicState, ...]
) -> tuple[TopicDependency, ...]:
    unit_by_id = {unit.id: unit for unit in graph.source_units}
    projected = tuple(topic for topic in topics if topic.topic_kind != TopicKind.SOURCE_MANIFEST)
    owners_by_unit = _owners_by_unit(projected)
    dependencies: list[TopicDependency] = []
    for topic in projected:
        dependencies.extend(_ancestor_dependencies(topic, owners_by_unit, unit_by_id))
    dependencies.extend(_sibling_dependencies(projected, unit_by_id))
    return tuple(dependencies)


def _ancestor_dependencies(
    topic: TopicState,
    owners_by_unit: dict[str, tuple[TopicState, ...]],
    unit_by_id: dict[str, SourceUnit],
) -> tuple[TopicDependency, ...]:
    dependencies: list[TopicDependency] = []
    for unit_id in topic.source_unit_ids:
        unit = unit_by_id.get(unit_id)
        parent_id = unit.parent_id if unit is not None else None
        while parent_id is not None:
            for parent_topic in owners_by_unit.get(parent_id, ()):
                if parent_topic.id != topic.id:
                    dependencies.append(
                        _structure_dependency(
                            topic,
                            parent_topic,
                            RelationshipKind.PART_OF,
                            _unit_order(topic, unit_by_id),
                        )
                    )
                    dependencies.append(
                        _structure_dependency(
                            parent_topic,
                            topic,
                            RelationshipKind.CONTEXTUALIZES,
                            _unit_order(topic, unit_by_id),
                        )
                    )
            parent = unit_by_id.get(parent_id)
            parent_id = parent.parent_id if parent is not None else None
    return tuple(dependencies)


def _sibling_dependencies(
    topics: tuple[TopicState, ...], unit_by_id: dict[str, SourceUnit]
) -> tuple[TopicDependency, ...]:
    by_parent: dict[str, list[TopicState]] = {}
    for topic in topics:
        anchor_id = _anchor_unit_id(topic, unit_by_id)
        anchor = unit_by_id.get(anchor_id)
        if anchor is not None and anchor.parent_id:
            by_parent.setdefault(anchor.parent_id, []).append(topic)
    dependencies: list[TopicDependency] = []
    for siblings in by_parent.values():
        ordered = sorted(siblings, key=lambda topic: (_anchor_order(topic, unit_by_id), topic.id))
        for first, second in zip(ordered, ordered[1:], strict=False):
            dependencies.append(
                _structure_dependency(
                    first,
                    second,
                    RelationshipKind.CONTEXTUALIZES,
                    _unit_order(second, unit_by_id),
                )
            )
            dependencies.append(
                _structure_dependency(
                    second,
                    first,
                    RelationshipKind.CONTEXTUALIZES,
                    _unit_order(first, unit_by_id),
                )
            )
    return tuple(dependencies)


def _owners_by_unit(topics: tuple[TopicState, ...]) -> dict[str, tuple[TopicState, ...]]:
    grouped: dict[str, list[TopicState]] = {}
    for topic in topics:
        for unit_id in topic.source_unit_ids:
            grouped.setdefault(unit_id, []).append(topic)
    return {unit_id: tuple(value) for unit_id, value in grouped.items()}


def _owner_by_record(topics: tuple[TopicState, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for topic in topics:
        if topic.topic_kind == TopicKind.SOURCE_MANIFEST:
            continue
        for record_id in (*topic.accepted_assertion_ids, *topic.accepted_technical_atom_ids):
            result.setdefault(record_id, topic.id)
    return result


def _anchor_unit_id(topic: TopicState, unit_by_id: dict[str, SourceUnit]) -> str:
    for unit_id in topic.source_unit_ids:
        unit = unit_by_id.get(unit_id)
        if unit is not None and unit.parent_id is not None:
            return unit.parent_id
    return topic.source_unit_ids[0] if topic.source_unit_ids else ""


def _anchor_order(topic: TopicState, unit_by_id: dict[str, SourceUnit]) -> int:
    anchor = unit_by_id.get(_anchor_unit_id(topic, unit_by_id))
    return anchor.source_order if anchor is not None else _unit_order(topic, unit_by_id)


def _unit_order(topic: TopicState, unit_by_id: dict[str, SourceUnit]) -> int:
    orders = [
        unit_by_id[unit_id].source_order
        for unit_id in topic.source_unit_ids
        if unit_id in unit_by_id
    ]
    return min(orders) if orders else 0


def _source_order(assertion_ids: tuple[str, ...], assertion_by_id: dict[str, Assertion]) -> int:
    orders = [
        int(assertion.source_unit_ids[0].rsplit("_", 1)[-1])
        for assertion_id in assertion_ids
        if (assertion := assertion_by_id.get(assertion_id)) is not None
        and assertion.source_unit_ids
    ]
    return min(orders) if orders else 0


def _structure_dependency(
    from_topic: TopicState, to_topic: TopicState, relation: RelationshipKind, source_order: int
) -> TopicDependency:
    return TopicDependency(
        id=_dependency_id(f"structure-{relation.value}", from_topic.id, to_topic.id),
        from_topic_state_id=from_topic.id,
        to_topic_state_id=to_topic.id,
        relation=relation,
        required_status=DependencyStatus.REQUIRED,
        source_order=source_order,
    )


def _dependency_id(record_id: str, from_topic: str, to_topic: str) -> str:
    return f"tdp_{short_digest(record_id + '|' + from_topic + '|' + to_topic)}"
