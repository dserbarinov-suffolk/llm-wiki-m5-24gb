from __future__ import annotations

from assertion_graph_fixtures import (
    accepted_assertion,
    evidence_span,
    provenance_activity,
    source_unit,
    technical_atom,
)

from llmwiki.domain.assertion_graph import (
    ArgumentEdge,
    DependencyStatus,
    GapKind,
    PageCoverageRecord,
    PageProjection,
    ProjectionPolicy,
    Relationship,
    RelationshipKind,
    TopicDependency,
    TopicGap,
    TopicKind,
    TopicState,
)


def test_valid_assertion_graph_records_can_be_constructed() -> None:
    activity = provenance_activity()
    unit = source_unit()
    span = evidence_span()
    atom = technical_atom()
    assertion = accepted_assertion()
    relationship = Relationship(
        id="rel_claim_to_atom",
        subject_id=assertion.id,
        predicate=RelationshipKind.SUPPORTS,
        object_id=atom.id,
        assertion_ids=(assertion.id,),
        confidence=0.8,
        provenance_activity_ids=(activity.id,),
    )
    argument_edge = ArgumentEdge(
        id="arg_supports_1",
        from_assertion_id=assertion.id,
        to_assertion_id="ast_claim_2",
        relation=RelationshipKind.SUPPORTS,
        rationale="The first assertion supports the second.",
        evidence_span_ids=(span.id,),
        confidence=0.75,
        provenance_activity_id=activity.id,
    )
    dependency = TopicDependency(
        id="tdp_creation_tables",
        from_topic_state_id="tps_character_creation",
        to_topic_state_id="tps_creation_tables",
        relation=RelationshipKind.DEPENDS_ON,
        required_status=DependencyStatus.REQUIRED,
        rationale_assertion_ids=(assertion.id,),
        source_order=0,
    )
    gap = TopicGap(
        id="tgp_missing_example",
        gap_kind=GapKind.MISSING_DEPENDENCY,
        description="The example page is not yet present.",
    )
    topic_state = TopicState(
        id="tps_character_creation",
        topic_key="character-creation",
        label="Character Creation",
        topic_kind=TopicKind.PROCEDURE,
        accepted_assertion_ids=(assertion.id,),
        accepted_technical_atom_ids=(atom.id,),
        relationship_ids=(relationship.id,),
        argument_edge_ids=(argument_edge.id,),
        source_unit_ids=(unit.id,),
        required_dependency_ids=(dependency.id,),
        unresolved_gap_ids=(gap.id,),
        projection_policy=ProjectionPolicy(page_kind="procedure", page_family="rpg"),
    )
    page = PageProjection(
        id="pgp_character_creation",
        topic_state_id=topic_state.id,
        page_id="character-creation",
        page_kind="procedure",
        page_family="rpg",
        page_body="# Character Creation",
        coverage_records=(
            PageCoverageRecord(
                coverage_id="coverage-1",
                page_section="Overview",
                support_record_id=assertion.id,
                rendered_text="Character creation uses the table.",
            ),
        ),
    )

    assert page.topic_state_id == topic_state.id
    assert atom.evidence_span_ids == (span.id,)
    assert relationship.assertion_ids == (assertion.id,)
