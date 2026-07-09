import json

import pytest
from pydantic import ValidationError

from llmwiki.application.ingestion_trace_builder import build_ingestion_trace
from llmwiki.application.ingestion_trace_metrics import default_metric_providers
from llmwiki.application.ingestion_trace_records import (
    IngestionMetric,
    IngestionMetricGroup,
    IngestionTraceCheck,
    IngestionTraceFinding,
    ingestion_trace_artifact_from_json,
    ingestion_trace_artifact_to_json,
)
from llmwiki.domain.graph import GraphStatus
from llmwiki.domain.ledger.artifacts import PortableArtifactMember
from llmwiki.runtime.ingestion_trace_inspect import render_trace_stage, render_trace_summary

_HASH = "a" * 64


def test_trace_artifact_round_trips_with_stable_fingerprint() -> None:
    trace = _trace(_artifact_files())

    parsed = ingestion_trace_artifact_from_json(ingestion_trace_artifact_to_json(trace))

    assert parsed == trace
    assert (
        trace.ingestion_trace_artifact_id
        == f"ingestion-trace-{trace.ingestion_trace_fingerprint}"
    )
    assert [stage.stage_id for stage in trace.stages][:3] == [
        "source-plan",
        "source-extraction",
        "canonical-source",
    ]


def test_invalid_check_status_fails_fast() -> None:
    with pytest.raises(ValidationError):
        IngestionTraceCheck(
            check_id="bad",
            status="ignored",
            subject_kind="artifact-kind",
            subject_id="source-plan-artifact",
            message="bad status",
        )


def test_invalid_finding_severity_fails_fast() -> None:
    with pytest.raises(ValidationError):
        IngestionTraceFinding(
            finding_id="bad",
            severity="minor",
            stage_id="source-plan",
            reason="bad-severity",
            subject_kind="artifact-kind",
            subject_id="source-plan-artifact",
            message="bad severity",
        )


def test_missing_stage_artifacts_create_failed_checks_and_findings() -> None:
    trace = _trace({"source-plan.json": "{}"})

    source_extraction = _stage(trace, "source-extraction")

    assert source_extraction.postcondition_checks[0].status == "failed"
    assert source_extraction.finding_ids
    assert any(finding.stage_id == "source-extraction" for finding in trace.findings)


def test_metric_provider_can_be_added_and_removed_without_schema_change() -> None:
    def synthetic_provider(_inputs: object) -> IngestionMetricGroup:
        return IngestionMetricGroup(
            provider_id="synthetic-counts",
            metric_group_id="metric-group-synthetic-counts",
            source_artifact_kinds=("topic-state-artifact",),
            metrics=(
                IngestionMetric(
                    metric_id="metric-synthetic-count",
                    metric_kind="synthetic-count",
                    value=7,
                    unit="count",
                    subject_kind="synthetic",
                    subject_id="synthetic-count",
                ),
            ),
        )

    with_provider = _trace(_artifact_files(), providers=(synthetic_provider,))
    without_provider = _trace(_artifact_files(), providers=())

    assert any(group.provider_id == "synthetic-counts" for group in with_provider.metric_groups)
    assert without_provider.metric_groups == ()
    assert ingestion_trace_artifact_from_json(ingestion_trace_artifact_to_json(without_provider))


def test_trace_builder_uses_artifacts_not_generated_wiki_markdown() -> None:
    artifact_files = _artifact_files()
    artifact_files["generated-page.md"] = "# Generated page should be ignored\n"

    trace = _trace(artifact_files)

    assert all(
        pointer.portable_artifact_kind != "generated-wiki-page"
        for pointer in trace.artifact_pointers
    )
    assert "generated-page.md" not in ingestion_trace_artifact_to_json(trace)


def test_diagnostics_surface_projection_assertion_and_boundary_issues() -> None:
    trace = _trace(_diagnostic_artifact_files(), providers=default_metric_providers())

    summary = render_trace_summary(trace)
    page_projection = render_trace_stage(trace, "page-projection")
    assertion_graph = render_trace_stage(trace, "assertion-graph")
    canonical_source = render_trace_stage(trace, "canonical-source")

    assert "Diagnostics:" in summary
    assert "concept page rendered a Procedure section" in summary
    assert summary.index("extreme projection size") < summary.index("weak subject 'They'")
    assert "extreme projection size" in page_projection
    assert "weak subject 'They'" in assertion_graph
    assert "heading appears inside a sentence continuation" in canonical_source


def test_zero_rejections_with_diagnostics_surfaces_gate_effectiveness_warning() -> None:
    trace = _trace(_diagnostic_artifact_files(), providers=default_metric_providers())

    lint = render_trace_stage(trace, "lint-run")

    assert "accepted-output-with-diagnostics" in lint
    assert "rejected 0 pages" in lint


def _trace(artifact_files: dict[str, str], providers: tuple = ()):
    return build_ingestion_trace(
        source_locator="src.pdf",
        source_hash=_HASH,
        run_id="run-1",
        artifact_files=artifact_files,
        artifact_members=(PortableArtifactMember("source-plan-artifact", "source-plan-1", "fp"),),
        graph_status=GraphStatus("current", 3, 2, 0, "current"),
        metric_providers=providers,
    )


