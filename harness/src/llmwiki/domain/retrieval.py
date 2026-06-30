"""Deterministic retrieval over compiled wiki artifacts.

The wiki is already a structured, maintained knowledge layer. Retrieval should
therefore search authored identifiers, summaries, headings, page metadata, and
links before falling back to body text repetition.
"""

from __future__ import annotations

import re
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass

from llmwiki.domain.index import IndexEntry, parse_index
from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import PageError, PageMetadata, parse_page

_WORD_RE = re.compile(r"[a-z0-9]+")
_SNIPPET_CHARS = 220
_QUERY_STOPWORDS = frozenset(
    {
        "a",
        "about",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "by",
        "can",
        "did",
        "do",
        "does",
        "for",
        "from",
        "how",
        "in",
        "is",
        "it",
        "new",
        "of",
        "on",
        "or",
        "that",
        "the",
        "this",
        "to",
        "was",
        "were",
        "what",
        "when",
        "where",
        "which",
        "who",
        "why",
        "with",
    }
)


@dataclass(frozen=True)
class RetrievalSignal:
    name: str
    score: int
    detail: str


@dataclass(frozen=True)
class RetrievalCandidate:
    page_id: str
    page_kind: str
    summary: str
    score: int
    snippet: str
    signals: tuple[RetrievalSignal, ...]
    related_page_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class WikiContextPack:
    query: str
    candidates: tuple[RetrievalCandidate, ...]
    source_scope: tuple[str, ...] = ()


def retrieve_wiki_context(
    *,
    query: str,
    index_text: str,
    page_texts: Mapping[str, str],
    limit: int = 8,
    related_limit: int = 4,
) -> WikiContextPack:
    terms = query_terms(query)
    if not terms:
        return WikiContextPack(query=query, candidates=())
    index_entries = {entry.page_id: entry for entry in parse_index(index_text)}
    links_by_page = {page_id: extract_links(text) for page_id, text in page_texts.items()}
    backlinks = _backlinks(links_by_page)
    metadata_by_page = {
        page_id: _metadata_for_page(page_id, text, index_entries.get(page_id))
        for page_id, text in page_texts.items()
    }
    source_scope = _detect_source_scope(terms, metadata_by_page)
    candidates = [
        candidate
        for page_id, text in page_texts.items()
        if _in_source_scope(metadata_by_page[page_id], source_scope)
        if (
            candidate := _candidate_for_page(
                page_id,
                text,
                terms,
                metadata_by_page[page_id],
                links_by_page,
                backlinks,
                related_limit,
            )
        )
        is not None
    ]
    candidates.sort(key=lambda candidate: (-candidate.score, candidate.page_id))
    return WikiContextPack(
        query=query,
        candidates=tuple(candidates[:limit]),
        source_scope=source_scope,
    )


def render_context_pack(pack: WikiContextPack) -> str:
    if not pack.candidates:
        return "No wiki retrieval candidates matched. Try search_wiki with alternate terms."
    lines = [
        "Wiki retrieval context:",
        "Use these page ids as starting points. Read pages before detailed answers.",
    ]
    if pack.source_scope:
        lines.append("Source scope: " + ", ".join(pack.source_scope))
    for index, candidate in enumerate(pack.candidates, start=1):
        lines.extend(
            [
                "",
                f"{index}. [[{candidate.page_id}]] "
                f"(score {candidate.score}, kind {candidate.page_kind})",
                f"   summary: {candidate.summary}",
                f"   why: {_render_signals(candidate.signals)}",
                f"   excerpt: {candidate.snippet}",
            ]
        )
        if candidate.related_page_ids:
            related = ", ".join(f"[[{page_id}]]" for page_id in candidate.related_page_ids)
            lines.append(f"   nearby: {related}")
    return "\n".join(lines)


def query_terms(query: str) -> set[str]:
    tokens = tokens_for_text(query)
    content_terms = [token for token in tokens if token not in _QUERY_STOPWORDS]
    return set(content_terms or tokens)


def tokens_for_text(text: str) -> list[str]:
    return _WORD_RE.findall(text.lower())


def token_keys_for_text(text: str) -> set[str]:
    keys: set[str] = set()
    for token in tokens_for_text(text):
        keys.update(_token_keys(token))
    return keys


