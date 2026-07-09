"""Source-neutral diagnostic metric providers for ingestion traces."""

from __future__ import annotations

from collections import Counter

from .ingestion_trace_diagnostic_helpers import (
    EXTREME_COVERAGE_MIN,
    OVERSIZED_ASSERTION_MIN,
    artifact,
    boundary_finding,
    continuation_text,
    coverage_count,
    dict_item,
    extreme_threshold,
    finding,
    first_span_text,
    group,
    int_value,
    items,
    kind,
    list_len,
    median_value,
    metric,
    nested,
    sections,
    starts_continuation,
    top_findings,
    unterminated,
    weak_subject,
)
from .ingestion_trace_metrics import IngestionTraceInput
from .ingestion_trace_records import IngestionMetricGroup, IngestionTraceFinding


def diagnostic_metric_providers():
    return (
        projection_diagnostics,
        assertion_quality_diagnostics,
        source_boundary_diagnostics,
        topic_aggregation_diagnostics,
        gate_effectiveness_diagnostics,
    )


def projection_diagnostics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    pages = items(inputs, "page-projection-artifact", "page_projections")
    families = Counter(str(page.get("page_family", "")) for page in pages if dict_item(page))
    coverage_counts = [coverage_count(page) for page in pages if dict_item(page)]
    metrics = [
        metric("projection-diagnostics", "page-family-count", len(families)),
        metric("projection-diagnostics", "max-coverage-records", max(coverage_counts, default=0)),
        metric("projection-diagnostics", "median-coverage-records", median_value(coverage_counts)),
    ]
    metrics.extend(
        metric("projection-diagnostics", f"page-family-{family or 'unknown'}", count)
        for family, count in sorted(families.items())
    )
    findings: list[tuple[int, IngestionTraceFinding]] = []
    for page in pages:
        if not dict_item(page):
            continue
        page_id = str(page.get("page_id", "unknown-page"))
        page_kind = str(page.get("page_kind", ""))
        page_family = str(page.get("page_family", ""))
        if page_family == "source-manifest":
            continue
        page_coverage = coverage_count(page)
        if page_kind == "concept" and "Procedure" in sections(str(page.get("page_body", ""))):
            findings.append(
                (
                    1000 - page_coverage,
                    finding(
                        "page-projection",
                        "concept-rendered-as-procedure",
                        "page",
                        page_id,
                        (
                            f"{page_id}: concept page rendered a Procedure section; "
                            f"family={page_family}; coverage={page_coverage}."
                        ),
                    ),
                )
            )
        if page_coverage >= extreme_threshold(coverage_counts):
            findings.append(
                (
                    -page_coverage,
                    finding(
                        "page-projection",
                        "extreme-projection-coverage",
                        "page",
                        page_id,
                        (
                            f"{page_id}: extreme projection size with {page_coverage} "
                            "coverage records."
                        ),
                    ),
                )
            )
    return group(
        "projection-diagnostics",
        ("page-projection-artifact",),
        tuple(metrics),
        tuple(finding for _, finding in sorted(findings, key=lambda item: item[0])[:8]),
    )


def assertion_quality_diagnostics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    graph = artifact(inputs, "assertion-graph-artifact")
    assertions = items(inputs, "assertion-graph-artifact", "assertions")
    spans = {
        str(span.get("id")): span
        for span in items(inputs, "assertion-graph-artifact", "evidence_spans")
        if dict_item(span)
    }
    weak = fragments = mid_sentence = 0
    findings: list[IngestionTraceFinding] = []
    for assertion in assertions:
        if not dict_item(assertion):
            continue
        assertion_id = str(assertion.get("id", "unknown-assertion"))
        subject = str(assertion.get("subject", "")).strip()
        span_text = first_span_text(assertion, spans)
        reasons: list[str] = []
        if weak_subject(subject):
            weak += 1
            reasons.append(f"weak subject {subject!r}")
        if continuation_text(subject):
            fragments += 1
            reasons.append(f"fragment-like subject {subject!r}")
        if continuation_text(span_text):
            mid_sentence += 1
            reasons.append("evidence span starts like sentence continuation")
        if reasons:
            findings.append(
                finding(
                    "assertion-graph",
                    "weak-assertion-attribution",
                    "assertion",
                    assertion_id,
                    f"{assertion_id}: {', '.join(reasons)}.",
                )
            )
    metrics = (
        metric("assertion-quality", "accepted-assertion-count", list_len(graph, "assertions")),
        metric("assertion-quality", "weak-subject-count", weak),
        metric("assertion-quality", "fragment-subject-count", fragments),
        metric("assertion-quality", "mid-sentence-evidence-count", mid_sentence),
    )
    return group(
        "assertion-quality-diagnostics",
        ("assertion-graph-artifact",),
        metrics,
        top_findings(findings),
    )


