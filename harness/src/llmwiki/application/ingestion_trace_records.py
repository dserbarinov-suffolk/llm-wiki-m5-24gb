"""Portable ingestion trace records."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict

from llmwiki.domain.ledger.canonical import artifact_fingerprint, canonical_json
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT

CheckStatus = Literal["passed", "warning", "failed"]
FindingSeverity = Literal["blocking", "warning", "info"]
MetricValue = int | float | str


class IngestionTraceCheck(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    check_id: str
    status: CheckStatus
    subject_kind: str
    subject_id: str
    message: str


class IngestionMetric(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    metric_id: str
    metric_kind: str
    value: MetricValue
    unit: str
    subject_kind: str
    subject_id: str


class IngestionTraceFinding(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    finding_id: str
    severity: FindingSeverity
    stage_id: str
    reason: str
    subject_kind: str
    subject_id: str
    message: str


class IngestionMetricGroup(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    provider_id: str
    metric_group_id: str
    source_artifact_kinds: tuple[str, ...]
    metrics: tuple[IngestionMetric, ...]
    findings: tuple[IngestionTraceFinding, ...] = ()


class IngestionTraceArtifactPointer(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    portable_artifact_kind: str
    target_artifact_id: str
    target_artifact_fingerprint: str


class IngestionTraceStage(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    stage_id: str
    label: str
    input_artifact_kinds: tuple[str, ...]
    output_artifact_kinds: tuple[str, ...]
    precondition_checks: tuple[IngestionTraceCheck, ...]
    postcondition_checks: tuple[IngestionTraceCheck, ...]
    decisions: dict[str, str]
    summary_counts: tuple[IngestionMetric, ...]
    finding_ids: tuple[str, ...]


class IngestionTraceArtifact(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    ingestion_trace_artifact_id: str
    ingestion_trace_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    run_id: str
    stages: tuple[IngestionTraceStage, ...]
    metric_groups: tuple[IngestionMetricGroup, ...]
    artifact_pointers: tuple[IngestionTraceArtifactPointer, ...]
    summary_counts: tuple[IngestionMetric, ...]
    findings: tuple[IngestionTraceFinding, ...]


def finalized_trace_artifact(draft: IngestionTraceArtifact) -> IngestionTraceArtifact:
    fingerprint = artifact_fingerprint(
        draft.model_dump(mode="json"),
        exclude=("ingestion_trace_artifact_id", "ingestion_trace_fingerprint"),
    )
    return draft.model_copy(
        update={
            "ingestion_trace_artifact_id": f"ingestion-trace-{fingerprint}",
            "ingestion_trace_fingerprint": fingerprint,
        }
    )


def ingestion_trace_artifact_to_json(artifact: IngestionTraceArtifact) -> str:
    return canonical_json(artifact, indent=2)


def ingestion_trace_artifact_from_json(text: str) -> IngestionTraceArtifact:
    return IngestionTraceArtifact.model_validate_json(text)


def draft_trace_artifact(
    *,
    source_locator: str,
    source_hash: str,
    run_id: str,
    stages: tuple[IngestionTraceStage, ...],
    metric_groups: tuple[IngestionMetricGroup, ...],
    artifact_pointers: tuple[IngestionTraceArtifactPointer, ...],
    findings: tuple[IngestionTraceFinding, ...],
) -> IngestionTraceArtifact:
    return IngestionTraceArtifact(
        ingestion_trace_artifact_id="pending",
        ingestion_trace_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_locator=source_locator,
        source_hash=source_hash,
        run_id=run_id,
        stages=stages,
        metric_groups=metric_groups,
        artifact_pointers=artifact_pointers,
        summary_counts=tuple(metric for group in metric_groups for metric in group.metrics),
        findings=findings,
    )
