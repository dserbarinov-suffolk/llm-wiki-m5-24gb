"""Build portable AssociationGraph artifacts."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.association_graph_building import build_association_graph
from llmwiki.domain.assertion_graph import AssociationGraph
from llmwiki.domain.ledger.canonical import artifact_fingerprint, canonical_json
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT


class AssociationGraphArtifact(BaseModel):
    """Portable shadow artifact for association and grouping experiments."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    association_graph_artifact_id: str
    association_graph_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    assertion_graph_artifact_id: str
    graph: AssociationGraph


def build_association_graph_artifact(
    assertion_graph: AssertionGraphArtifact,
) -> AssociationGraphArtifact:
    draft = AssociationGraphArtifact(
        association_graph_artifact_id="pending",
        association_graph_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_locator=assertion_graph.source_locator,
        source_hash=assertion_graph.source_hash,
        assertion_graph_artifact_id=assertion_graph.assertion_graph_artifact_id,
        graph=build_association_graph(assertion_graph),
    )
    fingerprint = artifact_fingerprint(
        draft.model_dump(mode="json"),
        exclude=("association_graph_artifact_id", "association_graph_fingerprint"),
    )
    return draft.model_copy(
        update={
            "association_graph_artifact_id": f"association-graph-{fingerprint}",
            "association_graph_fingerprint": fingerprint,
        }
    )


def association_graph_artifact_to_json(artifact: AssociationGraphArtifact) -> str:
    return canonical_json(artifact, indent=2)
