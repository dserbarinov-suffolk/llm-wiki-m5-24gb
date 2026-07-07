"""Procedure evidence closure for complete procedure page projection."""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.atom_addressing import technical_atom_link
from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.common import ReviewReason
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.procedure_decisions import DecisionPoint
from llmwiki.domain.ledger.procedures import ProcedureGuide, ProcedureStep, atom_label
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode
from llmwiki.domain.ledger.technical_atom_trust import atom_is_authoritative

DEPENDENCY_AUTHORITATIVE = "authoritative"
DEPENDENCY_REVIEW_ONLY = "review-only"
DEPENDENCY_MISSING = "missing"
PROJECTION_READY = "ready"
PROJECTION_PARTIAL = "partial"
PROJECTION_BLOCKED = "blocked"

_DEPENDENCY_KINDS = frozenset({"table", "formula", "procedure", "rule", "worked-example"})


@dataclass(frozen=True)
class ProcedureDependency:
    atom: TechnicalAtom
    dependency_status: str
    page_id: str = ""
    review_reason: ReviewReason | None = None

    @property
    def dependency_kind(self) -> str:
        return self.atom.technical_atom_kind

    @property
    def label(self) -> str:
        return atom_label(self.atom)

    @property
    def source_range_id(self) -> str:
        return self.atom.source_range_id

    @property
    def source_locator(self) -> str:
        return self.atom.source_locator


@dataclass(frozen=True)
class ProcedureStepEvidenceClosure:
    step: ProcedureStep
    claims: tuple[LedgerEntry, ...]
    dependencies: tuple[ProcedureDependency, ...]


@dataclass(frozen=True)
class ProcedureProjectionStatus:
    status: str
    authoritative_dependency_count: int
    review_only_dependency_count: int
    missing_dependency_count: int = 0


@dataclass(frozen=True)
class ProcedureEvidenceClosure:
    guide: ProcedureGuide
    steps: tuple[ProcedureStepEvidenceClosure, ...]
    decision_points: tuple[DecisionPoint, ...]
    authoritative_dependencies: tuple[ProcedureDependency, ...]
    review_only_dependencies: tuple[ProcedureDependency, ...]
    missing_dependencies: tuple[ProcedureDependency, ...]
    projection_status: ProcedureProjectionStatus


def build_procedure_evidence_closure(
    guide: ProcedureGuide,
    *,
    ledger: ClaimLedger | None = None,
    structure: DocumentStructure | None = None,
) -> ProcedureEvidenceClosure:
    page_by_atom = _step_page_by_atom(guide.steps)
    step_closures = tuple(
        ProcedureStepEvidenceClosure(
            step=step,
            claims=step.claims,
            dependencies=_dependencies_for_atoms(step.technical_atoms, page_by_atom),
        )
        for step in guide.steps
    )
    authoritative = _dependencies_for_atoms(
        guide.technical_atoms,
        page_by_atom,
        fallback_page_id=guide.source_section_page_id,
    )
    review_only = (
        _review_only_dependencies(guide, ledger, structure)
        if ledger is not None and structure is not None
        else ()
    )
    missing: tuple[ProcedureDependency, ...] = ()
    status = _projection_status(authoritative, review_only, missing)
    return ProcedureEvidenceClosure(
        guide=guide,
        steps=step_closures,
        decision_points=_rendered_decision_points(guide),
        authoritative_dependencies=authoritative,
        review_only_dependencies=review_only,
        missing_dependencies=missing,
        projection_status=status,
    )


def dependency_link(dependency: ProcedureDependency) -> str:
    if dependency.page_id:
        return technical_atom_link(dependency.page_id, dependency.atom, dependency.label)
    return dependency.label


def dependency_citation(dependency: ProcedureDependency) -> str:
    return f"{dependency.source_locator} ({dependency.source_range_id})"


def review_reason_text(dependency: ProcedureDependency) -> str:
    reason = dependency.review_reason or dependency.atom.review_reason
    if reason is not None:
        return f"{reason.reason_kind}: {reason.detail}"
    if dependency.atom.trust_reasons:
        return ", ".join(dependency.atom.trust_reasons)
    return dependency.dependency_status


def _dependencies_for_atoms(
    atoms: tuple[TechnicalAtom, ...],
    page_by_atom: dict[str, str],
    *,
    fallback_page_id: str = "",
) -> tuple[ProcedureDependency, ...]:
    return _unique_dependencies(
        tuple(
            ProcedureDependency(
                atom=atom,
                dependency_status=DEPENDENCY_AUTHORITATIVE,
                page_id=page_by_atom.get(atom.technical_atom_id, fallback_page_id),
            )
            for atom in atoms
            if _relevant_atom(atom) and atom_is_authoritative(atom)
        )
    )


