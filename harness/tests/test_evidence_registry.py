"""Tests for generated source evidence registry objects."""

from llmwiki.domain.evidence_registry import (
    SourceRange,
    build_evidence_registry,
    source_text_from_text,
)
from llmwiki.domain.evidence_registry_io import registry_from_json, registry_to_json
from llmwiki.domain.objects import ExtractedUnit, RawSource, SourceBundle
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE
from llmwiki.domain.planning import build_markdown_page_plan, build_page_plan

TODAY = "2026-06-23"


def test_source_evidence_registry_builds_stable_records_for_markdown() -> None:
    raw_source = RawSource.from_locator("antikythera-mechanism.md")
    source_text = "# Device\n\nThe device may predict eclipses."
    plan = build_markdown_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text=source_text,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )
    source = source_text_from_text(raw_source.source_locator, source_text)

    first = build_evidence_registry(plan, (source,))
    second = build_evidence_registry(plan, (source,))

    assert first == second
    assert first.source_texts[0].source_text_kind == "markdown"
    assert first.source_texts[0].line_count == 3
    assert first.source_ranges
    assert first.evidence_records
    assert first.evidence_records[0].source_claim_id.startswith("source-claim-")
    assert first.evidence_banks[0].evidence_ids == (first.evidence_records[0].evidence_id,)
    assert registry_from_json(registry_to_json(first)) == first


def test_source_range_contains_matching_source_span() -> None:
    source_range = SourceRange(
        source_range_id="source-range-book-functions",
        page_id="book-functions",
        source_locator="book.pdf",
        page_range=(1, 8),
        line_range=(4, 20),
        heading_path="Functions",
    )

    assert source_range.contains_source_span(source_path="raw/book.pdf", page_range=(2, 3))
    assert source_range.contains_source_span(source_path="raw/book.pdf", line_range=(5, 6))
    assert not source_range.contains_source_span(source_path="raw/book.pdf", page_range=(9, 10))
    assert not source_range.contains_source_span(source_path="raw/other.pdf", page_range=(2, 3))


def test_page_plan_registry_tracks_pdf_source_ranges() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            unit_id="unit-0001",
            raw_source=raw_source,
            locator="p.1-2",
            heading_path="Functions",
            text="Functions are values.",
            extraction_status="ok",
            source_hash="hash-book",
        ),
        ExtractedUnit(
            unit_id="unit-0002",
            raw_source=raw_source,
            locator="p.3-4",
            heading_path="Closures",
            text="Closures capture scope.",
            extraction_status="ok",
            source_hash="hash-book",
        ),
    )
    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today=TODAY,
    )
    registry = build_evidence_registry(
        plan,
        (
            source_text_from_text(
                "book.pdf",
                "Functions are values.\nClosures capture scope.",
                "pdf-cache",
            ),
        ),
    )

    assert {source_range.page_range for source_range in registry.source_ranges} >= {
        (1, 2),
        (3, 4),
    }
    assert all(record.source_range_id for record in registry.evidence_records)
