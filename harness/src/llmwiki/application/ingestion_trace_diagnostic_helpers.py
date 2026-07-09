"""Shared helpers for source-neutral ingestion diagnostics."""

from __future__ import annotations

import re
from collections.abc import Mapping
from statistics import median
from typing import TypeGuard

from llmwiki.domain.ledger.canonical import short_digest

from .ingestion_trace_metrics import IngestionTraceInput
from .ingestion_trace_records import (
    IngestionMetric,
    IngestionMetricGroup,
    IngestionTraceFinding,
)

MAX_FINDINGS = 8
EXTREME_COVERAGE_MIN = 120
OVERSIZED_ASSERTION_MIN = 120
WEAK_SUBJECTS = frozenset(
    {"he", "she", "it", "they", "this", "that", "these", "those", "we", "you"}
)
CONTINUATION_STARTS = frozenset(
    {
        "and",
        "but",
        "or",
        "nor",
        "so",
        "yet",
        "therefore",
        "however",
        "because",
        "then",
        "also",
    }
)

TERMINAL_RE = re.compile(r"""[.!?]["')\]]*$""")
HEADING_RE = re.compile(r"^#{1,6}\s+")


def group(
    provider_id: str,
    kinds: tuple[str, ...],
    metrics: tuple[IngestionMetric, ...],
    findings: tuple[IngestionTraceFinding, ...],
) -> IngestionMetricGroup:
    return IngestionMetricGroup(
        provider_id=provider_id,
        metric_group_id=f"metric-group-{provider_id}",
        source_artifact_kinds=kinds,
        metrics=metrics,
        findings=findings,
    )


def metric(provider_id: str, kind: str, value: int | float | str) -> IngestionMetric:
    return IngestionMetric(
        metric_id=f"metric-{provider_id}-{kind}",
        metric_kind=kind,
        value=value,
        unit="count" if isinstance(value, int | float) else "value",
        subject_kind=provider_id,
        subject_id=kind,
    )


def score_metric(provider_id: str, kind: str, value: float) -> IngestionMetric:
    return IngestionMetric(
        metric_id=f"metric-{provider_id}-{kind}",
        metric_kind=kind,
        value=value,
        unit="score",
        subject_kind=provider_id,
        subject_id=kind,
    )


def finding(
    stage_id: str, reason: str, subject_kind: str, subject_id: str, message: str
) -> IngestionTraceFinding:
    return IngestionTraceFinding(
        finding_id=f"ingestion-trace-{stage_id}-{reason}-{short_digest(subject_id + message)}",
        severity="warning",
        stage_id=stage_id,
        reason=reason,
        subject_kind=subject_kind,
        subject_id=subject_id,
        message=message,
    )


def artifact(inputs: IngestionTraceInput, kind: str) -> Mapping[str, object]:
    return inputs.artifacts.get(kind, {})


def items(inputs: IngestionTraceInput, artifact_kind: str, key: str) -> list[object]:
    value = artifact(inputs, artifact_kind).get(key)
    return value if isinstance(value, list) else []


def dict_item(value: object) -> TypeGuard[dict[str, object]]:
    return isinstance(value, dict)


def list_len(data: Mapping[str, object], key: str) -> int:
    value = data.get(key)
    return len(value) if isinstance(value, list | tuple) else 0


def int_value(value: object) -> int:
    return value if isinstance(value, int) else 0


def nested(data: Mapping[str, object], *keys: str) -> object:
    value: object = data
    for key in keys:
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def coverage_count(page: object) -> int:
    return list_len(page, "coverage_records") if isinstance(page, dict) else 0


def median_value(values: list[int]) -> float:
    return float(median(values)) if values else 0.0


def sections(page_body: str) -> set[str]:
    return {
        match.group(1).strip()
        for match in re.finditer(r"^##\s+(.+)$", page_body, flags=re.MULTILINE)
    }


def extreme_threshold(counts: list[int]) -> int:
    if len(counts) < 4:
        return EXTREME_COVERAGE_MIN
    med = median_value(counts)
    return max(EXTREME_COVERAGE_MIN, int(med * 4))


def weak_subject(subject: str) -> bool:
    return subject.casefold() in WEAK_SUBJECTS


def continuation_text(text: str) -> bool:
    stripped = HEADING_RE.sub("", text).strip()
    if not stripped:
        return False
    first = stripped.split(maxsplit=1)[0].strip(",:;").casefold()
    return (
        first in CONTINUATION_STARTS
        or stripped[0].islower()
        or stripped.startswith((",", ";", ":", ")", "]"))
    )


def unterminated(unit: Mapping[str, object]) -> bool:
    text = str(unit.get("text", "")).strip()
    return bool(text) and kind(unit) != "heading" and not TERMINAL_RE.search(text)


def starts_continuation(unit: Mapping[str, object]) -> bool:
    return kind(unit) != "heading" and continuation_text(str(unit.get("text", "")))


def kind(unit: Mapping[str, object]) -> str:
    return str(unit.get("kind", ""))


def page_label(unit: Mapping[str, object]) -> str:
    span = unit.get("page_span")
    if not isinstance(span, list | tuple) or len(span) != 2:
        return "document"
    start, end = span
    if not isinstance(start, int) or not isinstance(end, int) or start <= 0 or end <= 0:
        return "document"
    return f"p.{start}" if start == end else f"p.{start}-{end}"


def preview(text: str) -> str:
    return " ".join(text.split())[:120]


def top_findings(
    findings: list[IngestionTraceFinding],
) -> tuple[IngestionTraceFinding, ...]:
    return tuple(findings[:MAX_FINDINGS])


def first_span_text(assertion: Mapping[str, object], spans: Mapping[str, object]) -> str:
    span_ids = assertion.get("evidence_span_ids")
    if not isinstance(span_ids, list) or not span_ids:
        return ""
    span = spans.get(str(span_ids[0]))
    return str(span.get("exact_text", "")) if isinstance(span, dict) else ""


def boundary_finding(reason: str, unit: dict) -> IngestionTraceFinding:
    unit_id = str(unit.get("id", "unknown-source-unit"))
    label = "heading appears inside a sentence continuation"
    if reason == "parent-change-across-continuation":
        label = "parent changed across a sentence-continuation boundary"
    return finding(
        "canonical-source",
        reason,
        "source-unit",
        unit_id,
        f"{unit_id}: {label}; page={page_label(unit)}; text={preview(str(unit.get('text', '')))}.",
    )
