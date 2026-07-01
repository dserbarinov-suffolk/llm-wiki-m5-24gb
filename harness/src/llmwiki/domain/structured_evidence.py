"""Universal structured evidence extraction for task packs."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence

from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.structured_evidence_blocks import extract_structured_artifacts
from llmwiki.domain.structured_evidence_types import StructuredEvidenceArtifact

__all__ = ["StructuredEvidenceArtifact", "select_structured_evidence_artifacts"]

_MAX_ARTIFACT_CHARS = 900
_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9'~-]{2,}")
_TABLE_LABEL_RE = re.compile(
    r"\bTable\s+[A-Za-z0-9][A-Za-z0-9.-]*(?::\s*[^,.\n_`>()]+)?",
)
_STOP_TERMS = frozenset(
    {
        "about",
        "also",
        "and",
        "are",
        "can",
        "from",
        "has",
        "have",
        "into",
        "must",
        "not",
        "section",
        "source",
        "step",
        "that",
        "the",
        "their",
        "then",
        "this",
        "with",
        "you",
    }
)


def select_structured_evidence_artifacts(
    pages: Mapping[str, str],
    page_ids: Sequence[str],
    focus_texts: Sequence[str],
    *,
    max_artifacts: int = 24,
    max_total_chars: int = 12_000,
) -> tuple[StructuredEvidenceArtifact, ...]:
    """Select table, code, formula, and example artifacts from candidate pages."""

    focus_terms = _terms("\n".join(focus_texts))
    scored: list[tuple[int, int, StructuredEvidenceArtifact]] = []
    for page_order, page_id in enumerate(page_ids):
        text = pages.get(page_id)
        if text is None:
            continue
        try:
            page = parse_page(text)
        except PageError:
            continue
        if page.page_metadata.page_family == "source-manifest":
            continue
        for artifact in extract_structured_artifacts(page.page_id, page.page_body):
            scored.append((_score(artifact, focus_terms, page_order), page_order, artifact))
    return _select_artifacts(scored, max_artifacts=max_artifacts, max_total_chars=max_total_chars)


def _select_artifacts(
    scored: Sequence[tuple[int, int, StructuredEvidenceArtifact]],
    *,
    max_artifacts: int,
    max_total_chars: int,
) -> tuple[StructuredEvidenceArtifact, ...]:
    selected: list[StructuredEvidenceArtifact] = []
    seen: set[str] = set()
    total = 0
    index_artifact = _table_index_artifact(scored)
    if index_artifact is not None:
        selected.append(index_artifact)
        seen.add(_fingerprint(index_artifact))
        total += len(index_artifact.excerpt)
    for _score_value, _page_order, artifact in sorted(scored, key=_sort_key):
        if len(selected) >= max_artifacts:
            break
        key = _fingerprint(artifact)
        if key in seen:
            continue
        excerpt = _clip(artifact.excerpt, _MAX_ARTIFACT_CHARS)
        if total + len(excerpt) > max_total_chars:
            break
        seen.add(key)
        total += len(excerpt)
        selected.append(
            StructuredEvidenceArtifact(
                page_id=artifact.page_id,
                category=artifact.category,
                heading=artifact.heading,
                excerpt=excerpt,
            )
        )
    return tuple(selected)


def _table_index_artifact(
    scored: Sequence[tuple[int, int, StructuredEvidenceArtifact]],
) -> StructuredEvidenceArtifact | None:
    entries: list[str] = []
    seen: set[str] = set()
    page_id = ""
    for _score_value, _page_order, artifact in sorted(scored, key=_sort_key):
        for label in _table_labels(artifact.excerpt):
            key = label.lower()
            if key in seen:
                continue
            seen.add(key)
            page_id = page_id or artifact.page_id
            entries.append(f"- {label} ([[{artifact.page_id}]])")
            if len(entries) >= 28:
                break
        if len(entries) >= 28:
            break
    if not entries:
        return None
    return StructuredEvidenceArtifact(
        page_id=page_id,
        category="table-index",
        heading="Exact table references",
        excerpt="Exact table references found in candidate evidence:\n" + "\n".join(entries),
    )


def _table_labels(text: str) -> tuple[str, ...]:
    labels: list[str] = []
    for match in _TABLE_LABEL_RE.finditer(text):
        label = " ".join(match.group(0).split()).rstrip(" ,.;:")
        label = re.split(r"\s+(?:shows|is|must|does|determine|or|and)\b", label, maxsplit=1)[0]
        if label.lower() != "table":
            labels.append(label)
    return tuple(labels)


def _score(
    artifact: StructuredEvidenceArtifact,
    focus_terms: frozenset[str],
    page_order: int,
) -> int:
    artifact_terms = _terms(f"{artifact.heading}\n{artifact.excerpt}")
    overlap = len(artifact_terms & focus_terms)
    category_bonus = {
        "table-index": 30,
        "raw-table-text": 24,
        "markdown-table": 22,
        "code-block": 20,
        "table": 18,
        "formula": 16,
        "worked-example": 12,
    }.get(artifact.category, 0)
    return overlap * 5 + category_bonus - page_order


def _sort_key(item: tuple[int, int, StructuredEvidenceArtifact]) -> tuple[int, int, str, str]:
    score, page_order, artifact = item
    return (-score, page_order, artifact.page_id, artifact.heading)


def _terms(text: str) -> frozenset[str]:
    return frozenset(
        token.lower()
        for token in _TOKEN_RE.findall(text)
        if token.lower() not in _STOP_TERMS
    )


def _fingerprint(artifact: StructuredEvidenceArtifact) -> str:
    return "\n".join(
        (
            artifact.page_id,
            artifact.category,
            artifact.heading,
            " ".join(artifact.excerpt.split()).lower(),
        )
    )


def _clip(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    clipped = text[:max_chars].rstrip()
    return f"{clipped}\n\n[TRUNCATED: structured evidence artifact]"
