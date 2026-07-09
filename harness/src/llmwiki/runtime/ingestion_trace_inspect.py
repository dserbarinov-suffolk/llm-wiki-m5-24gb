"""Read-only rendering for ingestion trace artifacts."""

from __future__ import annotations

from llmwiki.application.ingestion_trace_records import (
    IngestionMetric,
    IngestionMetricGroup,
    IngestionTraceArtifact,
    IngestionTraceCheck,
    IngestionTraceFinding,
    IngestionTraceStage,
)

_SUMMARY_FINDING_LIMIT = 12


def render_trace_summary(trace: IngestionTraceArtifact) -> str:
    lines = [
        f"Ingestion trace for raw/{trace.source_locator}",
        f"Source hash: {trace.source_hash}",
        f"Run id: {trace.run_id}",
        f"Stages: {len(trace.stages)}",
        "",
    ]
    for stage in trace.stages:
        failed = _failed_count(stage)
        finding_label = f", findings={len(stage.finding_ids)}" if stage.finding_ids else ""
        lines.append(
            f"- {stage.stage_id}: {_status_label(failed)}"
            f" ({_counts_label(stage.summary_counts)}{finding_label})"
        )
    if trace.findings:
        lines.extend(("", "Diagnostics:"))
        lines.extend(_finding_lines(_ranked_findings(trace.findings)[:_SUMMARY_FINDING_LIMIT]))
        omitted = len(trace.findings) - _SUMMARY_FINDING_LIMIT
        if omitted > 0:
            lines.append(f"- ... {omitted} additional finding(s)")
    return "\n".join(lines).rstrip()


def render_trace_stage(trace: IngestionTraceArtifact, stage_id: str) -> str:
    stage = next((item for item in trace.stages if item.stage_id == stage_id), None)
    if stage is None:
        valid = ", ".join(item.stage_id for item in trace.stages)
        raise ValueError(f"Unknown trace stage {stage_id!r}. Valid stages: {valid}")
    groups = _stage_metric_groups(trace, stage)
    lines = [
        f"Ingestion trace stage: {stage.stage_id}",
        f"Label: {stage.label}",
        f"Inputs: {', '.join(stage.input_artifact_kinds) or 'none'}",
        f"Outputs: {', '.join(stage.output_artifact_kinds) or 'none'}",
        "",
        "Preconditions:",
        *_check_lines(stage.precondition_checks),
        "",
        "Postconditions:",
        *_check_lines(stage.postcondition_checks),
    ]
    if stage.decisions:
        lines.extend(
            ("", "Decisions:", *[f"- {key}: {value}" for key, value in stage.decisions.items()])
        )
    if stage.summary_counts:
        lines.extend(("", "Stage Counts:", *_metric_lines(stage.summary_counts)))
    if groups:
        lines.append("")
        lines.append("Metric Groups:")
        for group in groups:
            lines.append(f"- {group.provider_id}")
            lines.extend(f"  - {line.removeprefix('- ')}" for line in _metric_lines(group.metrics))
    findings = [finding for finding in trace.findings if finding.finding_id in stage.finding_ids]
    if findings:
        lines.extend(("", "Findings:"))
        lines.extend(_finding_lines(_ranked_findings(tuple(findings))))
    return "\n".join(lines).rstrip()


def _stage_metric_groups(
    trace: IngestionTraceArtifact, stage: IngestionTraceStage
) -> tuple[IngestionMetricGroup, ...]:
    output_kinds = set(stage.output_artifact_kinds)
    return tuple(
        group
        for group in trace.metric_groups
        if output_kinds.intersection(group.source_artifact_kinds)
    )


def _check_lines(checks: tuple[IngestionTraceCheck, ...]) -> list[str]:
    if not checks:
        return ["- none"]
    return [f"- {check.status}: {check.subject_id} - {check.message}" for check in checks]


def _metric_lines(metrics: tuple[IngestionMetric, ...]) -> list[str]:
    if not metrics:
        return ["- none"]
    return [f"- {metric.metric_kind}: {metric.value} {metric.unit}" for metric in metrics]


def _finding_lines(findings: tuple[IngestionTraceFinding, ...]) -> list[str]:
    return [
        f"- {finding.severity}: {finding.stage_id}/{finding.reason}: {finding.message}"
        for finding in findings
    ]


def _ranked_findings(
    findings: tuple[IngestionTraceFinding, ...],
) -> tuple[IngestionTraceFinding, ...]:
    severity_rank = {"blocking": 0, "warning": 1, "info": 2}
    reason_rank = {
        "extreme-projection-coverage": 0,
        "oversized-topic-closure": 1,
        "concept-rendered-as-procedure": 2,
        "heading-in-continuation": 3,
        "parent-change-across-continuation": 4,
        "weak-assertion-attribution": 5,
        "accepted-output-with-diagnostics": 6,
    }
    return tuple(
        sorted(
            findings,
            key=lambda finding: (
                severity_rank[finding.severity],
                reason_rank.get(finding.reason, 99),
                finding.reason,
                finding.stage_id,
                finding.subject_id,
            ),
        )
    )


def _failed_count(stage: IngestionTraceStage) -> int:
    return sum(
        1
        for check in (*stage.precondition_checks, *stage.postcondition_checks)
        if check.status == "failed"
    )


def _status_label(failed: int) -> str:
    return "ok" if failed == 0 else f"{failed} failed check(s)"


def _counts_label(metrics: tuple[IngestionMetric, ...]) -> str:
    if not metrics:
        return "no stage counts"
    return ", ".join(f"{metric.metric_kind}={metric.value}" for metric in metrics)
