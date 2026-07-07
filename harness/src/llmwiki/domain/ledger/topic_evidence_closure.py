"""Source-neutral evidence closure for topic pages.

Lexical matching may discover a topic candidate, but only source-derived
provenance and semantic fields may admit evidence into the projected topic.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_substance import entry_is_unresolved_context_pointer
from llmwiki.domain.ledger.structure import DocumentStructure
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


@dataclass(frozen=True)
class TopicEvidenceClosure:
    topic_key: str
    label: str
    evidence_kind: str
    admitted_entry_ids: tuple[str, ...]
    admitted_atom_ids: tuple[str, ...]
    omitted_entry_count: int
    omitted_atom_count: int
    closure_reason: str
    is_broad: bool = False


def build_topic_evidence_closure(
    candidate: TopicCandidate,
    indexed_entries: tuple[TopicEntryIndex, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
    matcher: re.Pattern[str],
    required_terms: tuple[str, ...],
    *,
    max_statement_words: int,
) -> TopicEvidenceClosure:
    matched, atom_ids, reason = _candidate_evidence(
        candidate, indexed_entries, ledger, structure, matcher, required_terms
    )
    filtered = tuple(
        entry
        for entry in matched
        if len((entry.normalized_text or entry.source_text).split()) <= max_statement_words
    )
    ordered = tuple(
        sorted(filtered, key=lambda entry: (_source_order(ledger, entry), entry.ledger_entry_id))
    )
    entry_ids = tuple(entry.ledger_entry_id for entry in ordered)
    atom_ids = tuple(dict.fromkeys(atom_ids))
    return TopicEvidenceClosure(
        topic_key=candidate.topic_key,
        label=candidate.label,
        evidence_kind=candidate.evidence_kind,
        admitted_entry_ids=entry_ids,
        admitted_atom_ids=atom_ids,
        omitted_entry_count=max(0, len(matched) - len(entry_ids)),
        omitted_atom_count=0,
        closure_reason=reason,
        is_broad=False,
    )


def _candidate_evidence(
    candidate: TopicCandidate,
    indexed_entries: tuple[TopicEntryIndex, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
    matcher: re.Pattern[str],
    required_terms: tuple[str, ...],
) -> tuple[tuple[LedgerEntry, ...], tuple[str, ...], str]:
    if candidate.evidence_kind in ("section", "section-repeat"):
        return _section_topic(
            candidate, indexed_entries, ledger, structure, matcher, required_terms
        )
    if candidate.evidence_kind == "section-component":
        return _section_component_topic(candidate, indexed_entries, ledger, matcher, required_terms)
    if candidate.evidence_kind == "concept":
        matched = _entries_for_candidate_evidence(candidate, indexed_entries)
        atom_ids = atom_ids_near_entries(
            ledger, structure, list(matched), matcher, candidate.terms, required_terms
        )
        return (
            matched,
            _with_payload_atoms(candidate, ledger, structure, matcher, required_terms, atom_ids),
            "concept-closure",
        )
    matched = _entries_for_subject_term(indexed_entries, matcher, candidate.terms, required_terms)
    atom_ids = atom_ids_near_entries(
        ledger, structure, list(matched), matcher, candidate.terms, required_terms
    )
    return (
        matched,
        _with_payload_atoms(candidate, ledger, structure, matcher, required_terms, atom_ids),
        "subject-field-closure",
    )


def _section_topic(
    candidate: TopicCandidate,
    indexed_entries: tuple[TopicEntryIndex, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
    matcher: re.Pattern[str],
    required_terms: tuple[str, ...],
) -> tuple[tuple[LedgerEntry, ...], tuple[str, ...], str]:
    matched = _entries_for_candidate_evidence(candidate, indexed_entries)
    near_atoms = (
        atom_ids_near_entries(
            ledger, structure, list(matched), matcher, candidate.terms, required_terms
        )
        if candidate.evidence_kind == "section-repeat"
        else ()
    )
    atom_ids = tuple(dict.fromkeys((*candidate.evidence_atom_ids, *near_atoms)))
    reason = (
        "section-repeat-structural-closure"
        if candidate.evidence_kind == "section-repeat"
        else "section-structural-closure"
    )
    return matched, atom_ids, reason


def _section_component_topic(
    candidate: TopicCandidate,
    indexed_entries: tuple[TopicEntryIndex, ...],
    ledger: ClaimLedger,
    matcher: re.Pattern[str],
    required_terms: tuple[str, ...],
) -> tuple[tuple[LedgerEntry, ...], tuple[str, ...], str]:
    section_entries = _entries_for_candidate_evidence(candidate, indexed_entries)
    matched = tuple(
        index.entry
        for index in indexed_entries
        if index.entry.ledger_entry_id in set(candidate.evidence_entry_ids)
        and topic_entry_index_supports_topic(index, matcher, candidate.terms, required_terms)
    )
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
    return matched, atom_ids, "section-component-structural-closure"


def _entries_for_candidate_evidence(
    candidate: TopicCandidate, indexed_entries: tuple[TopicEntryIndex, ...]
) -> tuple[LedgerEntry, ...]:
    evidence_ids = set(candidate.evidence_entry_ids)
    return tuple(
        index.entry for index in indexed_entries if index.entry.ledger_entry_id in evidence_ids
    )


def _entries_for_subject_term(
    indexed_entries: tuple[TopicEntryIndex, ...],
    matcher: re.Pattern[str],
    terms: tuple[str, ...],
    required_terms: tuple[str, ...],
) -> tuple[LedgerEntry, ...]:
    return tuple(
        index.entry
        for index in indexed_entries
        if topic_field_index_matches(
            index.subject_tokens, index.entry.subject, matcher, terms, required_terms
        )
    )


def _with_payload_atoms(
    candidate: TopicCandidate,
    ledger: ClaimLedger,
    structure: DocumentStructure,
    matcher: re.Pattern[str],
    required_terms: tuple[str, ...],
    atom_ids: tuple[str, ...],
) -> tuple[str, ...]:
    return tuple(
        dict.fromkeys(
            (
                *atom_ids,
                *atom_ids_matching_table_payload(
                    ledger, matcher, candidate.terms, required_terms, structure
                ),
            )
        )
    )


def _source_order(ledger: ClaimLedger, entry: LedgerEntry) -> int:
    for index, statement in enumerate(ledger.source_statements):
        if statement.source_range_id == entry.source_range_id:
            return index
    return len(ledger.source_statements)
