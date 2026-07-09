"""AssociationGraph ingestion trace metrics."""

from __future__ import annotations

from collections.abc import Iterable, Mapping

from llmwiki.application.ingestion_trace_metrics import IngestionTraceInput
from llmwiki.application.ingestion_trace_records import (
    IngestionMetric,
    IngestionMetricGroup,
    IngestionTraceFinding,
)
from llmwiki.domain.ledger.canonical import short_digest


def association_graph_metric_provider(inputs: IngestionTraceInput) -> IngestionMetricGroup:
    metrics = association_graph_metrics(inputs.artifacts)
    return IngestionMetricGroup(
        provider_id="association-graph-counts",
        metric_group_id="metric-group-association-graph-counts",
        source_artifact_kinds=("association-graph-artifact",),
        metrics=metrics,
        findings=_split_findings(inputs.artifacts),
    )


def association_graph_metrics(
    artifacts: Mapping[str, Mapping[str, object]],
) -> tuple[IngestionMetric, ...]:
    graph = _graph(artifacts)
    nodes = _list(graph, "nodes")
    edges = _list(graph, "edges")
    clusters = _list(graph, "clusters")
    metrics = [
        _metric("association-node-count", len(nodes)),
        _metric("association-edge-count", len(edges)),
        _metric("association-cluster-count", len(clusters)),
        _metric("topic-split-candidate-count", len(_topic_split_candidates(artifacts))),
        _metric("median-cluster-size", _median(_cluster_sizes(clusters))),
        _metric("max-cluster-size", max(_cluster_sizes(clusters), default=0)),
        _metric("oversized-cluster-count", _flag_count(clusters, "oversized")),
        _metric("ambiguous-cluster-count", _ambiguous_count(clusters)),
        _metric("shape-contamination-count", sum(1 for item in clusters if _contaminated(item))),
        _metric("unassigned-assertion-count", _unassigned_assertions(artifacts, clusters)),
        _metric(
            "cluster-cohesion-median",
            _median(_float_field(cluster, "cohesion_score") for cluster in clusters),
        ),
        _metric(
            "cluster-separation-median",
            _median(_float_field(cluster, "separation_score") for cluster in clusters),
        ),
    ]
    metrics.extend(
        _metric(f"edge-kind-{kind}", _edge_kind_count(edges, kind)) for kind in _edge_kinds(edges)
    )
    return tuple(metrics)


def _graph(artifacts: Mapping[str, Mapping[str, object]]) -> Mapping[str, object]:
    data = artifacts.get("association-graph-artifact", {})
    graph = data.get("graph") if isinstance(data, dict) else {}
    return graph if isinstance(graph, dict) else {}


def _list(data: Mapping[str, object], key: str) -> list[object]:
    value = data.get(key)
    return value if isinstance(value, list) else []


def _tuple_field(data: object, key: str) -> tuple[object, ...]:
    if not isinstance(data, dict):
        return ()
    value = data.get(key)
    return tuple(value) if isinstance(value, list | tuple) else ()


def _cluster_sizes(clusters: list[object]) -> list[int]:
    return [len(_tuple_field(cluster, "member_node_ids")) for cluster in clusters]


def _flag_count(items: list[object], key: str) -> int:
    return sum(1 for item in items if isinstance(item, dict) and item.get(key))


def _ambiguous_count(clusters: list[object]) -> int:
    return sum(1 for cluster in clusters if _float_field(cluster, "separation_score") <= 0.45)


def _float_field(data: object, key: str) -> float:
    if not isinstance(data, dict):
        return 0.0
    value = data.get(key)
    return float(value) if isinstance(value, int | float) else 0.0


def _median(values: Iterable[int | float]) -> float:
    ordered = sorted(float(value) for value in values)
    if not ordered:
        return 0.0
    midpoint = len(ordered) // 2
    if len(ordered) % 2:
        return round(ordered[midpoint], 3)
    return round((ordered[midpoint - 1] + ordered[midpoint]) / 2, 3)


