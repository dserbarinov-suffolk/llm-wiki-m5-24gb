"""index.md as data: parse and upsert entries. Format defined by Schema.

Entry format: `- [[page_id]] — one-line summary`, grouped under one
heading per page_kind. All transformations are pure
text-to-text so the file stays human-readable and diff-friendly.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.pages import PageMetadata
from llmwiki.domain.schema import PAGE_KIND_HEADINGS

_ENTRY_RE = re.compile(r"^- \[\[(?P<page_id>[a-z0-9-]+)\]\] — (?P<summary>.*)$")


@dataclass(frozen=True)
class IndexEntry:
    page_metadata: PageMetadata

    @property
    def page_id(self) -> str:
        return self.page_metadata.page_id

    @property
    def page_kind(self) -> str:
        return self.page_metadata.page_kind

    @property
    def summary(self) -> str:
        return self.page_metadata.summary


def _entry_line(page_metadata: PageMetadata) -> str:
    return f"- [[{page_metadata.page_id}]] — {page_metadata.summary}"


def parse_index(text: str) -> list[IndexEntry]:
    """Extract all entries with the page_kind they appear under."""
    heading_to_page_kind = {h: c for c, h in PAGE_KIND_HEADINGS.items()}
    entries: list[IndexEntry] = []
    page_kind: str | None = None
    for line in text.splitlines():
        if line.strip() in heading_to_page_kind:
            page_kind = heading_to_page_kind[line.strip()]
            continue
        match = _ENTRY_RE.match(line.strip())
        if match and page_kind is not None:
            metadata = PageMetadata(
                page_id=match["page_id"],
                page_kind=page_kind,
                summary=match["summary"],
            )
            entries.append(IndexEntry(page_metadata=metadata))
    return entries


def index_page_ids(text: str) -> set[str]:
    return {entry.page_id for entry in parse_index(text)}


def upsert_index_entry(text: str, page_metadata: PageMetadata) -> str:
    """Insert or replace the entry for PageMetadata, keeping its page_kind block sorted.

    A page that changed page_kind is removed from its old block first, so a
    page appears in exactly one place.
    """
    heading = PAGE_KIND_HEADINGS[page_metadata.page_kind]
    page_id = page_metadata.page_id
    lines = []
    for line in text.splitlines():
        match = _ENTRY_RE.match(line.strip())
        if match and match["page_id"] == page_id:
            continue
        lines.append(line)
    if heading not in [line.strip() for line in lines]:
        raise ValueError(f"index.md is missing the {heading!r} heading; restore it from Schema.")

    result: list[str] = []
    inserted = False
    in_block = False
    for line in lines:
        stripped = line.strip()
        if stripped == heading:
            in_block = True
            result.append(line)
            continue
        if in_block and not inserted:
            existing = _ENTRY_RE.match(stripped)
            block_ended = stripped.startswith("## ")
            if existing and existing["page_id"] > page_id:
                result.append(_entry_line(page_metadata))
                inserted = True
            elif block_ended:
                # Insert before the next heading, after any trailing blanks.
                while result and result[-1].strip() == "":
                    result.pop()
                result.extend([_entry_line(page_metadata), ""])
                inserted = True
                in_block = False
        result.append(line)
    if not inserted:
        while result and result[-1].strip() == "":
            result.pop()
        result.append(_entry_line(page_metadata))
    return "\n".join(result) + "\n"
