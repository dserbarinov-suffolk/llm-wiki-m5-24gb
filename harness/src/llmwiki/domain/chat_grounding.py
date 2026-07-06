"""Grounding policy for conversational wiki turns."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum

from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile
from llmwiki.domain.retrieval import render_context_pack, retrieve_wiki_context

CHAT_GROUNDING_HIT_LIMIT = 12

_INDEX_LINK_RE = re.compile(r"\[\[([a-z0-9][a-z0-9-]*)\]\]")


class ChatEvidenceMode(StrEnum):
    PAGE = "page"
    CATALOG_OR_PAGE = "catalog-or-page"
    CONVERSATION = "conversation"


class ChatTaskMode(StrEnum):
    NONE = "none"
    EXPLAIN_PROCEDURE = "explain-procedure"
    EXECUTE_PROCEDURE = "execute-procedure"
    SOURCE_AUDIT = "source-audit"


@dataclass(frozen=True)
class ChatGroundingPlan:
    evidence_mode: ChatEvidenceMode
    include_index: bool
    include_search_results: bool
    task_mode: ChatTaskMode = ChatTaskMode.NONE

    @property
    def allow_index_response(self) -> bool:
        return self.evidence_mode in {
            ChatEvidenceMode.CATALOG_OR_PAGE,
            ChatEvidenceMode.CONVERSATION,
        }

    @property
    def require_wiki_read(self) -> bool:
        return self.evidence_mode is not ChatEvidenceMode.CONVERSATION


_CATALOG_TERMS = re.compile(
    r"\b("
    r"catalog|coverage|cover|covers|covered|index|pages?|sources?|"
    r"what\s+is\s+this\s+wiki\s+about|what\s+does\s+this\s+wiki"
    r")\b",
    re.IGNORECASE,
)

_CONVERSATION_FOLLOWUP = re.compile(
    r"^\s*("
    r"shorter(?:\s+please)?|"
    r"say\s+that\s+shorter|"
    r"make\s+(?:that|it)\s+shorter|"
    r"more\s+concise|"
    r"summarize\s+(?:that|it)|"
    r"rephrase\s+(?:that|it)|"
    r"rewrite\s+(?:that|it)|"
    r"clean\s+(?:that|it)\s+up|"
    r"tl;?dr|"
    r"go\s+on|"
    r"continue(?:\s+(?:that|it))?"
    r")\s*[.!?]?\s*$",
    re.IGNORECASE,
)

_PROCEDURE_EXPLANATION = re.compile(
    r"\b(how\s+do\s+i|how\s+to|steps?|procedure|workflow|process)\b",
    re.IGNORECASE,
)

_PROCEDURE_EXECUTION = re.compile(
    r"\b("
    r"actually\s+(create|make|build|generate|run|do)|"
    r"(create|make|build|generate)\s+(?:a|an|the|new)\b|"
    r"run\s+(?:the\s+)?(procedure|workflow|process)|"
    r"walk\s+through\s+(creating|making|building|generating)"
    r")\b",
    re.IGNORECASE,
)

_SOURCE_AUDIT = re.compile(
    r"\b(compare|check|verify|validate|audit|match)\b.*\b("
    r"source\s+material|source|sources|evidence|wiki\s+evidence"
    r")\b",
    re.IGNORECASE,
)


def build_chat_grounding(
    question: str,
    *,
    index_text: str,
    page_texts: Mapping[str, str],
    budget_tokens: int | None = None,
    hit_limit: int = CHAT_GROUNDING_HIT_LIMIT,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> str:
    """A compact catalog excerpt for the opening chat turn."""
    resolved_budget = budget_tokens or model_profile.chat_grounding_tokens
    pack = retrieve_wiki_context(
        query=question,
        index_text=index_text,
        page_texts=page_texts,
        limit=hit_limit,
    )
    lines = render_context_pack(pack).splitlines()
    if not pack.candidates:
        lines.append(
            "No local search hits. Bounded catalog sample follows; "
            "use search_wiki with alternate terms."
        )
        lines.extend(_fallback_index_lines(index_text, lines, resolved_budget, model_profile))
        return "\n".join(lines)
    return _trim_to_budget(lines, resolved_budget, model_profile)


def plan_chat_grounding(question: str, *, grounded: bool, has_window: bool) -> ChatGroundingPlan:
    _ = grounded
    if _is_catalog_question(question):
        return ChatGroundingPlan(
            evidence_mode=ChatEvidenceMode.CATALOG_OR_PAGE,
            include_index=True,
            include_search_results=False,
            task_mode=_task_mode(question),
        )
    if has_window and _is_conversation_followup(question):
        return ChatGroundingPlan(
            evidence_mode=ChatEvidenceMode.CONVERSATION,
            include_index=False,
            include_search_results=False,
        )
    return ChatGroundingPlan(
        evidence_mode=ChatEvidenceMode.PAGE,
        include_index=False,
        include_search_results=True,
        task_mode=_task_mode(question),
    )


def render_grounded_user_message(
    question: str,
    plan: ChatGroundingPlan,
    *,
    index_text: str = "",
    search_results: str = "",
    task_evidence_pack: str = "",
) -> str:
    if plan.include_index:
        return (
            f"The wiki's index - the catalog of every page:\n\n{index_text}\n\nQuestion: {question}"
        )
    if plan.include_search_results:
        task_guidance = _task_guidance(plan.task_mode)
        if task_evidence_pack.strip():
            return (
                "Initial wiki search results for the question. These are discovery "
                "hints only. The deterministic task evidence pack below contains "
                "already-read wiki page evidence and is the bounded evidence "
                "surface for this task. Use the pack contents directly; do not "
                "ask for read/search tools when the pack answers the question.\n\n"
                f"{search_results}\n\n"
                f"{task_guidance}"
                f"\n\n{task_evidence_pack}\n\n"
                f"Question: {question}"
            )
        return (
            "Initial wiki search results for the question. These are discovery "
            "hints, not enough evidence for a substantive answer; read a "
            "relevant page before responding.\n\n"
            f"{search_results}\n\n"
            f"{task_guidance}"
            "\n\n"
            f"Question: {question}"
        )
    return question


def _fallback_index_lines(
    index_text: str,
    existing_lines: list[str],
    budget_tokens: int,
    model_profile: ModelProfile,
) -> list[str]:
    selected: list[str] = []
    for raw_line in index_text.splitlines():
        line = " ".join(raw_line.split())
        if not _INDEX_LINK_RE.search(line):
            continue
        if _over_budget((*existing_lines, *selected, line), budget_tokens, model_profile):
            break
        selected.append(line)
    return selected


def _trim_to_budget(
    lines: list[str], budget_tokens: int, model_profile: ModelProfile
) -> str:
    selected: list[str] = []
    for line in lines:
        if _over_budget((*selected, line), budget_tokens, model_profile):
            break
        selected.append(line)
    return "\n".join(selected)


def _over_budget(
    lines: tuple[str, ...], budget_tokens: int, model_profile: ModelProfile
) -> bool:
    return model_profile.estimate_tokens("\n".join(lines)) > budget_tokens


def _is_catalog_question(question: str) -> bool:
    normalized = " ".join(question.lower().split())
    if _is_source_audit(normalized):
        return False
    return _CATALOG_TERMS.search(normalized) is not None


def _is_conversation_followup(question: str) -> bool:
    normalized = " ".join(question.lower().split())
    return _CONVERSATION_FOLLOWUP.search(normalized) is not None


def _task_mode(question: str) -> ChatTaskMode:
    normalized = " ".join(question.lower().split())
    if _is_source_audit(normalized):
        return ChatTaskMode.SOURCE_AUDIT
    asks_for_explanation = _PROCEDURE_EXPLANATION.search(normalized) is not None
    if _PROCEDURE_EXECUTION.search(normalized) and not asks_for_explanation:
        return ChatTaskMode.EXECUTE_PROCEDURE
    if asks_for_explanation:
        return ChatTaskMode.EXPLAIN_PROCEDURE
    return ChatTaskMode.NONE


def _task_guidance(task_mode: ChatTaskMode) -> str:
    if task_mode is ChatTaskMode.EXECUTE_PROCEDURE:
        return (
            "Task intent: execute the relevant procedure, not merely summarize it. "
            "If submit_procedure_execution is available, your next tool call should "
            "be submit_procedure_execution with a typed ProcedureExecution built "
            "from the deterministic task evidence pack. Include every required "
            "step; use unresolved outputs instead of searching indefinitely. "
            "Read the best procedure page and any linked evidence pages needed for "
            "specific choices, tables, formulas, or constraints. If the user did not "
            "provide choices or random results, make explicit assumptions or use "
            "source-provided worked examples; label those assumptions in the answer. "
            "Do not fill missing table or formula details from memory; when the "
            "needed rule detail is not available in the read wiki pages, mark that "
            "field unresolved instead of inventing it. Return a completed procedure "
            "output, not a future-tense plan: include one concrete result or "
            "explicit unresolved note for each procedure step. Cite the wiki pages "
            "read.\n\n"
        )
    if task_mode is ChatTaskMode.SOURCE_AUDIT:
        return (
            "Task intent: audit a previous answer against source material. Use the "
            "conversation history to identify the answer being checked, then read "
            "the procedure or evidence pages cited in that answer before responding. "
            "Report matches, mismatches, unsupported fields, and corrections with "
            "wiki page citations.\n\n"
        )
    if task_mode is ChatTaskMode.EXPLAIN_PROCEDURE:
        return (
            "Task intent: explain the relevant procedure. Prefer procedure pages "
            "when present. Use the deterministic "
            "task evidence pack when present as already-read wiki evidence. Walk "
            "through each required step, name relevant tables/formulas/worked "
            "examples, and cite the wiki pages named in the pack. Do not ask for "
            "read/search tools and do not answer with a meta-summary that the "
            "procedure exists; provide the procedure explanation now.\n\n"
        )
    return ""


def _is_source_audit(normalized_question: str) -> bool:
    return _SOURCE_AUDIT.search(normalized_question) is not None
