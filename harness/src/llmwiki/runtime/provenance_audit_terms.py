"""Reusable text heuristics for provenance auditing."""

from __future__ import annotations

import re

WORD_RE = re.compile(r"[A-Za-z0-9]+")
ROOT_CAUSES = {
    "missing-ledger-range": "projection references a source range absent from source artifacts",
    "structure-only-range": "projection references a source segment with no claim or atom",
    "context-pointer-projected": "projection included an unresolved context pointer",
    "fragmentary-statement": "source segmentation split prose across source ranges",
    "topic-support-gap": "topic planning attached evidence without local lexical support",
    "technical-atom-topic-gap": "technical atom matching attached an atom without topic support",
    "range-order-outlier": "projection mixed distant source-order ranges on one page",
}
_STOPWORDS = frozenset(
    {
        "about",
        "after",
        "also",
        "and",
        "any",
        "are",
        "because",
        "but",
        "can",
        "for",
        "from",
        "has",
        "have",
        "into",
        "its",
        "may",
        "not",
        "one",
        "only",
        "section",
        "source",
        "that",
        "the",
        "their",
        "them",
        "there",
        "these",
        "this",
        "those",
        "when",
        "which",
        "with",
        "you",
    }
)


def topic_terms(text: str) -> frozenset[str]:
    terms: list[str] = []
    for raw in WORD_RE.findall(str(text).lower()[:4_000]):
        if len(raw) < 3 or raw.isdigit():
            continue
        term = singular(raw)
        if term not in _STOPWORDS:
            terms.append(term)
    return frozenset(terms)


def singular(token: str) -> str:
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith(("ches", "shes")) and len(token) > 5:
        return token[:-2]
    if token.endswith("s") and not token.endswith("ss") and len(token) > 4:
        return token[:-1]
    return token


def fragmentary(text: str) -> bool:
    stripped = " ".join(text.split())
    if not stripped:
        return False
    lowered = stripped.lower()
    return bool(
        stripped[0].islower()
        or lowered.startswith(("and ", "or ", "but ", "because ", "believe in "))
        or lowered.endswith((",", " and", " or", " but"))
    )


def clean_excerpt(text: str) -> str:
    return " ".join(WORD_RE.findall(text))[:220]
