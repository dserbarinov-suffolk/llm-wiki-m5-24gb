"""Pure page projection builder for admitted topic state."""

from __future__ import annotations

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.page_projection_artifacts import (
    page_id_for_topic,
    page_projection_id,
    related_link,
)
from llmwiki.application.page_projection_rendering import (
    source_manifest_body,
    topic_body,
)
from llmwiki.application.topic_state_artifacts import TopicStateArtifact
from llmwiki.domain.assertion_graph import (
    Assertion,
    PageProjection,
    ProjectionFinding,
    RenderedRelatedLink,
    TechnicalAtom,
    TopicGap,
    TopicKind,
    TopicState,
)


def build_page_projections(
    *,
    graph: AssertionGraphArtifact,
    topic_artifact: TopicStateArtifact,
    source_page_id: str,
    source_title: str,
    source_summary: str,
    source_review: str = "",
) -> tuple[PageProjection, ...]:
    page_id_by_topic = _page_ids(topic_artifact.topic_states, source_page_id)
    topic_by_id = {topic.id: topic for topic in topic_artifact.topic_states}
    source_topic = next(
        topic
        for topic in topic_artifact.topic_states
        if topic.topic_kind == TopicKind.SOURCE_MANIFEST
    )
    topic_pages = tuple(
        _topic_projection(
            graph,
            topic_artifact,
            topic,
            page_id_by_topic,
            page_id_by_topic[source_topic.id],
        )
        for topic in topic_artifact.topic_states
        if topic.topic_kind != TopicKind.SOURCE_MANIFEST
    )
    source_projection = _source_manifest_projection(
        source_topic,
        topic_pages,
        topic_by_id,
        page_id_by_topic,
        source_page_id,
        source_title,
        graph.source_locator,
        source_summary,
        source_review,
    )
    return (source_projection, *sorted(topic_pages, key=lambda item: item.page_id))


def _page_ids(topics: tuple[TopicState, ...], source_page_id: str) -> dict[str, str]:
    return {
        topic.id: page_id_for_topic(
            source_page_id,
            topic.topic_key,
            topic.topic_kind == TopicKind.SOURCE_MANIFEST,
        )
        for topic in topics
    }


def _topic_projection(
    graph: AssertionGraphArtifact,
    topic_artifact: TopicStateArtifact,
    topic: TopicState,
    page_id_by_topic: dict[str, str],
    source_page_id: str,
) -> PageProjection:
    assertions = _assertions(topic, graph)
    atoms = _atoms(topic, graph)
    gaps = _gaps(topic, topic_artifact)
    related = _related_links(topic, topic_artifact, page_id_by_topic)
    body, coverage = topic_body(
        topic=topic,
        assertions=assertions,
        atoms=atoms,
        gaps=gaps,
        related=related,
        graph=graph,
        source_page_id=source_page_id,
    )
    return PageProjection(
        id=page_projection_id(topic.id, page_id_by_topic[topic.id]),
        topic_state_id=topic.id,
        page_id=page_id_by_topic[topic.id],
        page_kind=topic.projection_policy.page_kind,
        page_family=topic.projection_policy.page_family,
        page_body=body,
        coverage_records=tuple(coverage),
        source_locators=(f"raw/{graph.source_locator}",),
        rendered_related_links=related,
        projection_findings=_projection_findings(gaps),
    )


def _source_manifest_projection(
    topic: TopicState,
    topic_pages: tuple[PageProjection, ...],
    topic_by_id: dict[str, TopicState],
    page_id_by_topic: dict[str, str],
    source_page_id: str,
    source_title: str,
    source_locator: str,
    source_summary: str,
    source_review: str,
) -> PageProjection:
    body, coverage, links = source_manifest_body(
        topic,
        topic_pages,
        topic_by_id,
        page_id_by_topic,
        source_title,
        source_locator,
        source_summary,
        source_review,
    )
    return PageProjection(
        id=page_projection_id(topic.id, source_page_id),
        topic_state_id=topic.id,
        page_id=source_page_id,
        page_kind=topic.projection_policy.page_kind,
        page_family=topic.projection_policy.page_family,
        page_body=body,
        coverage_records=tuple(coverage),
        source_locators=(f"raw/{source_locator}",),
        rendered_related_links=links,
    )


def _related_links(
    topic: TopicState,
    topic_artifact: TopicStateArtifact,
    page_id_by_topic: dict[str, str],
) -> tuple[RenderedRelatedLink, ...]:
    dependencies = [
        dependency
        for dependency in topic_artifact.topic_dependencies
        if dependency.id in topic.required_dependency_ids
        and dependency.to_topic_state_id in page_id_by_topic
    ]
    return tuple(
        related_link(
            page_id_by_topic[dependency.to_topic_state_id],
            dependency.relation.value.replace("_", " "),
            "source-supported topic dependency",
            (dependency.id,),
        )
        for dependency in sorted(dependencies, key=lambda item: (item.source_order, item.id))
    )


def _assertions(topic: TopicState, graph: AssertionGraphArtifact) -> tuple[Assertion, ...]:
    by_id = {assertion.id: assertion for assertion in graph.assertions}
    return tuple(by_id[item] for item in topic.accepted_assertion_ids if item in by_id)


def _atoms(topic: TopicState, graph: AssertionGraphArtifact) -> tuple[TechnicalAtom, ...]:
    by_id = {atom.id: atom for atom in graph.technical_atoms}
    return tuple(by_id[item] for item in topic.accepted_technical_atom_ids if item in by_id)


def _gaps(topic: TopicState, topic_artifact: TopicStateArtifact) -> tuple[TopicGap, ...]:
    by_id = {gap.id: gap for gap in topic_artifact.topic_gaps}
    return tuple(by_id[item] for item in topic.unresolved_gap_ids if item in by_id)


def _projection_findings(gaps: tuple[TopicGap, ...]) -> tuple[ProjectionFinding, ...]:
    return tuple(
        ProjectionFinding(
            finding_kind=gap.gap_kind.value,
            detail=gap.description,
            support_record_ids=(gap.id,),
        )
        for gap in gaps
    )
