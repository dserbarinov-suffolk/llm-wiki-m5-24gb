"""Trace metrics for positive projected page quality scores."""

from __future__ import annotations

from collections import Counter
from statistics import median
from typing import Literal

from .ingestion_trace_diagnostic_helpers import artifact, dict_item, group, metric, score_metric
from .ingestion_trace_metrics import IngestionTraceInput
from .ingestion_trace_records import (
    IngestionMetricGroup,
    IngestionTraceFinding,
)

_SCORE_FIELDS = (
    "source_locality_score",
    "topic_boundary_cohesion",
    "technical_atom_integrity_rate",
    "page_shape_fit",
    "walkability_score",
)
_BANDS = ("exemplary", "good", "usable", "suspect", "bad")


def page_quality_metric_provider(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    records = _quality_records(inputs)
    counts = Counter(str(record.get("overall_quality_band", "")) for record in records)
    metrics = [
        metric("page-quality", "quality-page-count", len(records)),
        *(metric("page-quality", f"quality-{band}-count", counts[band]) for band in _BANDS),
        *(
            score_metric("page-quality", f"median-{field}", _median_score(records, field))
            for field in _SCORE_FIELDS
        ),
    ]
    findings = (*_candidate_findings(records), *_low_quality_findings(records))
    return group(
        "page-quality",
        ("page-projection-artifact", "page-quality-report-artifact"),
        tuple(metrics),
        findings,
    )


def _quality_records(inputs: IngestionTraceInput) -> list[dict[str, object]]:
    report = artifact(inputs, "page-quality-report-artifact").get("report")
    if not isinstance(report, dict):
        return []
    records = report.get("page_quality_records")
    return [record for record in records if dict_item(record)] if isinstance(records, list) else []


def _median_score(records: list[dict[str, object]], field: str) -> float:
    values = [
        float(value)
        for record in records
        if isinstance(value := record.get(field), int | float)
    ]
    return round(float(median(values)), 3) if values else 0.0


def _candidate_findings(records: list[dict[str, object]]) -> tuple[IngestionTraceFinding, ...]:
    candidates = [
        record
        for record in records
        if str(record.get("overall_quality_band")) == "exemplary"
    ]
    if not candidates:
        candidates = [
            record for record in records if str(record.get("overall_quality_band")) == "good"
        ]
    candidates.sort(
        key=lambda record: (_minimum_score(record), _overall_score(record)),
        reverse=True,
    )
    return tuple(
        _quality_finding("info", "page-quality-candidate", record)
        for record in candidates[:5]
    )


def _low_quality_findings(records: list[dict[str, object]]) -> tuple[IngestionTraceFinding, ...]:
    candidates = [
        record
        for record in records
        if str(record.get("overall_quality_band")) in {"suspect", "bad"}
    ]
    candidates.sort(key=_overall_score)
    return tuple(
        _quality_finding("warning", "low-page-quality", record) for record in candidates[:8]
    )


def _quality_finding(
    severity: Literal["warning", "info"], reason: str, record: dict[str, object]
) -> IngestionTraceFinding:
    page_id = str(record.get("page_id", "unknown-page"))
    band = str(record.get("overall_quality_band", "unknown"))
    score = _minimum_score(record) if reason == "low-page-quality" else _overall_score(record)
    score_label = "minimum score" if reason == "low-page-quality" else "median score"
    raw_negatives = record.get("negative_reasons", ())
    negative_reasons = raw_negatives if isinstance(raw_negatives, list | tuple) else ()
    negatives = ", ".join(str(item) for item in negative_reasons[:3])
    suffix = f"; reasons={negatives}" if negatives else ""
    return IngestionTraceFinding(
        finding_id=f"ingestion-trace-page-quality-{reason}-{page_id}",
        severity=severity,
        stage_id="page-projection",
        reason=reason,
        subject_kind="page",
        subject_id=page_id,
        message=f"{page_id}: quality band {band}; {score_label}={score:.3f}{suffix}.",
    )


def _overall_score(record: dict[str, object]) -> float:
    values = [
        float(value)
        for field in _SCORE_FIELDS
        if isinstance(value := record.get(field), int | float)
    ]
    return float(median(values)) if values else 0.0


def _minimum_score(record: dict[str, object]) -> float:
    values = [
        float(value)
        for field in _SCORE_FIELDS
        if isinstance(value := record.get(field), int | float)
    ]
    return min(values) if values else 0.0
