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


def test_large_source_topic_clusters_are_bounded_and_traceable() -> None:
    raw_source = RawSource.from_locator("large-manual.pdf")
    units = tuple(
        ExtractedUnit(
            unit_id=f"unit-{idx:04d}",
            raw_source=raw_source,
            locator=f"p.{idx}",
            heading_path="Chapter Alpha / Procedure",
            text=(
                "The procedure defines a repeatable operation. "
                f"Step {idx} records one observable requirement."
            ),
            extraction_status="ok",
        )
        for idx in range(1, 246)
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-30",
    )

    assert max(len(cluster.extracted_units) for cluster in plan.topic_clusters) <= 12
    assert all(cluster.candidate_claims for cluster in plan.topic_clusters)
    assert all(cluster.source_claim_groups for cluster in plan.topic_clusters)


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


def test_source_summary_plan_filters_global_claim_groups_to_page_units() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            unit_id="unit-0001",
            raw_source=raw_source,
            locator="p.1-10",
            heading_path="Functions",
            text="Functions are values. Functions may close over scope.",
            extraction_status="ok",
        ),
        ExtractedUnit(
            unit_id="unit-0002",
            raw_source=raw_source,
            locator="p.11-20",
            heading_path="Closures",
            text="Closures are functions with remembered bindings. Closures may retain state.",
            extraction_status="ok",
        ),
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
    )

    claims_by_id = {claim.source_claim_id: claim for claim in plan.source_claims}
    for write in plan.planned_writes:
        if write.page_metadata.page_id == "book":
            continue
        assert write.source_summary_plan is not None
        selected_units = {
            claims_by_id[claim_id].extracted_unit_id
            for claim_id in write.source_summary_plan.selected_source_claims
        }
        assert selected_units <= set(write.extracted_units)
        assert selected_units == set(write.extracted_units)


def test_high_section_pdf_units_group_into_bounded_source_writes() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = tuple(
        ExtractedUnit(
            unit_id=f"unit-{idx:04d}",
            raw_source=raw_source,
            locator=f"p.{idx}",
            heading_path=f"Section {idx}",
            text=(
                f"Section {idx} describes function behavior, scope behavior, "
                "and explicit limitations for the reader."
            ),
            extraction_status="ok",
        )
        for idx in range(1, 46)
    )

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages={},
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-19",
    )

    section_writes = [
        write for write in plan.planned_writes if write.page_metadata.page_id != "book"
    ]
    assert len(section_writes) == 9
    assert all(len(write.extracted_units) <= 5 for write in section_writes)
    assert any(len(write.extracted_units) > 1 for write in section_writes)
    for write in section_writes:
        assert len(write.page_metadata.sources) == len(write.extracted_units)
        if len(write.extracted_units) > 1:
            assert write.resolved_page_body_contract.required_source_citations == ("raw/book.pdf",)


def test_high_section_pdf_units_coalesce_existing_source_page_targets() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    units = (
        ExtractedUnit(
            unit_id="unit-0001",
            raw_source=raw_source,
            locator="p.1",
            heading_path="Functions",
            text="Functions are values and may return other functions.",
            extraction_status="ok",
        ),
        *(
            ExtractedUnit(
                unit_id=f"unit-{idx:04d}",
                raw_source=raw_source,
                locator=f"p.{idx}",
                heading_path=f"Section {idx}",
                text=f"Section {idx} describes scoped behavior and limitations.",
                extraction_status="ok",
            )
            for idx in range(2, 42)
        ),
        ExtractedUnit(
            unit_id="unit-0042",
            raw_source=raw_source,
            locator="p.42",
            heading_path="Functions",
            text="Functions also support higher-order programming patterns.",
            extraction_status="ok",
        ),
    )
    existing_pages = {"book-functions": _page("book-functions", "Existing functions source page.")}

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=units,
        existing_pages=existing_pages,
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-23",
    )

    planned_page_ids = [write.page_metadata.page_id for write in plan.planned_writes]
    function_writes = [
        write for write in plan.planned_writes if write.page_metadata.page_id == "book-functions"
    ]
    assert len(planned_page_ids) == len(set(planned_page_ids))
    assert len(function_writes) == 1
    assert function_writes[0].extracted_units == ("unit-0001", "unit-0042")
    assert function_writes[0].action == "enrich-existing"


def test_generic_section_terms_do_not_match_existing_source_pages() -> None:
    raw_source = RawSource.from_locator("book.pdf")
    unit = ExtractedUnit(
        unit_id="unit-0001",
        raw_source=raw_source,
        locator="p.106-107",
        heading_path="destructuring and return values",
        text="Destructuring can be used with returned values.",
        extraction_status="ok",
    )
    existing_pages = {
        "book-functions-and-identities-through-functions-that-return-values-and-evaluate": _page(
            "book-functions-and-identities-through-functions-that-return-values-and-evaluate",
            "Functions can return values and evaluate expressions.",
        )
    }

    plan = build_page_plan(
        plan_id="test-plan",
        source_bundle=SourceBundle.one(raw_source),
        raw_source=raw_source,
        extracted_units=(unit,),
        existing_pages=existing_pages,
        wiki_structure=LOCAL_FLAT_STRUCTURE,
        today="2026-06-23",
    )

    planned_pages = {write.page_metadata.page_id for write in plan.planned_writes}
    assert "book-destructuring-and-return-values" in planned_pages
    assert (
        "book-functions-and-identities-through-functions-that-return-values-and-evaluate"
        not in planned_pages
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
