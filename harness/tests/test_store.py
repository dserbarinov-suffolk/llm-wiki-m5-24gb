"""WikiStore boundary tests: confinement, immutability, index coupling."""

import pytest

from llmwiki.config import SOURCE_READ_BUDGET_CHARS, WikiPaths
from llmwiki.domain.pages import PageMetadata, PathTemplate, WikiPage, WikiStructure
from llmwiki.store import PageNotFoundError, SourceNotFoundError, WikiStore, WikiStoreError


def _page(page_id: str = "hittites", page_kind: str = "entity") -> WikiPage:
    metadata = PageMetadata(
        page_id=page_id,
        page_kind=page_kind,
        summary=f"About {page_id}.",
        sources=("article.md",),
        updated="2026-06-10",
    )
    return WikiPage.from_metadata(metadata, f"The {page_id} page. See [[other]].")


class TestRawLayer:
    def test_read_source(self, paths: WikiPaths, store: WikiStore) -> None:
        (paths.raw_dir / "article.md").write_text("Source text.", encoding="utf-8")
        assert store.read_source("article.md") == "Source text."

    def test_traversal_outside_raw_rejected(self, paths: WikiPaths, store: WikiStore) -> None:
        (paths.root / "secret.md").write_text("nope", encoding="utf-8")
        with pytest.raises(SourceNotFoundError):
            store.read_source("../secret.md")

    def test_missing_source_lists_available(self, paths: WikiPaths, store: WikiStore) -> None:
        (paths.raw_dir / "exists.md").write_text("x", encoding="utf-8")
        with pytest.raises(SourceNotFoundError, match="exists.md"):
            store.read_source("missing.md")

    def test_oversized_source_truncated_with_marker(
        self, paths: WikiPaths, store: WikiStore
    ) -> None:
        (paths.raw_dir / "big.md").write_text("x" * (SOURCE_READ_BUDGET_CHARS + 100))
        text = store.read_source("big.md")
        assert "[TRUNCATED" in text
        assert len(text) < SOURCE_READ_BUDGET_CHARS + 200


class TestWikiLayer:
    def test_write_page_creates_file_and_index_entry(
        self, paths: WikiPaths, store: WikiStore
    ) -> None:
        store.write_page(_page())
        assert (paths.wiki_dir / "hittites.md").exists()
        assert "- [[hittites]] — About hittites." in store.read_index()
        assert store.list_pages() == ["hittites"]

    def test_write_page_uses_current_structure(self, store: WikiStore) -> None:
        page = _page(page_id="hittites", page_kind="entity")
        store.write_page(page)
        assert store.rendered_page_path(page) == "hittites.md"
        assert store.read_wiki_page("hittites").page_metadata == page.page_metadata

    def test_write_page_can_project_to_nested_structure(self, paths: WikiPaths) -> None:
        structure = WikiStructure(
            structure_id="nested",
            default_path_template=PathTemplate(
                template_text="{Domain}/{CategoryPath}/{PageId}.md",
                required_page_metadata_fields=("Domain", "CategoryPath", "PageId"),
            ),
        )
        store = WikiStore(paths, structure=structure)
        metadata = PageMetadata(
            page_id="lcn-4040xp",
            page_kind="source",
            summary="LCN closer source page.",
            domain="doors",
            category_path="hardware/closers",
            updated="2026-06-18",
        )
        page = WikiPage.from_metadata(metadata, "Body.")

        store.write_page(page)

        assert (paths.wiki_dir / "doors/hardware/closers/lcn-4040xp.md").exists()
        assert store.read_wiki_page("lcn-4040xp").page_metadata == page.page_metadata
        assert store.list_pages() == ["lcn-4040xp"]

    def test_rewrite_updates_in_place(self, store: WikiStore) -> None:
        store.write_page(_page())
        store.write_page(
            WikiPage.from_metadata(
                PageMetadata(
                    page_id="hittites",
                    page_kind="entity",
                    summary="Updated summary.",
                    updated="2026-06-11",
                ),
                "New body.",
            )
        )
        assert store.read_index().count("[[hittites]]") == 1
        assert "Updated summary." in store.read_index()
        assert "New body." in store.read_page("hittites")

    def test_reserved_names_rejected(self, store: WikiStore) -> None:
        with pytest.raises(WikiStoreError, match="reserved"):
            store.write_page(_page(page_id="index", page_kind="concept"))

    def test_read_missing_page(self, store: WikiStore) -> None:
        with pytest.raises(PageNotFoundError):
            store.read_page("nope")

    def test_index_and_log_not_listed_as_pages(self, store: WikiStore) -> None:
        assert store.list_pages() == []


class TestLog:
    def test_append_log_is_append_only(self, store: WikiStore, paths: WikiPaths) -> None:
        before = paths.log_path.read_text(encoding="utf-8")
        store.append_log("2026-06-10", "ingest", "article.md", "Wrote pages.")
        after = paths.log_path.read_text(encoding="utf-8")
        assert after.startswith(before)
        assert "## [2026-06-10] ingest | article.md" in after
