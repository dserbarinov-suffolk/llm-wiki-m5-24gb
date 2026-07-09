"""Package accepted assertion graph records as a portable artifact."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from llmwiki.application.assertion_graph_mapping import (
    accepted_assertions,
    accepted_technical_atoms,
    assertion_activity_id,
    assertion_source_span_ids,
    build_source_index,
    technical_atom_span_ids,
)
from llmwiki.application.assertion_graph_mining import (
    mine_argument_edges,
    mine_relationships,
    mining_activity_id,
    review_mined_records,
)
from llmwiki.application.source_artifacts import CanonicalSourceArtifact
from llmwiki.domain.assertion_graph import (
    ArgumentEdge,
    Assertion,
    EvidenceSpan,
    ProposedChange,
    ProvenanceActivity,
    ProvenanceActivityKind,
    Relationship,
    SourceUnit,
    TechnicalAtom,
)
from llmwiki.domain.ledger.canonical import artifact_fingerprint, canonical_json
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.vocab import ARTIFACT_FORMAT


class AssertionGraphArtifact(BaseModel):
    """Portable accepted assertion graph for one source ingest."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    assertion_graph_artifact_id: str
    assertion_graph_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    source_artifact_id: str
    claim_ledger_id: str
    provenance_activities: tuple[ProvenanceActivity, ...]
    source_units: tuple[SourceUnit, ...]
    evidence_spans: tuple[EvidenceSpan, ...]
    technical_atoms: tuple[TechnicalAtom, ...]
    assertions: tuple[Assertion, ...]
    relationships: tuple[Relationship, ...]
    argument_edges: tuple[ArgumentEdge, ...]
    proposed_changes: tuple[ProposedChange, ...]


def build_assertion_graph_artifact(
    *, source_artifact: CanonicalSourceArtifact, ledger: ClaimLedger
) -> AssertionGraphArtifact:
    index = build_source_index(source_artifact, ledger)
    assertions = accepted_assertions(ledger, index)
    technical_atoms = accepted_technical_atoms(ledger, index)
    assertion_activity = _activity(
        "assertion-graph-build",
        assertion_activity_id(ledger),
        ProvenanceActivityKind.ASSERTION_PROPOSAL,
        source_artifact,
        _record_ids(assertions, technical_atoms),
    )
    relationships = mine_relationships(assertions, technical_atoms, index, source_artifact)
    argument_edges = mine_argument_edges(assertions, index, source_artifact)
    mining_activity = _activity(
        "assertion-graph-relationship-mining",
        mining_activity_id(source_artifact),
        ProvenanceActivityKind.RELATIONSHIP_MINING,
        source_artifact,
        _record_ids(relationships, argument_edges),
    )
    proposed_changes, review_activities = review_mined_records(
        source_artifact.source_locator, (*relationships, *argument_edges), assertions
    )
    used_span_ids = _used_span_ids(assertions, technical_atoms, argument_edges)
    used_unit_ids = _used_unit_ids(source_artifact, used_span_ids)
    draft = AssertionGraphArtifact(
        assertion_graph_artifact_id="pending",
        assertion_graph_fingerprint="",
        artifact_format=ARTIFACT_FORMAT,
        source_locator=source_artifact.source_locator,
        source_hash=source_artifact.source_hash,
        source_artifact_id=source_artifact.source_artifact_id,
        claim_ledger_id=ledger.claim_ledger_id,
        provenance_activities=(
            *source_artifact.provenance_activities,
            assertion_activity,
            mining_activity,
            *review_activities,
        ),
        source_units=tuple(
            unit for unit in source_artifact.source_units if unit.id in used_unit_ids
        ),
        evidence_spans=tuple(
            span for span in source_artifact.evidence_spans if span.id in used_span_ids
        ),
        technical_atoms=technical_atoms,
        assertions=assertions,
        relationships=relationships,
        argument_edges=argument_edges,
        proposed_changes=proposed_changes,
    )
    _validate_graph_references(draft)
    fingerprint = artifact_fingerprint(
        draft.model_dump(mode="json"),
        exclude=("assertion_graph_artifact_id", "assertion_graph_fingerprint"),
    )
    return draft.model_copy(
        update={
            "assertion_graph_artifact_id": f"assertion-graph-{fingerprint}",
            "assertion_graph_fingerprint": fingerprint,
        }
    )


