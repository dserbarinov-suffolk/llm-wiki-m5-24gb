"""Data-in/data-out tests for the pure domain layer."""

import pytest

from llmwiki.domain.index import index_page_ids, parse_index, upsert_index_entry
from llmwiki.domain.links import compute_findings, extract_links
from llmwiki.domain.log import format_log_entry
from llmwiki.domain.objects import (
    IngestRun,
    PageBodyContract,
    RawSource,
    Schema,
    SourceBundle,
    SourcePlan,
    SourcePlanContractSelection,
    SourceSummaryBullet,
    SourceSummaryDraft,
    SourceSummaryPlan,
)
from llmwiki.domain.page_body_contracts import (
    canonicalize_source_summary_draft,
    canonicalize_source_summary_page_body,
    contract_for_page_kind,
    render_source_summary_draft,
    resolve_page_body_contract,
    validate_page_body,
    validate_source_summary_draft,
)
from llmwiki.domain.pages import (
    LOCAL_FLAT_STRUCTURE,
    PageError,
    PageMetadata,
    PathTemplate,
    WikiPage,
    WikiStructure,
    parse_page,
    render_page,
)
from llmwiki.domain.search import search_pages

INDEX = """# Index

## Sources

- [[alpha-source]] — about alpha

## Entities

## Concepts

- [[bravo]] — concept b
- [[delta]] — concept d

## Syntheses
"""


class TestPages:
    def test_render_parse_roundtrip(self) -> None:
        metadata = PageMetadata(
            page_id="bronze-age",
            page_kind="concept",
            summary="The Bronze Age collapse.",
            sources=("article.md",),
            updated="2026-06-10",
        )
        page = WikiPage.from_metadata(
            metadata,
            "Linked to [[sea-peoples]].\n\nEvidence: (raw/article.md)",
        )
        rendered = render_page(page)
        assert "page_id: bronze-age" in rendered
        assert "page_kind: concept" in rendered
        assert "category:" not in rendered
        assert parse_page(rendered) == page

    @pytest.mark.parametrize("page_id", ["Bad Name", "UPPER", "trailing-", "-leading", "a--b", ""])
    def test_invalid_page_ids_rejected(self, page_id: str) -> None:
        with pytest.raises(PageError):
            PageMetadata(page_id=page_id, page_kind="entity", summary="s")

    def test_invalid_page_kind_rejected(self) -> None:
        with pytest.raises(PageError):
            PageMetadata(page_id="ok", page_kind="article", summary="s")

    def test_summary_collapsed_to_one_line(self) -> None:
        with pytest.raises(PageError):
            PageMetadata(page_id="ok", page_kind="entity", summary="  \n ")

    def test_page_metadata_projects_to_flat_path(self) -> None:
        metadata = PageMetadata(
            page_id="javascriptallonge-chapter-5",
            page_kind="source",
            summary="Chapter source page.",
            sources=("raw/javascriptallonge.pdf p.49-61",),
            updated="2026-06-18",
        )
        assert str(LOCAL_FLAT_STRUCTURE.render_path(metadata)) == "javascriptallonge-chapter-5.md"

    def test_page_metadata_projects_to_declared_folder_path(self) -> None:
        structure = WikiStructure(
            structure_id="domain-category",
            default_path_template=PathTemplate(
                template_text="{Domain}/{CategoryPath}/{PageId}.md",
                required_page_metadata_fields=("Domain", "CategoryPath", "PageId"),
            ),
        )
        metadata = PageMetadata(
            page_id="lcn-4040xp",
            page_kind="source",
            summary="LCN closer source page.",
            domain="doors",
            category_path="hardware/closers",
        )

        assert str(structure.render_path(metadata)) == "doors/hardware/closers/lcn-4040xp.md"

    def test_page_metadata_required_field_is_enforced(self) -> None:
        structure = WikiStructure(
            structure_id="domain-category",
            default_path_template=PathTemplate(
                template_text="{Domain}/{PageId}.md",
                required_page_metadata_fields=("Domain", "PageId"),
            ),
        )
        metadata = PageMetadata(page_id="lcn-4040xp", page_kind="source", summary="LCN closer.")

        with pytest.raises(PageError, match="Domain"):
            structure.render_path(metadata)

    def test_wiki_page_exposes_page_metadata(self) -> None:
        metadata = PageMetadata(
            page_id="closure",
            page_kind="concept",
            summary="A captured lexical environment.",
            sources=("raw/javascriptallonge.pdf",),
            updated="2026-06-18",
            domain="javascript",
            category_path="language/functions",
            source_id="javascriptallonge.pdf",
            tags=("closure",),
            aliases=("lexical-closure",),
        )
        page = WikiPage.from_metadata(metadata, "Body.")
        assert page.page_metadata == metadata
        assert page.page_body == "Body."
        assert str(page.page_path()) == "closure.md"


