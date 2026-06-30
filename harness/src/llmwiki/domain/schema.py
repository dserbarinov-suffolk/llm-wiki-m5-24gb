"""Shared Schema defaults for local LLM-Wiki."""

from __future__ import annotations

PAGE_KINDS = ("source", "entity", "concept", "synthesis")

PAGE_FAMILIES = ("source-manifest", "section-reference", "topic-concept", "broad-topic")

PAGE_KIND_HEADINGS = {
    "source": "## Sources",
    "entity": "## Entities",
    "concept": "## Concepts",
    "synthesis": "## Syntheses",
}

PAGE_METADATA_FIELDS = (
    "PageId",
    "PageKind",
    "PageFamily",
    "Summary",
    "Sources",
    "Updated",
)
