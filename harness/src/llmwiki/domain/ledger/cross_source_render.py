"""Render a CrossSourceWikiPage body from a cross-source topic.

Each source-backed position is rendered as its own generated page claim with
its own source citation — positions are never merged, so conflicting views stay
side by side. A cross-source relations section lists the typed relationships.
Every position and relationship gets one projection coverage entry.
"""

from __future__ import annotations

from llmwiki.domain.ledger.canonical import deterministic_id, short_digest
from llmwiki.domain.ledger.coverage import (
    PageBodyBuilder,
    PageTextRange,
    ProjectionCoverage,
    ProjectionCoverageEntry,
    RenderedPage,
    clean_statement,
)
from llmwiki.domain.ledger.cross_source import CrossSourceTopic


def render_cross_source_page(topic: CrossSourceTopic, wiki_page_locator: str) -> RenderedPage:
    body = PageBodyBuilder()
    entries: list[ProjectionCoverageEntry] = []
    body.add(f"# {topic.label}\n\n")
    body.add(
        f"Cross-source {topic.page_kind}: how {len(topic.positions)} source(s) treat "
        f"{topic.label}.\n\n## Positions\n\n"
    )
    for position in topic.positions:
        span = body.add(
            f"- {clean_statement(position.text)} _([[{_source_page(position.source_locator)}]] "
            f"— {position.citation_label})_\n"
        )
        entries.append(
            _coverage(
                wiki_page_locator,
                "generated-page-claim",
                span,
                selected=(position.ledger_entry_id,),
            )
        )
    if topic.relationships:
        body.add("\n## Cross-source relations\n\n")
        by_id = {p.source_backed_position_id: p for p in topic.positions}
        for relationship in topic.relationships:
            labels = " / ".join(
                f"[[{_source_page(by_id[pid].source_locator)}]]"
                for pid in relationship.related_position_ids
                if pid in by_id
            )
            span = body.add(f"- {relationship.cross_source_relationship_kind}: {labels}\n")
            entries.append(
                _coverage(
                    wiki_page_locator,
                    "cross-source-relationship",
                    span,
                    cross_source_relationship_id=relationship.cross_source_relationship_id,
                )
            )
    text = body.text()
    return RenderedPage(text, short_digest(text, 32), ProjectionCoverage(tuple(entries)))


def _coverage(
    wiki_page_locator: str,
    unit_kind: str,
    span: PageTextRange,
    *,
    selected: tuple[str, ...] = (),
    cross_source_relationship_id: str = "",
) -> ProjectionCoverageEntry:
    entry_id = deterministic_id(
        "projection-coverage-entry",
        wiki_page_locator,
        unit_kind,
        f"{span.start}-{span.end}",
        "|".join(selected) or cross_source_relationship_id,
    )
    return ProjectionCoverageEntry(
        projection_coverage_entry_id=entry_id,
        projection_coverage_unit_kind=unit_kind,
        page_text_range=span,
        selected_ledger_entry_ids=selected,
        cross_source_relationship_id=cross_source_relationship_id,
    )


def _source_page(source_locator: str) -> str:
    from llmwiki.domain.pages import slugify

    return slugify(source_locator.rsplit(".", 1)[0])
