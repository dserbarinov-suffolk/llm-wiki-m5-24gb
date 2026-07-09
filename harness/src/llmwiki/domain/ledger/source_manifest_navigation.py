"""Source-manifest helpers retained by KoteKomi page projection."""

from __future__ import annotations


def source_review_section(page_body: str) -> str:
    marker = "## Source review"
    start = page_body.find(marker)
    if start < 0:
        return ""
    return page_body[start:].strip()
