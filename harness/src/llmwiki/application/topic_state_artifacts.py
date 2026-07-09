"""Build portable topic-state artifacts from an assertion graph."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.topic_state_admission import (
    admitted_topic_states,
    topic_state_build_activity,
)
from llmwiki.application.topic_state_dependencies import (
    attach_dependencies,
    topic_dependencies,
)
from llmwiki.domain.assertion_graph import (
    ProvenanceActivity,
    TopicDependency,
    TopicGap,
    TopicState,
)
from llmwiki.domain.ledger.canonical import artifact_fingerprint, canonical_json
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT


class TopicStateArtifact(BaseModel):
    """Portable admitted topic states for one source ingest."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    topic_state_artifact_id: str
    topic_state_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    assertion_graph_artifact_id: str
    provenance_activities: tuple[ProvenanceActivity, ...]
    topic_states: tuple[TopicState, ...]
    topic_dependencies: tuple[TopicDependency, ...]
    topic_gaps: tuple[TopicGap, ...]


def build_topic_state_artifact(graph: AssertionGraphArtifact) -> TopicStateArtifact:
    topics, gaps = admitted_topic_states(graph)
    dependencies = topic_dependencies(graph, topics)
    topics = attach_dependencies(topics, dependencies)
    draft = TopicStateArtifact(
        topic_state_artifact_id="pending",
        topic_state_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_locator=graph.source_locator,
        source_hash=graph.source_hash,
        assertion_graph_artifact_id=graph.assertion_graph_artifact_id,
        provenance_activities=(*graph.provenance_activities, topic_state_build_activity(graph)),
        topic_states=topics,
        topic_dependencies=dependencies,
        topic_gaps=gaps,
    )
    _validate_topic_state_references(draft, graph)
    fingerprint = artifact_fingerprint(
        draft.model_dump(mode="json"),
        exclude=("topic_state_artifact_id", "topic_state_fingerprint"),
    )
    return draft.model_copy(
        update={
            "topic_state_artifact_id": f"topic-state-{fingerprint}",
            "topic_state_fingerprint": fingerprint,
        }
    )


def topic_state_artifact_to_json(artifact: TopicStateArtifact) -> str:
    return canonical_json(artifact, indent=2)


def _validate_topic_state_references(
    artifact: TopicStateArtifact, graph: AssertionGraphArtifact
) -> None:
    assertion_ids = {assertion.id for assertion in graph.assertions}
    atom_ids = {atom.id for atom in graph.technical_atoms}
    relationship_ids = {relationship.id for relationship in graph.relationships}
    edge_ids = {edge.id for edge in graph.argument_edges}
    unit_ids = {unit.id for unit in graph.source_units}
    dep_ids = {dependency.id for dependency in artifact.topic_dependencies}
    gap_ids = {gap.id for gap in artifact.topic_gaps}
    for topic in artifact.topic_states:
        _require_all(topic.accepted_assertion_ids, assertion_ids, "topic assertion")
        _require_all(topic.accepted_technical_atom_ids, atom_ids, "topic technical atom")
        _require_all(topic.relationship_ids, relationship_ids, "topic relationship")
        _require_all(topic.argument_edge_ids, edge_ids, "topic argument edge")
        _require_all(topic.source_unit_ids, unit_ids, "topic source unit")
        _require_all(topic.required_dependency_ids, dep_ids, "topic dependency")
        _require_all(topic.unresolved_gap_ids, gap_ids, "topic gap")


def _require_all(values: tuple[str, ...], valid: set[str], label: str) -> None:
    missing = tuple(value for value in values if value not in valid)
    if missing:
        raise ValueError(f"{label} reference missing: {missing[0]}")
