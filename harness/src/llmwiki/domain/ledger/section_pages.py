"""Source-structure reference pages.

Topic pages are selective. These pages follow the source's own headings and are
therefore better for authoritative lookup inside a chapter or section.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.projection_policy import PAGE_FAMILY_SECTION_REFERENCE
from llmwiki.domain.ledger.section_navigation import (
    SectionPageRef,
    nodes_by_topic_key,
    related_section_links,
    section_page_id,
    section_title,
)
from llmwiki.domain.ledger.section_page_atoms import atoms_for_section_entries
from llmwiki.domain.ledger.section_page_render import append_atoms, append_claims, claim_entries
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_relations import RelatedTopicLink
from llmwiki.domain.ledger.walkability import audit_related_links, related_links_markdown
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify

_SECTION_NODE_KINDS = {"chapter", "section", "heading", "record"}


@dataclass(frozen=True)
class _SectionProjection:
    node: StructureNode
    page_id: str
    title: str
    direct_entries: tuple[LedgerEntry, ...]
    rollup_entries: tuple[LedgerEntry, ...]
    atoms: tuple[TechnicalAtom, ...]

    @property
    def page_ref(self) -> SectionPageRef:
        return SectionPageRef(self.node, self.page_id, self.title)


def build_section_pages(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    section_plan: SectionGroundedPlan,
    source_page_id: str,
    source_locator: str,
    today: str,
    topics: tuple[SourceTopic, ...] = (),
    projection_context: ProjectionContext | None = None,
    extra_related_links_by_page_id: dict[str, tuple[RelatedTopicLink, ...]] | None = None,
) -> tuple[WikiPage, ...]:
    extra_related_links_by_page_id = extra_related_links_by_page_id or {}
    projections = _section_projections(ledger, structure, source_page_id, section_plan)
    by_node = {projection.node.structure_node_id: projection.page_ref for projection in projections}
    same_topic = nodes_by_topic_key(tuple(projection.node for projection in projections))
    topic_page_ids = {
        topic.topic_key: slugify(f"{source_page_id}-{topic.topic_key}") for topic in topics
    }
    pages: list[WikiPage] = []
    for projection in projections:
        related = related_section_links(
            projection.page_ref, structure, by_node, same_topic, topic_page_ids
        )
        related = (*related, *extra_related_links_by_page_id.get(projection.page_id, ()))
        walkability = audit_related_links(
            projection.page_id,
            related,
            ledger,
            projection_context=projection_context,
        )
        body = _body(
            ledger,
            structure,
            projection,
            source_page_id,
            walkability.accepted_links,
            projection_context,
        )
        metadata = PageMetadata(
            page_id=projection.page_id,
            page_kind="source",
            summary=(
                f"{projection.title}: {len(projection.rollup_entries)} source-backed entries and "
                f"{len(projection.atoms)} atom(s) from raw/{source_locator}."
            ),
            sources=(f"raw/{source_locator}",),
            updated=today,
            domain=source_page_id,
            category_path=f"sources/{source_page_id}/sections",
            source_id=source_locator,
            projection_coverage_pointer=f"section-{projection.page_id}@{short_digest(body, 32)}",
            page_family=PAGE_FAMILY_SECTION_REFERENCE,
        )
        pages.append(WikiPage.from_metadata(metadata, body))
    return tuple(pages)


def _body(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    projection: _SectionProjection,
    source_page_id: str,
    related_links: tuple[RelatedTopicLink, ...],
    projection_context: ProjectionContext | None,
) -> str:
    lines = [f"# {projection.title}", "", f"From [[{source_page_id}]].", ""]
    if related_links:
        lines.extend(("## Related pages", ""))
        lines.extend(related_links_markdown(related_links).splitlines())
        lines.append("")
    direct_claims = claim_entries(projection.direct_entries)
    if direct_claims:
        lines.extend(("## Statements", ""))
        append_claims(lines, direct_claims, projection_context)
        lines.append("")
    grouped = _group_descendant_claims(structure, projection.node, projection.rollup_entries)
    if grouped:
        lines.extend(("## Statements by subsection", ""))
        for node, claims in grouped:
            lines.extend((f"### {section_title(structure, node)}", ""))
            append_claims(lines, claims, projection_context)
            lines.append("")
    if projection.atoms:
        lines.extend(("## Technical atoms", ""))
        append_atoms(lines, ledger, projection.atoms, projection_context)
    return "\n".join(lines).strip() + "\n"


def _section_projections(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    source_page_id: str,
    section_plan: SectionGroundedPlan,
) -> tuple[_SectionProjection, ...]:
    projections: list[_SectionProjection] = []
    promoted_node_ids = tuple(
        dict.fromkeys(
            target.structure_node_id for target in section_plan.page_targets if target.page_promoted
        )
    )
    promoted_node_id_set = frozenset(promoted_node_ids)
    for node in _promoted_section_nodes(structure, promoted_node_ids):
        rollup_entries = _entries_for_promoted_node(
            ledger, node.structure_node_id, promoted_node_id_set
        )
        atoms = atoms_for_section_entries(ledger, rollup_entries, structure, node)
        if (
            not rollup_entries
            and not atoms
            and not _has_promoted_descendant(structure, node, promoted_node_id_set)
        ):
            continue
        projections.append(
            _SectionProjection(
                node=node,
                page_id=section_page_id(source_page_id, structure, node),
                title=section_title(structure, node),
                direct_entries=_direct_entries_for_node(ledger, node.structure_node_id),
                rollup_entries=rollup_entries,
                atoms=atoms,
            )
        )
    return tuple(projections)


def _promoted_section_nodes(
    structure: DocumentStructure, promoted_node_ids: tuple[str, ...]
) -> tuple[StructureNode, ...]:
    promoted = set(promoted_node_ids)
    return tuple(
        node
        for node in sorted(structure.structure_nodes, key=lambda item: item.source_order)
        if node.structure_node_kind in _SECTION_NODE_KINDS and node.structure_node_id in promoted
    )


def _group_descendant_claims(
    structure: DocumentStructure, node: StructureNode, entries: tuple[LedgerEntry, ...]
) -> tuple[tuple[StructureNode, tuple[LedgerEntry, ...]], ...]:
    grouped: dict[str, list[LedgerEntry]] = {}
    for entry in claim_entries(entries):
        nearest = entry.structure_node_ids[0] if entry.structure_node_ids else ""
        if not nearest or nearest == node.structure_node_id:
            continue
        grouped.setdefault(nearest, []).append(entry)
    result: list[tuple[StructureNode, tuple[LedgerEntry, ...]]] = []
    for descendant in structure.descendants(node.structure_node_id):
        claims = tuple(grouped.get(descendant.structure_node_id, ()))
        if claims:
            result.append((descendant, claims))
    return tuple(result)


def _direct_entries_for_node(ledger: ClaimLedger, node_id: str) -> tuple[LedgerEntry, ...]:
    return tuple(
        entry
        for entry in ledger.usable_entries
        if entry.structure_node_ids[:1] == (node_id,)
        and (entry.normalized_text or entry.source_text or entry.technical_atom_id)
    )


def _entries_for_node(ledger: ClaimLedger, node_id: str) -> tuple[LedgerEntry, ...]:
    return tuple(
        entry
        for entry in ledger.usable_entries
        if node_id in entry.structure_node_ids
        and (entry.normalized_text or entry.source_text or entry.technical_atom_id)
    )


def _entries_for_promoted_node(
    ledger: ClaimLedger,
    node_id: str,
    promoted_node_ids: frozenset[str],
) -> tuple[LedgerEntry, ...]:
    return tuple(
        entry
        for entry in ledger.usable_entries
        if _owning_promoted_node_id(entry.structure_node_ids, promoted_node_ids) == node_id
        and (entry.normalized_text or entry.source_text or entry.technical_atom_id)
    )


def _owning_promoted_node_id(
    entry_node_ids: tuple[str, ...], promoted_node_ids: frozenset[str]
) -> str:
    for candidate in entry_node_ids:
        if candidate in promoted_node_ids:
            return candidate
    return ""


def _has_promoted_descendant(
    structure: DocumentStructure, node: StructureNode, promoted_node_ids: frozenset[str]
) -> bool:
    return any(
        descendant.structure_node_id in promoted_node_ids
        for descendant in structure.descendants(node.structure_node_id)
    )
