"""Proposed-change review gate for ledger records."""

from __future__ import annotations

import json

from llmwiki.domain.assertion_graph import ReviewStatus
from llmwiki.domain.ledger.atoms import AtomCandidate, CodeBlockPayload, TechnicalAtom
from llmwiki.domain.ledger.common import ConfidenceBasis
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.proposed_change_review import (
    LedgerProposedChangeReviewer,
    proposed_change_review_artifact_to_json,
)


def _entry(**overrides: object) -> LedgerEntry:
    values = {
        "ledger_entry_id": "ledger-entry-1",
        "source_statement_id": "source-statement-1",
        "ledger_entry_kind": "claim",
        "ledger_entry_status": "usable",
        "extraction_confidence": "high",
        "confidence_basis": ConfidenceBasis("unit-test"),
        "source_locator": "source.pdf",
        "source_hash": "abc123",
        "source_range_id": "source-range-1",
        "evidence_ids": ("ev-1",),
        "source_text": "Arrays store indexed values.",
        "subject": "Arrays",
        "predicate": "store",
        "object_value": "indexed values",
    }
    values.update(overrides)
    return LedgerEntry(**values)  # type: ignore[arg-type]


def _atom(**overrides: object) -> TechnicalAtom:
    values = {
        "technical_atom_id": "technical-atom-1",
        "technical_atom_kind": "code-block",
        "payload": CodeBlockPayload(
            raw_code_text="const value = items[0];",
            parse_status="parsed",
            source_locator="source.pdf",
        ),
        "source_locator": "source.pdf",
        "source_range_id": "source-range-2",
        "evidence_ids": ("ev-2",),
    }
    values.update(overrides)
    return TechnicalAtom(**values)  # type: ignore[arg-type]


def test_reviewer_accepts_valid_entry_and_records_proposed_change() -> None:
    reviewer = LedgerProposedChangeReviewer(source_locator="source.pdf", source_hash="abc123")

    decision = reviewer.review_entry(_entry())
    artifact = reviewer.artifact()

    assert decision.accepted_entry is not None
    assert decision.accepted_entry.proposed_change_id.startswith("pcg_")
    assert decision.proposed_change is not None
    assert decision.proposed_change.review_status == ReviewStatus.APPROVED
    assert decision.proposed_change.accepted_record is not None
    assert artifact.approved_count == 1
    assert artifact.rejected_count == 0


def test_reviewer_rejects_incomplete_claim_without_accepting_record() -> None:
    reviewer = LedgerProposedChangeReviewer(source_locator="source.pdf", source_hash="abc123")

    decision = reviewer.review_entry(_entry(object_value=""))

    assert decision.accepted_entry is None
    assert decision.proposed_change is not None
    assert decision.proposed_change.review_status == ReviewStatus.REJECTED
    assert decision.proposed_change.accepted_record is None


def test_reviewer_accepts_valid_technical_atom() -> None:
    reviewer = LedgerProposedChangeReviewer(source_locator="source.pdf", source_hash="abc123")

    decision = reviewer.review_atom(_atom())

    assert decision.accepted_atom is not None
    assert decision.accepted_atom.proposed_change_id.startswith("pcg_")
    assert decision.proposed_change is not None
    assert decision.proposed_change.review_status == ReviewStatus.APPROVED


def test_reviewer_records_rejected_candidate_as_portable_change() -> None:
    reviewer = LedgerProposedChangeReviewer(source_locator="source.pdf", source_hash="abc123")
    candidate = AtomCandidate(
        atom_candidate_id="atom-candidate-1",
        extractor_decision_id="extractor-decision-1",
        extractor_capability_id="table-extractor",
        technical_atom_kind="table",
        ranker_score=0.1,
        calibration_bucket="low",
        source_range_id="source-range-3",
        validation_status="invalid",
        validation_detail="schema-mismatch",
    )

    change = reviewer.reject_candidate(candidate, "schema-mismatch")
    artifact = reviewer.artifact()
    serialized = json.loads(proposed_change_review_artifact_to_json(artifact))

    assert change.review_status == ReviewStatus.REJECTED
    assert artifact.approved_count == 0
    assert artifact.rejected_count == 1
    assert serialized["proposed_changes"][0]["proposed_record"]["record_type"] == "AtomCandidate"
