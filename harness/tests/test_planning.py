"""Tests for global ingest planning."""

from llmwiki.domain.objects import ExtractedUnit, RawSource, SourceBundle
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE, WikiPage, render_page
from llmwiki.domain.planning import build_page_plan


def test_existing_source_section_slug_wins_over_semantic_match() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    unit = ExtractedUnit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.109-125",
        heading_path="Self-Similarity",
        text="Recursive list mapping, folding, copy-on-write, and linked list examples.",
        extraction_status="ok",
    )
    existing_pages = {
        "book-copy-on-write": render_page(
            WikiPage(
                name="book-copy-on-write",
                category="source",
                summary="Copy-on-write source page.",
                body="copy-on-write linked list mapping folding recursion",
            )
        ),
        "book-self-similarity": render_page(
            WikiPage(
                name="book-self-similarity",
                category="source",
                summary="Self-similarity source page.",
                body="recursive lists and self-similar data",
            )
        ),
    }

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages=existing_pages,
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-18",
    )

    planned_pages = {write.page_metadata.page_id for write in plan.planned_writes}
    assert "book-self-similarity" in planned_pages
    assert all(
        "unit-0001" not in write.extracted_units
        for write in plan.planned_writes
        if write.page_metadata.page_id == "book-copy-on-write"
    )
