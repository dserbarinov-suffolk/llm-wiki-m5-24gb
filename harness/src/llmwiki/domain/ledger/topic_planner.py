"""Evidence-led per-source topic planning."""

from __future__ import annotations

import re
from collections import Counter

from llmwiki.domain.ledger.concepts import concept_topic_keys
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_substance import entry_is_unresolved_context_pointer
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_atom_match import atom_ids_matching_table_payload
from llmwiki.domain.ledger.topic_atom_selection import (
    atom_has_matching_context,
    atom_ids_near_entries,
)
from llmwiki.domain.ledger.topic_candidates import (
    TopicCandidate,
    repeated_section_candidates,
    section_component_candidates,
)
from llmwiki.domain.ledger.topic_entry_index import (
    TopicEntryIndex,
    topic_entry_index,
    topic_entry_index_supports_topic,
    topic_field_index_matches,
)
from llmwiki.domain.ledger.topic_models import SourceTopic
from llmwiki.domain.ledger.topic_terms import (
    content_terms,
    required_topic_terms,
    single_term_topic_candidate_allowed,
    topic_matcher,
)

_TOPIC_KINDS = ("claim", "event", "concept")
_MIN_TERM_FREQUENCY = 4
_MIN_MATCHES = 3
_MAX_TOPICS = 96
_HEADING_BONUS = 3.0
_CONCEPT_BONUS = 2.0
_REPEATED_SECTION_BONUS = 12.0
_MAX_STATEMENT_WORDS = 45
_MAX_ENTRIES_FOR_SUBJECT_TERM_CANDIDATES = 2_000


def plan_source_topics(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    section_plan: SectionGroundedPlan | None = None,
    max_topics: int = _MAX_TOPICS,
    min_matches: int = _MIN_MATCHES,
) -> tuple[SourceTopic, ...]:
    entries = [
        entry
        for entry in ledger.usable_entries
        if entry.ledger_entry_kind in _TOPIC_KINDS and (entry.subject or entry.normalized_text)
    ]
    candidates = (
        repeated_section_candidates(section_plan)
        + section_component_candidates(section_plan)
        + _concept_candidates(entries)
        + (
            _term_candidates(entries)
            if len(entries) <= _MAX_ENTRIES_FOR_SUBJECT_TERM_CANDIDATES
            else []
        )
    )
    indexed_entries = tuple(topic_entry_index(entry) for entry in entries)
    protected_keys = _protected_topic_keys(candidates)
    topics: dict[str, SourceTopic] = {}
    for candidate in candidates:
        if candidate.topic_key in topics:
            continue
        topic = _aggregate(candidate, indexed_entries, ledger, structure)
        if topic is None:
            continue
        minimum = 1 if candidate.from_heading or candidate.evidence_entry_ids else min_matches
        if len(topic.entry_ids) + len(topic.atom_ids) >= minimum:
            topics[candidate.topic_key] = topic
    ranked = sorted(topics.values(), key=lambda topic: (-topic.salience, topic.topic_key))
    protected = [topic for topic in ranked if topic.topic_key in protected_keys]
    regular = [topic for topic in ranked if topic.topic_key not in protected_keys]
    return tuple((*protected, *regular[: max(0, max_topics - len(protected))]))


def _protected_topic_keys(candidates: list[TopicCandidate]) -> set[str]:
    return {
        candidate.topic_key
        for candidate in candidates
        if candidate.evidence_kind == "section-repeat"
    }


def _concept_candidates(entries: list[LedgerEntry]) -> list[TopicCandidate]:
    keyed: dict[str, tuple[str, tuple[str, ...], list[str]]] = {}
    for entry in entries:
        if entry.ledger_entry_kind != "concept" or not entry.concept_facets:
            continue
        for facet in entry.concept_facets:
            keys = concept_topic_keys((facet,))
            terms = tuple(content_terms(facet))
            if not keys or not terms:
                continue
            label, existing_terms, entry_ids = keyed.get(keys[0], (facet.title(), terms, []))
            entry_ids.append(entry.ledger_entry_id)
            keyed[keys[0]] = (label, existing_terms, entry_ids)
    return [
        TopicCandidate(key, label, terms, "concept", evidence_entry_ids=tuple(entry_ids))
        for key, (label, terms, entry_ids) in keyed.items()
    ]


def _term_candidates(entries: list[LedgerEntry]) -> list[TopicCandidate]:
    counts: Counter[str] = Counter()
    for entry in entries:
        for token in content_terms(entry.subject):
            counts[token] += 1
    candidates: list[TopicCandidate] = []
    for term, frequency in counts.most_common():
        if frequency < _MIN_TERM_FREQUENCY:
            break
        if single_term_topic_candidate_allowed(term):
            candidates.append(TopicCandidate(term, term.title(), (term,), "subject-term"))
    return candidates


def _aggregate(
    candidate: TopicCandidate,
    indexed_entries: tuple[TopicEntryIndex, ...],
    ledger: ClaimLedger,
    structure: DocumentStructure,
) -> SourceTopic | None:
    matcher = topic_matcher(candidate.terms)
    if matcher is None:
        return None
    required_terms = required_topic_terms(candidate.terms)
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
    matched = [
        entry
        for entry in matched
        if len((entry.normalized_text or entry.source_text).split()) <= _MAX_STATEMENT_WORDS
    ]
    matched.sort(key=lambda entry: (_source_order(ledger, entry), entry.ledger_entry_id))
    return _source_topic(candidate, matched, atom_ids)


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
    candidate: TopicCandidate, entries: list[LedgerEntry], atom_ids: tuple[str, ...]
) -> SourceTopic:
    entry_ids = tuple(entry.ledger_entry_id for entry in entries)
    salience = (
        len(entry_ids)
        + 1.5 * len(atom_ids)
        + (_HEADING_BONUS if candidate.from_heading else 0.0)
        + (_CONCEPT_BONUS if candidate.evidence_entry_ids else 0.0)
        + (_REPEATED_SECTION_BONUS if candidate.evidence_kind == "section-repeat" else 0.0)
    )
    return SourceTopic(
        candidate.topic_key,
        candidate.label,
        "concept",
        candidate.terms,
        entry_ids,
        atom_ids,
        candidate.from_heading,
        salience,
    )


def _source_order(ledger: ClaimLedger, entry: LedgerEntry) -> int:
    for index, statement in enumerate(ledger.source_statements):
        if statement.source_range_id == entry.source_range_id:
            return index
    return len(ledger.source_statements)
