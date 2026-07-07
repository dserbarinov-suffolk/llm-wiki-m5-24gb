"""Admission gate for executable procedure shapes.

The invariant is source-neutral: a procedure page must represent an executable
state flow, not a catalog or reference section that happens to have ordered
children and technical records.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Protocol

from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCandidate
from llmwiki.domain.ledger.procedure_language import action_type, has_task_noun
from llmwiki.domain.ledger.procedure_state_flow import ProcedureStateFlow

_EXECUTABLE_ACTION_TYPES = frozenset(
    {"choose", "generate", "calculate", "allocate", "acquire", "record", "validate", "finalize"}
)
_DERIVATION_ATOM_KINDS = frozenset({"formula", "procedure"})


class ProcedureStepLike(Protocol):
    @property
    def action_type(self) -> str: ...

    @property
    def heading_action_type(self) -> str: ...

    @property
    def source_node_id(self) -> str: ...

    @property
    def claims(self) -> tuple[LedgerEntry, ...]: ...

    @property
    def technical_atoms(self) -> tuple[TechnicalAtom, ...]: ...


@dataclass(frozen=True)
class ProcedureShapeAdmission:
    accepted: bool
    reason: str
    step_node_ids: tuple[str, ...]
    rejected_child_node_ids: tuple[str, ...]
    downgrade_shape_kind: str = ""
    executable_step_count: int = 0
    explicit_procedure_step_count: int = 0


def admit_procedure_shape(
    candidate: KnowledgeShapeCandidate,
    steps: Sequence[ProcedureStepLike],
    state_flow: ProcedureStateFlow,
) -> ProcedureShapeAdmission:
    step_node_ids = tuple(
        getattr(step, "source_node_id", "") for step in steps if getattr(step, "source_node_id", "")
    )
    rejected_child_ids = tuple(
        node_id for node_id in candidate.child_structure_node_ids if node_id not in step_node_ids
    )
    if len(steps) < 2:
        return _reject("too-few-steps", step_node_ids, rejected_child_ids, "section-container")
    if not state_flow.has_state_flow:
        return _reject("no-state-flow", step_node_ids, rejected_child_ids, "section-container")
    executable_count = sum(1 for step in steps if _step_has_executable_action(step))
    explicit_count = sum(1 for step in steps if _step_has_explicit_procedure_evidence(step))
    if _has_compact_derived_state_flow(steps, state_flow, executable_count):
        return ProcedureShapeAdmission(
            True,
            "derived-state-flow",
            step_node_ids,
            rejected_child_ids,
            executable_step_count=executable_count,
            explicit_procedure_step_count=explicit_count,
        )
    if executable_count >= 2 and (
        _has_execution_anchor(candidate, state_flow, explicit_count)
        or len(_executable_action_types(steps)) >= 2
    ):
        return ProcedureShapeAdmission(
            True,
            "executable-state-flow",
            step_node_ids,
            rejected_child_ids,
            executable_step_count=executable_count,
            explicit_procedure_step_count=explicit_count,
        )
    if explicit_count >= 2:
        return ProcedureShapeAdmission(
            True,
            "explicit-procedure-evidence",
            step_node_ids,
            rejected_child_ids,
            executable_step_count=executable_count,
            explicit_procedure_step_count=explicit_count,
        )
    return _reject(
        "reference-or-catalog-shape",
        step_node_ids,
        rejected_child_ids,
        "section-container",
        executable_count,
        explicit_count,
    )


def _has_execution_anchor(
    candidate: KnowledgeShapeCandidate, state_flow: ProcedureStateFlow, explicit_count: int
) -> bool:
    return bool(
        has_task_noun(candidate.label)
        or action_type(candidate.label) in _EXECUTABLE_ACTION_TYPES
        or explicit_count > 0
        or state_flow.prior_output_dependency_count > 0
        or state_flow.technical_output_step_count >= 2
    )


def _step_has_executable_action(step: ProcedureStepLike) -> bool:
    return step.action_type in _EXECUTABLE_ACTION_TYPES or (
        step.heading_action_type in _EXECUTABLE_ACTION_TYPES
    )


def _executable_action_types(steps: Sequence[ProcedureStepLike]) -> frozenset[str]:
    actions: set[str] = set()
    for step in steps:
        if step.action_type in _EXECUTABLE_ACTION_TYPES:
            actions.add(step.action_type)
        if step.heading_action_type in _EXECUTABLE_ACTION_TYPES:
            actions.add(step.heading_action_type)
    return frozenset(actions)


def _step_has_explicit_procedure_evidence(step: ProcedureStepLike) -> bool:
    return any(atom.technical_atom_kind == "procedure" for atom in step.technical_atoms)


def _has_compact_derived_state_flow(
    steps: Sequence[ProcedureStepLike],
    state_flow: ProcedureStateFlow,
    executable_count: int,
) -> bool:
    return bool(
        executable_count == 0
        and len(steps) <= 4
        and state_flow.prior_output_dependency_count > 0
        and state_flow.technical_output_step_count >= 2
        and sum(1 for step in steps if _step_has_derivation_atom(step)) >= 2
    )


def _step_has_derivation_atom(step: ProcedureStepLike) -> bool:
    return any(atom.technical_atom_kind in _DERIVATION_ATOM_KINDS for atom in step.technical_atoms)


def _reject(
    reason: str,
    step_node_ids: tuple[str, ...],
    rejected_child_ids: tuple[str, ...],
    downgrade_shape_kind: str,
    executable_count: int = 0,
    explicit_count: int = 0,
) -> ProcedureShapeAdmission:
    return ProcedureShapeAdmission(
        False,
        reason,
        step_node_ids,
        rejected_child_ids,
        downgrade_shape_kind,
        executable_count,
        explicit_count,
    )