def _review_only_dependencies(
    guide: ProcedureGuide, ledger: ClaimLedger, structure: DocumentStructure
) -> tuple[ProcedureDependency, ...]:
    authoritative_ids = {atom.technical_atom_id for atom in guide.technical_atoms}
    return _unique_dependencies(
        tuple(
            ProcedureDependency(
                atom=atom,
                dependency_status=DEPENDENCY_REVIEW_ONLY,
                review_reason=atom.review_reason,
            )
            for atom in ledger.technical_atoms
            if _relevant_atom(atom)
            and atom.technical_atom_id not in authoritative_ids
            and not atom_is_authoritative(atom)
            and _atom_in_admitted_scope(atom, guide, structure)
        )
    )


def _projection_status(
    authoritative: tuple[ProcedureDependency, ...],
    review_only: tuple[ProcedureDependency, ...],
    missing: tuple[ProcedureDependency, ...],
) -> ProcedureProjectionStatus:
    if missing:
        status = PROJECTION_BLOCKED
    elif review_only:
        status = PROJECTION_PARTIAL
    else:
        status = PROJECTION_READY
    return ProcedureProjectionStatus(
        status=status,
        authoritative_dependency_count=len(authoritative),
        review_only_dependency_count=len(review_only),
        missing_dependency_count=len(missing),
    )


def _rendered_decision_points(guide: ProcedureGuide) -> tuple[DecisionPoint, ...]:
    shown_claim_keys = {_entry_key(claim) for step in guide.steps for claim in step.claims}
    supporting_context_range_ids = _supporting_context_range_ids(guide.decision_points)
    return tuple(
        point
        for point in guide.decision_points
        if (
            _entry_key(point.entry) not in shown_claim_keys
            or _decision_has_contextual_evidence(point)
        )
        and point.entry.source_range_id not in supporting_context_range_ids
    )


def _supporting_context_range_ids(points: tuple[DecisionPoint, ...]) -> frozenset[str]:
    return frozenset(
        range_id
        for point in points
        for range_id in point.evidence_block.source_range_ids
        if range_id != point.entry.source_range_id
    )


def _decision_has_contextual_evidence(point: DecisionPoint) -> bool:
    entry_text = _entry_text(point.entry)
    return (
        len(point.evidence_block.source_range_ids) > 1
        or point.evidence_block.source_text.strip() != entry_text
    )


def _step_page_by_atom(steps: tuple[ProcedureStep, ...]) -> dict[str, str]:
    page_by_atom: dict[str, str] = {}
    for step in steps:
        for atom in step.technical_atoms:
            page_by_atom.setdefault(atom.technical_atom_id, step.section_page_id)
    return page_by_atom


def _unique_dependencies(
    dependencies: tuple[ProcedureDependency, ...],
) -> tuple[ProcedureDependency, ...]:
    seen: set[tuple[str, str, str]] = set()
    unique: list[ProcedureDependency] = []
    for dependency in dependencies:
        key = (
            dependency.atom.technical_atom_id,
            dependency.source_range_id,
            dependency.label,
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(dependency)
    return tuple(unique)


def _relevant_atom(atom: TechnicalAtom) -> bool:
    return atom.technical_atom_kind in _DEPENDENCY_KINDS


def _atom_in_node_scope(
    atom: TechnicalAtom, source_node: StructureNode, structure: DocumentStructure
) -> bool:
    atom_order = _source_order_from_range_id(atom.source_range_id)
    if atom_order is None:
        return False
    node_ids = {
        source_node.structure_node_id,
        *(node.structure_node_id for node in structure.descendants(source_node.structure_node_id)),
    }
    start = source_node.source_order
    end = min(
        (
            node.source_order
            for node in structure.structure_nodes
            if node.structure_node_id not in node_ids and node.source_order > start
        ),
        default=None,
    )
    return atom_order >= start and (end is None or atom_order < end)


def _atom_in_admitted_scope(
    atom: TechnicalAtom, guide: ProcedureGuide, structure: DocumentStructure
) -> bool:
    direct_step_nodes = tuple(
        node
        for step in guide.steps
        if (node := structure.node(step.source_node_id)) is not None
    )
    if any(_atom_in_node_scope(atom, node, structure) for node in direct_step_nodes):
        return True
    return _atom_in_node_scope(atom, guide.source_node, structure) and any(
        atom.source_range_id == candidate.source_range_id
        for candidate in (guide.source_node, *direct_step_nodes)
    )


def _source_order_from_range_id(source_range_id: str) -> int | None:
    match = re.search(r"-(\d+)$", source_range_id)
    return int(match.group(1)) if match is not None else None


def _entry_key(entry: LedgerEntry) -> tuple[str, str]:
    return (entry.source_range_id, _entry_text(entry))


def _entry_text(entry: LedgerEntry) -> str:
    return (entry.normalized_text or entry.source_text).strip()