def token_key_counts(text: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for token in tokens_for_text(text):
        counts.update(_token_keys(token))
    return counts


def _candidate_for_page(
    page_id: str,
    text: str,
    terms: set[str],
    metadata: PageMetadata,
    links_by_page: Mapping[str, set[str]],
    backlinks: Mapping[str, set[str]],
    related_limit: int,
) -> RetrievalCandidate | None:
    body_counts = token_key_counts(text)
    signals = tuple(
        signal
        for signal in (
            _field_signal("page-id", 40, terms, page_id),
            _field_signal("summary", 18, terms, metadata.summary),
            _field_signal("heading", 20, terms, _headings_text(text)),
            _field_signal("metadata", 14, terms, _metadata_text(metadata)),
            _body_signal(terms, body_counts),
        )
        if signal is not None
    )
    score = sum(signal.score for signal in signals)
    if score == 0:
        return None
    return RetrievalCandidate(
        page_id=page_id,
        page_kind=metadata.page_kind,
        summary=metadata.summary,
        score=score,
        snippet=_snippet(text, terms),
        signals=signals,
        related_page_ids=_related_pages(page_id, links_by_page, backlinks, related_limit),
    )


def _metadata_for_page(
    page_id: str, text: str, index_entry: IndexEntry | None
) -> PageMetadata:
    try:
        return parse_page(text).page_metadata
    except PageError:
        if index_entry is not None:
            return index_entry.page_metadata
        return PageMetadata(page_id=page_id, page_kind="concept", summary="Invalid page metadata.")


def _field_signal(
    name: str, weight: int, terms: set[str], text: str
) -> RetrievalSignal | None:
    text_keys = token_keys_for_text(text)
    matches = {term for term in terms if _token_keys(term) & text_keys}
    if not matches:
        return None
    score = weight * len(matches)
    return RetrievalSignal(name=name, score=score, detail=", ".join(sorted(matches)))


def _body_signal(terms: set[str], body_counts: Counter[str]) -> RetrievalSignal | None:
    matches = {term for term in terms if any(body_counts[key] > 0 for key in _token_keys(term))}
    if not matches:
        return None
    capped_frequency = sum(
        min(sum(body_counts[key] for key in _token_keys(term)), 4) for term in matches
    )
    score = (6 * len(matches)) + capped_frequency
    return RetrievalSignal("body", score=score, detail=", ".join(sorted(matches)))


def _metadata_text(metadata: PageMetadata) -> str:
    return " ".join(
        (
            metadata.domain,
            metadata.category_path,
            metadata.source_id,
            metadata.page_family,
            " ".join(metadata.sources),
            " ".join(metadata.tags),
            " ".join(metadata.aliases),
        )
    )


def _detect_source_scope(
    terms: set[str], metadata_by_page: Mapping[str, PageMetadata]
) -> tuple[str, ...]:
    source_scores: Counter[str] = Counter()
    for metadata in metadata_by_page.values():
        if not metadata.sources:
            continue
        identity_keys = token_keys_for_text(_source_identity_text(metadata))
        matched_terms = {
            term for term in terms if len(term) >= 3 and token_keys_for_text(term) & identity_keys
        }
        if len(matched_terms) < 2:
            continue
        for source in metadata.sources:
            source_scores[source] += len(matched_terms)
    if not source_scores:
        return ()
    best_score = max(source_scores.values())
    return tuple(
        source for source, score in sorted(source_scores.items()) if score == best_score
    )


def _source_identity_text(metadata: PageMetadata) -> str:
    return " ".join(
        (
            metadata.domain,
            metadata.category_path,
            metadata.source_id,
            " ".join(metadata.sources),
        )
    )


def _in_source_scope(metadata: PageMetadata, source_scope: tuple[str, ...]) -> bool:
    return not source_scope or bool(set(metadata.sources) & set(source_scope))


def _headings_text(text: str) -> str:
    return " ".join(line.lstrip("#").strip() for line in text.splitlines() if line.startswith("#"))


def _snippet(text: str, terms: set[str]) -> str:
    body = _page_body_text(text)
    lower = body.lower()
    first = min((pos for pos in (lower.find(term) for term in terms) if pos >= 0), default=0)
    start = max(0, first - _SNIPPET_CHARS // 4)
    return " ".join(body[start : start + _SNIPPET_CHARS].split())


def _page_body_text(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def _related_pages(
    page_id: str,
    links_by_page: Mapping[str, set[str]],
    backlinks: Mapping[str, set[str]],
    limit: int,
) -> tuple[str, ...]:
    related = sorted(
        (links_by_page.get(page_id, set()) | backlinks.get(page_id, set())) - {page_id}
    )
    return tuple(related[:limit])


def _backlinks(links_by_page: Mapping[str, set[str]]) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for source, targets in links_by_page.items():
        for target in targets:
            result.setdefault(target, set()).add(source)
    return result


def _token_keys(token: str) -> set[str]:
    keys = {token}
    if len(token) <= 4:
        return keys
    for suffix in ("ing", "ed", "es", "s", "e"):
        if token.endswith(suffix) and len(token) > len(suffix) + 3:
            keys.add(token[: -len(suffix)])
    if token.endswith("ion") and len(token) > 6:
        keys.add(token[:-3])
    return keys


def _render_signals(signals: tuple[RetrievalSignal, ...]) -> str:
    ordered = sorted(signals, key=lambda signal: (-signal.score, signal.name))
    return "; ".join(f"{signal.name} matched {signal.detail}" for signal in ordered[:4])