def source_boundary_diagnostics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    units = [
        item
        for item in items(inputs, "assertion-graph-source-artifact", "source_units")
        if dict_item(item)
    ]
    units.sort(key=lambda item: int_value(item.get("source_order")))
    by_order = {int_value(unit.get("source_order")): unit for unit in units}
    parent_changes = continuation_pairs = heading_interruptions = 0
    findings: list[IngestionTraceFinding] = []
    for unit in units:
        order = int_value(unit.get("source_order"))
        prev = by_order.get(order - 1)
        next_unit = by_order.get(order + 1)
        if (
            kind(unit) == "heading"
            and prev
            and next_unit
            and unterminated(prev)
            and starts_continuation(next_unit)
        ):
            heading_interruptions += 1
            findings.append(boundary_finding("heading-in-continuation", unit))
        if next_unit and unterminated(unit) and starts_continuation(next_unit):
            continuation_pairs += 1
            if unit.get("parent_id") != next_unit.get("parent_id"):
                parent_changes += 1
                findings.append(
                    boundary_finding("parent-change-across-continuation", next_unit)
                )
    metrics = (
        metric("source-boundary", "source-unit-count", len(units)),
        metric("source-boundary", "continuation-pair-count", continuation_pairs),
        metric("source-boundary", "parent-change-continuation-count", parent_changes),
        metric("source-boundary", "heading-interruption-count", heading_interruptions),
    )
    return group(
        "source-boundary-diagnostics",
        ("assertion-graph-source-artifact",),
        metrics,
        top_findings(findings),
    )


def topic_aggregation_diagnostics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    topics = items(inputs, "topic-state-artifact", "topic_states")
    pages = {
        str(page.get("topic_state_id")): page
        for page in items(inputs, "page-projection-artifact", "page_projections")
        if dict_item(page)
    }
    topic_sizes: list[int] = []
    oversized = broad_topics = 0
    findings: list[tuple[int, IngestionTraceFinding]] = []
    for topic in topics:
        if not dict_item(topic):
            continue
        topic_id = str(topic.get("id", "unknown-topic"))
        page = pages.get(topic_id, {})
        family = str(nested(topic, "projection_policy", "page_family") or "")
        if family == "source-manifest":
            continue
        assertions = list_len(topic, "accepted_assertion_ids")
        atoms = list_len(topic, "accepted_technical_atom_ids")
        page_coverage = coverage_count(page)
        topic_sizes.append(assertions)
        broad_topics += int(family == "broad-topic")
        if assertions >= OVERSIZED_ASSERTION_MIN or page_coverage >= EXTREME_COVERAGE_MIN:
            oversized += 1
            page_id = str(page.get("page_id", topic_id)) if dict_item(page) else topic_id
            findings.append(
                (
                    -max(assertions, page_coverage),
                    finding(
                        "topic-state",
                        "oversized-topic-closure",
                        "topic-state",
                        topic_id,
                        (
                            f"{page_id}: oversized topic closure; assertions={assertions}; "
                            f"atoms={atoms}; coverage={page_coverage}; "
                            f"family={family or 'unknown'}."
                        ),
                    ),
                )
            )
    metrics = (
        metric("topic-aggregation", "topic-state-count", len(topics)),
        metric("topic-aggregation", "broad-topic-count", broad_topics),
        metric("topic-aggregation", "oversized-topic-count", oversized),
        metric("topic-aggregation", "max-topic-assertions", max(topic_sizes, default=0)),
        metric("topic-aggregation", "median-topic-assertions", median_value(topic_sizes)),
    )
    return group(
        "topic-aggregation-diagnostics",
        ("topic-state-artifact", "page-projection-artifact"),
        metrics,
        top_findings([finding for _, finding in sorted(findings, key=lambda item: item[0])]),
    )


def gate_effectiveness_diagnostics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    rejected = list_len(artifact(inputs, "projection-lint-run-artifact"), "rejected_page_ids")
    rejected += list_len(artifact(inputs, "publish-run-artifact"), "rejected_page_ids")
    signals = _diagnostic_signal_count(inputs)
    findings: tuple[IngestionTraceFinding, ...] = ()
    if rejected == 0 and signals > 0:
        findings = (
            finding(
                "lint-run",
                "accepted-output-with-diagnostics",
                "projection-lint-run",
                inputs.source_locator,
                (
                    f"lint/publish rejected 0 pages while {signals} diagnostic "
                    "signal(s) indicate suspicious output."
                ),
            ),
        )
    metrics = (
        metric("gate-effectiveness", "diagnostic-signal-count", signals),
        metric("gate-effectiveness", "rejected-page-count", rejected),
    )
    return group(
        "gate-effectiveness-diagnostics",
        ("projection-lint-run-artifact", "publish-run-artifact"),
        metrics,
        findings,
    )


def _diagnostic_signal_count(inputs: IngestionTraceInput) -> int:
    return (
        len(projection_diagnostics(inputs).findings)
        + len(assertion_quality_diagnostics(inputs).findings)
        + len(source_boundary_diagnostics(inputs).findings)
        + len(topic_aggregation_diagnostics(inputs).findings)
    )
