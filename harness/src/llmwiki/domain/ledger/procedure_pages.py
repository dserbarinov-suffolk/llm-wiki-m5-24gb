"""Render procedure guide pages from procedure domain objects."""

from __future__ import annotations

from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCatalog
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.procedure_closure import (
    ProcedureDependency,
    ProcedureEvidenceClosure,
    build_procedure_evidence_closure,
    dependency_citation,
    dependency_link,
    review_reason_text,
)
from llmwiki.domain.ledger.procedure_decisions import DecisionPoint
from llmwiki.domain.ledger.procedures import (
    PAGE_FAMILY_PROCEDURE_GUIDE,
    ProcedureGuide,
    plan_procedure_guides,
    procedure_aliases,
)
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.pages import PageMetadata, WikiPage

_DEPENDENCY_KIND_ORDER = ("table", "formula", "rule", "worked-example", "procedure")


def build_procedure_pages(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    source_page_id: str,
    source_locator: str,
    today: str,
    section_plan: SectionGroundedPlan,
    shape_catalog: KnowledgeShapeCatalog | None = None,
) -> tuple[WikiPage, ...]:
    guides = plan_procedure_guides(
        ledger,
        structure,
        source_page_id=source_page_id,
        section_plan=section_plan,
        shape_catalog=shape_catalog,
    )
    pages: list[WikiPage] = []
    for guide in guides:
        closure = build_procedure_evidence_closure(guide, ledger=ledger, structure=structure)
        body = render_procedure_page(closure, source_page_id)
        status = closure.projection_status
        metadata = PageMetadata(
            page_id=guide.procedure_id,
            page_kind="procedure",
            page_family=PAGE_FAMILY_PROCEDURE_GUIDE,
            summary=(
                f"{guide.goal}: {len(guide.steps)} ordered step(s), "
                f"{len(closure.decision_points)} decision point(s), "
                f"{status.authoritative_dependency_count} authoritative dependency reference(s), "
                f"{status.review_only_dependency_count} review-only dependency reference(s), "
                f"projection {status.status} from raw/{source_locator}."
            ),
            sources=(f"raw/{source_locator}",),
            updated=today,
            domain=source_page_id,
            category_path=f"procedures/{source_page_id}",
            source_id=source_locator,
            aliases=procedure_aliases(guide),
            projection_coverage_pointer=f"procedure-{guide.procedure_id}@{short_digest(body, 32)}",
        )
        pages.append(WikiPage.from_metadata(metadata, body))
    return tuple(pages)


def render_procedure_page(
    procedure: ProcedureGuide | ProcedureEvidenceClosure, source_page_id: str
) -> str:
    closure = (
        procedure
        if isinstance(procedure, ProcedureEvidenceClosure)
        else build_procedure_evidence_closure(procedure)
    )
    guide = closure.guide
    lines = [f"# {guide.title}", "", f"From [[{source_page_id}]].", ""]
    lines.extend(("## Goal", "", f"- {guide.goal}.", ""))
    lines.extend(("## Procedure Steps", ""))
    for step_closure in closure.steps:
        step = step_closure.step
        lines.append(
            f"{step.sequence}. **{step.title}** (`{step.action_type}`) - "
            f"evidence section [[{step.section_page_id}]]."
        )
        for claim in step_closure.claims:
            lines.append(f"   - {_entry_text(claim)} _({_citation(claim)})_")
        if step_closure.dependencies:
            lines.append("   - Evidence dependencies:")
            for dependency in step_closure.dependencies:
                lines.append(
                    "     - "
                    f"`{dependency.dependency_kind}`: {dependency_link(dependency)} "
                    f"_({dependency_citation(dependency)})_"
                )
    lines.append("")
    if closure.decision_points:
        lines.extend(("## Decisions And Constraints", ""))
        for point in closure.decision_points:
            lines.append(f"- {_decision_text(point)} _({_decision_citation(point)})_")
        lines.append("")
    if closure.authoritative_dependencies:
        lines.extend(("## Authoritative Dependencies", ""))
        for kind, dependencies in _dependencies_by_kind(closure.authoritative_dependencies):
            lines.append(f"### {kind.title()}")
            for dependency in dependencies:
                lines.append(
                    f"- {dependency_link(dependency)} _({dependency_citation(dependency)})_"
                )
            lines.append("")
    if closure.review_only_dependencies:
        lines.extend(("## Review-Only Dependencies", ""))
        for dependency in closure.review_only_dependencies:
            lines.append(
                f"- `{dependency.dependency_kind}`: {dependency.label} "
                f"_({dependency_citation(dependency)}; {review_reason_text(dependency)})_"
            )
        lines.append("")
    if closure.missing_dependencies:
        lines.extend(("## Missing Dependencies", ""))
        for dependency in closure.missing_dependencies:
            lines.append(
                f"- `{dependency.dependency_kind}`: {dependency.label} "
                f"_({review_reason_text(dependency)})_"
            )
        lines.append("")
    lines.extend(
        (
            "## Execution Readiness",
            "",
            f"- Projection status: `{closure.projection_status.status}`.",
            "- Authoritative dependencies: "
            f"{closure.projection_status.authoritative_dependency_count}.",
            "- Review-only dependencies: "
            f"{closure.projection_status.review_only_dependency_count}.",
            f"- Missing dependencies: {closure.projection_status.missing_dependency_count}.",
            "- The procedure is complete when every step output has been recorded or validated.",
            "",
            "## Source Trail",
            "",
            f"- Source manifest: [[{source_page_id}]]",
            f"- Source section: [[{guide.source_section_page_id}]]",
        )
    )
    return "\n".join(lines).strip() + "\n"


def _entry_text(entry: LedgerEntry) -> str:
    return (entry.normalized_text or entry.source_text).strip()


def _decision_text(point: DecisionPoint) -> str:
    return point.evidence_block.source_text


def _decision_citation(point: DecisionPoint) -> str:
    ranges = ", ".join(point.evidence_block.source_range_ids)
    return f"{point.entry.source_locator} ({ranges})"


def _citation(entry: LedgerEntry) -> str:
    return f"{entry.source_locator} ({entry.source_range_id})"


def _dependencies_by_kind(
    dependencies: tuple[ProcedureDependency, ...],
) -> tuple[tuple[str, tuple[ProcedureDependency, ...]], ...]:
    grouped: list[tuple[str, tuple[ProcedureDependency, ...]]] = []
    for kind in _DEPENDENCY_KIND_ORDER:
        items = tuple(
            dependency for dependency in dependencies if dependency.dependency_kind == kind
        )
        if items:
            grouped.append((kind, items))
    remaining = tuple(
        dependency
        for dependency in dependencies
        if dependency.dependency_kind not in _DEPENDENCY_KIND_ORDER
    )
    if remaining:
        grouped.append(("other", remaining))
    return tuple(grouped)
