"""Aggregate admitted topic candidates into source topics."""

from __future__ import annotations

from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_admission import admit_topic_candidate
from llmwiki.domain.ledger.topic_candidates import TopicCandidate
from llmwiki.domain.ledger.topic_entry_index import TopicEntryIndex
from llmwiki.domain.ledger.topic_evidence_closure import (
    TopicEvidenceClosure,
    build_topic_evidence_closure,
)
from llmwiki.domain.ledger.topic_models import RejectedTopicCandidate, SourceTopic
from llmwiki.domain.ledger.topic_terms import required_topic_terms, topic_matcher


def aggregate_topic_candidate(
    candidate: TopicCandidate,
    indexed_entries: tuple[TopicEntryIndex, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
    exact_section_keys: frozenset[str],
    *,
    max_statement_words: int,
) -> tuple[SourceTopic | None, RejectedTopicCandidate | None]:
    matcher = topic_matcher(candidate.terms)
    if matcher is None:
        return None, _rejected(candidate, "no-topic-matcher", 0, 0)
    required_terms = required_topic_terms(candidate.terms)
    closure = build_topic_evidence_closure(
        candidate,
        indexed_entries,
        ledger,
        structure,
        matcher,
        required_terms,
        max_statement_words=max_statement_words,
    )
    matched_tuple = tuple(
        entry
        for entry_id in closure.admitted_entry_ids
        if (entry := ledger.entry(entry_id)) is not None
    )
    decision = admit_topic_candidate(
        candidate,
        matched_tuple,
        closure.admitted_atom_ids,
        structure,
        exact_section_topic_keys=exact_section_keys,
    )
    if not decision.accepted:
        return None, _rejected(
            candidate,
            decision.reason,
            len(matched_tuple),
            len(closure.admitted_atom_ids),
        )
    return _source_topic(candidate, matched_tuple, closure, decision.reason), None


def _source_topic(
    candidate: TopicCandidate,
    entries: tuple[LedgerEntry, ...],
    closure: TopicEvidenceClosure,
    admission_reason: str,
) -> SourceTopic:
    entry_ids = tuple(entry.ledger_entry_id for entry in entries)
    salience = len(entry_ids) + 1.5 * len(closure.admitted_atom_ids)
    if candidate.from_heading:
        salience += 3.0
    if candidate.evidence_entry_ids:
        salience += 2.0
    if candidate.evidence_kind == "section-repeat":
        salience += 12.0
    return SourceTopic(
        candidate.topic_key,
        candidate.label,
        "concept",
        candidate.terms,
        entry_ids,
        closure.admitted_atom_ids,
        candidate.from_heading,
        salience,
        candidate.evidence_kind,
        admission_reason,
        closure.closure_reason,
        closure.omitted_entry_count,
        closure.omitted_atom_count,
    )


def _rejected(
    candidate: TopicCandidate, reason: str, entry_count: int, atom_count: int
) -> RejectedTopicCandidate:
    return RejectedTopicCandidate(
        topic_key=candidate.topic_key,
        label=candidate.label,
        candidate_origin=candidate.evidence_kind,
        rejection_reason=reason,
        match_terms=candidate.terms,
        entry_count=entry_count,
        atom_count=atom_count,
    )
