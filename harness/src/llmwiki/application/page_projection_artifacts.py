"""Build portable page projections from topic state."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.topic_state_artifacts import TopicStateArtifact
from llmwiki.domain.assertion_graph import (
    PageProjection,
    ProvenanceActivity,
    RenderedRelatedLink,
)
from llmwiki.domain.ledger.canonical import artifact_fingerprint, canonical_json, short_digest
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT
from llmwiki.domain.pages import slugify


class PageProjectionArtifact(BaseModel):
    """Portable markdown projections derived from admitted topic state."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    page_projection_artifact_id: str
    page_projection_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    assertion_graph_artifact_id: str
    topic_state_artifact_id: str
    provenance_activities: tuple[ProvenanceActivity, ...]
    page_projections: tuple[PageProjection, ...]


def build_page_projection_artifact(
    *,
    graph: AssertionGraphArtifact,
    topic_artifact: TopicStateArtifact,
    source_page_id: str,
    source_title: str,
    source_summary: str,
    source_review: str = "",
) -> PageProjectionArtifact:
    from llmwiki.application.page_projection_builder import build_page_projections

    projections = build_page_projections(
        graph=graph,
        topic_artifact=topic_artifact,
        source_page_id=source_page_id,
        source_title=source_title,
        source_summary=source_summary,
        source_review=source_review,
    )
    draft = PageProjectionArtifact(
        page_projection_artifact_id="pending",
        page_projection_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_locator=graph.source_locator,
        source_hash=graph.source_hash,
        assertion_graph_artifact_id=graph.assertion_graph_artifact_id,
        topic_state_artifact_id=topic_artifact.topic_state_artifact_id,
        provenance_activities=topic_artifact.provenance_activities,
        page_projections=projections,
    )
    _validate_projection_references(draft, graph, topic_artifact)
    fingerprint = artifact_fingerprint(
        draft.model_dump(mode="json"),
        exclude=("page_projection_artifact_id", "page_projection_fingerprint"),
    )
    return draft.model_copy(
        update={
            "page_projection_artifact_id": f"page-projection-{fingerprint}",
            "page_projection_fingerprint": fingerprint,
        }
    )


def page_projection_artifact_to_json(artifact: PageProjectionArtifact) -> str:
    return canonical_json(artifact, indent=2)


def page_id_for_topic(source_page_id: str, topic_key: str, is_source_manifest: bool) -> str:
    if is_source_manifest:
        return source_page_id
    return slugify(f"{source_page_id}-{topic_key}")[:180]


def page_projection_id(topic_state_id: str, page_id: str) -> str:
    return f"pgp_{short_digest(topic_state_id + '|' + page_id)}"


def related_link(
    target_page_id: str,
    relation_label: str,
    description: str,
    support_record_ids: tuple[str, ...],
) -> RenderedRelatedLink:
    return RenderedRelatedLink(
        target_page_id=target_page_id,
        relation_label=relation_label,
        description=description,
        support_record_ids=support_record_ids,
    )


def _validate_projection_references(
    artifact: PageProjectionArtifact,
    graph: AssertionGraphArtifact,
    topic_artifact: TopicStateArtifact,
) -> None:
    valid = {
        *(assertion.id for assertion in graph.assertions),
        *(atom.id for atom in graph.technical_atoms),
        *(relationship.id for relationship in graph.relationships),
        *(edge.id for edge in graph.argument_edges),
        *(topic.id for topic in topic_artifact.topic_states),
        *(dependency.id for dependency in topic_artifact.topic_dependencies),
        *(gap.id for gap in topic_artifact.topic_gaps),
    }
    topic_ids = {topic.id for topic in topic_artifact.topic_states}
    page_ids = {projection.page_id for projection in artifact.page_projections}
    for projection in artifact.page_projections:
        if projection.topic_state_id not in topic_ids:
            raise ValueError(f"page projection topic missing: {projection.topic_state_id}")
        for coverage in projection.coverage_records:
            if coverage.support_record_id not in valid:
                raise ValueError(f"coverage support missing: {coverage.support_record_id}")
        for link in projection.rendered_related_links:
            if link.target_page_id not in page_ids:
                raise ValueError(f"related link target missing: {link.target_page_id}")
            _require_all(link.support_record_ids, valid, "related link support")


def _require_all(values: tuple[str, ...], valid: set[str], label: str) -> None:
    missing = tuple(value for value in values if value not in valid)
    if missing:
        raise ValueError(f"{label} reference missing: {missing[0]}")
