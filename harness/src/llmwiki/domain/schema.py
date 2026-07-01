"""Shared Schema defaults for local LLM-Wiki."""

from __future__ import annotations

PAGE_KINDS = ("source", "entity", "concept", "procedure", "recipe", "synthesis")

PAGE_FAMILIES = (
    "source-manifest",
    "section-reference",
    "topic-concept",
    "procedure-guide",
    "recipe-pattern",
    "broad-topic",
    "entity-profile",
    "cross-source-synthesis",
)

PAGE_KIND_HEADINGS = {
    "source": "## Sources",
    "entity": "## Entities",
    "concept": "## Concepts",
    "procedure": "## Procedures",
    "recipe": "## Recipes",
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
