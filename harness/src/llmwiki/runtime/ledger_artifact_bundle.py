"""Serialize claim-ledger ingest artifacts and their portable manifest."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.page_projection_artifacts import PageProjectionArtifact
from llmwiki.application.source_artifacts import CanonicalSourceArtifact
from llmwiki.application.topic_state_artifacts import TopicStateArtifact
from llmwiki.domain.ledger.artifacts import (
    BlockedWriteDiagnosticArtifact,
    ClaimLedgerArtifact,
    DocumentStructureArtifact,
    LedgerQualityReportArtifact,
    PortableArtifactMember,
    PortableArtifactSet,
    ProjectionCoverageArtifact,
    QualityCheckCatalogArtifact,
    SourceCoverageArtifact,
    build_portable_artifact_set,
)
from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.proposed_change_review import ProposedChangeReviewArtifact
from llmwiki.domain.ledger.staged_contracts import (
    LedgerExtractionResult,
    ProjectionLintRun,
    PublishRun,
    SourcePlan,
    StagedWikiPageSet,
)
from llmwiki.runtime.ledger_artifact_files import artifact_files


@dataclass(frozen=True)
class SerializedLedgerArtifacts:
    artifact_files: dict[str, str]
    portable_artifact_set: PortableArtifactSet


def build_serialized_artifact_bundle(
    *,
    ds_artifact: DocumentStructureArtifact,
    ledger_artifact: ClaimLedgerArtifact,
    catalog_artifact: QualityCheckCatalogArtifact,
    ledger_report_artifact: LedgerQualityReportArtifact,
    projection_report_artifact: LedgerQualityReportArtifact,
    coverage_artifact: ProjectionCoverageArtifact,
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
) -> SerializedLedgerArtifacts:
    members = _artifact_members(
        ds_artifact,
        ledger_artifact,
        catalog_artifact,
        ledger_report_artifact,
        projection_report_artifact,
        coverage_artifact,
        source_coverage_artifact,
        blocked,
        source_plan,
        extraction_result,
        staged_page_set,
        lint_run,
        publish_run,
        source_artifact,
        proposed_change_review_artifact,
        assertion_graph_artifact,
        topic_state_artifact,
        page_projection_artifact,
    )
    files = artifact_files(
        ds_artifact=ds_artifact,
        ledger_artifact=ledger_artifact,
        catalog_artifact=catalog_artifact,
        ledger_report_artifact=ledger_report_artifact,
        projection_report_artifact=projection_report_artifact,
        coverage_artifact=coverage_artifact,
        source_coverage_artifact=source_coverage_artifact,
        blocked=blocked,
        source_plan=source_plan,
        extraction_result=extraction_result,
        staged_page_set=staged_page_set,
        lint_run=lint_run,
        publish_run=publish_run,
        source_artifact=source_artifact,
        proposed_change_review_artifact=proposed_change_review_artifact,
        assertion_graph_artifact=assertion_graph_artifact,
        topic_state_artifact=topic_state_artifact,
        page_projection_artifact=page_projection_artifact,
    )
    manifest = build_portable_artifact_set(tuple(members))
    files["portable-artifact-set.json"] = canonical_json(manifest, indent=2)
    return SerializedLedgerArtifacts(files, manifest)


def _artifact_members(
    ds_artifact: DocumentStructureArtifact,
    ledger_artifact: ClaimLedgerArtifact,
    catalog_artifact: QualityCheckCatalogArtifact,
    ledger_report_artifact: LedgerQualityReportArtifact,
    projection_report_artifact: LedgerQualityReportArtifact,
    coverage_artifact: ProjectionCoverageArtifact,
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
) -> list[PortableArtifactMember]:
    members = [
        _member(
            "document-structure-artifact",
            ds_artifact.document_structure_artifact_id,
            ds_artifact.document_structure_fingerprint,
        ),
        _member(
            "claim-ledger-artifact",
            ledger_artifact.claim_ledger_id,
            ledger_artifact.claim_ledger_fingerprint,
        ),
        _member(
            "quality-check-catalog-artifact",
            catalog_artifact.quality_check_catalog_artifact_id,
            catalog_artifact.quality_check_catalog_fingerprint,
        ),
        _member(
            "ledger-quality-report-artifact",
            ledger_report_artifact.ledger_quality_report_artifact_id,
            ledger_report_artifact.ledger_quality_report_fingerprint,
        ),
        _member(
            "ledger-quality-report-artifact",
            projection_report_artifact.ledger_quality_report_artifact_id,
            projection_report_artifact.ledger_quality_report_fingerprint,
        ),
        _member(
            "projection-coverage-artifact",
            coverage_artifact.projection_coverage_artifact_id,
            coverage_artifact.projection_coverage_fingerprint,
        ),
        _member(
            "source-plan-artifact",
            source_plan.source_plan_id,
            source_plan.source_plan_fingerprint,
        ),
        _member(
            "extraction-result-artifact",
            extraction_result.extraction_result_id,
            extraction_result.extraction_result_fingerprint,
        ),
        _member(
            "staged-wiki-page-set-artifact",
            staged_page_set.staged_page_set_id,
            staged_page_set.staged_page_set_fingerprint,
        ),
        _member(
            "projection-lint-run-artifact",
            lint_run.lint_run_id,
            lint_run.lint_run_fingerprint,
        ),
        _member(
            "publish-run-artifact",
            publish_run.publish_run_id,
            publish_run.publish_run_fingerprint,
        ),
    ]
    if source_artifact is not None:
        members.append(
            _member(
                "assertion-graph-source-artifact",
                source_artifact.source_artifact_id,
                source_artifact.source_artifact_fingerprint,
            )
        )
    if proposed_change_review_artifact is not None:
        members.append(
            _member(
                "proposed-change-review-artifact",
                proposed_change_review_artifact.proposed_change_review_artifact_id,
                proposed_change_review_artifact.proposed_change_review_fingerprint,
            )
        )
    if assertion_graph_artifact is not None:
        members.append(
            _member(
                "assertion-graph-artifact",
                assertion_graph_artifact.assertion_graph_artifact_id,
                assertion_graph_artifact.assertion_graph_fingerprint,
            )
        )
    if topic_state_artifact is not None:
        members.append(
            _member(
                "topic-state-artifact",
                topic_state_artifact.topic_state_artifact_id,
                topic_state_artifact.topic_state_fingerprint,
            )
        )
    if page_projection_artifact is not None:
        members.append(
            _member(
                "page-projection-artifact",
                page_projection_artifact.page_projection_artifact_id,
                page_projection_artifact.page_projection_fingerprint,
            )
        )
    if source_coverage_artifact is not None:
        members.append(
            _member(
                "source-coverage-artifact",
                source_coverage_artifact.source_coverage_artifact_id,
                source_coverage_artifact.source_coverage_fingerprint,
            )
        )
    if blocked is not None:
        members.append(
            _member(
                "blocked-write-diagnostic-artifact",
                blocked.blocked_write_diagnostic_artifact_id,
                blocked.blocked_write_diagnostic_fingerprint,
            )
        )
    return members


def _member(kind: str, target_id: str, fingerprint: str) -> PortableArtifactMember:
    return PortableArtifactMember(kind, target_id, fingerprint)
