"""Technical atom selection for topic pages."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atom_context import atom_context_matches
from llmwiki.domain.ledger.atom_projection import atom_is_topic_projectable
from llmwiki.domain.ledger.atoms import atom_raw_text
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.section_navigation import section_title
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.ledger.topic_terms import topic_field_matches


def atom_ids_near_entries(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    entries: list[LedgerEntry],
    matcher: re.Pattern[str],
    terms: tuple[str, ...],
    required_terms: tuple[str, ...],
) -> tuple[str, ...]:
    nodes = {node_id for entry in entries for node_id in entry.structure_node_ids[:1]}
    ids: list[str] = []
    for entry in ledger.usable_entries:
        if entry.ledger_entry_kind != "technical-atom" or not entry.technical_atom_id:
            continue
        if nodes and not nodes.intersection(entry.structure_node_ids):
            continue
        if not atom_entry_belongs_to_topic(
            ledger, structure, entry, matcher, terms, required_terms
        ):
            continue
        if atom_has_matching_context(
            ledger, entry.technical_atom_id, matcher, terms, required_terms
        ):
            ids.append(entry.technical_atom_id)
    return tuple(dict.fromkeys(ids))


def atom_entry_belongs_to_topic(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    entry: LedgerEntry,
    matcher: re.Pattern[str],
    terms: tuple[str, ...],
    required_terms: tuple[str, ...],
) -> bool:
    if len(required_terms) <= 1:
        return True
    node = structure.node(entry.structure_node_ids[0]) if entry.structure_node_ids else None
    if node is not None and topic_field_matches(
        section_title(structure, node), matcher, terms, required_terms
    ):
        return True
    atom = ledger.atom(entry.technical_atom_id)
    return atom is not None and topic_field_matches(
        atom_raw_text(atom.payload), matcher, terms, required_terms
    )


def atom_has_matching_context(
    ledger: ClaimLedger,
    atom_id: str,
    matcher: re.Pattern[str],
    terms: tuple[str, ...],
    required_terms: tuple[str, ...],
) -> bool:
    atom = ledger.atom(atom_id)
    return (
        atom is not None
        and atom_is_topic_projectable(atom, ledger.source_profile)
        and atom_context_matches(ledger.atom_contexts(atom_id), matcher, terms, required_terms)
    )