def assertion_graph_artifact_to_json(artifact: AssertionGraphArtifact) -> str:
    return canonical_json(artifact, indent=2)


def _used_span_ids(
    assertions: tuple[Assertion, ...],
    atoms: tuple[TechnicalAtom, ...],
    argument_edges: tuple[ArgumentEdge, ...],
) -> frozenset[str]:
    edge_spans = frozenset(span_id for edge in argument_edges for span_id in edge.evidence_span_ids)
    return assertion_source_span_ids(assertions) | technical_atom_span_ids(atoms) | edge_spans


def _used_unit_ids(
    source_artifact: CanonicalSourceArtifact, span_ids: frozenset[str]
) -> frozenset[str]:
    direct_ids = frozenset(
        unit_id
        for span in source_artifact.evidence_spans
        if span.id in span_ids
        for unit_id in span.source_unit_ids
    )
    unit_by_id = {unit.id: unit for unit in source_artifact.source_units}
    with_ancestors = set(direct_ids)
    for unit_id in direct_ids:
        unit = unit_by_id.get(unit_id)
        parent_id = unit.parent_id if unit is not None else None
        while parent_id is not None and parent_id in unit_by_id:
            with_ancestors.add(parent_id)
            parent_id = unit_by_id[parent_id].parent_id
    return frozenset(with_ancestors)


def _validate_graph_references(artifact: AssertionGraphArtifact) -> None:
    assertion_ids = {assertion.id for assertion in artifact.assertions}
    atom_ids = {atom.id for atom in artifact.technical_atoms}
    span_ids = {span.id for span in artifact.evidence_spans}
    unit_ids = {unit.id for unit in artifact.source_units}
    activity_ids = {activity.id for activity in artifact.provenance_activities}
    for assertion in artifact.assertions:
        _require_all(assertion.source_unit_ids, unit_ids, "assertion source unit")
        _require_all(assertion.evidence_span_ids, span_ids, "assertion evidence span")
        _require_all(assertion.provenance_activity_ids, activity_ids, "assertion provenance")
    for atom in artifact.technical_atoms:
        _require_all(atom.evidence_span_ids, span_ids, "technical atom evidence span")
        _require_all(atom.provenance_activity_ids, activity_ids, "technical atom provenance")
    for relationship in artifact.relationships:
        if relationship.subject_id not in assertion_ids | atom_ids:
            raise ValueError(f"relationship subject missing: {relationship.subject_id}")
        if relationship.object_id not in assertion_ids | atom_ids:
            raise ValueError(f"relationship object missing: {relationship.object_id}")
        _require_all(relationship.assertion_ids, assertion_ids, "relationship assertion")
        _require_all(relationship.provenance_activity_ids, activity_ids, "relationship provenance")
    for edge in artifact.argument_edges:
        _require_all(
            (edge.from_assertion_id, edge.to_assertion_id), assertion_ids, "edge assertion"
        )
        _require_all(edge.evidence_span_ids, span_ids, "edge evidence span")
        _require_all((edge.provenance_activity_id,), activity_ids, "edge provenance")


def _require_all(values: tuple[str, ...], valid: set[str], label: str) -> None:
    missing = tuple(value for value in values if value not in valid)
    if missing:
        raise ValueError(f"{label} reference missing: {missing[0]}")


def _activity(
    purpose: str,
    activity_id: str,
    kind: ProvenanceActivityKind,
    source_artifact: CanonicalSourceArtifact,
    output_ids: tuple[str, ...],
) -> ProvenanceActivity:
    return ProvenanceActivity(
        id=activity_id,
        activity_kind=kind,
        actor=f"llmwiki-{purpose}",
        input_record_ids=(),
        output_record_ids=output_ids,
        source_locator=source_artifact.source_locator,
    )


def _record_ids(
    first: tuple[Assertion, ...] | tuple[Relationship, ...],
    second: tuple[TechnicalAtom, ...] | tuple[ArgumentEdge, ...],
) -> tuple[str, ...]:
    return tuple(record.id for record in first) + tuple(record.id for record in second)