class TestObjectBoundaries:
    def test_source_bundle_requires_raw_source(self) -> None:
        with pytest.raises(ValueError):
            SourceBundle(raw_sources=())

    def test_raw_source_derives_format(self) -> None:
        raw = RawSource.from_locator("javascriptallonge.pdf")
        assert raw.source_locator == "javascriptallonge.pdf"
        assert raw.source_format == "pdf"

    def test_local_ingest_run_is_serial_only(self) -> None:
        raw = RawSource.from_locator("article.md")
        run = IngestRun(source_bundle=SourceBundle.one(raw))
        assert run.ingest_topology == "serial"
        with pytest.raises(ValueError):
            IngestRun(source_bundle=SourceBundle.one(raw), ingest_topology="parallel")


class TestPageBodyContracts:
    def test_schema_has_generic_default_page_body_contracts(self) -> None:
        schema = Schema()
        contracts = {contract.contract_id for contract in schema.page_body_contracts}
        assert {"source-summary", "entity-page", "concept-page", "synthesis-page"} <= contracts
        claim_roles = {role.tag_name for role in schema.claim_role_tags}
        assert {"identity", "uncertainty", "negative-evidence"} <= claim_roles
        source_contract = contract_for_page_kind(schema, "source")
        assert source_contract.contract_id == "source-summary"
        assert source_contract.min_claim_bullets == 3
        assert source_contract.coverage_policy == "main-supported-claims-and-explicit-limits"
        assert not hasattr(RawSource.from_locator("article.md"), "page_body_contract")

    def test_source_plan_can_select_page_body_contract_without_changing_raw_source(self) -> None:
        raw = RawSource.from_locator("article.md")
        selection = SourcePlanContractSelection(
            contract_id="architecture-product-source",
            page_ids=("lcn-4040xp-source",),
            max_words_override=120,
        )
        plan = SourcePlan(
            raw_source=raw,
            source_classification="legacy source record",
            ingest_disposition="create-new",
            page_body_contract_selections=(selection,),
        )

        assert plan.raw_source == raw
        assert plan.page_body_contract_selections == (selection,)

    def test_source_summary_contract_rejects_near_full_source_copy(self) -> None:
        source_text = (
            "The Antikythera mechanism may have tracked astronomical cycles. "
            "The device was recovered from a shipwreck and its inscriptions "
            "suggest possible calendrical and eclipse functions."
        )
        contract = resolve_page_body_contract(
            contract_for_page_kind(Schema(), "source"),
            required_link_page_ids=("antikythera-mechanism",),
            required_source_citations=("raw/antikythera-mechanism.md",),
            required_uncertainty_terms=("may", "suggest", "possible"),
        )
        page_body = (
            "The Antikythera mechanism may have tracked astronomical cycles. "
            "The device was recovered from a shipwreck and its inscriptions "
            "suggest possible calendrical and eclipse functions. "
            "See [[antikythera-mechanism]]. (raw/antikythera-mechanism.md)"
        )

        findings = validate_page_body(page_body, contract, source_text=source_text)

        assert {finding.finding_type for finding in findings} >= {
            "RequiredSections",
            "RequiredMarkdownShape",
            "MaxCopiedNGramRatio",
        }

    def test_source_summary_contract_accepts_compact_grounded_claims(self) -> None:
        source_text = (
            "The Antikythera mechanism may have tracked astronomical cycles. "
            "The device was recovered from a shipwreck and its inscriptions "
            "suggest possible calendrical and eclipse functions."
        )
        contract = resolve_page_body_contract(
            contract_for_page_kind(Schema(), "source"),
            required_link_page_ids=("antikythera-mechanism",),
            required_source_citations=("raw/antikythera-mechanism.md",),
            required_uncertainty_terms=("may", "suggest", "possible"),
        )
        page_body = (
            "## Source record\n\n"
            "Source record for [[antikythera-mechanism]]. "
            "The evidence may remain uncertain. (raw/antikythera-mechanism.md)\n\n"
            "## Key supported claims\n\n"
            "- The source supports an astronomical interpretation. "
            "(raw/antikythera-mechanism.md)\n"
            "- The source preserves possible functions without resolving them. "
            "(raw/antikythera-mechanism.md)\n"
            "- The source points to unresolved origin evidence. "
            "(raw/antikythera-mechanism.md)"
        )

        assert validate_page_body(page_body, contract, source_text=source_text) == ()

    def test_source_summary_draft_must_cover_selected_source_claims(self) -> None:
        plan = SourceSummaryPlan(
            source_summary_plan_id="source-summary-plan-alpha",
            page_id="alpha-source",
            selected_source_claims=("source-claim-unit-0001-0001", "source-claim-unit-0001-0002"),
        )
        draft = SourceSummaryDraft(
            source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
            claim_bullets=(
                SourceSummaryBullet(
                    "The source supports a first compact claim. (raw/alpha.md)",
                    ("source-claim-unit-0001-0001",),
                ),
            ),
        )

        findings = validate_source_summary_draft(draft, plan)

        assert [finding.finding_type for finding in findings] == ["SelectedSourceClaims"]

    def test_source_summary_draft_rejects_copied_source_phrase(self) -> None:
        source_text = (
            "The ancient device contains a complex gear train that predicts eclipse cycles "
            "with a dial display."
        )
        plan = SourceSummaryPlan(
            source_summary_plan_id="source-summary-plan-alpha",
            page_id="alpha-source",
            selected_source_claims=("source-claim-unit-0001-0001",),
        )
        draft = SourceSummaryDraft(
            source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
            claim_bullets=(
                SourceSummaryBullet(
                    "The ancient device contains a complex gear train that predicts "
                    "eclipse cycles. (raw/alpha.md)",
                    ("source-claim-unit-0001-0001",),
                ),
            ),
        )

        findings = validate_source_summary_draft(draft, plan, source_text=source_text)

        assert [finding.finding_type for finding in findings] == ["CopiedSourcePhrase"]

    def test_source_summary_draft_requires_bullet_citations(self) -> None:
        plan = SourceSummaryPlan(
            source_summary_plan_id="source-summary-plan-alpha",
            page_id="alpha-source",
            selected_source_claims=("source-claim-unit-0001-0001",),
            required_source_citations=("raw/alpha.md",),
        )
        draft = SourceSummaryDraft(
            source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
            claim_bullets=(
                SourceSummaryBullet(
                    "The source supports a compact claim.",
                    ("source-claim-unit-0001-0001",),
                ),
            ),
        )

        findings = validate_source_summary_draft(draft, plan)

        assert [finding.finding_type for finding in findings] == ["SourceSummaryBulletCitation"]

    def test_source_summary_draft_rejects_source_framing_bullets(self) -> None:
        plan = SourceSummaryPlan(
            source_summary_plan_id="source-summary-plan-alpha",
            page_id="alpha-source",
            selected_source_claims=("source-claim-unit-0001-0001",),
            required_source_citations=("raw/alpha.md",),
        )
        draft = SourceSummaryDraft(
            source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
            claim_bullets=(
                SourceSummaryBullet(
                    "The source discusses a compact claim. (raw/alpha.md)",
                    ("source-claim-unit-0001-0001",),
                ),
            ),
        )

        findings = validate_source_summary_draft(draft, plan)

        assert [finding.finding_type for finding in findings] == ["SourceFramingBullet"]

    def test_source_summary_draft_canonicalizes_simple_source_framing(self) -> None:
        draft = SourceSummaryDraft(
            source_record_text=" Source record for [[alpha]]. (raw/alpha.md) ",
            claim_bullets=(
                SourceSummaryBullet(
                    "The text mentions that a generalized recipe was not written. (raw/alpha.md)",
                    ("source-claim-unit-0001-0001",),
                ),
                SourceSummaryBullet(
                    "The section describes two recipes for applying one argument. (raw/alpha.md)",
                    ("source-claim-unit-0001-0002",),
                ),
                SourceSummaryBullet(
                    "The text does not provide a complete method. (raw/alpha.md)",
                    ("source-claim-unit-0001-0003",),
                ),
            ),
        )

        canonical = canonicalize_source_summary_draft(draft)

        assert canonical.source_record_text == "Source record for [[alpha]]. (raw/alpha.md)"
        assert canonical.claim_bullets[0].bullet_text.startswith("A generalized recipe")
        assert canonical.claim_bullets[1].bullet_text.startswith("Two recipes")
        assert canonical.claim_bullets[2].bullet_text.startswith("A complete method")
        assert (
            validate_source_summary_draft(
                canonical,
                SourceSummaryPlan(
                    source_summary_plan_id="source-summary-plan-alpha",
                    page_id="alpha-source",
                    selected_source_claims=(
                        "source-claim-unit-0001-0001",
                        "source-claim-unit-0001-0002",
                        "source-claim-unit-0001-0003",
                    ),
                    required_source_citations=("raw/alpha.md",),
                ),
            )
            == ()
        )

    def test_source_summary_page_body_canonicalizes_simple_source_framing(self) -> None:
        contract = resolve_page_body_contract(
            PageBodyContract(
                contract_id="source-summary",
                match_page_kinds=("source",),
                required_sections=("Source record", "Key supported claims"),
                required_markdown_shape="claim-bullets",
                min_claim_bullets=3,
            )
        )
        page_body = (
            "## Source record\n\n"
            "Source record for [[alpha]]. (raw/alpha.md)\n\n"
            "## Key supported claims\n\n"
            "- Alpha identifies the subject. (raw/alpha.md)\n"
            "- The source discusses a compact claim. (raw/alpha.md)\n"
            "- The text highlights a second compact claim. (raw/alpha.md)"
        )

        findings = validate_page_body(page_body, contract)
        canonical = canonicalize_source_summary_page_body(page_body, contract)

        assert [finding.finding_type for finding in findings] == [
            "SourceFramingBullet",
            "SourceFramingBullet",
        ]
        assert "- A compact claim. (raw/alpha.md)" in canonical
        assert "- A second compact claim. (raw/alpha.md)" in canonical
        assert validate_page_body(canonical, contract) == ()

    def test_source_summary_draft_does_not_render_source_claim_ids(self) -> None:
        plan = SourceSummaryPlan(
            source_summary_plan_id="source-summary-plan-alpha",
            page_id="alpha-source",
            selected_source_claims=("source-claim-unit-0001-0001",),
        )
        draft = SourceSummaryDraft(
            source_record_text="Source record for [[alpha]]. (raw/alpha.md)",
            claim_bullets=(
                SourceSummaryBullet(
                    "The source supports a compact claim. (raw/alpha.md)",
                    ("source-claim-unit-0001-0001",),
                ),
            ),
        )

        assert validate_source_summary_draft(draft, plan) == ()
        rendered = render_source_summary_draft(draft)
        assert "source-claim-unit" not in rendered

        leaked = SourceSummaryDraft(
            source_record_text="Source record source-claim-unit-0001-0001 for [[alpha]].",
            claim_bullets=draft.claim_bullets,
        )
        findings = validate_source_summary_draft(leaked, plan)
        assert [finding.finding_type for finding in findings] == ["SourceClaimIdLeak"]

    def test_user_defined_contract_controls_page_shape(self) -> None:
        contract = PageBodyContract(
            contract_id="product-page",
            match_page_kinds=("entity",),
            required_sections=("Applications", "Limitations"),
        )
        resolved = resolve_page_body_contract(contract)

        findings = validate_page_body("## Applications\n\nDoor closer evidence.", resolved)
        assert [finding.finding_type for finding in findings] == ["RequiredSections"]
        assert (
            validate_page_body(
                "## Applications\n\nDoor closer evidence.\n\n## Limitations\n\nOpen items.",
                resolved,
            )
            == ()
        )


