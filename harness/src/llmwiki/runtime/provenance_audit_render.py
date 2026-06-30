"""Markdown projection for provenance audit reports."""

from __future__ import annotations

from llmwiki.runtime.provenance_audit_terms import ROOT_CAUSES
from llmwiki.runtime.provenance_audit_types import ProvenanceAuditReport


def render_markdown(report: ProvenanceAuditReport) -> str:
    lines = [
        "# Provenance Audit",
        "",
        "## Scope",
        "",
        f"- Source page id: `{report.source_page_id}`",
        f"- Pages audited: {report.page_count}",
        f"- Cited source-range items audited: {report.cited_item_count}",
        f"- Findings: {report.finding_count}",
        "",
        "## Finding Counts",
        "",
    ]
    lines.extend(f"- {kind}: {count}" for kind, count in report.finding_counts.items())
    lines.extend(["", "## Non-Manifest Finding Counts", ""])
    lines.append(f"- total: {report.non_manifest_finding_count}")
    lines.extend(
        f"- {kind}: {count}" for kind, count in report.non_manifest_finding_counts.items()
    )
    lines.extend(["", "## Source Manifest Finding Counts", ""])
    lines.append(f"- total: {report.source_manifest_finding_count}")
    lines.extend(
        f"- {kind}: {count}" for kind, count in report.source_manifest_finding_counts.items()
    )
    lines.extend(["", "## Root-Cause Classes", ""])
    lines.extend(
        f"- {kind}: {ROOT_CAUSES.get(kind, 'unclassified')}" for kind in report.finding_counts
    )
    lines.extend(["", "## Highest-Risk Pages", ""])
    for summary in sorted(report.page_summaries, key=lambda item: -item.finding_count)[:25]:
        if summary.finding_count:
            lines.append(
                f"- [[{summary.page_id}]]: {summary.finding_count} finding(s), "
                f"{summary.cited_item_count} cited item(s) - {summary.title}"
            )
    lines.extend(["", "## Representative Findings", ""])
    for finding in report.findings[:200]:
        lines.append(
            f"- {finding.finding_type} on [[{finding.page_id}]] line {finding.line_no}: "
            f"{finding.source_range_id}; {finding.root_cause}; "
            f"section `{finding.section_path}`; excerpt `{finding.excerpt}`"
        )
    return "\n".join(lines).strip() + "\n"
