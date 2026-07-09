from __future__ import annotations

import pytest
from assertion_graph_fixtures import SOURCE_HASH
from pydantic import ValidationError

from llmwiki.domain.assertion_graph import (
    ArgumentEdge,
    Assertion,
    AssertionKind,
    AssertionStatus,
    ParseStatus,
    ProjectionPolicy,
    ProposedChange,
    RecordPayload,
    Relationship,
    RelationshipKind,
    ReviewStatus,
    SourceUnit,
    SourceUnitKind,
    TechnicalAtom,
    TechnicalAtomKind,
    TopicKind,
    TopicState,
)


def test_invalid_source_unit_shape_fails_fast() -> None:
    with pytest.raises(ValidationError):
        SourceUnit(
            id="source-unit",
            source_locator="raw/source.pdf",
            source_hash=SOURCE_HASH,
            source_order=0,
            kind=SourceUnitKind.PARAGRAPH,
        )

    with pytest.raises(ValidationError):
        SourceUnit(
            id="su_bad_span",
            source_locator="raw/source.pdf",
            source_hash=SOURCE_HASH,
            source_order=0,
            kind=SourceUnitKind.PARAGRAPH,
            page_span=(2, 1),
        )


def test_technical_atoms_require_evidence() -> None:
    with pytest.raises(ValidationError):
        TechnicalAtom(
            id="tat_no_evidence",
            atom_kind=TechnicalAtomKind.CODE_BLOCK,
            evidence_span_ids=(),
            exact_payload="fmt.Println(x)",
            parse_status=ParseStatus.PARSED,
            source_order=0,
            provenance_activity_ids=("prv_ingest_1",),
        )


def test_accepted_source_backed_assertions_require_evidence_and_provenance() -> None:
    with pytest.raises(ValidationError, match="evidence spans"):
        Assertion(
            id="ast_no_evidence",
            kind=AssertionKind.SOURCE_CLAIM,
            subject="Arrays",
            predicate="have",
            object_value="fixed length",
            status=AssertionStatus.ACCEPTED,
            confidence=0.9,
            source_unit_ids=("su_intro",),
            provenance_activity_ids=("prv_ingest_1",),
        )

    with pytest.raises(ValidationError, match="provenance"):
        Assertion(
            id="ast_no_provenance",
            kind=AssertionKind.SOURCE_CLAIM,
            subject="Arrays",
            predicate="have",
            object_value="fixed length",
            status=AssertionStatus.ACCEPTED,
            confidence=0.9,
            source_unit_ids=("su_intro",),
            evidence_span_ids=("evs_sentence",),
        )


def test_non_source_backed_assertions_are_limited_to_analytic_inference() -> None:
    with pytest.raises(ValidationError, match="analytic inference"):
        Assertion(
            id="ast_bad_non_source",
            kind=AssertionKind.SOURCE_CLAIM,
            subject="Topic",
            predicate="implies",
            object_value="something",
            status=AssertionStatus.PROPOSED,
            confidence=0.5,
            source_backed=False,
        )

    assertion = Assertion(
        id="ast_inference",
        kind=AssertionKind.ANALYTIC_INFERENCE,
        subject="Topic",
        predicate="implies",
        object_value="something",
        status=AssertionStatus.ACCEPTED,
        confidence=0.5,
        source_backed=False,
        provenance_activity_ids=("prv_review_1",),
    )

    assert assertion.source_backed is False


def test_assertion_must_have_exactly_one_object() -> None:
    with pytest.raises(ValidationError, match="exactly one object"):
        Assertion(
            id="ast_no_object",
            kind=AssertionKind.SOURCE_CLAIM,
            subject="Topic",
            predicate="has",
            status=AssertionStatus.PROPOSED,
            confidence=0.5,
        )

    with pytest.raises(ValidationError, match="exactly one object"):
        Assertion(
            id="ast_two_objects",
            kind=AssertionKind.SOURCE_CLAIM,
            subject="Topic",
            predicate="has",
            object_entity_id="tat_table_1",
            object_value="value",
            status=AssertionStatus.PROPOSED,
            confidence=0.5,
        )


def test_relationships_cannot_use_page_projection_ids() -> None:
    with pytest.raises(ValidationError):
        Relationship(
            id="rel_bad_page",
            subject_id="pgp_character_creation",
            predicate=RelationshipKind.SUPPORTS,
            object_id="ast_claim_1",
            assertion_ids=("ast_claim_1",),
            confidence=0.8,
            provenance_activity_ids=("prv_ingest_1",),
        )


def test_argument_edges_cannot_point_to_same_assertion() -> None:
    with pytest.raises(ValidationError, match="must differ"):
        ArgumentEdge(
            id="arg_loop",
            from_assertion_id="ast_claim_1",
            to_assertion_id="ast_claim_1",
            relation=RelationshipKind.SUPPORTS,
            rationale="Self support is not a valid argument edge.",
            confidence=0.5,
            provenance_activity_id="prv_ingest_1",
        )


def test_empty_topic_state_requires_gap() -> None:
    with pytest.raises(ValidationError, match="accepted content or explicit gaps"):
        TopicState(
            id="tps_empty",
            topic_key="empty",
            label="Empty",
            topic_kind=TopicKind.CONCEPT,
            projection_policy=ProjectionPolicy(page_kind="concept", page_family="test"),
        )


def test_proposed_change_review_state_is_validated() -> None:
    proposed = RecordPayload(record_type="Assertion", json_text='{"id":"ast_claim_1"}')

    with pytest.raises(ValidationError, match="accepted record"):
        ProposedChange(
            id="pcg_bad_approved",
            review_status=ReviewStatus.APPROVED,
            proposed_record=proposed,
            source_locator="raw/source.pdf",
            model_name="qwen3",
            prompt_id="assertions-v1",
            provenance_activity_id="prv_propose_1",
        )

    with pytest.raises(ValidationError, match="cannot have accepted record"):
        ProposedChange(
            id="pcg_bad_pending",
            review_status=ReviewStatus.PENDING,
            proposed_record=proposed,
            accepted_record=proposed,
            source_locator="raw/source.pdf",
            model_name="qwen3",
            prompt_id="assertions-v1",
            provenance_activity_id="prv_propose_1",
        )
