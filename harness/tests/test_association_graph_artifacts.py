"""AssociationGraph shadow artifact tests."""

from __future__ import annotations

import json

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.association_graph_artifacts import (
    association_graph_artifact_to_json,
    build_association_graph_artifact,
)
from llmwiki.application.ingestion_trace_association import association_graph_metrics
from llmwiki.domain.assertion_graph import (
    ArgumentEdge,
    Assertion,
    AssertionKind,
    AssertionStatus,
    EvidenceSpan,
    ParseStatus,
    ProvenanceActivity,
    ProvenanceActivityKind,
    Relationship,
    RelationshipKind,
    SourceUnit,
    SourceUnitKind,
    TechnicalAtom,
    TechnicalAtomKind,
)

SOURCE_HASH = "a" * 64


def test_association_graph_clusters_records_by_strong_evidence_edges() -> None:
    graph = _assertion_graph()

    artifact = build_association_graph_artifact(graph)

    assert artifact.association_graph_artifact_id.startswith("association-graph-")
    assert artifact.graph.nodes
    assert artifact.graph.edges
    assert artifact.graph.clusters
    assert any(
        cluster.dominant_shape == "catalog_record"
        and "ast_character_table" in cluster.assertion_ids
        and "tat_character_table" in cluster.technical_atom_ids
        for cluster in artifact.graph.clusters
    )
    assert any(edge.edge_kind == "assertion_uses_atom" for edge in artifact.graph.edges)


def test_association_graph_metrics_report_cluster_health() -> None:
    artifact = build_association_graph_artifact(_assertion_graph())
    payload = json.loads(association_graph_artifact_to_json(artifact))

    metrics = association_graph_metrics(
        {
            "association-graph-artifact": payload,
            "assertion-graph-artifact": {
                "assertions": [{"id": "ast_character_table"}, {"id": "ast_character_step"}]
            },
        }
    )

    by_kind = {metric.metric_kind: metric.value for metric in metrics}
    assert by_kind["association-node-count"] > 0
    assert by_kind["association-edge-count"] > 0
    assert by_kind["association-cluster-count"] > 0
    assert by_kind["unassigned-assertion-count"] == 0


def _assertion_graph() -> AssertionGraphArtifact:
    activity = ProvenanceActivity(
        id="prv_test",
        activity_kind=ProvenanceActivityKind.ASSERTION_PROPOSAL,
        actor="test",
        source_locator="source.pdf",
    )
    units = (
        SourceUnit(
            id="su_heading",
            source_locator="source.pdf",
            source_hash=SOURCE_HASH,
            source_order=1,
            kind=SourceUnitKind.HEADING,
            text="Character Creation",
        ),
        SourceUnit(
            id="su_table",
            source_locator="source.pdf",
            source_hash=SOURCE_HASH,
            source_order=2,
            kind=SourceUnitKind.TABLE,
            parent_id="su_heading",
            text="Character creation table",
        ),
    )
    spans = (
        EvidenceSpan(
            id="evs_table",
            source_locator="source.pdf",
            source_hash=SOURCE_HASH,
            source_unit_ids=("su_table",),
            exact_text="Character creation table",
            text_fingerprint="fp-table",
            confidence=1.0,
            provenance_activity_ids=("prv_test",),
        ),
    )
    atom = TechnicalAtom(
        id="tat_character_table",
        atom_kind=TechnicalAtomKind.TABLE,
        evidence_span_ids=("evs_table",),
        exact_payload="| Step | Value |\n| Race | Human |",
        parse_status=ParseStatus.PARSED,
        source_order=2,
        provenance_activity_ids=("prv_test",),
    )
    assertions = (
        Assertion(
            id="ast_character_table",
            kind=AssertionKind.SOURCE_CLAIM,
            subject="Character creation",
            predicate="uses",
            object_entity_id="tat_character_table",
            status=AssertionStatus.ACCEPTED,
            confidence=0.9,
            source_unit_ids=("su_table",),
            evidence_span_ids=("evs_table",),
            technical_atom_ids=("tat_character_table",),
            provenance_activity_ids=("prv_test",),
        ),
        Assertion(
            id="ast_character_step",
            kind=AssertionKind.SOURCE_CLAIM,
            subject="Character creation",
            predicate="includes",
            object_value="choosing a race",
            status=AssertionStatus.ACCEPTED,
            confidence=0.9,
            source_unit_ids=("su_table",),
            evidence_span_ids=("evs_table",),
            provenance_activity_ids=("prv_test",),
        ),
    )
    return AssertionGraphArtifact(
        assertion_graph_artifact_id="assertion-graph-test",
        assertion_graph_fingerprint="fp",
        artifact_format="llmwiki-ledger-v1",
        source_locator="source.pdf",
        source_hash=SOURCE_HASH,
        source_artifact_id="source-artifact-test",
        claim_ledger_id="claim-ledger-test",
        provenance_activities=(activity,),
        source_units=units,
        evidence_spans=spans,
        technical_atoms=(atom,),
        assertions=assertions,
        relationships=(
            Relationship(
                id="rel_table",
                subject_id="ast_character_table",
                predicate=RelationshipKind.CONTEXTUALIZES,
                object_id="tat_character_table",
                assertion_ids=("ast_character_table",),
                confidence=0.8,
                provenance_activity_ids=("prv_test",),
            ),
        ),
        argument_edges=(
            ArgumentEdge(
                id="arg_step",
                from_assertion_id="ast_character_table",
                to_assertion_id="ast_character_step",
                relation=RelationshipKind.ELABORATES,
                rationale="The table assertion elaborates the step assertion.",
                confidence=0.6,
                provenance_activity_id="prv_test",
            ),
        ),
        proposed_changes=(),
    )
