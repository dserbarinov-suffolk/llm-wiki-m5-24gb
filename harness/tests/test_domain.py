"""Data-in/data-out tests for the pure domain layer."""

import pytest

from llmwiki.domain.index import index_page_ids, parse_index, upsert_index_entry
from llmwiki.domain.links import compute_findings, extract_links
from llmwiki.domain.log import format_log_entry
from llmwiki.domain.objects import IngestRun, RawSource, SourceBundle
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
