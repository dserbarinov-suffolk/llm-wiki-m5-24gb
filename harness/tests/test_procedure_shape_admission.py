from dataclasses import dataclass

from llmwiki.domain.ledger.knowledge_shapes import KnowledgeShapeCandidate
from llmwiki.domain.ledger.procedure_shape_admission import admit_procedure_shape
from llmwiki.domain.ledger.procedure_state_flow import ProcedureStateFlow


@dataclass(frozen=True)
class _Claim:
    claim_role_tags: tuple[str, ...] = ()


@dataclass(frozen=True)
class _Atom:
    technical_atom_kind: str


@dataclass(frozen=True)
class _Step:
    action_type: str
    heading_action_type: str
    source_node_id: str
    claims: tuple[_Claim, ...] = ()
    technical_atoms: tuple[_Atom, ...] = ()


def test_procedure_shape_admits_executable_state_flow() -> None:
    admission = admit_procedure_shape(
        _candidate("Artifact Creation", ("choose", "score", "record")),
        (
            _Step("choose", "choose", "choose"),
            _Step("generate", "generate", "score", technical_atoms=(_Atom("table"),)),
            _Step("record", "record", "record"),
        ),
        ProcedureStateFlow(3, 0, 1, 1),
    )

    assert admission.accepted
    assert admission.reason == "executable-state-flow"
    assert admission.step_node_ids == ("choose", "score", "record")


def test_procedure_shape_rejects_reference_collection_with_one_actionable_child() -> None:
    admission = admit_procedure_shape(
        _candidate("Variant Materials", ("silver", "magic", "mithril")),
        (
            _Step("step", "", "silver", technical_atoms=(_Atom("table"),)),
            _Step("acquire", "", "magic", technical_atoms=(_Atom("rule"),)),
            _Step("step", "", "mithril", technical_atoms=(_Atom("table"),)),
        ),
        ProcedureStateFlow(2, 0, 3, 0),
    )

    assert not admission.accepted
    assert admission.reason == "reference-or-catalog-shape"
    assert admission.downgrade_shape_kind == "section-container"


def test_procedure_shape_accepts_explicit_procedure_evidence_without_domain_words() -> None:
    admission = admit_procedure_shape(
        _candidate("Lumo", ("alpha", "beta")),
        (
            _Step("step", "", "alpha", technical_atoms=(_Atom("procedure"),)),
            _Step("step", "", "beta", technical_atoms=(_Atom("procedure"),)),
        ),
        ProcedureStateFlow(0, 2, 0, 0),
    )

    assert admission.accepted
    assert admission.reason == "explicit-procedure-evidence"


def _candidate(label: str, child_node_ids: tuple[str, ...]) -> KnowledgeShapeCandidate:
    return KnowledgeShapeCandidate(
        shape_kind="procedure",
        knowledge_shape_id=f"shape-{label}",
        label=label,
        structure_node_id="root",
        source_range_id="range-root",
        entry_ids=(),
        atom_ids=(),
        child_structure_node_ids=child_node_ids,
        evidence_roles=(),
        score=1,
    )
