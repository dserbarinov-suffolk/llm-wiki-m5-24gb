"""Source-agnostic knowledge-shape classification.

Knowledge shapes are derived from authored structure plus typed ledger
evidence. The classifier does not key off domain nouns or source-specific
phrases; headings label the resulting objects, but do not decide their kind.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.canonical import content_fingerprint, deterministic_id
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shape_evidence import (
    UnitEvidence,
    example_atoms,
    roles_for_evidence,
    unit_has_branch,
    unit_has_recipe_shape,
    unit_transforms_state,
)
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.procedure_evidence_index import (
    atoms_by_node,
    entries_by_node,
    rollup_atoms,
    rollup_entries,
    section_nodes,
)
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode

_STRUCTURAL_CONTAINER_PREFIX = re.compile(
    r"^\s*(chapter|part|appendix|volume|book)\b", re.IGNORECASE
)
_STRUCTURED_STEP_NUMBER = re.compile(r"^\s*\d+(?:\.\d+)+\b")


@dataclass(frozen=True)
class KnowledgeShapeCandidate:
    shape_kind: str
    knowledge_shape_id: str
    label: str
    structure_node_id: str
    source_range_id: str
    entry_ids: tuple[str, ...]
    atom_ids: tuple[str, ...]
    child_structure_node_ids: tuple[str, ...]
    evidence_roles: tuple[str, ...]
    score: int


@dataclass(frozen=True)
class KnowledgeShapeCatalog:
    knowledge_shape_catalog_id: str
    knowledge_shape_catalog_fingerprint: str
    source_locator: str
    source_hash: str
    candidates: tuple[KnowledgeShapeCandidate, ...]

    def candidates_of_kind(self, shape_kind: str) -> tuple[KnowledgeShapeCandidate, ...]:
        return tuple(item for item in self.candidates if item.shape_kind == shape_kind)


def build_knowledge_shape_catalog(
    ledger: ClaimLedger, structure: DocumentStructure
) -> KnowledgeShapeCatalog:
    grouped_entries = entries_by_node(ledger)
    grouped_atoms = atoms_by_node(ledger, structure)
    procedure_candidates = _procedure_candidates(ledger, structure, grouped_entries, grouped_atoms)
    procedure_scope = _procedure_scope_node_ids(structure, procedure_candidates)
    recipe_candidates = _recipe_candidates(
        ledger,
        structure,
        grouped_entries,
        grouped_atoms,
        procedure_scope,
    )
    candidates = tuple(
        sorted(
            (*procedure_candidates, *recipe_candidates),
            key=lambda item: item.knowledge_shape_id,
        )
    )
    fingerprint = content_fingerprint((ledger.source_locator, ledger.source_hash, candidates))
    return KnowledgeShapeCatalog(
        knowledge_shape_catalog_id=deterministic_id(
            "knowledge-shape-catalog", ledger.source_hash, fingerprint
        ),
        knowledge_shape_catalog_fingerprint=fingerprint,
        source_locator=ledger.source_locator,
        source_hash=ledger.source_hash,
        candidates=candidates,
    )


def _procedure_candidates(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
) -> tuple[KnowledgeShapeCandidate, ...]:
    candidates: list[KnowledgeShapeCandidate] = []
    for node in section_nodes(structure):
        direct_unit = _direct_unit(grouped_entries, grouped_atoms, node)
        if _is_unanchored_container(node, direct_unit):
            continue
        child_units = tuple(
            _rolled_unit(structure, grouped_entries, grouped_atoms, child)
            for child in structure.children(node.structure_node_id)
        )
        child_units = tuple(unit for unit in child_units if unit.has_evidence)
        if len(child_units) < 2:
            continue
        if not _has_structured_child_sequence(child_units):
            continue
        state_units = tuple(unit for unit in child_units if unit_transforms_state(unit))
        branch_units = tuple(unit for unit in child_units if unit_has_branch(unit))
        if len(state_units) < 2:
            continue
        if not branch_units and not any("procedure" in unit.roles for unit in child_units):
            continue
        entries = rollup_entries(structure, grouped_entries, node)
        atoms = rollup_atoms(structure, grouped_atoms, node)
        roles = roles_for_evidence(entries, atoms, child_units)
        score = len(child_units) + len(state_units) + len(branch_units)
        candidates.append(
            _candidate(
                "procedure",
                ledger,
                node,
                entries,
                atoms,
                tuple(unit.node.structure_node_id for unit in child_units),
                roles,
                score,
            )
        )
    return tuple(candidates)


def _recipe_candidates(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    procedure_scope: frozenset[str],
) -> tuple[KnowledgeShapeCandidate, ...]:
    candidates: list[KnowledgeShapeCandidate] = []
    sibling_shapes = _sibling_recipe_shape_counts(structure, grouped_entries, grouped_atoms)
    for node in section_nodes(structure):
        if node.structure_node_id in procedure_scope:
            continue
        if structure.children(node.structure_node_id):
            continue
        unit = _direct_unit(grouped_entries, grouped_atoms, node)
        if not unit_has_recipe_shape(unit):
            continue
        sibling_count = sibling_shapes.get(node.parent_structure_node_id, 0)
        if sibling_count < 3 and len(example_atoms(unit.atoms)) < 2 and len(unit.entries) < 3:
            continue
        roles = roles_for_evidence(unit.entries, unit.atoms, ())
        score = len(unit.entries) + (2 * len(example_atoms(unit.atoms))) + sibling_count
        candidates.append(
            _candidate(
                "recipe",
                ledger,
                node,
                unit.entries,
                unit.atoms,
                (),
                roles,
                score,
            )
        )
    candidates.sort(key=lambda item: (-item.score, item.label))
    return tuple(candidates[:96])


def _sibling_recipe_shape_counts(
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
) -> dict[str, int]:
    counts: dict[str, int] = {}
    for node in section_nodes(structure):
        unit = _direct_unit(grouped_entries, grouped_atoms, node)
        if unit_has_recipe_shape(unit):
            counts[node.parent_structure_node_id] = counts.get(node.parent_structure_node_id, 0) + 1
    return counts


def _procedure_scope_node_ids(
    structure: DocumentStructure, candidates: tuple[KnowledgeShapeCandidate, ...]
) -> frozenset[str]:
    scoped: set[str] = set()
    for candidate in candidates:
        scoped.add(candidate.structure_node_id)
        scoped.update(
            child.structure_node_id for child in structure.descendants(candidate.structure_node_id)
        )
    return frozenset(scoped)


def _is_unanchored_container(node: StructureNode, direct_unit: UnitEvidence) -> bool:
    if not _STRUCTURAL_CONTAINER_PREFIX.match(node.heading_text):
        return False
    return "procedure" not in direct_unit.roles and not any(
        atom.technical_atom_kind == "procedure" for atom in direct_unit.atoms
    )


def _has_structured_child_sequence(child_units: tuple[UnitEvidence, ...]) -> bool:
    numbered = tuple(
        unit for unit in child_units if _STRUCTURED_STEP_NUMBER.match(unit.node.heading_text)
    )
    return len(numbered) >= 2


def _rolled_unit(
    structure: DocumentStructure,
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    node: StructureNode,
) -> UnitEvidence:
    entries = rollup_entries(structure, grouped_entries, node)
    atoms = rollup_atoms(structure, grouped_atoms, node)
    return UnitEvidence(node, entries, atoms, frozenset(roles_for_evidence(entries, atoms, ())))


def _direct_unit(
    grouped_entries: dict[str, tuple[LedgerEntry, ...]],
    grouped_atoms: dict[str, tuple[TechnicalAtom, ...]],
    node: StructureNode,
) -> UnitEvidence:
    entries = grouped_entries.get(node.structure_node_id, ())
    atoms = grouped_atoms.get(node.structure_node_id, ())
    return UnitEvidence(node, entries, atoms, frozenset(roles_for_evidence(entries, atoms, ())))


def _candidate(
    shape_kind: str,
    ledger: ClaimLedger,
    node: StructureNode,
    entries: tuple[LedgerEntry, ...],
    atoms: tuple[TechnicalAtom, ...],
    child_node_ids: tuple[str, ...],
    roles: tuple[str, ...],
    score: int,
) -> KnowledgeShapeCandidate:
    return KnowledgeShapeCandidate(
        shape_kind=shape_kind,
        knowledge_shape_id=deterministic_id(
            "knowledge-shape", ledger.source_hash, shape_kind, node.structure_node_id
        ),
        label=node.heading_text.strip(),
        structure_node_id=node.structure_node_id,
        source_range_id=node.source_range_id,
        entry_ids=tuple(entry.ledger_entry_id for entry in entries),
        atom_ids=tuple(atom.technical_atom_id for atom in atoms),
        child_structure_node_ids=child_node_ids,
        evidence_roles=roles,
        score=score,
    )
