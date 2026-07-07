"""Source-neutral inbound navigation closure for generated projections."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.topic_relations import RelatedTopicLink
from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import WikiPage

_SOURCE_SECTION_RE = re.compile(
    r"(?:Source section|Broader source section):\s+\[\[([a-z0-9-]+)\]\]"
)

_SECTION_BACKLINK_RELATIONS = {
    "collection-page": "collection page",
    "procedure-guide": "procedure guide",
    "recipe-pattern": "recipe pattern",
}


@dataclass(frozen=True)
class GeneratedProjectionRef:
    page_id: str
    label: str
    page_family: str
    owner_section_page_id: str
    relation: str
    summary: str


@dataclass(frozen=True)
class ProjectionNavigationFinding:
    finding_type: str
    page_id: str
    message: str


def generated_projection_refs(pages: tuple[WikiPage, ...]) -> tuple[GeneratedProjectionRef, ...]:
    refs: list[GeneratedProjectionRef] = []
    for page in pages:
        relation = _SECTION_BACKLINK_RELATIONS.get(page.page_metadata.page_family)
        if relation is None:
            continue
        owner_section = _owner_section_page_id(page.page_body)
        if not owner_section:
            continue
        refs.append(
            GeneratedProjectionRef(
                page_id=page.page_id,
                label=_page_title(page),
                page_family=page.page_metadata.page_family,
                owner_section_page_id=owner_section,
                relation=relation,
                summary=page.summary,
            )
        )
    return tuple(refs)


def section_backlinks_for_generated_pages(
    pages: tuple[WikiPage, ...]
) -> dict[str, tuple[RelatedTopicLink, ...]]:
    grouped: dict[str, list[RelatedTopicLink]] = {}
    for ref in generated_projection_refs(pages):
        grouped.setdefault(ref.owner_section_page_id, []).append(
            RelatedTopicLink(ref.page_id, ref.label, ref.relation)
        )
    return {
        key: tuple(sorted(value, key=lambda link: (link.relation, link.page_id)))
        for key, value in grouped.items()
    }


def generated_page_navigation_findings(
    *,
    source_page_id: str,
    page_bodies: dict[str, str],
    page_families: dict[str, str],
) -> tuple[ProjectionNavigationFinding, ...]:
    inbound: dict[str, set[str]] = {page_id: set() for page_id in page_bodies}
    page_ids = set(page_bodies)
    for source_id, body in page_bodies.items():
        for target_id in extract_links(body) & page_ids:
            if target_id != source_id:
                inbound[target_id].add(source_id)
    findings: list[ProjectionNavigationFinding] = []
    for page_id in sorted(page_bodies):
        if _is_navigation_exempt(page_id, source_page_id, page_families.get(page_id, "")):
            continue
        if inbound[page_id]:
            continue
        findings.append(
            ProjectionNavigationFinding(
                "generated-page-has-no-inbound-route",
                page_id,
                "generated source-scoped page has no inbound route from this staged projection",
            )
        )
    return tuple(findings)


def _is_navigation_exempt(page_id: str, source_page_id: str, page_family: str) -> bool:
    return page_id == source_page_id or page_family == "source-manifest"


def _owner_section_page_id(page_body: str) -> str:
    match = _SOURCE_SECTION_RE.search(page_body)
    return match.group(1) if match else ""


def _page_title(page: WikiPage) -> str:
    for line in page.page_body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return page.page_id.replace("-", " ").title()