def _stage(trace, stage_id: str):
    return next(stage for stage in trace.stages if stage.stage_id == stage_id)


def _artifact_files() -> dict[str, str]:
    payloads = {
        "source-plan.json": {"source_plan_id": "source-plan-1"},
        "extraction-result.json": {
            "accepted_entry_ids": ["entry-1"],
            "needs_review_entry_ids": [],
            "technical_atom_ids": ["atom-1"],
            "rejected_candidate_count": 0,
        },
        "assertion-graph-source-artifact.json": {"source_units": [{}]},
        "document-structure.json": {"document_structure": {}},
        "claim-ledger.json": {
            "ledger": {
                "entries": [{"review_required": False}],
                "source_statements": [{}],
                "technical_atoms": [{}],
                "source_family_assignment": "coding",
            }
        },
        "proposed-change-review.json": {"accepted_change_ids": []},
        "assertion-graph.json": {"assertions": [{}], "technical_atoms": [{}]},
        "topic-states.json": {
            "topic_states": [{}],
            "topic_dependencies": [],
            "topic_gaps": [{"id": "gap-1"}],
        },
        "page-projections.json": {"page_projections": [{}]},
        "staged-pages.json": {"pages": [{}]},
        "lint-run.json": {
            "status": "accepted",
            "upstream_write_decision": "write-authoritative-page",
            "accepted_page_ids": ["src"],
            "rejected_page_ids": [],
            "findings": [],
        },
        "publish-run.json": {
            "status": "published",
            "accepted_page_ids": ["src"],
            "rejected_page_ids": [],
        },
        "projection-coverage.json": {"projection_coverage": {}},
        "provenance-audit.json": {
            "finding_count": 0,
            "non_manifest_finding_count": 0,
            "page_count": 1,
        },
    }
    return {filename: json.dumps(payload) for filename, payload in payloads.items()}


def _diagnostic_artifact_files() -> dict[str, str]:
    files = _artifact_files()
    files.update(
        {
            "assertion-graph-source-artifact.json": json.dumps(
                {
                    "source_units": [
                        {
                            "id": "su_aaaaaaaa_00001",
                            "kind": "paragraph",
                            "text": "The record starts but does not finish",
                            "source_order": 1,
                            "page_span": [9, 9],
                            "parent_id": "su_aaaaaaaa_parent",
                        },
                        {
                            "id": "su_aaaaaaaa_00002",
                            "kind": "heading",
                            "text": "## Category",
                            "source_order": 2,
                            "page_span": [9, 9],
                            "parent_id": None,
                        },
                        {
                            "id": "su_aaaaaaaa_00003",
                            "kind": "paragraph",
                            "text": "and continues after the heading.",
                            "source_order": 3,
                            "page_span": [9, 9],
                            "parent_id": "su_aaaaaaaa_00002",
                        },
                    ]
                }
            ),
            "assertion-graph.json": json.dumps(
                {
                    "assertions": [
                        {
                            "id": "ast_weak",
                            "subject": "They",
                            "predicate": "are",
                            "object_value": "unclear without context",
                            "evidence_span_ids": ["evs_weak"],
                        },
                        {
                            "id": "ast_fragment",
                            "subject": "and therefore",
                            "predicate": "can",
                            "object_value": "continue",
                            "evidence_span_ids": ["evs_fragment"],
                        },
                    ],
                    "technical_atoms": [],
                    "evidence_spans": [
                        {
                            "id": "evs_weak",
                            "exact_text": "They are unclear without context.",
                        },
                        {
                            "id": "evs_fragment",
                            "exact_text": "and therefore can continue.",
                        },
                    ],
                }
            ),
            "topic-states.json": json.dumps(
                {
                    "topic_states": [
                        {
                            "id": "tps_big",
                            "accepted_assertion_ids": [f"ast_{index}" for index in range(130)],
                            "accepted_technical_atom_ids": [],
                            "projection_policy": {"page_family": "broad-topic"},
                        }
                    ],
                    "topic_dependencies": [],
                    "topic_gaps": [],
                }
            ),
            "page-projections.json": json.dumps(
                {
                    "page_projections": [
                        {
                            "page_id": "category",
                            "topic_state_id": "tps_big",
                            "page_kind": "concept",
                            "page_family": "broad-topic",
                            "page_body": "# Category\n\n## Procedure\n\n- They are unclear.",
                            "coverage_records": [
                                {"support_record_id": f"ast_{index}"} for index in range(130)
                            ],
                            "rendered_related_links": [],
                        }
                    ]
                }
            ),
            "lint-run.json": json.dumps(
                {
                    "status": "accepted",
                    "accepted_page_ids": ["category"],
                    "rejected_page_ids": [],
                    "findings": [],
                }
            ),
            "publish-run.json": json.dumps(
                {
                    "status": "published",
                    "accepted_page_ids": ["category"],
                    "rejected_page_ids": [],
                }
            ),
        }
    )
    return files