def _contaminated(cluster: object) -> bool:
    if not isinstance(cluster, dict):
        return False
    shape = str(cluster.get("dominant_shape", ""))
    assertions = len(_tuple_field(cluster, "assertion_ids"))
    atoms = len(_tuple_field(cluster, "technical_atom_ids"))
    return shape in {"mixed"} or (shape == "concept" and assertions > 0 and atoms > 0)


def _topic_split_candidates(artifacts: Mapping[str, Mapping[str, object]]) -> tuple[dict, ...]:
    record_cluster = _record_cluster_index(_list(_graph(artifacts), "clusters"))
    topics = _list(artifacts.get("topic-state-artifact", {}), "topic_states")
    candidates: list[dict] = []
    for topic in topics:
        if not isinstance(topic, dict):
            continue
        topic_id = str(topic.get("id", ""))
        if str(topic.get("topic_kind")) == "source_manifest":
            continue
        record_ids = (
            *_tuple_field(topic, "accepted_assertion_ids"),
            *_tuple_field(topic, "accepted_technical_atom_ids"),
        )
        cluster_ids = {record_cluster[item] for item in record_ids if item in record_cluster}
        if len(cluster_ids) > 1:
            candidates.append(
                {
                    "topic_id": topic_id,
                    "label": str(topic.get("label", topic_id)),
                    "record_count": len(record_ids),
                    "cluster_count": len(cluster_ids),
                }
            )
    return tuple(sorted(candidates, key=lambda item: (-item["cluster_count"], item["label"])))


def _record_cluster_index(clusters: list[object]) -> dict[object, str]:
    result: dict[object, str] = {}
    for cluster in clusters:
        if not isinstance(cluster, dict):
            continue
        cluster_id = str(cluster.get("id", ""))
        for record_id in (
            *_tuple_field(cluster, "assertion_ids"),
            *_tuple_field(cluster, "technical_atom_ids"),
        ):
            result[record_id] = cluster_id
    return result


def _split_findings(
    artifacts: Mapping[str, Mapping[str, object]],
) -> tuple[IngestionTraceFinding, ...]:
    findings = []
    for item in _topic_split_candidates(artifacts)[:8]:
        label = str(item["label"])
        findings.append(
            IngestionTraceFinding(
                finding_id=f"association-topic-split-{short_digest(label)}",
                severity="info",
                stage_id="association-graph",
                reason="topic-spans-many-association-clusters",
                subject_kind="topic-state",
                subject_id=str(item["topic_id"]),
                message=(
                    f"{label}: current topic has {item['record_count']} accepted records "
                    f"spread across {item['cluster_count']} association clusters."
                ),
            )
        )
    return tuple(findings)


def _unassigned_assertions(
    artifacts: Mapping[str, Mapping[str, object]], clusters: list[object]
) -> int:
    assertion_ids = {
        assertion.get("id")
        for assertion in _list(artifacts.get("assertion-graph-artifact", {}), "assertions")
        if isinstance(assertion, dict)
    }
    clustered = {
        assertion_id
        for cluster in clusters
        for assertion_id in _tuple_field(cluster, "assertion_ids")
    }
    return len(assertion_ids - clustered)


def _edge_kinds(edges: list[object]) -> tuple[str, ...]:
    return tuple(
        sorted(
            {
                str(edge.get("edge_kind"))
                for edge in edges
                if isinstance(edge, dict) and edge.get("edge_kind")
            }
        )
    )


def _edge_kind_count(edges: list[object], kind: str) -> int:
    return sum(1 for edge in edges if isinstance(edge, dict) and edge.get("edge_kind") == kind)


def _metric(kind: str, value: int | float | str) -> IngestionMetric:
    return IngestionMetric(
        metric_id=f"metric-association-graph-{kind}",
        metric_kind=kind,
        value=value,
        unit="count" if isinstance(value, int | float) else "value",
        subject_kind="association-graph",
        subject_id=kind,
    )
