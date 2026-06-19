"""Tests for global ingest planning."""

from llmwiki.domain.objects import ExtractedUnit, PageBodyContract, RawSource, Schema, SourceBundle
from llmwiki.domain.pages import LOCAL_FLAT_STRUCTURE, PageMetadata, WikiPage, render_page
from llmwiki.domain.planning import build_markdown_page_plan, build_page_plan


def _page(page_id: str, page_body: str) -> str:
    metadata = PageMetadata(
        page_id=page_id,
        page_kind="source",
        summary=f"About {page_id}.",
    )
    return render_page(WikiPage.from_metadata(metadata, page_body))


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
        "book-copy-on-write": _page(
            "book-copy-on-write",
            "copy-on-write linked list mapping folding recursion",
        ),
        "book-self-similarity": _page(
            "book-self-similarity",
            "recursive lists and self-similar data",
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


def test_markdown_page_plan_uses_raw_source_stem_for_page_identity() -> None:
    raw_source = RawSource.from_locator("antikythera-mechanism.md")
    plan = build_markdown_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text="# The Antikythera Mechanism\n\nThe device may have originated in Corinth.",
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
    )

    planned_pages = [write.page_metadata.page_id for write in plan.planned_writes]
    assert planned_pages == ["antikythera-mechanism-source", "antikythera-mechanism"]
    assert plan.planned_writes[0].resolved_page_body_contract.contract_id == "source-summary"
    assert plan.planned_writes[0].resolved_page_body_contract.required_link_page_ids == (
        "antikythera-mechanism",
    )
    assert plan.planned_writes[1].resolved_page_body_contract.contract_id == "entity-page"
    assert plan.planned_writes[1].resolved_page_body_contract.required_link_page_ids == (
        "antikythera-mechanism-source",
    )
    assert plan.source_claims
    assert plan.source_claim_groups
    assert plan.topic_clusters[0].source_claim_groups
    assert plan.topic_clusters[0].candidate_claims
    source_summary_plan = plan.planned_writes[0].source_summary_plan
    assert source_summary_plan is not None
    assert source_summary_plan.selected_source_claims
    assert source_summary_plan.required_source_citations == ("raw/antikythera-mechanism.md",)
    assert set(source_summary_plan.selected_source_claims) <= {
        claim.source_claim_id for claim in plan.source_claims
    }


def test_markdown_page_plan_uses_schema_page_body_contract_mapping() -> None:
    raw_source = RawSource.from_locator("lcn-4040xp.md")
    default_schema = Schema()
    schema = Schema(
        page_body_contracts=default_schema.page_body_contracts
        + (
            PageBodyContract(
                contract_id="product-page",
                match_page_kinds=("entity",),
                required_sections=("Applications", "Limitations"),
            ),
        ),
        page_body_contract_by_page_kind=(
            ("source", "source-summary"),
            ("entity", "product-page"),
            ("concept", "concept-page"),
            ("synthesis", "synthesis-page"),
        ),
    )

    plan = build_markdown_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text="# LCN 4040XP\n\nDoor closer evidence.",
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
        schema=schema,
    )

    assert plan.planned_writes[1].resolved_page_body_contract.contract_id == "product-page"
    assert plan.planned_writes[1].resolved_page_body_contract.required_sections == (
        "Applications",
        "Limitations",
    )


def test_markdown_page_plan_extracts_source_claims_from_hard_wrapped_paragraphs() -> None:
    raw_source = RawSource.from_locator("wrapped.md")
    plan = build_markdown_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        source_text=(
            "# Wrapped Source\n\n"
            "The device is a compact mechanism, often\n"
            "described as a useful benchmark. It may require verification."
        ),
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
    )

    statements = [claim.statement for claim in plan.source_claims]
    assert "The device is a compact mechanism, often described as a useful benchmark." in statements
