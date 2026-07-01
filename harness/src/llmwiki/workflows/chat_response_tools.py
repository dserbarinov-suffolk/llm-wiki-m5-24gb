"""Forge adapters for chat response validation."""

from __future__ import annotations

from forge.core.workflow import ToolDef, ToolSpec
from forge.tools.respond import RESPOND_DESCRIPTION, RespondParams

from llmwiki.domain.chat_response_gate import (
    ChatResponseEvidenceState,
    ChatResponseGateConfig,
    decide_chat_response,
)
from llmwiki.store import WikiStoreError
from llmwiki.workflows.procedure_execution_tools import ProcedureExecutionState


def grounded_chat_respond_tool(
    missing_focus_reports: set[str],
    read_tracker: set[str] | None = None,
    *,
    allow_index_response: bool = True,
    require_wiki_read: bool = True,
    require_read_page_citation: bool = False,
    procedure_execution_state: ProcedureExecutionState | None = None,
    require_procedure_execution: bool = False,
) -> ToolDef:
    def _respond(**kwargs: object) -> str:
        params = RespondParams(**kwargs)  # type: ignore[arg-type]
        decision = decide_chat_response(
            params.message,
            config=ChatResponseGateConfig(
                allow_index_response=allow_index_response,
                require_wiki_read=require_wiki_read,
                require_read_page_citation=require_read_page_citation,
                require_procedure_execution=require_procedure_execution,
            ),
            evidence=_evidence_state(
                missing_focus_reports,
                read_tracker,
                procedure_execution_state,
            ),
        )
        if not decision.allowed:
            raise WikiStoreError(decision.message)
        return params.message

    return ToolDef(
        spec=ToolSpec(
            name="respond",
            description=RESPOND_DESCRIPTION,
            parameters=RespondParams,
        ),
        callable=_respond,
    )


def _evidence_state(
    missing_focus_reports: set[str],
    read_tracker: set[str] | None,
    procedure_execution_state: ProcedureExecutionState | None,
) -> ChatResponseEvidenceState:
    if read_tracker is None:
        read_page_ids = None
        index_was_read = False
    else:
        read_page_ids = frozenset(read_tracker - {"index.md"})
        index_was_read = "index.md" in read_tracker
    procedure_execution_satisfied = (
        procedure_execution_state is not None and procedure_execution_state.has_valid_execution
    )
    return ChatResponseEvidenceState(
        missing_focus_reports=frozenset(missing_focus_reports),
        read_page_ids=read_page_ids,
        index_was_read=index_was_read,
        procedure_execution_satisfied=procedure_execution_satisfied,
    )
