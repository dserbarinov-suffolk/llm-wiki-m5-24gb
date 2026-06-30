"""Aggregate admitted topic candidates into source topics."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_substance import entry_is_unresolved_context_pointer
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_admission import admit_topic_candidate
from llmwiki.domain.ledger.topic_atom_match import atom_ids_matching_table_payload
from llmwiki.domain.ledger.topic_atom_selection import (
    atom_has_matching_context,
    atom_ids_near_entries,
)
from llmwiki.domain.ledger.topic_candidates import TopicCandidate
from llmwiki.domain.ledger.topic_entry_index import (
    TopicEntryIndex,
    topic_entry_index_supports_topic,
    topic_field_index_matches,
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
    matched, atom_ids = _candidate_evidence(
        candidate, indexed_entries, ledger, structure, matcher, required_terms
    )
    matched = [
        entry
        for entry in matched
        if len((entry.normalized_text or entry.source_text).split()) <= max_statement_words
    ]
    matched.sort(key=lambda entry: (_source_order(ledger, entry), entry.ledger_entry_id))
    matched_tuple = tuple(matched)
    decision = admit_topic_candidate(
        candidate,
        matched_tuple,
        atom_ids,
        structure,
        exact_section_topic_keys=exact_section_keys,
    )
    if not decision.accepted:
        return None, _rejected(candidate, decision.reason, len(matched_tuple), len(atom_ids))
    return _source_topic(candidate, matched_tuple, atom_ids, decision.reason), None


def _candidate_evidence(
    candidate: TopicCandidate,
    indexed_entries: tuple[TopicEntryIndex, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
    matcher: re.Pattern[str],
    required_terms: tuple[str, ...],
) -> tuple[list[LedgerEntry], tuple[str, ...]]:
    if candidate.evidence_kind in ("section", "section-repeat"):
        matched, atom_ids = _section_topic(
            candidate, indexed_entries, ledger, structure, matcher, required_terms
        )
    elif candidate.evidence_kind == "section-component":
        matched, atom_ids = _section_component_topic(
            candidate, indexed_entries, ledger, structure, matcher, required_terms
        )
    elif candidate.evidence_kind == "concept":
        matched = _entries_for_concept(candidate, indexed_entries)
        atom_ids = atom_ids_near_entries(
            ledger, structure, matched, matcher, candidate.terms, required_terms
        )
    else:
        matched = _entries_for_subject_term(
            indexed_entries, matcher, candidate.terms, required_terms
        )
        atom_ids = atom_ids_near_entries(
            ledger, structure, matched, matcher, candidate.terms, required_terms
        )
    if candidate.evidence_kind not in ("section", "section-repeat", "section-component"):
        atom_ids = tuple(
            dict.fromkeys(
                (
                    *atom_ids,
                    *atom_ids_matching_table_payload(
                        ledger, matcher, candidate.terms, required_terms, structure
                    ),
                )
            )
        )
    return matched, atom_ids


def _section_topic(
    candidate: TopicCandidate,
    indexed_entries: tuple[TopicEntryIndex, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
    matcher: re.Pattern[str],
    required_terms: tuple[str, ...],
) -> tuple[list[LedgerEntry], tuple[str, ...]]:
    evidence_ids = set(candidate.evidence_entry_ids)
    matched = [
        index.entry
        for index in indexed_entries
        if index.entry.ledger_entry_id in evidence_ids
        or (
            candidate.evidence_kind == "section-repeat"
            and topic_entry_index_supports_topic(index, matcher, candidate.terms, required_terms)
        )
    ]
    near_atoms = (
        atom_ids_near_entries(ledger, structure, matched, matcher, candidate.terms, required_terms)
        if candidate.evidence_kind == "section-repeat"
        else ()
    )
    return matched, tuple(dict.fromkeys((*candidate.evidence_atom_ids, *near_atoms)))


def _section_component_topic(
    candidate: TopicCandidate,
    indexed_entries: tuple[TopicEntryIndex, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
    matcher: re.Pattern[str],
    required_terms: tuple[str, ...],
) -> tuple[list[LedgerEntry], tuple[str, ...]]:
    evidence_ids = set(candidate.evidence_entry_ids)
    matched = [
        index.entry
        for index in indexed_entries
        if index.entry.ledger_entry_id in evidence_ids
        and topic_entry_index_supports_topic(index, matcher, candidate.terms, required_terms)
    ]
    section_entries = [
        index.entry for index in indexed_entries if index.entry.ledger_entry_id in evidence_ids
    ]
    if (
        matched
        and all(entry_is_unresolved_context_pointer(entry) for entry in matched)
        and any(not entry_is_unresolved_context_pointer(entry) for entry in section_entries)
    ):
        matched = section_entries
    atom_ids = tuple(
        atom_id
        for atom_id in candidate.evidence_atom_ids
        if atom_has_matching_context(ledger, atom_id, matcher, candidate.terms, required_terms)
    )
    if not atom_ids and len(matched) > 1:
        atom_ids = candidate.evidence_atom_ids
    return matched, atom_ids


def _entries_for_concept(
    candidate: TopicCandidate, indexed_entries: tuple[TopicEntryIndex, ...]
) -> list[LedgerEntry]:
    evidence_ids = set(candidate.evidence_entry_ids)
    return [index.entry for index in indexed_entries if index.entry.ledger_entry_id in evidence_ids]


def _entries_for_subject_term(
    indexed_entries: tuple[TopicEntryIndex, ...],
    matcher: re.Pattern[str],
    terms: tuple[str, ...],
    required_terms: tuple[str, ...],
) -> list[LedgerEntry]:
    return [
        index.entry
        for index in indexed_entries
        if topic_field_index_matches(
            index.subject_tokens, index.entry.subject, matcher, terms, required_terms
        )
    ]


def _source_topic(
    candidate: TopicCandidate,
    entries: tuple[LedgerEntry, ...],
    atom_ids: tuple[str, ...],
    admission_reason: str,
) -> SourceTopic:
    entry_ids = tuple(entry.ledger_entry_id for entry in entries)
    salience = len(entry_ids) + 1.5 * len(atom_ids)
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
        atom_ids,
        candidate.from_heading,
        salience,
        candidate.evidence_kind,
        admission_reason,
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


def _source_order(ledger: ClaimLedger, entry: LedgerEntry) -> int:
    for index, statement in enumerate(ledger.source_statements):
        if statement.source_range_id == entry.source_range_id:
            return index
    return len(ledger.source_statements)
