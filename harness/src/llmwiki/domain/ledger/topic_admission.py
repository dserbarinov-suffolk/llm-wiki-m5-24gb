"""Preventative admission rules for source-backed topic pages.

The invariant is universal: a wiki page target must be anchored in source
structure or semantic extraction, not merely in repeated lexical residue.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_candidates import TopicCandidate
from llmwiki.domain.ledger.topic_terms import source_label_terms

_SOURCE_DERIVED_KINDS = frozenset({"section-repeat", "section-component", "concept"})


@dataclass(frozen=True)
class TopicAdmissionDecision:
    accepted: bool
    reason: str


def admit_topic_candidate(
    candidate: TopicCandidate,
    entries: tuple[LedgerEntry, ...],
    atom_ids: tuple[str, ...],
    structure: DocumentStructure,
    *,
    exact_section_topic_keys: frozenset[str] = frozenset(),
) -> TopicAdmissionDecision:
    """Decide whether a candidate is allowed to become a topic page.

    Candidate labels from authored source structure, extracted concept facets,
    and section components are already semantic anchors. Raw subject-token
    candidates must prove an independent anchor before page creation.
    """
    if candidate.evidence_kind in _SOURCE_DERIVED_KINDS:
        return TopicAdmissionDecision(True, f"{candidate.evidence_kind}-anchor")
    if candidate.evidence_kind != "subject-term":
        return TopicAdmissionDecision(True, "source-derived-candidate")
    if candidate.topic_key in exact_section_topic_keys:
        return TopicAdmissionDecision(False, "exact-authored-section-page-target")
    if not entries and not atom_ids:
        return TopicAdmissionDecision(False, "no-topic-evidence")
    if _has_definition_or_concept(entries):
        return TopicAdmissionDecision(True, "definition-or-concept-anchor")
    if _heading_anchor_count(candidate.terms, structure) > 0:
        return TopicAdmissionDecision(True, "source-heading-anchor")
    if atom_ids:
        return TopicAdmissionDecision(False, "technical-atom-without-semantic-anchor")
    return TopicAdmissionDecision(False, "lexical-subject-frequency-only")


def _has_definition_or_concept(entries: tuple[LedgerEntry, ...]) -> bool:
    return any(
        entry.ledger_entry_kind == "concept"
        or bool(entry.concept_facets)
        or "definition" in entry.claim_role_tags
        for entry in entries
    )


def _heading_anchor_count(terms: tuple[str, ...], structure: DocumentStructure) -> int:
    required = frozenset(term for term in terms if term)
    if not required:
        return 0
    count = 0
    for node in structure.structure_nodes:
        if node.structure_node_kind == "root":
            continue
        heading_terms = frozenset(source_label_terms(node.heading_text))
        if required.issubset(heading_terms):
            count += 1
    return count
