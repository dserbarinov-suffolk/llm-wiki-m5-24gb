"""Build portable ingestion traces from parsed ingest artifacts."""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from llmwiki.domain.graph import GraphStatus
from llmwiki.domain.ledger.artifacts import PortableArtifactMember
from llmwiki.domain.ledger.canonical import short_digest

from .ingestion_trace_metrics import (
    IngestionMetricProvider,
    IngestionTraceInput,
    lint_metrics,
    page_projection_metrics,
    publish_metrics,
    topic_state_metrics,
)
from .ingestion_trace_records import (
    IngestionMetricGroup,
    IngestionTraceArtifact,
    IngestionTraceArtifactPointer,
    IngestionTraceCheck,
    IngestionTraceFinding,
    IngestionTraceStage,
    draft_trace_artifact,
    finalized_trace_artifact,
)


@dataclass(frozen=True)
class _StageSpec:
    stage_id: str
    label: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]


_STAGES = (
    _StageSpec("source-plan", "Source Plan", (), ("source-plan-artifact",)),
    _StageSpec(
        "source-extraction",
        "Source Extraction",
        ("source-plan-artifact",),
        ("extraction-result-artifact",),
    ),
    _StageSpec(
        "canonical-source",
        "Canonical Source",
        ("extraction-result-artifact",),
        ("assertion-graph-source-artifact",),
    ),
    _StageSpec(
        "document-structure",
        "Document Structure",
        ("assertion-graph-source-artifact",),
        ("document-structure-artifact",),
    ),
    _StageSpec(
        "claim-ledger",
        "Claim Ledger",
        ("document-structure-artifact",),
        ("claim-ledger-artifact",),
    ),
    _StageSpec(
        "proposed-change-review",
        "Proposed Change Review",
        ("claim-ledger-artifact",),
        ("proposed-change-review-artifact",),
    ),
    _StageSpec(
        "assertion-graph",
        "Assertion Graph",
        ("claim-ledger-artifact", "assertion-graph-source-artifact"),
        ("assertion-graph-artifact",),
    ),
    _StageSpec(
        "topic-state",
        "Topic State",
        ("assertion-graph-artifact",),
        ("topic-state-artifact",),
    ),
    _StageSpec(
        "page-projection",
        "Page Projection",
        ("topic-state-artifact",),
        ("page-projection-artifact",),
    ),
    _StageSpec(
        "staged-pages",
        "Staged Pages",
        ("page-projection-artifact",),
        ("staged-wiki-page-set-artifact",),
    ),
    _StageSpec(
        "lint-run",
        "Lint Run",
        ("staged-wiki-page-set-artifact",),
        ("projection-lint-run-artifact",),
    ),
    _StageSpec(
        "publish-run",
        "Publish Run",
        ("projection-lint-run-artifact",),
        ("publish-run-artifact",),
    ),
    _StageSpec(
        "projection-coverage",
        "Projection Coverage",
        ("publish-run-artifact",),
        ("projection-coverage-artifact",),
    ),
    _StageSpec(
        "provenance-audit",
        "Provenance Audit",
        ("projection-coverage-artifact",),
        ("provenance-audit-report",),
    ),
    _StageSpec("graph-export", "Graph Export", ("publish-run-artifact",), ("graph-export",)),
)

_ARTIFACT_FILES = {
    "assertion-graph-artifact": "assertion-graph.json",
    "assertion-graph-source-artifact": "assertion-graph-source-artifact.json",
    "blocked-write-diagnostic-artifact": "blocked-write-diagnostic.json",
    "claim-ledger-artifact": "claim-ledger.json",
    "document-structure-artifact": "document-structure.json",
    "extraction-result-artifact": "extraction-result.json",
    "page-projection-artifact": "page-projections.json",
    "projection-coverage-artifact": "projection-coverage.json",
    "projection-lint-run-artifact": "lint-run.json",
    "proposed-change-review-artifact": "proposed-change-review.json",
    "provenance-audit-report": "provenance-audit.json",
    "publish-run-artifact": "publish-run.json",
    "source-plan-artifact": "source-plan.json",
    "staged-wiki-page-set-artifact": "staged-pages.json",
    "topic-state-artifact": "topic-states.json",
}


def build_ingestion_trace(
    *,
    source_locator: str,
    source_hash: str,
    run_id: str,
    artifact_files: Mapping[str, str],
    artifact_members: Sequence[PortableArtifactMember],
    graph_status: GraphStatus | None,
    metric_providers: Sequence[IngestionMetricProvider],
) -> IngestionTraceArtifact:
    artifacts = _parse_artifacts(artifact_files, graph_status)
    inputs = IngestionTraceInput(source_locator, source_hash, artifacts, graph_status)
    findings: list[IngestionTraceFinding] = []
    metric_groups = tuple(_metric_groups(inputs, metric_providers, findings))
    stages = tuple(_stage(spec, artifacts, findings) for spec in _STAGES)
    return finalized_trace_artifact(
        draft_trace_artifact(
            source_locator=source_locator,
            source_hash=source_hash,
            run_id=run_id,
            stages=stages,
            metric_groups=metric_groups,
            artifact_pointers=tuple(_pointer(member) for member in artifact_members),
            findings=tuple(findings),
        )
    )


