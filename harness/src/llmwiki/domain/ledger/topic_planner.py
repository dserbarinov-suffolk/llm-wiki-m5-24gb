"""Evidence-led per-source topic planning."""

from __future__ import annotations

from collections import Counter

from llmwiki.domain.ledger.concepts import concept_topic_keys
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.section_planning import SectionGroundedPlan
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_aggregation import aggregate_topic_candidate
from llmwiki.domain.ledger.topic_candidates import (
    TopicCandidate,
    repeated_section_candidates,
    section_component_candidates,
)
from llmwiki.domain.ledger.topic_entry_index import topic_entry_index
from llmwiki.domain.ledger.topic_models import (
    RejectedTopicCandidate,
    SourceTopic,
    TopicPlanningResult,
)
from llmwiki.domain.ledger.topic_terms import (
    content_terms,
    single_term_topic_candidate_allowed,
)

_TOPIC_KINDS = ("claim", "event", "concept")
_MIN_TERM_FREQUENCY = 4
_MIN_MATCHES = 3
_MAX_TOPICS = 96
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
    return plan_source_topic_result(
        ledger,
        structure,
        section_plan=section_plan,
        max_topics=max_topics,
        min_matches=min_matches,
    ).topics


def plan_source_topic_result(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    section_plan: SectionGroundedPlan | None = None,
    max_topics: int = _MAX_TOPICS,
    min_matches: int = _MIN_MATCHES,
) -> TopicPlanningResult:
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
    exact_section_keys = _exact_section_keys(section_plan)
    topics: dict[str, SourceTopic] = {}
    rejected: list[RejectedTopicCandidate] = []
    for candidate in candidates:
        if candidate.topic_key in topics:
            continue
        topic, rejected_candidate = aggregate_topic_candidate(
            candidate,
            indexed_entries,
            ledger,
            structure,
            exact_section_keys,
            max_statement_words=_MAX_STATEMENT_WORDS,
        )
        if rejected_candidate is not None:
            rejected.append(rejected_candidate)
        if topic is None:
            continue
        minimum = 1 if candidate.from_heading or candidate.evidence_entry_ids else min_matches
        if len(topic.entry_ids) + len(topic.atom_ids) >= minimum:
            topics[candidate.topic_key] = topic
    ranked = sorted(topics.values(), key=lambda topic: (-topic.salience, topic.topic_key))
    protected = [topic for topic in ranked if topic.topic_key in protected_keys]
    regular = [topic for topic in ranked if topic.topic_key not in protected_keys]
    return TopicPlanningResult(
        tuple((*protected, *regular[: max(0, max_topics - len(protected))])),
        tuple(rejected),
    )


def _protected_topic_keys(candidates: list[TopicCandidate]) -> set[str]:
    return {
        candidate.topic_key
        for candidate in candidates
        if candidate.evidence_kind == "section-repeat"
    }


def _exact_section_keys(section_plan: SectionGroundedPlan | None) -> frozenset[str]:
    if section_plan is None:
        return frozenset()
    repeated = _protected_topic_keys(repeated_section_candidates(section_plan))
    return frozenset(
        target.topic_key
        for target in section_plan.page_targets
        if target.topic_key and target.topic_key not in repeated
    )


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