class TestIndex:
    def test_parse_extracts_entries_with_page_kinds(self) -> None:
        entries = parse_index(INDEX)
        assert [(e.page_id, e.page_kind) for e in entries] == [
            ("alpha-source", "source"),
            ("bravo", "concept"),
            ("delta", "concept"),
        ]

    def test_upsert_inserts_sorted_within_page_kind(self) -> None:
        metadata = PageMetadata(page_id="charlie", page_kind="concept", summary="concept c")
        updated = upsert_index_entry(INDEX, metadata)
        page_ids = [e.page_id for e in parse_index(updated) if e.page_kind == "concept"]
        assert page_ids == ["bravo", "charlie", "delta"]

    def test_upsert_replaces_existing_entry(self) -> None:
        metadata = PageMetadata(page_id="bravo", page_kind="concept", summary="new summary")
        updated = upsert_index_entry(INDEX, metadata)
        entries = {e.page_id: e.summary for e in parse_index(updated)}
        assert entries["bravo"] == "new summary"
        assert len([e for e in parse_index(updated) if e.page_id == "bravo"]) == 1

    def test_upsert_moves_page_between_page_kinds(self) -> None:
        metadata = PageMetadata(page_id="bravo", page_kind="synthesis", summary="now a synthesis")
        updated = upsert_index_entry(INDEX, metadata)
        entries = {e.page_id: e.page_kind for e in parse_index(updated)}
        assert entries["bravo"] == "synthesis"

    def test_upsert_into_empty_page_kind(self) -> None:
        metadata = PageMetadata(page_id="ada", page_kind="entity", summary="a person")
        updated = upsert_index_entry(INDEX, metadata)
        assert ("ada", "entity") in [(e.page_id, e.page_kind) for e in parse_index(updated)]

    def test_index_page_ids(self) -> None:
        assert index_page_ids(INDEX) == {"alpha-source", "bravo", "delta"}