def _parse_artifacts(
    artifact_files: Mapping[str, str], graph: GraphStatus | None
) -> dict[str, Mapping[str, object]]:
    parsed: dict[str, Mapping[str, object]] = {}
    for kind, filename in _ARTIFACT_FILES.items():
        if text := artifact_files.get(filename):
            parsed[kind] = json.loads(text)
    if graph is not None:
        parsed["graph-export"] = {
            "status": graph.status,
            "node_count": graph.node_count,
            "edge_count": graph.edge_count,
            "unresolved_edge_count": graph.unresolved_edge_count,
        }
    return parsed


def _stage(
    spec: _StageSpec,
    artifacts: Mapping[str, Mapping[str, object]],
    findings: list[IngestionTraceFinding],
) -> IngestionTraceStage:
    pre = tuple(
        _check(spec.stage_id, "precondition", kind, kind in artifacts)
        for kind in spec.inputs
    )
    post = tuple(
        _check(spec.stage_id, "postcondition", kind, kind in artifacts)
        for kind in spec.outputs
    )
    stage_findings = tuple(
        _finding(spec.stage_id, "missing-stage-artifact", check.subject_id, check.message)
        for check in (*pre, *post)
        if check.status == "failed"
    )
    existing_stage_findings = tuple(
        finding for finding in findings if finding.stage_id == spec.stage_id
    )
    findings.extend(stage_findings)
    all_stage_findings = (*existing_stage_findings, *stage_findings)
    return IngestionTraceStage(
        stage_id=spec.stage_id,
        label=spec.label,
        input_artifact_kinds=spec.inputs,
        output_artifact_kinds=spec.outputs,
        precondition_checks=pre,
        postcondition_checks=post,
        decisions=_decisions(spec.stage_id, artifacts),
        summary_counts=_stage_counts(spec.stage_id, artifacts),
        finding_ids=tuple(finding.finding_id for finding in all_stage_findings),
    )


def _check(stage_id: str, prefix: str, artifact_kind: str, ok: bool) -> IngestionTraceCheck:
    return IngestionTraceCheck(
        check_id=f"{stage_id}-{prefix}-{artifact_kind}",
        status="passed" if ok else "failed",
        subject_kind="artifact-kind",
        subject_id=artifact_kind,
        message=f"{artifact_kind} {'present' if ok else 'missing'}",
    )


def _finding(stage_id: str, reason: str, subject_id: str, message: str) -> IngestionTraceFinding:
    return IngestionTraceFinding(
        finding_id=f"ingestion-trace-{stage_id}-{reason}-{short_digest(subject_id)}",
        severity="warning",
        stage_id=stage_id,
        reason=reason,
        subject_kind="artifact-kind",
        subject_id=subject_id,
        message=message,
    )


def _decisions(stage_id: str, artifacts: Mapping[str, Mapping[str, object]]) -> dict[str, str]:
    if stage_id == "claim-ledger":
        assignment = _nested(
            artifacts, "claim-ledger-artifact", "ledger", "source_family_assignment"
        )
        return {"source_family": str(assignment)} if assignment else {}
    if stage_id == "lint-run":
        return _string_fields(
            artifacts.get("projection-lint-run-artifact", {}),
            ("status", "upstream_write_decision"),
        )
    if stage_id == "publish-run":
        return _string_fields(
            artifacts.get("publish-run-artifact", {}), ("status", "blocked_reason")
        )
    if stage_id == "graph-export":
        return _string_fields(artifacts.get("graph-export", {}), ("status",))
    return {}


def _stage_counts(
    stage_id: str, artifacts: Mapping[str, Mapping[str, object]]
):
    if stage_id == "topic-state":
        return topic_state_metrics(artifacts)
    if stage_id == "page-projection":
        return page_projection_metrics(artifacts)
    if stage_id == "lint-run":
        return lint_metrics(artifacts)
    if stage_id == "publish-run":
        return publish_metrics(artifacts)
    return ()


def _metric_groups(
    inputs: IngestionTraceInput,
    providers: Sequence[IngestionMetricProvider],
    findings: list[IngestionTraceFinding],
) -> list[IngestionMetricGroup]:
    groups = []
    for provider in providers:
        try:
            group = provider(inputs)
            findings.extend(group.findings)
            groups.append(group)
        except Exception as exc:
            provider_id = getattr(provider, "__name__", "metric-provider")
            finding = IngestionTraceFinding(
                finding_id=f"ingestion-trace-provider-failed-{short_digest(provider_id)}",
                severity="warning",
                stage_id="metric-provider",
                reason="metric-provider-failed",
                subject_kind="metric-provider",
                subject_id=provider_id,
                message=str(exc),
            )
            findings.append(finding)
            groups.append(
                IngestionMetricGroup(
                    provider_id=provider_id,
                    metric_group_id=f"metric-group-{provider_id}",
                    source_artifact_kinds=(),
                    metrics=(),
                    findings=(finding,),
                )
            )
    return groups


def _nested(
    artifacts: Mapping[str, Mapping[str, object]], artifact_kind: str, *keys: str
) -> object:
    value: object = artifacts.get(artifact_kind, {})
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def _string_fields(data: Mapping[str, object], fields: tuple[str, ...]) -> dict[str, str]:
    return {field: str(value) for field in fields if (value := data.get(field))}


def _pointer(member: PortableArtifactMember) -> IngestionTraceArtifactPointer:
    return IngestionTraceArtifactPointer(
        portable_artifact_kind=member.portable_artifact_kind,
        target_artifact_id=member.target_artifact_id,
        target_artifact_fingerprint=member.target_artifact_fingerprint,
    )
