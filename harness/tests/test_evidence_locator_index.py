"""Tests for stable evidence locator domain objects."""

from __future__ import annotations

from dataclasses import replace

from llmwiki.domain.evidence_locator_builder import (
    build_evidence_locator_index,
    validate_evidence_locator_index,
)
from llmwiki.domain.evidence_locator_index import EvidenceLocator, EvidenceLocatorIndex
from llmwiki.domain.evidence_locator_index_io import (
    evidence_locator_index_from_json,
    evidence_locator_index_to_json,
)
from llmwiki.domain.evidence_registry import build_evidence_registry, source_text_from_text
from llmwiki.domain.objects import (
    ExtractedUnit,
    PagePlan,
    PlannedPageWrite,
    RawSource,
    SourceBundle,
)
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE, PageMetadata
from llmwiki.domain.planning import build_page_plan

TODAY = "2026-06-23"


def test_evidence_record_identity_survives_page_id_changes() -> None:
    claim = "The mechanism predicts solar eclipses."
    source = source_text_from_text("article.md", claim)
    first = build_evidence_registry(_plan("alpha", claim), (source,))
    second = build_evidence_registry(_with_page_prefix(_plan("alpha", claim), "moved"), (source,))

    assert first.source_ranges[0].source_range_id != second.source_ranges[0].source_range_id
    assert first.evidence_records[0].evidence_id == second.evidence_records[0].evidence_id
    assert (
        first.evidence_records[0].evidence_identity_id
        == second.evidence_records[0].evidence_identity_id
    )


def test_evidence_record_identity_changes_when_canonical_excerpt_changes() -> None:
    first_claim = "The mechanism predicts solar eclipses."
    second_claim = "The mechanism predicts lunar eclipses."
    source = source_text_from_text("article.md", f"{first_claim}\n{second_claim}")
    first = build_evidence_registry(_plan("alpha", first_claim), (source,))
    second = build_evidence_registry(_plan("alpha", second_claim), (source,))

    assert first.evidence_records[0].evidence_id != second.evidence_records[0].evidence_id


def test_evidence_locator_index_validates_normalized_line_ranges() -> None:
    source = source_text_from_text("article.md", "one\ntwo\nthree\nfour\nfive")
    valid = EvidenceLocator.from_excerpt(
        source_locator="article.md",
        source_hash=source.source_hash,
        locator_text="normalized:L2-L3",
        locator_kind="normalized-line",
        range_start=2,
        range_end=3,
        excerpt="two three",
    )
    invalid = EvidenceLocator.from_excerpt(
        source_locator="article.md",
        source_hash=source.source_hash,
        locator_text="normalized:L6",
        locator_kind="normalized-line",
        range_start=6,
        range_end=6,
        excerpt="missing",
    )

    assert validate_evidence_locator_index(
        EvidenceLocatorIndex.from_locators("article.md", source.source_hash, (valid,)),
        (source,),
    ) == ()
    findings = validate_evidence_locator_index(
        EvidenceLocatorIndex.from_locators("article.md", source.source_hash, (invalid,)),
        (source,),
    )
    assert [finding.category for finding in findings] == ["invalid-range"]


def test_evidence_locator_index_validates_page_ranges() -> None:
    source = source_text_from_text("book.pdf", "page text", "pdf-cache")
    invalid = EvidenceLocator.from_excerpt(
        source_locator="book.pdf",
        source_hash=source.source_hash,
        locator_text="p.8-2",
        locator_kind="page-range",
        range_start=8,
        range_end=2,
        excerpt="page text",
    )

    findings = validate_evidence_locator_index(
        EvidenceLocatorIndex.from_locators("book.pdf", source.source_hash, (invalid,)),
        (source,),
    )

    assert [finding.category for finding in findings] == ["invalid-range"]


def test_evidence_locator_index_round_trips_json() -> None:
    claim = "The mechanism predicts solar eclipses."
    source = source_text_from_text("article.md", claim)
    registry = build_evidence_registry(_plan("alpha", claim), (source,))
    index = build_evidence_locator_index(registry)

    assert evidence_locator_index_from_json(evidence_locator_index_to_json(index)) == index


def test_builder_prefers_page_range_for_page_scoped_records() -> None:
    claim = "The mechanism predicts solar eclipses."
    source = source_text_from_text("article.md", claim)
    registry = build_evidence_registry(_plan("alpha", claim), (source,))

    index = build_evidence_locator_index(registry)

    assert {locator.locator_text for locator in index.locators} == {"p.1"}
    assert {locator.locator_kind for locator in index.locators} == {"page-range"}


def _plan(prefix: str, unit_text: str) -> PagePlan:
    raw_source = RawSource.from_locator("article.md")
    unit = ExtractedUnit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.1",
        heading_path=prefix,
        text=unit_text,
        extraction_status="ok",
        source_hash="hash-article",
    )
    return build_page_plan(
        plan_id=f"plan-{prefix}",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )


def _with_page_prefix(plan: PagePlan, prefix: str) -> PagePlan:
    writes: list[PlannedPageWrite] = []
    for index, write in enumerate(plan.planned_writes, start=1):
        metadata = PageMetadata(
            page_id=f"{prefix}-{index}",
            page_kind=write.page_metadata.page_kind,
            summary=write.page_metadata.summary,
            sources=write.page_metadata.sources,
            updated=write.page_metadata.updated,
        )
        writes.append(replace(write, page_metadata=metadata))
    return replace(plan, planned_writes=tuple(writes))
