"""WikiStore boundary tests: confinement, immutability, index coupling."""

import pytest

from llmwiki.config import SOURCE_READ_BUDGET_CHARS, WikiPaths
from llmwiki.domain.pages import PageMetadata, PathTemplate, WikiPage, WikiStructure
from llmwiki.store import PageNotFoundError, SourceNotFoundError, WikiStore, WikiStoreError
from llmwiki.workflows.tools import read_page_tool


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

    def test_read_page_tool_chunks_large_pages(self, store: WikiStore) -> None:
        page = WikiPage.from_metadata(
            PageMetadata(page_id="large", page_kind="source", summary="Large page."),
            "x" * 100,
        )
        store.write_page(page)
        tool = read_page_tool(store)

        chunk = tool.callable(page_id="large", max_chars=10)
        next_chunk = tool.callable(page_id="large", offset=10, max_chars=10)

        assert chunk.startswith("[Showing wiki/large.md characters 0-10 of ")
        assert "[Truncated. Continue with read_page offset=10.]" in chunk
        assert next_chunk.startswith("[Showing wiki/large.md characters 10-20 of ")

    def test_read_page_tool_default_chunk_is_context_bounded(self, store: WikiStore) -> None:
        page = WikiPage.from_metadata(
            PageMetadata(page_id="large-default", page_kind="source", summary="Large page."),
            "x" * 6_000,
        )
        store.write_page(page)
        tool = read_page_tool(store)

        chunk = tool.callable(page_id="large-default")

        assert chunk.startswith("[Showing wiki/large-default.md characters 0-3000 of ")

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

    def test_delete_source_pages_not_in_removes_stale_generated_pages(
        self, store: WikiStore
    ) -> None:
        store.write_page(
            WikiPage.from_metadata(
                PageMetadata(
                    page_id="kept",
                    page_kind="concept",
                    summary="Kept page.",
                    sources=("raw/article.md",),
                ),
                "Kept body.",
            )
        )
        store.write_page(
            WikiPage.from_metadata(
                PageMetadata(
                    page_id="stale",
                    page_kind="concept",
                    summary="Stale page.",
                    sources=("raw/article.md",),
                ),
                "Stale body.",
            )
        )
        store.write_page(
            WikiPage.from_metadata(
                PageMetadata(
                    page_id="manual",
                    page_kind="concept",
                    summary="Manual page.",
                    sources=("other.md",),
                ),
                "Manual body.",
            )
        )

        removed = store.delete_source_pages_not_in("article.md", {"kept"})

        assert removed == ("stale",)
        assert store.read_page("kept")
        assert store.read_page("manual")
        with pytest.raises(PageNotFoundError):
            store.read_page("stale")
        assert "[[stale]]" not in store.read_index()

    def test_delete_cross_source_pages_not_in_uses_projection_pointer(
        self, store: WikiStore
    ) -> None:
        current = WikiPage.from_metadata(
            PageMetadata(
                page_id="current",
                page_kind="concept",
                summary="Current cross-source page.",
                projection_coverage_pointer="cross-source-current@hash",
            ),
            "Current body.",
        )
        stale = WikiPage.from_metadata(
            PageMetadata(
                page_id="old-shared",
                page_kind="concept",
                summary="Old cross-source page.",
                projection_coverage_pointer="cross-source-old-shared@hash",
            ),
            "Old body.",
        )
        store.write_page(current)
        store.write_page(stale)

        removed = store.delete_cross_source_pages_not_in({"current"})

        assert removed == ("old-shared",)
        assert store.read_page("current")
        with pytest.raises(PageNotFoundError):
            store.read_page("old-shared")
        assert "[[old-shared]]" not in store.read_index()

    def test_reserved_names_rejected(self, store: WikiStore) -> None:
        with pytest.raises(WikiStoreError, match="reserved"):
            store.write_page(_page(page_id="index", page_kind="concept"))

    def test_read_missing_page(self, store: WikiStore) -> None:
        with pytest.raises(PageNotFoundError):
            store.read_page("nope")

    def test_index_and_log_not_listed_as_pages(self, store: WikiStore) -> None:
        assert store.list_pages() == []

    def test_graph_json_roundtrip(self, store: WikiStore, paths: WikiPaths) -> None:
        assert store.read_graph_json() is None

        store.write_graph_json('{"nodes": []}\n')

        assert paths.graph_path.read_text(encoding="utf-8") == '{"nodes": []}\n'
        assert store.read_graph_json() == '{"nodes": []}\n'


class TestLog:
    def test_append_log_is_append_only(self, store: WikiStore, paths: WikiPaths) -> None:
        before = paths.log_path.read_text(encoding="utf-8")
        store.append_log("2026-06-10", "ingest", "article.md", "Wrote pages.")
        after = paths.log_path.read_text(encoding="utf-8")
        assert after.startswith(before)
        assert "## [2026-06-10] ingest | article.md" in after
