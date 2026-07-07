"""Compact source-manifest navigation page projection."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.collection_pages import CollectionPlan
from llmwiki.domain.ledger.projection_policy import (
    PAGE_FAMILY_COLLECTION_PAGE,
    PAGE_FAMILY_PROCEDURE_GUIDE,
    PAGE_FAMILY_SECTION_REFERENCE,
)
from llmwiki.domain.ledger.section_navigation import section_page_id, section_title
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.pages import WikiPage

_MAX_CONCEPT_ENTRY_POINTS = 24
@dataclass(frozen=True)
class SourceEntryPoint:
    page_id: str
    label: str
    relation_kind: str
    summary: str


@dataclass(frozen=True)
class PageFamilySummary:
    page_family: str
    count: int
    purpose: str


@dataclass(frozen=True)
class SourceEntryPointGroup:
    heading: str
    entries: tuple[SourceEntryPoint, ...]


@dataclass(frozen=True)
class SourceNavigationPlan:
    source_page_id: str
    title: str
    source_locator: str
    ledger_summary: str
    page_family_summaries: tuple[PageFamilySummary, ...]
    procedures: tuple[SourceEntryPoint, ...]
    collections: tuple[SourceEntryPoint, ...]
    concepts: tuple[SourceEntryPoint, ...]
    sections: tuple[SourceEntryPoint, ...]
    page_family_entry_groups: tuple[SourceEntryPointGroup, ...] = ()


def build_source_navigation_plan(
    *,
    source_page_id: str,
    title: str,
    source_locator: str,
    ledger_summary: str,
    linked_pages: tuple[WikiPage, ...],
    structure: DocumentStructure,
    collection_plans: tuple[CollectionPlan, ...] = (),
) -> SourceNavigationPlan:
    pages = tuple(sorted(linked_pages, key=lambda page: page.page_id))
    page_by_id = {page.page_id: page for page in pages}
    family_summaries = _family_summaries(pages)
    procedures = tuple(_entry(page, "procedure") for page in pages if _is_procedure(page))
    collections = tuple(
        _collection_entry(plan, page_by_id)
        for plan in collection_plans
        if plan.collection_page_id in page_by_id
    )
    concepts = tuple(_entry(page, "concept") for page in pages if _is_concept(page))
    sections = _section_entries(source_page_id, structure, page_by_id)
    page_family_entry_groups = _page_family_entry_groups(pages, collections)
    return SourceNavigationPlan(
        source_page_id=source_page_id,
        title=title,
        source_locator=source_locator,
        ledger_summary=ledger_summary,
        page_family_summaries=family_summaries,
        procedures=procedures,
        collections=collections,
        concepts=concepts[:_MAX_CONCEPT_ENTRY_POINTS],
        sections=sections,
        page_family_entry_groups=page_family_entry_groups,
    )


def render_source_manifest(plan: SourceNavigationPlan) -> str:
    lines = [
        f"# {plan.title}",
        "",
        "## Source",
        "",
        f"- Raw source: `raw/{plan.source_locator}`",
        f"- {plan.ledger_summary}",
        "",
        "## Page Families",
        "",
    ]
    for summary in plan.page_family_summaries:
        lines.append(f"- {summary.page_family}: {summary.count} page(s) - {summary.purpose}")
    for group in plan.page_family_entry_groups:
        _append_group(lines, group.heading, group.entries)
    _append_group(lines, "Source Section Index", plan.sections)
    return "\n".join(lines).strip() + "\n"


def source_manifest_body_hash(body: str) -> str:
    return short_digest(body, 32)


def source_review_section(page_body: str) -> str:
    marker = "## Source review"
    start = page_body.find(marker)
    if start < 0:
        return ""
    return page_body[start:].strip()


def _family_summaries(pages: tuple[WikiPage, ...]) -> tuple[PageFamilySummary, ...]:
    counts: dict[str, int] = {"source-manifest": 1}
    for page in pages:
        family = page.page_metadata.page_family or page.page_kind
        counts[family] = counts.get(family, 0) + 1
    return tuple(
        PageFamilySummary(family, count, _family_purpose(family))
        for family, count in sorted(counts.items())
    )


def _family_purpose(page_family: str) -> str:
    return {
        "source-manifest": "source entry point",
        PAGE_FAMILY_SECTION_REFERENCE: "source-order reference pages",
        "topic-concept": "focused concept pages",
        "broad-topic": "broad concept overview pages",
        PAGE_FAMILY_PROCEDURE_GUIDE: "ordered task pages",
        "recipe-pattern": "reusable example pattern pages",
        PAGE_FAMILY_COLLECTION_PAGE: "list and catalog pages",
    }.get(page_family, "generated wiki pages")


def _entry(page: WikiPage, relation_kind: str) -> SourceEntryPoint:
    label = _page_title(page)
    return SourceEntryPoint(page.page_id, label, relation_kind, page.summary)


def _collection_entry(
    plan: CollectionPlan, page_by_id: dict[str, WikiPage]
) -> SourceEntryPoint:
    page = page_by_id[plan.collection_page_id]
    return SourceEntryPoint(page.page_id, plan.title, "collection", page.summary)


def _section_entries(
    source_page_id: str, structure: DocumentStructure, page_by_id: dict[str, WikiPage]
) -> tuple[SourceEntryPoint, ...]:
    entries: list[SourceEntryPoint] = []
    for node in sorted(structure.structure_nodes, key=lambda item: item.source_order):
        if node.structure_node_id == structure.root_node_id:
            continue
        page_id = section_page_id(source_page_id, structure, node)
        page = page_by_id.get(page_id)
        if page is None:
            continue
        entries.append(
            SourceEntryPoint(
                page_id, section_title(structure, node), "source section", page.summary
            )
        )
    return tuple(entries)


def _append_group(lines: list[str], heading: str, entries: tuple[SourceEntryPoint, ...]) -> None:
    if not entries:
        return
    lines.extend(("", f"## {heading}", ""))
    for entry in entries:
        lines.append(f"- [[{entry.page_id}]] - {entry.relation_kind}: {entry.summary}")


def _page_family_entry_groups(
    pages: tuple[WikiPage, ...], collection_entries: tuple[SourceEntryPoint, ...]
) -> tuple[SourceEntryPointGroup, ...]:
    collection_by_page_id = {entry.page_id: entry for entry in collection_entries}
    grouped: dict[str, list[SourceEntryPoint]] = {}
    for page in pages:
        family = page.page_metadata.page_family
        if family in {"", PAGE_FAMILY_SECTION_REFERENCE, "source-manifest"}:
            continue
        if page.page_id in collection_by_page_id:
            entry = collection_by_page_id[page.page_id]
        else:
            entry = _entry(page, _entry_relation(family))
        grouped.setdefault(family, []).append(entry)
    return tuple(
        SourceEntryPointGroup(_family_heading(family), tuple(sorted(entries, key=_entry_sort_key)))
        for family, entries in sorted(grouped.items(), key=lambda item: _family_order(item[0]))
    )


def _entry_relation(page_family: str) -> str:
    return page_family.replace("-", " ")


def _family_heading(page_family: str) -> str:
    return {
        "topic-concept": "Concept Entry Points",
        "broad-topic": "Broad Topic Pages",
        PAGE_FAMILY_PROCEDURE_GUIDE: "Procedure Guides",
        "recipe-pattern": "Recipes",
        PAGE_FAMILY_COLLECTION_PAGE: "Collections",
    }.get(page_family, page_family.replace("-", " ").title())


def _family_order(page_family: str) -> tuple[int, str]:
    order = {
        PAGE_FAMILY_PROCEDURE_GUIDE: 0,
        "recipe-pattern": 1,
        PAGE_FAMILY_COLLECTION_PAGE: 2,
        "topic-concept": 3,
        "broad-topic": 4,
    }
    return (order.get(page_family, 99), page_family)


def _entry_sort_key(entry: SourceEntryPoint) -> tuple[str, str]:
    return (entry.label.casefold(), entry.page_id)


def _page_title(page: WikiPage) -> str:
    for line in page.page_body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return page.page_id.replace("-", " ").title()


def _is_procedure(page: WikiPage) -> bool:
    return page.page_metadata.page_family == PAGE_FAMILY_PROCEDURE_GUIDE


def _is_concept(page: WikiPage) -> bool:
    return page.page_kind == "concept"
