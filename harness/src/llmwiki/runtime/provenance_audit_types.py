"""Provenance audit report contracts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProvenanceFinding:
    page_id: str
    line_no: int
    source_range_id: str
    finding_type: str
    severity: str
    root_cause: str
    title: str
    section_path: str
    excerpt: str


@dataclass(frozen=True)
class PageAuditSummary:
    page_id: str
    title: str
    cited_item_count: int
    finding_count: int


@dataclass(frozen=True)
class ProvenanceAuditReport:
    source_page_id: str
    page_count: int
    cited_item_count: int
    finding_count: int
    finding_counts: dict[str, int]
    source_manifest_finding_count: int
    source_manifest_finding_counts: dict[str, int]
    non_manifest_finding_count: int
    non_manifest_finding_counts: dict[str, int]
    page_summaries: tuple[PageAuditSummary, ...]
    findings: tuple[ProvenanceFinding, ...]
