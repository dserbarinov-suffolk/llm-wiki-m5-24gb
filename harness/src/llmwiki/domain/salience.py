"""Deterministic salience: which WikiPages matter most, computed, never recalled.

Metric v2 (docs/open-questions.md #12 — each element fixes a measured
failure of v1):
- inbound `[[link]]` counts, EXCLUDING links from the hub being rebuilt —
  v1's hub fed the ranking that wrote the next hub (feedback loop);
- per-page write counts recorded during the ingest;
- term frequency of the page_id in the source text itself — the only
  signal that has read the book (iterable: 199 mentions vs a foreword
  author's 4); log-scaled so it informs without erasing the wiki signals;
- eligibility scoped to pages that cite the source — v1 ranked an
  Antikythera entity in a JavaScript book's report.

Pure data-in/data-out, mirroring `compute_findings`.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass

from llmwiki.domain.links import extract_links
from llmwiki.domain.pages import PageError, WikiPage, parse_page

# PageKinds eligible for hub key-lists; sources are the chapter list and
# syntheses are reports, neither belongs in "key entities/concepts".
_RANKED_PAGE_KINDS = ("entity", "concept")
_EXCLUDED_PAGES = frozenset({"wiki-health"})

# Top entries shown per page_kind. A constant pending evidence (design doc,
# open questions): too small hides mid-tier concepts, too large
# reintroduces model judgment.
TOP_N = 8

# Floor for the COMPUTED hub key-lists (not the report shown to the model):
# a page barely mentioned in the source cannot be "key" to it, however the
# wiki graph looks — this is what keeps foreword authors (2-4 mentions) off
# a book's key-entity line. Constant awaiting tuning across more sources.
KEY_LIST_MIN_MENTIONS = 10


@dataclass(frozen=True)
class SalienceEntry:
    page_id: str
    page_kind: str
    inbound_links: int
    ingest_writes: int
    source_mentions: int

    @property
    def score(self) -> float:
        # Wiki signals plus log-scaled source mentions: two orders of
        # magnitude in mentions (~+8) outweighs a couple of stray links;
        # single-digit mentions (~+2) doesn't.
        return self.inbound_links + self.ingest_writes + math.log2(1 + self.source_mentions)


@dataclass(frozen=True)
class SalienceReport:
    """Entries ranked by combined score (see SalienceEntry.score)."""

    entries: tuple[SalienceEntry, ...]

    def top(self, page_kind: str, n: int = TOP_N) -> tuple[SalienceEntry, ...]:
        return tuple(e for e in self.entries if e.page_kind == page_kind)[:n]

    def key_pages(self, page_kind: str, n: int = TOP_N) -> tuple[SalienceEntry, ...]:
        """Entries eligible for the computed hub key-lists (mentions floor)."""
        return tuple(
            e
            for e in self.entries
            if e.page_kind == page_kind and e.source_mentions >= KEY_LIST_MIN_MENTIONS
        )[:n]

    def render(self) -> str:
        """The prompt block. Counts are shown so the model sees *why*."""
        if not self.entries:
            return ""
        lines = [
            "Salience report — computed per page as (links: inbound wiki "
            "links, writes: times written this ingest, mentions: occurrences "
            "in the source text):"
        ]
        for page_kind, heading in (("concept", "Concepts"), ("entity", "Entities")):
            top = self.top(page_kind)
            if top:
                ranked = ", ".join(
                    f"[[{e.page_id}]] (links {e.inbound_links}, writes "
                    f"{e.ingest_writes}, mentions {e.source_mentions})"
                    for e in top
                )
                lines.append(f"{heading}: {ranked}")
        return "\n".join(lines)


# Matches key-list lines whoever wrote them — the model's variants and our
# own canonical line — so reconciliation is idempotent.
_KEY_LINE_RE = re.compile(r"^\s*\**\s*key (entities|concepts)\b", re.IGNORECASE)


def reconcile_key_lists(body: str, report: SalienceReport) -> str:
    """Replace any key-entity/key-concept lines with the computed ones.

    The key-lists are derived navigation with a single correct value, so the
    harness owns them — the same contract as index.md entries. Model-written
    variants are stripped; the canonical lines are appended from the report
    (subject to the mentions floor). Pure text-to-text; idempotent.
    """
    lines = [line for line in body.splitlines() if not _KEY_LINE_RE.match(line)]
    while lines and not lines[-1].strip():
        lines.pop()
    for page_kind, label in (("concept", "Key concepts"), ("entity", "Key entities")):
        page_ids = [e.page_id for e in report.key_pages(page_kind)]
        if page_ids:
            rendered = ", ".join(f"[[{page_id}]]" for page_id in page_ids)
            # Reader-facing label only — how the list is computed is harness
            # plumbing and stays out of the wiki layer.
            lines.extend(["", f"**{label}:** {rendered}"])
    return "\n".join(lines)


def _mention_count(page_id: str, source_text_lower: str) -> int:
    """Occurrences of the page_id in the source, word-boundary matched.

    The slug becomes a space-joined phrase; a trailing plural 's' on the
    last word is optional so `linked-lists` matches "linked list". Crude by
    design — the separations that matter span orders of magnitude.
    """
    if not source_text_lower:
        return 0
    words = [re.escape(w) for w in page_id.split("-") if w]
    if not words:
        return 0
    phrase = r"[\s-]+".join(words)
    if phrase.endswith("s"):
        phrase += "?"
    return len(re.findall(rf"\b{phrase}\b", source_text_lower))


def _cites_source(page: WikiPage, source_basename: str) -> bool:
    return any(source_basename in entry for entry in page.page_metadata.sources)


def compute_salience(
    page_texts: Mapping[str, str],
    write_counts: Mapping[str, int] | None = None,
    *,
    source_text: str = "",
    scope_source: str = "",
    exclude_inbound_from: frozenset[str] = frozenset(),
) -> SalienceReport:
    """Rank entity/concept pages by how load-bearing the evidence says they are.

    *scope_source* (a SourceLocator or filename) restricts eligibility to pages
    citing it; empty means wiki-global (lint). *exclude_inbound_from* names
    pages whose outbound links must not count — pass the hub being rebuilt.
    """
    writes = write_counts or {}
    page_ids = set(page_texts)
    source_basename = scope_source.rsplit("/", 1)[-1]
    text_lower = source_text.lower()

    inbound: Counter[str] = Counter()
    parsed: dict[str, WikiPage] = {}
    for page_id, text in page_texts.items():
        if page_id not in exclude_inbound_from:
            for target in extract_links(text) & page_ids - {page_id}:
                inbound[target] += 1
        try:
            parsed[page_id] = parse_page(text)
        except PageError:
            continue  # unparseable page: counted as a linker, never ranked

    def eligible(page_id: str) -> bool:
        page = parsed.get(page_id)
        if page is None or page.page_kind not in _RANKED_PAGE_KINDS:
            return False
        if page_id in _EXCLUDED_PAGES:
            return False
        return not source_basename or _cites_source(page, source_basename)

    entries = sorted(
        (
            SalienceEntry(
                page_id=page_id,
                page_kind=parsed[page_id].page_kind,
                inbound_links=inbound[page_id],
                ingest_writes=writes.get(page_id, 0),
                source_mentions=_mention_count(page_id, text_lower),
            )
            for page_id in page_ids
            if eligible(page_id)
        ),
        key=lambda e: (-e.score, -e.inbound_links, e.page_id),
    )
    return SalienceReport(entries=tuple(entries))
