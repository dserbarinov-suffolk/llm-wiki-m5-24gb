"""Bounded first-turn grounding for read-only wiki chat."""

from __future__ import annotations

import re
from collections.abc import Mapping

from llmwiki.domain.chatwindow import estimate_tokens
from llmwiki.domain.retrieval import render_context_pack, retrieve_wiki_context

CHAT_GROUNDING_TOKEN_BUDGET = 3500
CHAT_GROUNDING_HIT_LIMIT = 12

_INDEX_LINK_RE = re.compile(r"\[\[([a-z0-9][a-z0-9-]*)\]\]")


def build_chat_grounding(
    question: str,
    *,
    index_text: str,
    page_texts: Mapping[str, str],
    budget_tokens: int = CHAT_GROUNDING_TOKEN_BUDGET,
    hit_limit: int = CHAT_GROUNDING_HIT_LIMIT,
) -> str:
    """A compact catalog excerpt for the opening chat turn.

    The full index is the design's navigation source, but it can outgrow the
    local model context. This keeps index-first behavior by sending relevant
    index lines plus content snippets, then asking the model to drill into
    pages with tools.
    """
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
        lines.extend(_fallback_index_lines(index_text, lines, budget_tokens))
        return "\n".join(lines)
    return _trim_to_budget(lines, budget_tokens)


def _fallback_index_lines(
    index_text: str, existing_lines: list[str], budget_tokens: int
) -> list[str]:
    selected: list[str] = []
    for raw_line in index_text.splitlines():
        line = " ".join(raw_line.split())
        if not _INDEX_LINK_RE.search(line):
            continue
        if _over_budget((*existing_lines, *selected, line), budget_tokens):
            break
        selected.append(line)
    return selected


def _trim_to_budget(lines: list[str], budget_tokens: int) -> str:
    selected: list[str] = []
    for line in lines:
        if _over_budget((*selected, line), budget_tokens):
            break
        selected.append(line)
    return "\n".join(selected)


def _over_budget(lines: tuple[str, ...], budget_tokens: int) -> bool:
    return estimate_tokens("\n".join(lines)) > budget_tokens
