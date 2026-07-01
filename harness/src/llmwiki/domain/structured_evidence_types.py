"""Shared structured evidence domain types."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StructuredEvidenceArtifact:
    """A compact structured fact block lifted from an already-projected page."""

    page_id: str
    category: str
    heading: str
    excerpt: str
