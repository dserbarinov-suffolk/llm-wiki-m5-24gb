"""Source-neutral ingestion trace metric providers."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass

from llmwiki.domain.graph import GraphStatus

from .ingestion_trace_records import IngestionMetric, IngestionMetricGroup


@dataclass(frozen=True)
class IngestionTraceInput:
    source_locator: str
    source_hash: str
    artifacts: Mapping[str, Mapping[str, object]]
    graph_status: GraphStatus | None = None


IngestionMetricProvider = Callable[[IngestionTraceInput], IngestionMetricGroup]


def default_metric_providers() -> tuple[IngestionMetricProvider, ...]:
    from .ingestion_trace_association import association_graph_metric_provider
    from .ingestion_trace_diagnostics import diagnostic_metric_providers
    from .ingestion_trace_page_quality import page_quality_metric_provider

    return (
        _extraction_metrics,
        _ledger_metrics,
        association_graph_metric_provider,
        _topic_state_metrics,
        _page_projection_metrics,
        _staging_metrics,
        _provenance_metrics,
        _graph_metrics,
        *diagnostic_metric_providers(),
        page_quality_metric_provider,
    )


def _extraction_metrics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    data = inputs.artifacts.get("extraction-result-artifact", {})
    return _group(
        "extraction-counts",
        ("extraction-result-artifact",),
        (
            _metric("extraction", "accepted-entry-count", _len(data, "accepted_entry_ids")),
            _metric("extraction", "needs-review-entry-count", _len(data, "needs_review_entry_ids")),
            _metric("extraction", "technical-atom-count", _len(data, "technical_atom_ids")),
            _metric(
                "extraction",
                "rejected-candidate-count",
                _int(data.get("rejected_candidate_count")),
            ),
        ),
    )


def _ledger_metrics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    ledger = inputs.artifacts.get("claim-ledger-artifact", {}).get("ledger", {})
    ledger = ledger if isinstance(ledger, dict) else {}
    return _group(
        "ledger-counts",
        ("claim-ledger-artifact",),
        (
            _metric("ledger", "ledger-entry-count", _len(ledger, "entries")),
            _metric("ledger", "source-statement-count", _len(ledger, "source_statements")),
            _metric("ledger", "technical-atom-count", _len(ledger, "technical_atoms")),
            _metric("ledger", "needs-review-count", _review_count(ledger)),
        ),
    )


def _topic_state_metrics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    return _group(
        "topic-state-counts",
        ("topic-state-artifact",),
        topic_state_metrics(inputs.artifacts),
    )


def _page_projection_metrics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    return _group(
        "page-projection-counts",
        ("page-projection-artifact",),
        page_projection_metrics(inputs.artifacts),
    )


def _staging_metrics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    return _group(
        "staging-counts",
        ("projection-lint-run-artifact", "publish-run-artifact"),
        (*lint_metrics(inputs.artifacts), *publish_metrics(inputs.artifacts)),
    )


def _provenance_metrics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    data = inputs.artifacts.get("provenance-audit-report", {})
    return _group(
        "provenance-counts",
        ("provenance-audit-report",),
        (
            _metric("provenance", "finding-count", _int(data.get("finding_count"))),
            _metric(
                "provenance",
                "non-manifest-finding-count",
                _int(data.get("non_manifest_finding_count")),
            ),
            _metric("provenance", "page-count", _int(data.get("page_count"))),
        ),
    )


def _graph_metrics(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    data = inputs.artifacts.get("graph-export", {})
    return _group(
        "graph-counts",
        ("graph-export",),
        (
            _metric("graph", "node-count", _int(data.get("node_count"))),
            _metric("graph", "edge-count", _int(data.get("edge_count"))),
            _metric("graph", "unresolved-edge-count", _int(data.get("unresolved_edge_count"))),
        ),
    )


def topic_state_metrics(
    artifacts: Mapping[str, Mapping[str, object]],
) -> tuple[IngestionMetric, ...]:
    data = artifacts.get("topic-state-artifact", {})
    return (
        _metric("topic-state", "topic-state-count", _len(data, "topic_states")),
        _metric("topic-state", "topic-dependency-count", _len(data, "topic_dependencies")),
        _metric("topic-state", "topic-gap-count", _len(data, "topic_gaps")),
    )


def page_projection_metrics(
    artifacts: Mapping[str, Mapping[str, object]],
) -> tuple[IngestionMetric, ...]:
    data = artifacts.get("page-projection-artifact", {})
    return (_metric("page-projection", "page-projection-count", _len(data, "page_projections")),)


def lint_metrics(artifacts: Mapping[str, Mapping[str, object]]) -> tuple[IngestionMetric, ...]:
    data = artifacts.get("projection-lint-run-artifact", {})
    return (
        _metric("lint", "accepted-page-count", _len(data, "accepted_page_ids")),
        _metric("lint", "rejected-page-count", _len(data, "rejected_page_ids")),
        _metric("lint", "finding-count", _len(data, "findings")),
    )


def publish_metrics(artifacts: Mapping[str, Mapping[str, object]]) -> tuple[IngestionMetric, ...]:
    data = artifacts.get("publish-run-artifact", {})
    return (
        _metric("publish", "accepted-page-count", _len(data, "accepted_page_ids")),
        _metric("publish", "rejected-page-count", _len(data, "rejected_page_ids")),
    )


def _group(
    provider_id: str, kinds: tuple[str, ...], metrics: tuple[IngestionMetric, ...]
) -> IngestionMetricGroup:
    return IngestionMetricGroup(
        provider_id=provider_id,
        metric_group_id=f"metric-group-{provider_id}",
        source_artifact_kinds=kinds,
        metrics=metrics,
    )


def _metric(provider_id: str, kind: str, value: int | float | str) -> IngestionMetric:
    return IngestionMetric(
        metric_id=f"metric-{provider_id}-{kind}",
        metric_kind=kind,
        value=value,
        unit="count" if isinstance(value, int | float) else "value",
        subject_kind=provider_id,
        subject_id=kind,
    )


def _len(data: Mapping[str, object], key: str) -> int:
    value = data.get(key)
    return len(value) if isinstance(value, list | tuple) else 0


def _int(value: object) -> int:
    return value if isinstance(value, int) else 0


def _review_count(ledger: Mapping[str, object]) -> int:
    entries = ledger.get("entries")
    if not isinstance(entries, list):
        return 0
    return sum(1 for entry in entries if isinstance(entry, dict) and entry.get("review_required"))
