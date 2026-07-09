"""Deterministic proposed-change review for ledger records."""

from __future__ import annotations

from dataclasses import dataclass, replace

from pydantic import BaseModel, ConfigDict

from llmwiki.domain.assertion_graph import (
    ProposedChange,
    ProvenanceActivity,
    ProvenanceActivityKind,
    RecordPayload,
    ReviewStatus,
)
from llmwiki.domain.ledger.atoms import AtomCandidate, TechnicalAtom, atom_raw_text
from llmwiki.domain.ledger.canonical import artifact_fingerprint, canonical_json, short_digest
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.vocab import (
    ARTIFACT_FORMAT,
    EXTRACTION_CONFIDENCES,
    LEDGER_ENTRY_KINDS,
    LEDGER_ENTRY_STATUSES,
    TECHNICAL_ATOM_KINDS,
    TECHNICAL_ATOM_TRUST_STATUSES,
)


class ProposedChangeReviewArtifact(BaseModel):
    """Portable review record for accepted and rejected proposed changes."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    proposed_change_review_artifact_id: str
    proposed_change_review_fingerprint: str
    artifact_format: str
    source_locator: str
    source_hash: str
    proposed_changes: tuple[ProposedChange, ...]
    provenance_activities: tuple[ProvenanceActivity, ...]
    approved_count: int
    rejected_count: int


@dataclass(frozen=True)
class ReviewDecision:
    accepted_entry: LedgerEntry | None = None
    accepted_atom: TechnicalAtom | None = None
    proposed_change: ProposedChange | None = None


class LedgerProposedChangeReviewer:
    """Domain service that admits ledger records through proposed changes."""

    def __init__(self, *, source_locator: str, source_hash: str) -> None:
        self._source_locator = source_locator
        self._source_hash = source_hash
        self._proposed_changes: list[ProposedChange] = []
        self._activities: list[ProvenanceActivity] = []

    @property
    def proposed_changes(self) -> tuple[ProposedChange, ...]:
        return tuple(self._proposed_changes)

    @property
    def provenance_activities(self) -> tuple[ProvenanceActivity, ...]:
        return tuple(self._activities)

    def review_entry(self, entry: LedgerEntry) -> ReviewDecision:
        return self._review_record("LedgerEntry", entry, _entry_rejection_reason(entry))

    def review_atom(self, atom: TechnicalAtom) -> ReviewDecision:
        return self._review_record("TechnicalAtom", atom, _atom_rejection_reason(atom))

    def reject_candidate(self, candidate: AtomCandidate, reason: str) -> ProposedChange:
        change = self._change(
            record_type="AtomCandidate",
            proposed_record=candidate,
            accepted_record=None,
            review_status=ReviewStatus.REJECTED,
            reason=reason,
        )
        self._proposed_changes.append(change)
        return change

    def artifact(self) -> ProposedChangeReviewArtifact:
        draft = ProposedChangeReviewArtifact(
            proposed_change_review_artifact_id="pending",
            proposed_change_review_fingerprint="",
            artifact_format=ARTIFACT_FORMAT,
            source_locator=self._source_locator,
            source_hash=self._source_hash,
            proposed_changes=self.proposed_changes,
            provenance_activities=self.provenance_activities,
            approved_count=sum(1 for change in self._approved_changes()),
            rejected_count=sum(1 for change in self._rejected_changes()),
        )
        fingerprint = artifact_fingerprint(
            draft.model_dump(mode="json"),
            exclude=(
                "proposed_change_review_artifact_id",
                "proposed_change_review_fingerprint",
            ),
        )
        return draft.model_copy(
            update={
                "proposed_change_review_artifact_id": f"proposed-change-review-{fingerprint}",
                "proposed_change_review_fingerprint": fingerprint,
            }
        )

    def _review_record(
        self, record_type: str, record: LedgerEntry | TechnicalAtom, reason: str
    ) -> ReviewDecision:
        if reason:
            change = self._change(
                record_type=record_type,
                proposed_record=record,
                accepted_record=None,
                review_status=ReviewStatus.REJECTED,
                reason=reason,
            )
            self._proposed_changes.append(change)
            return ReviewDecision(proposed_change=change)
        accepted = replace(record, proposed_change_id=self._change_id(record_type, record))
        change = self._change(
            record_type=record_type,
            proposed_record=record,
            accepted_record=accepted,
            review_status=ReviewStatus.APPROVED,
            reason="approved",
        )
        self._proposed_changes.append(change)
        if isinstance(accepted, LedgerEntry):
            return ReviewDecision(accepted_entry=accepted, proposed_change=change)
        return ReviewDecision(accepted_atom=accepted, proposed_change=change)

    def _change(
        self,
        *,
        record_type: str,
        proposed_record: object,
        accepted_record: object | None,
        review_status: ReviewStatus,
        reason: str,
    ) -> ProposedChange:
        change_id = self._change_id(record_type, proposed_record)
        activity = ProvenanceActivity(
            id=f"prv_{short_digest(change_id + reason)}",
            activity_kind=ProvenanceActivityKind.PROPOSED_CHANGE_REVIEW,
            actor="llmwiki-proposed-change-review",
            input_record_ids=(),
            output_record_ids=(change_id,),
            source_locator=self._source_locator,
        )
        self._activities.append(activity)
        return ProposedChange(
            id=change_id,
            review_status=review_status,
            proposed_record=_payload(record_type, proposed_record),
            accepted_record=_payload(record_type, accepted_record) if accepted_record else None,
            source_locator=self._source_locator,
            source_unit_ids=(),
            model_name="deterministic",
            prompt_id="proposed-change-review",
            provenance_activity_id=activity.id,
        )

    def _change_id(self, record_type: str, record: object) -> str:
        return f"pcg_{short_digest(record_type + canonical_json(record))}"

    def _approved_changes(self) -> tuple[ProposedChange, ...]:
        return tuple(
            change
            for change in self._proposed_changes
            if change.review_status == ReviewStatus.APPROVED
        )

    def _rejected_changes(self) -> tuple[ProposedChange, ...]:
        return tuple(
            change
            for change in self._proposed_changes
            if change.review_status == ReviewStatus.REJECTED
        )


def proposed_change_review_artifact_to_json(artifact: ProposedChangeReviewArtifact) -> str:
    return canonical_json(artifact, indent=2)


def _payload(record_type: str, record: object) -> RecordPayload:
    return RecordPayload(record_type=record_type, json_text=canonical_json(record))


def _entry_rejection_reason(entry: LedgerEntry) -> str:
    if entry.ledger_entry_kind not in LEDGER_ENTRY_KINDS:
        return "invalid-ledger-entry-kind"
    if entry.ledger_entry_status not in LEDGER_ENTRY_STATUSES:
        return "invalid-ledger-entry-status"
    if entry.extraction_confidence not in EXTRACTION_CONFIDENCES:
        return "invalid-extraction-confidence"
    if not entry.source_locator or not entry.source_hash or not entry.source_range_id:
        return "missing-source-provenance"
    if not entry.evidence_ids:
        return "missing-evidence"
    if not entry.source_text.strip():
        return "missing-source-text"
    if (
        entry.is_claim_like
        and entry.is_usable
        and (not entry.subject or not entry.predicate or not entry.object_value)
    ):
        return "incomplete-usable-claim"
    if entry.ledger_entry_kind == "technical-atom" and (
        not entry.technical_atom_id or not entry.technical_atom_kind
    ):
        return "missing-technical-atom-reference"
    return ""


def _atom_rejection_reason(atom: TechnicalAtom) -> str:
    if atom.technical_atom_kind not in TECHNICAL_ATOM_KINDS:
        return "invalid-technical-atom-kind"
    if atom.trust_status not in TECHNICAL_ATOM_TRUST_STATUSES:
        return "invalid-technical-atom-trust-status"
    if atom.trust_status == "rejected":
        return "rejected-technical-atom"
    if not atom.source_locator or not atom.source_range_id:
        return "missing-source-provenance"
    if not atom.evidence_ids:
        return "missing-evidence"
    if not atom.payload or not atom_raw_text(atom.payload).strip():
        return "missing-exact-payload"
    return ""
