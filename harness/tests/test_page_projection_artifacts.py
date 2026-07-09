"""Page-projection artifacts derived from admitted topic state."""

from __future__ import annotations

import json

from test_assertion_graph_artifacts import _source_and_ledger

from llmwiki.application.assertion_graph_artifacts import build_assertion_graph_artifact
from llmwiki.application.page_projection_artifacts import (
    build_page_projection_artifact,
    page_projection_artifact_to_json,
)
from llmwiki.application.topic_state_artifacts import build_topic_state_artifact
from llmwiki.domain.assertion_graph import TopicKind


def test_page_projection_artifact_renders_portable_source_and_topic_pages() -> None:
    canonical_source, ledger = _source_and_ledger()
    graph = build_assertion_graph_artifact(
        source_artifact=canonical_source.artifact,
        ledger=ledger,
    )
    topic_artifact = build_topic_state_artifact(graph)

    artifact = build_page_projection_artifact(
        graph=graph,
        topic_artifact=topic_artifact,
        source_page_id="source",
        source_title="Source",
        source_summary="2 linked topic pages.",
    )

    assert artifact.page_projection_artifact_id.startswith("page-projection-")
    assert artifact.assertion_graph_artifact_id == graph.assertion_graph_artifact_id
    assert artifact.topic_state_artifact_id == topic_artifact.topic_state_artifact_id
    assert all(projection.coverage_records for projection in artifact.page_projections)
    source_projection = next(
        projection for projection in artifact.page_projections if projection.page_id == "source"
    )
    assert source_projection.page_kind == "source"
    assert "[[source-array]]" in source_projection.page_body
    assert source_projection.rendered_related_links
    topic_projection = next(
        projection
        for projection in artifact.page_projections
        if projection.topic_state_id
        in {
            topic.id
            for topic in topic_artifact.topic_states
            if topic.topic_kind == TopicKind.CONCEPT
        }
    )
    assert "Arrays have indexes" in topic_projection.page_body
    assert "value := items[0]" in topic_projection.page_body
    assert all(link.support_record_ids for link in source_projection.rendered_related_links)


def test_page_projection_artifact_json_has_no_dangling_references() -> None:
    canonical_source, ledger = _source_and_ledger()
    graph = build_assertion_graph_artifact(
        source_artifact=canonical_source.artifact,
        ledger=ledger,
    )
    topic_artifact = build_topic_state_artifact(graph)
    artifact = build_page_projection_artifact(
        graph=graph,
        topic_artifact=topic_artifact,
        source_page_id="source",
        source_title="Source",
        source_summary="2 linked topic pages.",
    )

    serialized = json.loads(page_projection_artifact_to_json(artifact))

    page_ids = {projection["page_id"] for projection in serialized["page_projections"]}
    support_ids = {
        *(assertion.id for assertion in graph.assertions),
        *(atom.id for atom in graph.technical_atoms),
        *(topic.id for topic in topic_artifact.topic_states),
        *(dependency.id for dependency in topic_artifact.topic_dependencies),
        *(gap.id for gap in topic_artifact.topic_gaps),
    }
    for projection in serialized["page_projections"]:
        for coverage in projection["coverage_records"]:
            assert coverage["support_record_id"] in support_ids
        for link in projection["rendered_related_links"]:
            assert link["target_page_id"] in page_ids
            assert set(link["support_record_ids"]) <= support_ids
