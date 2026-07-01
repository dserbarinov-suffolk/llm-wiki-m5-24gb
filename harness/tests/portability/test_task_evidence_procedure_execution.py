"""Portable task-evidence and procedure-execution contracts.

These tests use synthetic source nouns. A sister implementation can copy this
file unchanged and still prove the same source-agnostic invariants.
"""

from llmwiki.domain.procedure_execution import (
    ProcedureExecution,
    ProcedureOutput,
    ProcedureStepResult,
    validate_procedure_execution,
)

from .procedure_fixtures import procedure_pack


class TestTaskEvidencePackPortability:
    def test_task_evidence_pack_selects_procedure_steps_and_linked_evidence(self) -> None:
        pack = procedure_pack()

        assert pack.procedure_id == "aether-procedure-build-device"
        assert [step.title for step in pack.steps] == [
            "Select core",
            "Calculate load",
            "Record unresolved safety check",
        ]
        assert pack.page_ids >= {"aether-core", "aether-load", "aether-safety"}

    def test_task_evidence_pack_preserves_structured_atoms_as_whole_artifacts(self) -> None:
        pack = procedure_pack()

        artifacts = {
            (artifact.category, artifact.heading): artifact
            for artifact in pack.structured_artifacts
        }
        assert any(category == "table-index" for category, _heading in artifacts)
        assert any(category == "markdown-table" for category, _heading in artifacts)
        assert any(category == "formula" for category, _heading in artifacts)
        table_artifacts = [
            artifact
            for artifact in pack.structured_artifacts
            if artifact.category == "markdown-table"
        ]
        assert len(table_artifacts) == 1
        assert "| Copper | Small |" in table_artifacts[0].excerpt
        assert "| Silver | Large |" in table_artifacts[0].excerpt

    def test_task_evidence_rendering_has_execution_and_explanation_modes(self) -> None:
        pack = procedure_pack()

        execution_text = pack.render(require_procedure_execution=True)
        explanation_text = pack.render(require_procedure_execution=False)

        assert "Call submit_procedure_execution before respond" in execution_text
        assert "Procedure explanation checklist" in explanation_text
        assert "Table 3: Core Sizes" in explanation_text


class TestProcedureExecutionPortability:
    def test_valid_execution_covers_every_required_step_with_cited_evidence(self) -> None:
        pack = procedure_pack()
        execution = ProcedureExecution(
            procedure_id=pack.procedure_id,
            assumptions=("Choose the Copper core from the source table.",),
            step_results=(
                ProcedureStepResult(
                    sequence=1,
                    title="Select core",
                    status="completed",
                    outputs=(
                        ProcedureOutput(
                            name="Core",
                            value="Copper",
                            support="evidence",
                            evidence_page_ids=("aether-core",),
                        ),
                    ),
                ),
                ProcedureStepResult(
                    sequence=2,
                    title="Calculate load",
                    status="completed",
                    outputs=(
                        ProcedureOutput(
                            name="Load total",
                            value="6",
                            support="derived",
                            evidence_page_ids=("aether-load",),
                            derivation="Use the source formula 2 x 3 = 6.",
                        ),
                    ),
                ),
                ProcedureStepResult(
                    sequence=3,
                    title="Record unresolved safety check",
                    status="unresolved",
                    note="The source gives no threshold.",
                    outputs=(
                        ProcedureOutput(
                            name="Safety threshold",
                            value="",
                            support="unresolved",
                            note="The source gives no threshold.",
                        ),
                    ),
                ),
            ),
        )

        decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

        assert decision.allowed
        assert "Copper" in execution.render()
        assert "[[aether-core]]" in execution.render()

    def test_execution_rejects_missing_required_steps(self) -> None:
        pack = procedure_pack()
        execution = ProcedureExecution(
            procedure_id=pack.procedure_id,
            step_results=(
                ProcedureStepResult(
                    sequence=1,
                    title="Select core",
                    status="completed",
                    outputs=(
                        ProcedureOutput(
                            name="Core",
                            value="Copper",
                            support="evidence",
                            evidence_page_ids=("aether-core",),
                        ),
                    ),
                ),
            ),
        )

        decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

        assert not decision.allowed
        assert "Missing ProcedureExecution step" in decision.message

    def test_execution_rejects_evidence_value_not_present_in_cited_evidence(self) -> None:
        pack = procedure_pack()
        execution = ProcedureExecution(
            procedure_id=pack.procedure_id,
            step_results=(
                ProcedureStepResult(
                    sequence=1,
                    title="Select core",
                    status="completed",
                    outputs=(
                        ProcedureOutput(
                            name="Core",
                            value="Platinum",
                            support="evidence",
                            evidence_page_ids=("aether-core",),
                        ),
                    ),
                ),
                ProcedureStepResult(
                    sequence=2,
                    title="Calculate load",
                    status="unresolved",
                    note="x",
                ),
                ProcedureStepResult(
                    sequence=3,
                    title="Record unresolved safety check",
                    status="unresolved",
                    note="x",
                ),
            ),
        )

        decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

        assert not decision.allowed
        assert "does not appear in its cited evidence text" in decision.message

    def test_execution_rejects_citations_outside_the_evidence_pack(self) -> None:
        pack = procedure_pack()
        execution = ProcedureExecution(
            procedure_id=pack.procedure_id,
            step_results=(
                ProcedureStepResult(
                    sequence=1,
                    title="Select core",
                    status="completed",
                    outputs=(
                        ProcedureOutput(
                            name="Core",
                            value="Copper",
                            support="evidence",
                            evidence_page_ids=("unknown-page",),
                        ),
                    ),
                ),
                ProcedureStepResult(
                    sequence=2,
                    title="Calculate load",
                    status="unresolved",
                    note="x",
                ),
                ProcedureStepResult(
                    sequence=3,
                    title="Record unresolved safety check",
                    status="unresolved",
                    note="x",
                ),
            ),
        )

        decision = validate_procedure_execution(execution, pack, pack.evidence_texts)

        assert not decision.allowed
        assert "outside the evidence pack" in decision.message
