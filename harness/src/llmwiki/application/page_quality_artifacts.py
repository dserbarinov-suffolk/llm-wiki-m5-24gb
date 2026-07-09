"""Build portable page quality reports from projection artifacts."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.page_projection_artifacts import PageProjectionArtifact
from llmwiki.application.topic_state_artifacts import TopicStateArtifact
from llmwiki.domain.ledger.canonical import artifact_fingerprint, canonical_json
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT
from llmwiki.domain.page_quality import PageQualityReport, build_page_quality_report


class PageQualityReportArtifact(BaseModel):
    """Portable deterministic quality scores for projected wiki pages."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    page_quality_report_artifact_id: str
    page_quality_report_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    assertion_graph_artifact_id: str
    topic_state_artifact_id: str
    page_projection_artifact_id: str
    report: PageQualityReport


def build_page_quality_report_artifact(
    *,
    graph: AssertionGraphArtifact,
    topic_artifact: TopicStateArtifact,
    page_projection_artifact: PageProjectionArtifact,
) -> PageQualityReportArtifact:
    report = build_page_quality_report(
        source_locator=graph.source_locator,
        source_hash=graph.source_hash,
        pages=page_projection_artifact.page_projections,
        topics=topic_artifact.topic_states,
        assertions=graph.assertions,
        atoms=graph.technical_atoms,
        source_units=graph.source_units,
    )
    draft = PageQualityReportArtifact(
        page_quality_report_artifact_id="pending",
        page_quality_report_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_locator=graph.source_locator,
        source_hash=graph.source_hash,
        assertion_graph_artifact_id=graph.assertion_graph_artifact_id,
        topic_state_artifact_id=topic_artifact.topic_state_artifact_id,
        page_projection_artifact_id=page_projection_artifact.page_projection_artifact_id,
        report=report,
    )
    fingerprint = artifact_fingerprint(
        draft.model_dump(mode="json"),
        exclude=("page_quality_report_artifact_id", "page_quality_report_fingerprint"),
    )
    return draft.model_copy(
        update={
            "page_quality_report_artifact_id": f"page-quality-report-{fingerprint}",
            "page_quality_report_fingerprint": fingerprint,
        }
    )


def page_quality_report_artifact_to_json(artifact: PageQualityReportArtifact) -> str:
    return canonical_json(artifact, indent=2)
