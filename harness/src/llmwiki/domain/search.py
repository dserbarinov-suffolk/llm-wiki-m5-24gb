"""Compatibility search facade over deterministic wiki retrieval."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from llmwiki.domain.retrieval import retrieve_wiki_context


@dataclass(frozen=True)
class SearchHit:
    page_id: str
    score: int
    snippet: str


def search_pages(pages: Mapping[str, str], query: str, limit: int = 8) -> list[SearchHit]:
    pack = retrieve_wiki_context(query=query, index_text="", page_texts=pages, limit=limit)
    return [
        SearchHit(page_id=candidate.page_id, score=candidate.score, snippet=candidate.snippet)
        for candidate in pack.candidates
    ]


def render_hits(hits: list[SearchHit]) -> str:
    if not hits:
        return "No pages matched. Try different terms, or check the index with read_page."
    lines = [f"[[{h.page_id}]] (score {h.score}): {h.snippet}" for h in hits]
    return "\n".join(lines)
