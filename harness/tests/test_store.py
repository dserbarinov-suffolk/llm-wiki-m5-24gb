"""WikiStore boundary tests: confinement, immutability, index coupling."""

import pytest

from llmwiki.config import WikiPaths
from llmwiki.domain.model_profile import qwen3_14b_profile
from llmwiki.domain.pages import PageMetadata, PathTemplate, WikiPage, WikiStructure
from llmwiki.store import PageNotFoundError, SourceNotFoundError, WikiStore, WikiStoreError
from llmwiki.workflows.chat_response_tools import grounded_chat_respond_tool
from llmwiki.workflows.wiki_read_tools import (
    inspect_page_tool,
    read_page_tool,
)
from llmwiki.workflows.wiki_write_tools import (
    write_page_tool,
)


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
        (paths.raw_dir / "big.md").write_text(
            "x" * (store.model_profile.raw_source_read_chars + 100)
        )
        text = store.read_source("big.md")
        assert "[TRUNCATED" in text
        assert len(text) < store.model_profile.raw_source_read_chars + 200

    def test_ingest_source_read_is_not_prompt_bounded(
        self, paths: WikiPaths, store: WikiStore
    ) -> None:
        body = "x" * (store.model_profile.raw_source_read_chars + 100) + " sentinel-at-end"
        (paths.raw_dir / "big.md").write_text(body, encoding="utf-8")

        assert store.read_source_for_ingest("big.md") == body
        assert "sentinel-at-end" not in store.read_source("big.md")

    def test_source_read_budget_comes_from_model_profile(
        self, paths: WikiPaths
    ) -> None:
        profile = qwen3_14b_profile(8_192)
        store = WikiStore(paths, model_profile=profile)
        body = "x" * (profile.raw_source_read_chars + 100)
        (paths.raw_dir / "small-profile.md").write_text(body, encoding="utf-8")

        text = store.read_source("small-profile.md")

        assert "[TRUNCATED" in text
        assert len(text) < profile.raw_source_read_chars + 200


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

    def test_inspect_page_tool_returns_compact_page_map(self, store: WikiStore) -> None:
        page = WikiPage.from_metadata(
            PageMetadata(page_id="mapped", page_kind="source", summary="Mapped page."),
            "# Mapped\nSee [[other]].\n\n"
            "## Step\nEvidence. _(book.pdf (source-range-abc123-00001))_",
        )
        store.write_page(page)
        tool = inspect_page_tool(store)

        result = tool.callable(page_id="mapped")

        assert "Page map for [[mapped]]" in result
        assert "[[other]]" in result
        assert "source-range-abc123-00001" in result

    def test_write_page_tool_rejects_body_frontmatter(self, store: WikiStore) -> None:
        tool = write_page_tool(store, "2026-06-30")

        with pytest.raises(WikiStoreError, match="must not include frontmatter"):
            tool.callable(
                page_id="frontmatter-body",
                page_kind="concept",
                summary="Bad body.",
                page_body="---\npage_id: frontmatter-body\n---\n# Bad",
                sources=[],
            )

    def test_write_page_tool_rejects_truncated_read_markers(self, store: WikiStore) -> None:
        tool = write_page_tool(store, "2026-06-30")

        with pytest.raises(WikiStoreError, match="read_page chunk marker"):
            tool.callable(
                page_id="truncated-body",
                page_kind="concept",
                summary="Bad body.",
                page_body=(
                    "# Bad\n\n"
                    "[Showing wiki/source.md characters 0-3000 of 9000.]\n"
                    "[Truncated. Continue with read_page offset=3000.]"
                ),
                sources=[],
            )

    def test_inspect_page_tool_stops_after_manifest_reports_missing_focus(
        self, store: WikiStore
    ) -> None:
        manifest = WikiPage.from_metadata(
            PageMetadata(
                page_id="manual",
                page_kind="source",
                page_family="source-manifest",
                summary="Manual source manifest.",
                sources=("raw/manual.pdf",),
            ),
            "# Manual\n\n## Ability Scores\nUse modifiers.",
        )
        section = WikiPage.from_metadata(
            PageMetadata(
                page_id="manual-ability-scores",
                page_kind="source",
                page_family="section-reference",
                summary="Ability scores.",
                sources=("raw/manual.pdf",),
            ),
            "# Ability Scores\n\n## Statements\nUse modifiers.",
        )
        store.write_page(manifest)
        store.write_page(section)
        tool = inspect_page_tool(store)

        first_result = tool.callable(page_id="manual", focus_query="character creation")
        second_result = tool.callable(
            page_id="manual-ability-scores",
            focus_query="character creation",
        )

        assert "0 heading match(es)" in first_result
        assert "Focused source coverage was already checked" in second_result
        assert "Stop inspecting related pages" in second_result

    def test_grounded_chat_respond_requires_citations_after_missing_focus(self) -> None:
        tool = grounded_chat_respond_tool({"raw/manual.pdf::character creation"})

        with pytest.raises(WikiStoreError, match="missing inspected wiki page citation"):
            tool.callable(message="The procedure is missing. Would you like another source?")

        result = tool.callable(
            message=(
                "[[manual]] has no matching character-creation heading for "
                "source-range-abc123-00001, so the wiki lacks this procedure."
            )
        )

        assert result.startswith("[[manual]] has no matching")

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
