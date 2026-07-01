"""The three wiki operations as forge Workflows.

Guardrail contracts (enforced by forge's StepEnforcer, not by prompting):
- ingest: must read_source and write_page before finish_ingest; write_page
  is gated on a prior read_source.
- query: must search_wiki before respond (index-first navigation).
- lint: must read_page before finish_lint (no drive-by sign-off).
"""

from __future__ import annotations

from forge.core.workflow import Workflow
from forge.tools.respond import respond_tool

from llmwiki.domain.chat_grounding import ChatEvidenceScope
from llmwiki.domain.claim_support import (
    ClaimSupportCandidate,
    ClaimSupportFinding,
    ClaimSupportVerdict,
)
from llmwiki.domain.task_evidence import TaskEvidencePack
from llmwiki.store import WikiStore
from llmwiki.workflows import prompts
from llmwiki.workflows.claim_support_tools import record_claim_support_verdict_tool
from llmwiki.workflows.procedure_execution_tools import (
    ProcedureExecutionState,
    submit_procedure_execution_tool,
)
from llmwiki.workflows.tools import (
    finish_tool,
    grounded_chat_respond_tool,
    inspect_page_tool,
    read_index_tool,
    read_page_tool,
    read_source_tool,
    search_wiki_tool,
    write_page_tool,
)


def build_ingest_workflow(store: WikiStore, today: str) -> Workflow:
    seen: set[str] = set()  # read-before-rewrite contract, per run
    tools = [
        read_source_tool(store),
        search_wiki_tool(store),
        read_page_tool(store, read_tracker=seen),
        write_page_tool(store, today, prerequisites=["read_source"], read_tracker=seen),
        finish_tool(
            "finish_ingest",
            "Finish the ingest after the wiki fully reflects the source. "
            "Report which pages were written or updated.",
        ),
    ]
    return Workflow(
        name="ingest",
        description="Integrate one raw source into the wiki.",
        tools={t.name: t for t in tools},
        required_steps=["read_source", "write_page"],
        terminal_tool="finish_ingest",
        system_prompt_template=prompts.INGEST_TEMPLATE,
    )


def build_query_workflow(store: WikiStore, today: str) -> Workflow:
    seen: set[str] = set()
    tools = [
        search_wiki_tool(store),
        read_index_tool(store),
        inspect_page_tool(store),
        read_page_tool(store, read_tracker=seen),
        write_page_tool(store, today, read_tracker=seen),
        respond_tool(),
    ]
    return Workflow(
        name="query",
        description="Answer a question from the wiki with citations.",
        tools={t.name: t for t in tools},
        required_steps=["search_wiki"],
        terminal_tool="respond",
        system_prompt_template=prompts.QUERY_TEMPLATE,
    )


def build_chat_workflow(
    store: WikiStore,
    *,
    allow_index_response: bool = True,
    require_wiki_read: bool = True,
    evidence_scope: ChatEvidenceScope | None = None,
    task_evidence_pack: TaskEvidencePack | None = None,
    require_procedure_execution: bool = False,
) -> Workflow:
    """Read-only by construction: no write tool exists in this workflow.

    Grounding is provisioned, not enforced: the orchestrator prepends the
    wiki index to a conversation's first message (pattern doc: read the
    index first, then drill into pages). A required-search step was tried
    and removed — live, it interrupted a correct index-first flow, forced
    a junk search, and the model answered from the junk (recency wins in
    a 14B).
    """
    missing_focus_reports: set[str] = set()
    seen: set[str] = set(task_evidence_pack.page_ids if task_evidence_pack is not None else ())
    procedure_execution_state = ProcedureExecutionState()
    procedure_execution_required = require_procedure_execution and task_evidence_pack is not None
    if procedure_execution_required:
        assert task_evidence_pack is not None
        tools = [
            submit_procedure_execution_tool(
                store,
                task_evidence_pack,
                read_tracker=seen,
                state=procedure_execution_state,
            )
        ]
    else:
        tools = [
            search_wiki_tool(store),
            read_index_tool(store, read_tracker=seen),
            inspect_page_tool(store, missing_focus_reports=missing_focus_reports),
            read_page_tool(store, read_tracker=seen, evidence_scope=evidence_scope),
        ]
    tools.append(
        grounded_chat_respond_tool(
            missing_focus_reports,
            seen,
            allow_index_response=allow_index_response,
            require_wiki_read=require_wiki_read,
            require_read_page_citation=True,
            procedure_execution_state=procedure_execution_state,
            require_procedure_execution=procedure_execution_required,
        )
    )
    return Workflow(
        name="chat",
        description="Converse over the wiki (read-only).",
        tools={t.name: t for t in tools},
        required_steps=["submit_procedure_execution"] if procedure_execution_required else [],
        terminal_tool="respond",
        system_prompt_template=prompts.CHAT_TEMPLATE,
    )


def build_lint_workflow(store: WikiStore, today: str) -> Workflow:
    seen: set[str] = set()
    tools = [
        search_wiki_tool(store),
        read_page_tool(store, read_tracker=seen),
        write_page_tool(store, today, read_tracker=seen),
        finish_tool(
            "finish_lint",
            "Finish the lint pass with a concise wiki health report: issues "
            "found, fixes applied, suggested next steps.",
        ),
    ]
    return Workflow(
        name="lint",
        description="Health-check the wiki and repair what page edits can repair.",
        tools={t.name: t for t in tools},
        required_steps=["read_page"],
        terminal_tool="finish_lint",
        system_prompt_template=prompts.LINT_TEMPLATE,
    )


def build_claim_support_workflow(
    store: WikiStore,
    verdicts: list[ClaimSupportVerdict],
    candidates: tuple[ClaimSupportCandidate, ...],
    deterministic_findings: tuple[ClaimSupportFinding, ...],
) -> Workflow:
    tools = [
        record_claim_support_verdict_tool(store, verdicts, candidates, deterministic_findings),
        finish_tool(
            "finish_claim_support",
            "Finish the claim-support audit with audited scope, uncertainty, "
            "and curator next steps.",
        ),
    ]
    return Workflow(
        name="claim-support",
        description="Audit selected generated wiki claims against EvidenceRecords.",
        tools={t.name: t for t in tools},
        required_steps=[],
        terminal_tool="finish_claim_support",
        system_prompt_template=prompts.CLAIM_SUPPORT_TEMPLATE,
    )
