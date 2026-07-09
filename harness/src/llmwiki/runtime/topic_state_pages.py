"""Adapt portable page projections into wiki-page files."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.application.page_projection_artifacts import PageProjectionArtifact
from llmwiki.domain.assertion_graph import PageProjection
from llmwiki.domain.ledger.artifacts import (
    LedgerQualityReportArtifact,
    ProjectionCoverageArtifact,
    build_projection_coverage_artifact,
)
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.coverage import ProjectionCoverage
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.pointers import ledger_quality_report_pointer
from llmwiki.domain.ledger.projection import ProjectionSourceSupport
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.runtime.ledger_pages import ledger_summary


@dataclass(frozen=True)
class TopicStatePageProjection:
    source_page: WikiPage
    linked_pages: tuple[WikiPage, ...]
    coverage_artifact: ProjectionCoverageArtifact


def build_topic_state_page_projection(
    *,
    ledger: ClaimLedger,
    page_id: str,
    source_locator: str,
    today: str,
    decision: str,
    support: ProjectionSourceSupport,
    projection_report_artifact: LedgerQualityReportArtifact,
    page_projection_artifact: PageProjectionArtifact,
) -> TopicStatePageProjection:
    projections = {
        projection.page_id: projection
        for projection in page_projection_artifact.page_projections
    }
    source_projection = projections[page_id]
    linked_pages = tuple(
        _wiki_page(
            projection=projection,
            source_page_id=page_id,
            source_locator=source_locator,
            today=today,
            summary=_projection_summary(projection, source_locator),
            category_path=f"{projection.page_kind}s",
        )
        for projection in sorted(projections.values(), key=lambda item: item.page_id)
        if projection.page_id != page_id
    )
    source_body_hash = short_digest(source_projection.page_body, 32)
    coverage_artifact = build_projection_coverage_artifact(
        wiki_page_locator=page_id,
        page_body_hash=source_body_hash,
        support_set=(support,),
        coverage=ProjectionCoverage(()),
        ledger_quality_report_pointer=ledger_quality_report_pointer(
            projection_report_artifact.ledger_quality_report_artifact_id,
            projection_report_artifact.ledger_quality_report_fingerprint,
        ),
    )
    source_page = _wiki_page(
        projection=source_projection,
        source_page_id=page_id,
        source_locator=source_locator,
        today=today,
        summary=ledger_summary(ledger, decision, len(linked_pages)),
        category_path="sources",
        source_id=source_locator,
    )
    return TopicStatePageProjection(source_page, linked_pages, coverage_artifact)


def _wiki_page(
    *,
    projection: PageProjection,
    source_page_id: str,
    source_locator: str,
    today: str,
    summary: str,
    category_path: str,
    source_id: str = "",
) -> WikiPage:
    metadata = PageMetadata(
        page_id=projection.page_id,
        page_kind=projection.page_kind,
        summary=summary,
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=source_page_id,
        category_path=category_path,
        source_id=source_id,
        projection_coverage_pointer=(
            f"page-projection-{projection.id}@{short_digest(projection.page_body, 32)}"
        ),
        page_family=projection.page_family,
    )
    return WikiPage.from_metadata(metadata, projection.page_body)


def _projection_summary(projection: PageProjection, source_locator: str) -> str:
    return (
        f"{projection.page_family}: {len(projection.coverage_records)} supported fragment(s) "
        f"and {len(projection.rendered_related_links)} related link(s) from raw/{source_locator}."
    )
