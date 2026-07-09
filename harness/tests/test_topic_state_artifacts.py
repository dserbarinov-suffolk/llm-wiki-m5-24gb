"""Topic-state artifact admission from assertion graph records."""

from __future__ import annotations

import json

from test_assertion_graph_artifacts import _source_and_ledger

from llmwiki.application.assertion_graph_artifacts import build_assertion_graph_artifact
from llmwiki.application.topic_state_artifacts import (
    build_topic_state_artifact,
    topic_state_artifact_to_json,
)
from llmwiki.application.topic_state_dependencies import topic_dependencies
from llmwiki.domain.assertion_graph import (
    ProjectionPolicy,
    SourceUnit,
    SourceUnitKind,
    TopicKind,
    TopicState,
)


def test_topic_state_artifact_admits_coherent_topics_and_manifest() -> None:
    canonical_source, ledger = _source_and_ledger()
    graph = build_assertion_graph_artifact(
        source_artifact=canonical_source.artifact,
        ledger=ledger,
    )

    artifact = build_topic_state_artifact(graph)

    assert artifact.topic_state_artifact_id.startswith("topic-state-")
    assert artifact.assertion_graph_artifact_id == graph.assertion_graph_artifact_id
    assert any(topic.topic_kind == TopicKind.SOURCE_MANIFEST for topic in artifact.topic_states)
    concept_topics = [
        topic for topic in artifact.topic_states if topic.topic_kind == TopicKind.CONCEPT
    ]
    assert concept_topics
    assert concept_topics[0].accepted_assertion_ids
    assert concept_topics[0].accepted_technical_atom_ids


def test_topic_state_artifact_routes_weak_candidates_to_gaps_not_pages() -> None:
    canonical_source, ledger = _source_and_ledger()
    graph = build_assertion_graph_artifact(
        source_artifact=canonical_source.artifact,
        ledger=ledger,
    )
    one_assertion_graph = graph.model_copy(update={"assertions": graph.assertions[:1]})

    artifact = build_topic_state_artifact(one_assertion_graph)

    projected_topics = [
        topic for topic in artifact.topic_states if topic.topic_kind != TopicKind.SOURCE_MANIFEST
    ]
    assert not projected_topics
    assert artifact.topic_gaps
    assert artifact.topic_gaps[0].gap_kind == "weak_topic_identity"


def test_topic_state_artifact_json_has_no_dangling_references() -> None:
    canonical_source, ledger = _source_and_ledger()
    graph = build_assertion_graph_artifact(
        source_artifact=canonical_source.artifact,
        ledger=ledger,
    )
    artifact = build_topic_state_artifact(graph)

    serialized = json.loads(topic_state_artifact_to_json(artifact))

    assertion_ids = {assertion["id"] for assertion in graph.model_dump()["assertions"]}
    atom_ids = {atom["id"] for atom in graph.model_dump()["technical_atoms"]}
    for topic in serialized["topic_states"]:
        assert set(topic["accepted_assertion_ids"]) <= assertion_ids
        assert set(topic["accepted_technical_atom_ids"]) <= atom_ids
    kinds = {member["activity_kind"] for member in serialized["provenance_activities"]}
    assert "topic_state_build" in kinds


def test_topic_dependencies_link_adjacent_topics_by_source_section_anchors() -> None:
    canonical_source, ledger = _source_and_ledger()
    graph = build_assertion_graph_artifact(
        source_artifact=canonical_source.artifact,
        ledger=ledger,
    )
    graph = graph.model_copy(
        update={
            "source_units": (
                _unit("su_chapter", SourceUnitKind.HEADING, 1, None, ("su_first", "su_second")),
                _unit("su_first", SourceUnitKind.HEADING, 2, "su_chapter", ("su_first_body",)),
                _unit("su_first_body", SourceUnitKind.PARAGRAPH, 3, "su_first", ()),
                _unit("su_second", SourceUnitKind.HEADING, 4, "su_chapter", ("su_second_body",)),
                _unit("su_second_body", SourceUnitKind.PARAGRAPH, 5, "su_second", ()),
            ),
            "relationships": (),
            "argument_edges": (),
        }
    )
    topics = (
        _topic("tps_first", "first", "First", ("su_first_body",)),
        _topic("tps_second", "second", "Second", ("su_second_body",)),
    )

    dependencies = topic_dependencies(graph, topics)

    endpoints = {
        (dependency.from_topic_state_id, dependency.to_topic_state_id)
        for dependency in dependencies
    }
    assert ("tps_first", "tps_second") in endpoints
    assert ("tps_second", "tps_first") in endpoints


def _unit(
    unit_id: str,
    kind: SourceUnitKind,
    order: int,
    parent_id: str | None,
    child_ids: tuple[str, ...],
) -> SourceUnit:
    return SourceUnit(
        id=unit_id,
        source_locator="source.pdf",
        source_hash="a" * 64,
        source_order=order,
        kind=kind,
        text=unit_id,
        page_span=(1, 1),
        parent_id=parent_id,
        child_ids=child_ids,
    )


def _topic(
    topic_id: str, topic_key: str, label: str, unit_ids: tuple[str, ...]
) -> TopicState:
    return TopicState(
        id=topic_id,
        topic_key=topic_key,
        label=label,
        topic_kind=TopicKind.CONCEPT,
        accepted_assertion_ids=("ast_fake",),
        source_unit_ids=unit_ids,
        projection_policy=ProjectionPolicy(page_kind="concept", page_family="topic-concept"),
    )
