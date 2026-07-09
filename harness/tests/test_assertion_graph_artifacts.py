"""Assertion graph artifact projection from accepted ledger state."""

from __future__ import annotations

import json

from llmwiki.application.assertion_graph_artifacts import (
    assertion_graph_artifact_to_json,
    build_assertion_graph_artifact,
)
from llmwiki.application.source_artifacts import build_canonical_ledger_source
from llmwiki.domain.assertion_graph import RelationshipKind, ReviewStatus
from llmwiki.domain.ledger.builder import (
    SegmentInput,
    build_claim_ledger,
    default_schema_bundle,
)
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment

SOURCE_HASH = "a" * 64


def test_assertion_graph_artifact_maps_accepted_ledger_records() -> None:
    canonical_source, ledger = _source_and_ledger()

    artifact = build_assertion_graph_artifact(
        source_artifact=canonical_source.artifact, ledger=ledger
    )

    assert artifact.assertions
    assert artifact.technical_atoms
    assert artifact.relationships
    assert artifact.argument_edges
    assert all(assertion.status == "accepted" for assertion in artifact.assertions)
    assert all(assertion.evidence_span_ids for assertion in artifact.assertions)
    assert all(atom.evidence_span_ids for atom in artifact.technical_atoms)
    assert artifact.relationships[0].predicate == RelationshipKind.CONTEXTUALIZES
    assert artifact.relationships[0].assertion_ids[0] in {
        assertion.id for assertion in artifact.assertions
    }
    edge = artifact.argument_edges[0]
    assert edge.from_assertion_id != edge.to_assertion_id
    assert {change.review_status for change in artifact.proposed_changes} == {ReviewStatus.APPROVED}


def test_assertion_graph_artifact_json_is_portable() -> None:
    canonical_source, ledger = _source_and_ledger()
    artifact = build_assertion_graph_artifact(
        source_artifact=canonical_source.artifact, ledger=ledger
    )

    serialized = json.loads(assertion_graph_artifact_to_json(artifact))

    assert serialized["assertion_graph_artifact_id"].startswith("assertion-graph-")
    assert serialized["source_artifact_id"] == canonical_source.artifact.source_artifact_id
    assert serialized["claim_ledger_id"] == ledger.claim_ledger_id
    assert serialized["assertions"]
    assert serialized["relationships"]
    assert serialized["argument_edges"]


def _source_and_ledger():
    inputs = (
        _input(1, "heading", "# Arrays", ()),
        _input(
            2,
            "paragraph",
            "Arrays have indexes.",
            ("Arrays have indexes.",),
        ),
        _input(
            3,
            "paragraph",
            "Arrays have lengths.",
            ("Arrays have lengths.",),
        ),
        _input(4, "code-fence", "```go\nvalue := items[0]\n```", ()),
    )
    profiles = {
        item.segment.segment_id: profile_unit(
            extracted_unit_id=item.segment.segment_id,
            source_range_id=item.segment.source_range_id,
            text=item.segment.text,
            evidence_ids=item.segment.evidence_ids,
        )
        for item in inputs
    }
    canonical_source = build_canonical_ledger_source(
        source_locator="source.pdf",
        source_hash=SOURCE_HASH,
        segment_inputs=inputs,
        profiles=profiles,
    )
    result = build_claim_ledger(
        source_locator="source.pdf",
        source_hash=SOURCE_HASH,
        evidence_registry_hash="registry",
        segments=inputs,
        profiles=profiles,
        schema=default_schema_bundle(),
    )
    return canonical_source, result.ledger


def _input(order: int, kind: str, text: str, claims: tuple[str, ...]) -> SegmentInput:
    segment = SourceSegment(
        segment_id=f"segment-{order:05d}",
        source_range_id=f"source-range-test-{order:05d}",
        source_locator="source.pdf",
        source_hash=SOURCE_HASH,
        heading_path="Arrays",
        structure_node_id="",
        source_order=order,
        text=text,
        segment_kind=kind,
        evidence_ids=(f"ev-{order:05d}",),
    )
    return SegmentInput(
        segment,
        tuple(
            SegmentClaim(
                claim_id=f"claim-{order:05d}-{index:02d}",
                statement=claim,
                evidence_ids=segment.evidence_ids,
            )
            for index, claim in enumerate(claims)
        ),
    )
