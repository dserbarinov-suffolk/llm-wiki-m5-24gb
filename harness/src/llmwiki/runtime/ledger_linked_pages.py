"""Build source-linked wiki pages from ledger projection artifacts."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.artifacts import (
    LedgerQualityReportArtifact,
    ProjectionCoverageArtifact,
    build_projection_coverage_artifact,
)
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.coverage import RenderedPage
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.pointers import ledger_quality_report_pointer
from llmwiki.domain.ledger.procedure_pages import build_procedure_pages
from llmwiki.domain.ledger.projection import ProjectionSourceSupport
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.recipe_pages import build_recipe_pages
from llmwiki.domain.ledger.section_navigation import section_links_by_topic
from llmwiki.domain.ledger.section_pages import build_section_pages
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.pages import WikiPage
from llmwiki.runtime.ledger_pages import (
    append_source_page_links,
    build_source_wiki_page,
    build_topic_pages,
    ledger_summary,
)


@dataclass(frozen=True)
class LinkedPageProjection:
    source_page: WikiPage
    linked_pages: tuple[WikiPage, ...]
    coverage_artifact: ProjectionCoverageArtifact


def build_linked_page_projection(
    *,
    ledger: ClaimLedger,
    structure: DocumentStructure,
    section_plan: SectionGroundedPlan,
    shape_catalog: KnowledgeShapeCatalog,
    projection_context: ProjectionContext,
    topics: tuple[SourceTopic, ...],
    page_id: str,
    title: str,
    source_locator: str,
    today: str,
    decision: str,
    rendered: RenderedPage,
    support: ProjectionSourceSupport,
    projection_report_artifact: LedgerQualityReportArtifact,
) -> LinkedPageProjection:
    related = section_links_by_topic(section_plan, structure, source_page_id=page_id)
    topic_pages = build_topic_pages(
        topics,
        ledger,
        page_id,
        source_locator,
        today,
        related_pages_by_topic=related,
        projection_context=projection_context,
    )
    section_pages = build_section_pages(
        ledger,
        structure,
        source_page_id=page_id,
        source_locator=source_locator,
        today=today,
        topics=topics,
        projection_context=projection_context,
    )
    procedure_pages = build_procedure_pages(
        ledger,
        structure,
        source_page_id=page_id,
        source_locator=source_locator,
        today=today,
        shape_catalog=shape_catalog,
    )
    recipe_pages = build_recipe_pages(
        ledger,
        structure,
        source_page_id=page_id,
        source_locator=source_locator,
        today=today,
        shape_catalog=shape_catalog,
    )
    linked_pages = (*topic_pages, *section_pages, *procedure_pages, *recipe_pages)
    source_body = append_source_page_links(
        rendered.page_body,
        "Procedure Guides",
        procedure_pages,
    )
    source_body = append_source_page_links(source_body, "Recipes", recipe_pages)
    coverage_artifact = build_projection_coverage_artifact(
        wiki_page_locator=page_id,
        page_body_hash=short_digest(source_body, 32),
        support_set=(support,),
        coverage=rendered.coverage,
        ledger_quality_report_pointer=ledger_quality_report_pointer(
            projection_report_artifact.ledger_quality_report_artifact_id,
            projection_report_artifact.ledger_quality_report_fingerprint,
        ),
    )
    source_page = build_source_wiki_page(
        page_id,
        source_locator,
        title,
        ledger_summary(ledger, decision, len(linked_pages)),
        today,
        source_body,
        coverage_artifact,
    )
    return LinkedPageProjection(source_page, linked_pages, coverage_artifact)
