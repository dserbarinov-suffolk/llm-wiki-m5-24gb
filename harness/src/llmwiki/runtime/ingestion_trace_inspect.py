"""Read-only rendering for ingestion trace artifacts."""

from __future__ import annotations

from llmwiki.application.ingestion_trace_records import (
    IngestionMetric,
    IngestionMetricGroup,
    IngestionTraceArtifact,
    IngestionTraceCheck,
    IngestionTraceStage,
)


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
        lines.extend(f"- {finding.severity}: {finding.message}" for finding in findings)
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
