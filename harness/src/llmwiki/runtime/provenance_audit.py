"""Deterministic provenance audit for generated source pages."""

from __future__ import annotations

import re
from collections import Counter

from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.projection_policy import PAGE_FAMILY_SOURCE_MANIFEST
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.runtime.provenance_audit_index import (
    ProvenanceArtifactIndex,
    ProvenanceEvidence,
    provenance_index_from_artifacts,
)
from llmwiki.runtime.provenance_audit_terms import (
    ROOT_CAUSES,
    clean_excerpt,
    fragmentary,
    topic_terms,
)
from llmwiki.runtime.provenance_audit_types import (
    PageAuditSummary,
    ProvenanceAuditReport,
    ProvenanceFinding,
)

_SOURCE_RANGE = re.compile(r"source-range-[a-f0-9]+-\d+")
_ORDER_OUTLIER_DISTANCE = 1_200


def build_provenance_audit(
    page_texts: dict[str, str],
    *,
    source_page_id: str,
    artifact_files: dict[str, str],
) -> ProvenanceAuditReport:
    index = provenance_index_from_artifacts(artifact_files)
    findings: list[ProvenanceFinding] = []
    manifest_findings: list[ProvenanceFinding] = []
    projected_findings: list[ProvenanceFinding] = []
    summaries: list[PageAuditSummary] = []
    cited_total = 0
    for page_id, text in sorted(page_texts.items()):
        if not page_id.startswith(source_page_id):
            continue
        try:
            page = parse_page(text)
        except PageError:
            continue
        title = _page_title(page.page_body) or page.page_id
        page_findings, cited_count = _audit_page(page.page_id, title, page.page_body, index)
        cited_total += cited_count
        findings.extend(page_findings)
        if page.page_metadata.page_family == PAGE_FAMILY_SOURCE_MANIFEST:
            manifest_findings.extend(page_findings)
        else:
            projected_findings.extend(page_findings)
        summaries.append(PageAuditSummary(page.page_id, title, cited_count, len(page_findings)))
    return _report(
        source_page_id,
        cited_total,
        summaries,
        findings,
        manifest_findings,
        projected_findings,
    )


def report_to_json(report: ProvenanceAuditReport) -> str:
    return canonical_json(report, indent=2)


def _audit_page(
    page_id: str,
    title: str,
    body: str,
    index: ProvenanceArtifactIndex,
) -> tuple[list[ProvenanceFinding], int]:
    findings: list[ProvenanceFinding] = []
    page_terms = topic_terms(f"{title} {page_id}")
    cited_ranges: list[str] = []
    lines = body.splitlines()
    for line_no, line in enumerate(lines, start=1):
        line_ranges = tuple(_SOURCE_RANGE.findall(line))
        for source_range_id in line_ranges:
            cited_ranges.append(source_range_id)
            evidence = index.evidence(source_range_id)
            if evidence is None:
                findings.append(
                    _finding(
                        page_id,
                        title,
                        line_no,
                        source_range_id,
                        "missing-ledger-range",
                        line,
                    )
                )
                continue
            findings.extend(
                _evidence_findings(
                    page_id,
                    title,
                    line_no,
                    line,
                    page_terms,
                    evidence,
                    len(line_ranges),
                )
            )
    findings.extend(_order_findings(page_id, title, lines, cited_ranges, index))
    return findings, len(cited_ranges)


def _evidence_findings(
    page_id: str,
    title: str,
    line_no: int,
    line: str,
    page_terms: frozenset[str],
    evidence: ProvenanceEvidence,
    line_range_count: int,
) -> list[ProvenanceFinding]:
    findings: list[ProvenanceFinding] = []
    if evidence.context_pointer:
        findings.append(
            _finding(
                page_id,
                title,
                line_no,
                evidence.source_range_id,
                "context-pointer-projected",
                line,
                evidence.section_path,
            )
        )
    if evidence.fragmentary and not (line_range_count > 1 and not fragmentary(line)):
        findings.append(
            _finding(
                page_id,
                title,
                line_no,
                evidence.source_range_id,
                "fragmentary-statement",
                line,
                evidence.section_path,
            )
        )
    evidence_terms = topic_terms(f"{evidence.section_path} {evidence.excerpt}")
    if evidence.structure_only:
        findings.append(
            _finding(
                page_id,
                title,
                line_no,
                evidence.source_range_id,
                "structure-only-range",
                line,
                evidence.section_path,
            )
        )
    elif page_terms and evidence_terms and not page_terms.intersection(evidence_terms):
        kind = "technical-atom-topic-gap" if evidence.has_technical_atom else "topic-support-gap"
        findings.append(
            _finding(
                page_id,
                title,
                line_no,
                evidence.source_range_id,
                kind,
                line,
                evidence.section_path,
            )
        )
    return findings


def _order_findings(
    page_id: str,
    title: str,
    lines: list[str],
    cited_ranges: list[str],
    index: ProvenanceArtifactIndex,
) -> list[ProvenanceFinding]:
    orders = [index.source_order(source_range_id) for source_range_id in cited_ranges]
    orders = [order for order in orders if order > 0]
    if not orders:
        return []
    midpoint = sorted(orders)[len(orders) // 2]
    findings: list[ProvenanceFinding] = []
    for source_range_id in sorted(set(cited_ranges)):
        order = index.source_order(source_range_id)
        if order > 0 and abs(order - midpoint) > _ORDER_OUTLIER_DISTANCE:
            evidence = index.evidence(source_range_id)
            findings.append(
                _finding(
                    page_id,
                    title,
                    _first_line(lines, source_range_id),
                    source_range_id,
                    "range-order-outlier",
                    evidence.excerpt if evidence is not None else source_range_id,
                    evidence.section_path if evidence is not None else "",
                )
            )
    return findings


def _report(
    source_page_id: str,
    cited_total: int,
    summaries: list[PageAuditSummary],
    findings: list[ProvenanceFinding],
    manifest_findings: list[ProvenanceFinding],
    projected_findings: list[ProvenanceFinding],
) -> ProvenanceAuditReport:
    return ProvenanceAuditReport(
        source_page_id=source_page_id,
        page_count=len(summaries),
        cited_item_count=cited_total,
        finding_count=len(findings),
        finding_counts=_counts(findings),
        source_manifest_finding_count=len(manifest_findings),
        source_manifest_finding_counts=_counts(manifest_findings),
        non_manifest_finding_count=len(projected_findings),
        non_manifest_finding_counts=_counts(projected_findings),
        page_summaries=tuple(summaries),
        findings=tuple(findings),
    )


def _counts(findings: list[ProvenanceFinding]) -> dict[str, int]:
    return dict(sorted(Counter(finding.finding_type for finding in findings).items()))


def _page_title(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return ""


def _finding(
    page_id: str,
    title: str,
    line_no: int,
    source_range_id: str,
    finding_type: str,
    line: str,
    section_path: str = "",
) -> ProvenanceFinding:
    return ProvenanceFinding(
        page_id=page_id,
        line_no=line_no,
        source_range_id=source_range_id,
        finding_type=finding_type,
        severity="warning",
        root_cause=ROOT_CAUSES.get(finding_type, "unclassified"),
        title=title,
        section_path=section_path,
        excerpt=clean_excerpt(line),
    )


def _first_line(lines: list[str], source_range_id: str) -> int:
    for line_no, line in enumerate(lines, start=1):
        if source_range_id in line:
            return line_no
    return 0
