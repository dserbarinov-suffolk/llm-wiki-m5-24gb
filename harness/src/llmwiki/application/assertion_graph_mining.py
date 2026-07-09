"""Mine and review assertion graph relationships from accepted records."""

from __future__ import annotations

from llmwiki.application.assertion_graph_mapping import (
    SourceIndex,
    graph_record_id,
    same_parent_or_unit,
    unit_for_span,
    unit_order,
)
from llmwiki.application.source_artifacts import CanonicalSourceArtifact
from llmwiki.domain.assertion_graph import (
    ArgumentEdge,
    Assertion,
    ProposedChange,
    ProvenanceActivity,
    ProvenanceActivityKind,
    RecordPayload,
    Relationship,
    RelationshipKind,
    ReviewStatus,
    TechnicalAtom,
)
from llmwiki.domain.ledger.canonical import canonical_json


def mine_relationships(
    assertions: tuple[Assertion, ...],
    atoms: tuple[TechnicalAtom, ...],
    index: SourceIndex,
    source_artifact: CanonicalSourceArtifact,
) -> tuple[Relationship, ...]:
    activity_id = mining_activity_id(source_artifact)
    relationships: list[Relationship] = []
    for atom in atoms:
        atom_unit = unit_for_span(atom.evidence_span_ids[0], index)
        candidates = [
            assertion
            for assertion in assertions
            if same_parent_or_unit(assertion.source_unit_ids[0], atom_unit.id, index)
        ]
        if candidates:
            assertion = min(
                candidates,
                key=lambda item: abs(
                    unit_order(item.source_unit_ids[0], index) - atom_unit.source_order
                ),
            )
            relationships.append(_relationship(assertion, atom, activity_id))
    return tuple(relationships)


def mine_argument_edges(
    assertions: tuple[Assertion, ...], index: SourceIndex, source_artifact: CanonicalSourceArtifact
) -> tuple[ArgumentEdge, ...]:
    activity_id = mining_activity_id(source_artifact)
    by_subject: dict[str, list[Assertion]] = {}
    for assertion in assertions:
        by_subject.setdefault(assertion.subject.casefold(), []).append(assertion)
    edges: list[ArgumentEdge] = []
    for group in by_subject.values():
        ordered = sorted(group, key=lambda item: unit_order(item.source_unit_ids[0], index))
        for first, second in zip(ordered, ordered[1:], strict=False):
            if same_parent_or_unit(first.source_unit_ids[0], second.source_unit_ids[0], index):
                edges.append(_argument_edge(first, second, activity_id))
    return tuple(edges)


def review_mined_records(
    source_locator: str,
    records: tuple[Relationship | ArgumentEdge, ...],
    assertions: tuple[Assertion, ...],
) -> tuple[tuple[ProposedChange, ...], tuple[ProvenanceActivity, ...]]:
    assertions_by_id = {assertion.id: assertion for assertion in assertions}
    changes: list[ProposedChange] = []
    activities: list[ProvenanceActivity] = []
    for record in records:
        change_id = graph_record_id("pcg", type(record).__name__, record.id)
        activity = ProvenanceActivity(
            id=graph_record_id("prv", change_id, "review"),
            activity_kind=ProvenanceActivityKind.PROPOSED_CHANGE_REVIEW,
            actor="llmwiki-assertion-graph-review",
            input_record_ids=(record.id,),
            output_record_ids=(change_id,),
            source_locator=source_locator,
        )
        activities.append(activity)
        changes.append(
            ProposedChange(
                id=change_id,
                review_status=ReviewStatus.APPROVED,
                proposed_record=_payload(record),
                accepted_record=_payload(record),
                source_locator=source_locator,
                source_unit_ids=_record_source_unit_ids(record, assertions_by_id),
                model_name="deterministic",
                prompt_id="assertion-graph-mining",
                provenance_activity_id=activity.id,
            )
        )
    return tuple(changes), tuple(activities)


def mining_activity_id(source_artifact: CanonicalSourceArtifact) -> str:
    return graph_record_id(
        "prv", source_artifact.source_hash, "assertion-graph-relationship-mining"
    )


def _relationship(assertion: Assertion, atom: TechnicalAtom, activity_id: str) -> Relationship:
    return Relationship(
        id=graph_record_id("rel", assertion.id, RelationshipKind.CONTEXTUALIZES.value, atom.id),
        subject_id=assertion.id,
        predicate=RelationshipKind.CONTEXTUALIZES,
        object_id=atom.id,
        assertion_ids=(assertion.id,),
        confidence=min(assertion.confidence, 0.75),
        provenance_activity_ids=(activity_id,),
    )


def _argument_edge(first: Assertion, second: Assertion, activity_id: str) -> ArgumentEdge:
    return ArgumentEdge(
        id=graph_record_id("arg", first.id, RelationshipKind.ELABORATES.value, second.id),
        from_assertion_id=first.id,
        to_assertion_id=second.id,
        relation=RelationshipKind.ELABORATES,
        rationale="Assertions share a subject and local source structure.",
        evidence_span_ids=tuple(
            dict.fromkeys((*first.evidence_span_ids, *second.evidence_span_ids))
        ),
        confidence=min(first.confidence, second.confidence, 0.7),
        provenance_activity_id=activity_id,
    )


def _record_source_unit_ids(
    record: Relationship | ArgumentEdge, assertions_by_id: dict[str, Assertion]
) -> tuple[str, ...]:
    if isinstance(record, Relationship):
        ids = tuple(
            unit_id
            for assertion_id in record.assertion_ids
            if assertion_id in assertions_by_id
            for unit_id in assertions_by_id[assertion_id].source_unit_ids
        )
        return tuple(dict.fromkeys(ids))
    ids = (
        *assertions_by_id[record.from_assertion_id].source_unit_ids,
        *assertions_by_id[record.to_assertion_id].source_unit_ids,
    )
    return tuple(dict.fromkeys(ids))


def _payload(record: Relationship | ArgumentEdge) -> RecordPayload:
    return RecordPayload(record_type=type(record).__name__, json_text=canonical_json(record))
