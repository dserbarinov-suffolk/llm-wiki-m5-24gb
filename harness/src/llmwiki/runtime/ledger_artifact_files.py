"""Serialize individual claim-ledger ingest artifact files."""

from __future__ import annotations

from llmwiki.application.assertion_graph_artifacts import (
    AssertionGraphArtifact,
    assertion_graph_artifact_to_json,
)
from llmwiki.application.page_projection_artifacts import (
    PageProjectionArtifact,
    page_projection_artifact_to_json,
)
from llmwiki.application.source_artifacts import (
    CanonicalSourceArtifact,
    canonical_source_artifact_to_json,
)
from llmwiki.application.topic_state_artifacts import (
    TopicStateArtifact,
    topic_state_artifact_to_json,
)
from llmwiki.domain.ledger.artifacts import (
    BlockedWriteDiagnosticArtifact,
    ClaimLedgerArtifact,
    DocumentStructureArtifact,
    LedgerQualityReportArtifact,
    ProjectionContextArtifact,
    ProjectionCoverageArtifact,
    QualityCheckCatalogArtifact,
    SourceCoverageArtifact,
)
from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.proposed_change_review import (
    ProposedChangeReviewArtifact,
    proposed_change_review_artifact_to_json,
)
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.staged_contracts import (
    LedgerExtractionResult,
    ProjectionLintRun,
    PublishRun,
    SourcePlan,
    StagedWikiPageSet,
)


def artifact_files(
    *,
    ds_artifact: DocumentStructureArtifact,
    ledger_artifact: ClaimLedgerArtifact,
    catalog_artifact: QualityCheckCatalogArtifact,
    ledger_report_artifact: LedgerQualityReportArtifact,
    projection_report_artifact: LedgerQualityReportArtifact,
    coverage_artifact: ProjectionCoverageArtifact,
    projection_context_artifact: ProjectionContextArtifact,
    section_plan: SectionGroundedPlan,
    knowledge_shape_catalog: KnowledgeShapeCatalog,
    source_coverage_artifact: SourceCoverageArtifact | None,
    blocked: BlockedWriteDiagnosticArtifact | None,
    source_plan: SourcePlan,
    extraction_result: LedgerExtractionResult,
    staged_page_set: StagedWikiPageSet,
    lint_run: ProjectionLintRun,
    publish_run: PublishRun,
    source_artifact: CanonicalSourceArtifact | None,
    proposed_change_review_artifact: ProposedChangeReviewArtifact | None,
    assertion_graph_artifact: AssertionGraphArtifact | None,
    topic_state_artifact: TopicStateArtifact | None,
    page_projection_artifact: PageProjectionArtifact | None,
) -> dict[str, str]:
    files = {
        "document-structure.json": canonical_json(ds_artifact, indent=2),
        "claim-ledger.json": canonical_json(ledger_artifact, indent=2),
        "quality-check-catalog.json": canonical_json(catalog_artifact, indent=2),
        "ledger-quality-report.json": canonical_json(ledger_report_artifact, indent=2),
        "projection-quality-report.json": canonical_json(projection_report_artifact, indent=2),
        "projection-coverage.json": canonical_json(coverage_artifact, indent=2),
        "projection-context.json": canonical_json(projection_context_artifact, indent=2),
        "section-plan.json": canonical_json(section_plan, indent=2),
        "knowledge-shapes.json": canonical_json(knowledge_shape_catalog, indent=2),
        "source-plan.json": canonical_json(source_plan, indent=2),
        "extraction-result.json": canonical_json(extraction_result, indent=2),
        "staged-pages.json": canonical_json(staged_page_set, indent=2),
        "lint-run.json": canonical_json(lint_run, indent=2),
        "publish-run.json": canonical_json(publish_run, indent=2),
    }
    if source_artifact is not None:
        files["assertion-graph-source-artifact.json"] = canonical_source_artifact_to_json(
            source_artifact
        )
    if proposed_change_review_artifact is not None:
        files["proposed-change-review.json"] = proposed_change_review_artifact_to_json(
            proposed_change_review_artifact
        )
    if assertion_graph_artifact is not None:
        files["assertion-graph.json"] = assertion_graph_artifact_to_json(assertion_graph_artifact)
    if topic_state_artifact is not None:
        files["topic-states.json"] = topic_state_artifact_to_json(topic_state_artifact)
    if page_projection_artifact is not None:
        files["page-projections.json"] = page_projection_artifact_to_json(
            page_projection_artifact
        )
    if source_coverage_artifact is not None:
        files["source-coverage.json"] = canonical_json(source_coverage_artifact, indent=2)
    if blocked is not None:
        files["blocked-write-diagnostic.json"] = canonical_json(blocked, indent=2)
    return files
