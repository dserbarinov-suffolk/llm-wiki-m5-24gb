"""Projection coverage objects.

``ProjectionCoverage`` is the machine-checkable authority for how a page body
maps back to its source support: every projection coverage unit (generated
page claim, rendered technical atom block, source review item, disposition
count, cross-source relationship) gets one entry that records the page text
range it covers and the internal support ids it resolves to. Internal support
ids live here, never in the visible page body.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PageTextRange:
    start: int
    end: int


@dataclass(frozen=True)
class ProjectionCoverageEntry:
    projection_coverage_entry_id: str
    projection_coverage_unit_kind: str
    page_text_range: PageTextRange
    selected_ledger_entry_ids: tuple[str, ...] = ()
    technical_atom_id: str = ""
    ledger_entry_id: str = ""
    extracted_unit_disposition: str = ""
    cross_source_relationship_id: str = ""


@dataclass(frozen=True)
class ProjectionCoverage:
    entries: tuple[ProjectionCoverageEntry, ...]


@dataclass(frozen=True)
class RenderedPage:
    page_body: str
    page_body_hash: str
    coverage: ProjectionCoverage