class TestLog:
    def test_entry_has_greppable_prefix(self) -> None:
        entry = format_log_entry("2026-06-10", "ingest", "article.md", "Wrote 3 pages.")
        assert "## [2026-06-10] ingest | article.md" in entry
        assert "Wrote 3 pages." in entry

    def test_subject_collapsed_and_truncated(self) -> None:
        entry = format_log_entry("2026-06-10", "query", "a\nb" + "x" * 200, "d")
        prefix_line = next(line for line in entry.splitlines() if line.startswith("## ["))
        assert "\n" not in prefix_line
        assert len(prefix_line) < 120


class TestLinks:
    def test_extract_links(self) -> None:
        assert extract_links("See [[alpha]] and [[beta-2]]. Not [link].") == {"alpha", "beta-2"}

    def test_findings_detect_all_issue_kinds(self) -> None:
        pages = {
            "alpha": "links to [[beta]] and [[ghost]]",
            "beta": "no links here",
            "gamma": "links to [[alpha]]",
        }
        findings = compute_findings(pages, index_page_ids={"alpha", "beta", "zombie"})
        assert findings.broken_links == {"alpha": ("ghost",)}
        assert findings.orphan_pages == ("gamma",)
        assert findings.missing_from_index == ("gamma",)
        assert findings.stale_index_entries == ("zombie",)
        assert not findings.is_clean
        assert "ghost" in findings.render()

    def test_clean_wiki_is_clean(self) -> None:
        pages = {"alpha": "see [[beta]]", "beta": "see [[alpha]]"}
        findings = compute_findings(pages, index_page_ids={"alpha", "beta"})
        assert findings.is_clean

    def test_single_page_is_not_an_orphan(self) -> None:
        findings = compute_findings({"only": "text"}, index_page_ids={"only"})
        assert findings.orphan_pages == ()


class TestSearch:
    PAGES = {
        "bronze-age": "The Bronze Age collapse affected the Hittites.",
        "sea-peoples": "The Sea Peoples raided during the Bronze Age collapse collapse.",
        "unrelated": "Nothing relevant here.",
    }

    def test_ranks_by_term_frequency_and_name_match(self) -> None:
        hits = search_pages(self.PAGES, "bronze collapse")
        assert [h.page_id for h in hits] == ["bronze-age", "sea-peoples"]

    def test_no_match_returns_empty(self) -> None:
        assert search_pages(self.PAGES, "quasar") == []

    def test_snippet_contains_context(self) -> None:
        hits = search_pages(self.PAGES, "hittites")
        assert "Hittites" in hits[0].snippet
