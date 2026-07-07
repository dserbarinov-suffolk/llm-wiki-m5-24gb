"""Per-segment ledger assembly: candidates and claims into ledger entries.

Accepted atom candidates become technical atoms and atom entries; eligible,
decomposable claims become claim/relationship entries (a claim already
preserved verbatim by a rule/procedure atom is not duplicated); meaningful but
undecomposed segments become a needs-review source note. Each segment then
receives exactly one disposition.
"""

from __future__ import annotations

from dataclasses import replace

from llmwiki.domain.ledger.atoms import (
    AtomCandidate,
    TechnicalAtom,
    atom_raw_text,
    payload_fingerprint,
)
from llmwiki.domain.ledger.canonical import deterministic_id
from llmwiki.domain.ledger.common import ReviewReason
from llmwiki.domain.ledger.confidence import ConfidencePolicy
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.entry_build import (
    build_atom_entry,
    build_claim_entry,
    build_relationship_entry,
    build_source_note,
)
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.technical_atom_trust import (
    RAW_REVIEW_ONLY,
    REJECTED,
    REVIEW_ONLY,
    assess_technical_atom_trust,
)

_FURNITURE_ELIGIBILITIES = frozenset({"source-furniture", "source-framing"})
_MIN_MEANINGFUL_WORDS = 6


def build_segment_entries(
    seg: SourceSegment,
    claims: tuple[SegmentClaim, ...],
    candidates: tuple[AtomCandidate, ...],
    statement_id: str,
    node_ids: tuple[str, ...],
    policy: ConfidencePolicy,
    atoms: list[TechnicalAtom],
    rejected: list[AtomCandidate],
    ownership_review_reason: ReviewReason | None = None,
) -> list[LedgerEntry]:
    produced: list[LedgerEntry] = []
    atom_texts: list[str] = []
    for candidate in candidates:
        if candidate.validation_status == "valid" and candidate.payload is not None:
            atom = _materialize_atom(seg, candidate)
            trust = assess_technical_atom_trust(atom)
            atom = replace(
                atom,
                trust_status=trust.trust_status,
                trust_reasons=trust.trust_reasons,
                projection_policy=trust.projection_policy,
                review_reason=trust.review_reason or atom.review_reason,
            )
            if trust.trust_status == REJECTED:
                rejected.append(replace(candidate, review_reason=trust.review_reason))
                continue
            atom = _apply_ownership_review(atom, ownership_review_reason)
            atoms.append(atom)
            atom_texts.append(atom_raw_text(atom.payload))
            produced.append(
                build_atom_entry(
                    segment=seg,
                    atom=atom,
                    statement_id=statement_id,
                    structure_node_ids=node_ids,
                    policy=policy,
                )
            )
        else:
            rejected.append(candidate)
    for claim in claims:
        if claim.eligibility != "eligible" or _preserved_by_atom(claim.statement, atom_texts):
            continue
        entry = build_claim_entry(
            segment=seg,
            claim=claim,
            statement_id=statement_id,
            structure_node_ids=node_ids,
            policy=policy,
        )
        produced.append(entry)
        relationship = build_relationship_entry(
            segment=seg,
            claim=claim,
            primary_entry_id=entry.ledger_entry_id,
            statement_id=statement_id,
            structure_node_ids=node_ids,
        )
        if relationship is not None:
            produced.append(relationship)
    if not produced and _is_meaningful(seg, claims):
        produced.append(
            build_source_note(segment=seg, statement_id=statement_id, structure_node_ids=node_ids)
        )
    return produced


def _apply_ownership_review(
    atom: TechnicalAtom, review_reason: ReviewReason | None
) -> TechnicalAtom:
    if review_reason is None or atom.trust_status == REJECTED:
        return atom
    return replace(
        atom,
        trust_status=REVIEW_ONLY,
        trust_reasons=tuple(dict.fromkeys((*atom.trust_reasons, review_reason.reason_kind))),
        projection_policy=RAW_REVIEW_ONLY,
        review_reason=review_reason,
    )


def segment_disposition(produced: list[LedgerEntry], candidates: tuple[AtomCandidate, ...]) -> str:
    if any(entry.is_usable for entry in produced):
        return "accepted"
    if any(entry.ledger_entry_status == "needs-review" for entry in produced):
        return "needs-review"
    if candidates:
        return "rejected"
    return "non-claim"


def _materialize_atom(seg: SourceSegment, candidate: AtomCandidate) -> TechnicalAtom:
    assert candidate.payload is not None
    parse_status = getattr(candidate.payload, "parse_status", "parsed")
    return TechnicalAtom(
        technical_atom_id=deterministic_id(
            "technical-atom",
            seg.source_hash,
            seg.source_range_id,
            candidate.technical_atom_kind,
            payload_fingerprint(candidate.payload),
        ),
        technical_atom_kind=candidate.technical_atom_kind,
        payload=candidate.payload,
        source_locator=seg.source_locator,
        source_range_id=seg.source_range_id,
        evidence_ids=candidate.evidence_ids,
        parse_status=parse_status,
        review_reason=candidate.review_reason,
        source_unit_id=candidate.source_unit_id,
        source_block_ids=candidate.source_block_ids,
        source_element_ids=candidate.source_element_ids,
        source_page_start=candidate.source_page_start,
        source_page_end=candidate.source_page_end,
    )


def _preserved_by_atom(statement: str, atom_texts: list[str]) -> bool:
    """A deontic/procedural sentence captured by a rule/procedure atom is the
    atom's authoritative text; do not also emit a duplicate standalone claim."""
    normalized = " ".join(statement.split())
    return any(normalized and normalized in " ".join(text.split()) for text in atom_texts)


def _is_meaningful(seg: SourceSegment, claims: tuple[SegmentClaim, ...]) -> bool:
    if claims and all(claim.eligibility in _FURNITURE_ELIGIBILITIES for claim in claims):
        return False
    return len(seg.text.split()) >= _MIN_MEANINGFUL_WORDS
