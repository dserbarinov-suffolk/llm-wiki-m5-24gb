"""Cross-source synthesis pipeline (adapter/orchestrator).

Loads every stored per-source topic index, groups topics that recur across two
or more sources, and renders one ``CrossSourceWikiPage`` per shared topic plus a
synthesis overview. Each page is gated by a cross-source-projection quality
report and the write boundary. Deterministic: no model is called.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.artifacts import build_quality_check_catalog_artifact
from llmwiki.domain.ledger.cross_source import CrossSourceTopic, plan_cross_source_topics
from llmwiki.domain.ledger.cross_source_quality import build_cross_source_quality_report
from llmwiki.domain.ledger.cross_source_render import render_cross_source_page
from llmwiki.domain.ledger.pointers import PortableArtifactPointer, quality_check_catalog_pointer
from llmwiki.domain.ledger.quality import page_write_decision
from llmwiki.domain.ledger.quality_catalog import (
    QualityCheckCatalog,
    QualityFindingSeverityPolicy,
    default_quality_check_catalog,
    default_reason_applicability_policy,
    default_severity_policy,
)
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify
from llmwiki.runtime.cross_source_load import load_source_positions

_SYNTHESIS_PAGE = "cross-source-synthesis"
_RELATION_KINDS = ("agrees-with", "conflicts-with", "qualifies", "supersedes")


@dataclass(frozen=True)
class CrossSourceResult:
    pages: tuple[WikiPage, ...]
    topics: tuple[CrossSourceTopic, ...]
    blocked: tuple[str, ...]
    summary: str


def build_cross_source_pages(
    topic_index_jsons: tuple[str, ...], *, today: str
) -> CrossSourceResult:
    loaded = [load_source_positions(text) for text in topic_index_jsons]
    positions = tuple(position for source in loaded for position in source.positions)
    topics = plan_cross_source_topics(positions)
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    catalog_pointer = _catalog_pointer(catalog, severity)

    pages: list[WikiPage] = []
    written_topics: list[CrossSourceTopic] = []
    blocked: list[str] = []
    for topic in topics:
        page_id = slugify(topic.topic_key)
        rendered = render_cross_source_page(topic, page_id)
        report = build_cross_source_quality_report(
            topic,
            rendered.page_body,
            catalog=catalog,
            severity=severity,
            catalog_pointer=catalog_pointer,
        )
        if page_write_decision(report) == "block-authoritative-write":
            blocked.append(topic.topic_key)
            continue
        pages.append(
            _topic_page(topic, page_id, rendered.page_body, rendered.page_body_hash, today)
        )
        written_topics.append(topic)
    pages.append(_synthesis_page(written_topics, len(loaded), today))
    summary = (
        f"Cross-source synthesis over {len(loaded)} source(s): "
        f"{len(written_topics)} concept/entity page(s), {len(blocked)} blocked. "
        f"Relations: {_relation_summary(written_topics)}."
    )
    return CrossSourceResult(tuple(pages), tuple(written_topics), tuple(blocked), summary)


def _topic_page(
    topic: CrossSourceTopic, page_id: str, body: str, body_hash: str, today: str
) -> WikiPage:
    sources = tuple(sorted({f"raw/{position.source_locator}" for position in topic.positions}))
    metadata = PageMetadata(
        page_id=page_id,
        page_kind=topic.page_kind,
        summary=(
            f"Cross-source {topic.page_kind} '{topic.label}': "
            f"{len(topic.positions)} sources, {len(topic.relationships)} relation(s)."
        ),
        sources=sources,
        updated=today,
        category_path=f"{topic.page_kind}s",
        projection_coverage_pointer=f"cross-source-{page_id}@{body_hash}",
    )
    return WikiPage.from_metadata(metadata, body)


def _synthesis_page(topics: list[CrossSourceTopic], source_count: int, today: str) -> WikiPage:
    lines = [
        "# Cross-Source Synthesis",
        "",
        f"Concept and entity pages built from {source_count} ingested source ledger(s).",
        "",
        "## Topics",
        "",
    ]
    for topic in topics:
        lines.append(
            f"- [[{slugify(topic.topic_key)}]] — {topic.page_kind}, "
            f"{len(topic.support_ids)} sources, {len(topic.relationships)} relation(s)"
        )
    lines.extend(["", "## Relation summary", ""])
    counts = _relation_counts(topics)
    lines.extend(f"- {kind}: {counts.get(kind, 0)}" for kind in _RELATION_KINDS)
    metadata = PageMetadata(
        page_id=_SYNTHESIS_PAGE,
        page_kind="synthesis",
        summary=f"Cross-source synthesis index: {len(topics)} shared topics.",
        updated=today,
    )
    return WikiPage.from_metadata(metadata, "\n".join(lines) + "\n")


def _relation_counts(topics: list[CrossSourceTopic]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for topic in topics:
        for relationship in topic.relationships:
            kind = relationship.cross_source_relationship_kind
            counts[kind] = counts.get(kind, 0) + 1
    return counts


def _relation_summary(topics: list[CrossSourceTopic]) -> str:
    counts = _relation_counts(topics)
    return ", ".join(f"{kind}={counts.get(kind, 0)}" for kind in _RELATION_KINDS)


def _catalog_pointer(
    catalog: QualityCheckCatalog, severity: QualityFindingSeverityPolicy
) -> PortableArtifactPointer:
    artifact = build_quality_check_catalog_artifact(
        catalog, default_reason_applicability_policy(), severity
    )
    return quality_check_catalog_pointer(
        artifact.quality_check_catalog_artifact_id, artifact.quality_check_catalog_fingerprint
    )
