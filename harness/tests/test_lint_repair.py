from llmwiki.domain.lint_repair import (
    LINT_LINK_SECTION,
    add_related_link,
    remove_broken_link,
    replace_link_target,
)
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.store import WikiStore
from llmwiki.workflows import build_lint_workflow
from llmwiki.workflows.lint_repair_tools import add_related_link_tool, replace_link_target_tool

TODAY = "2026-07-08"


def _page(
    page_id: str,
    body: str,
    *,
    page_kind: str = "concept",
    page_family: str = "",
) -> WikiPage:
    return WikiPage.from_metadata(
        PageMetadata(
            page_id=page_id,
            page_kind=page_kind,
            page_family=page_family,
            summary=f"{page_id} summary.",
            sources=("raw/source.pdf",),
            updated="2026-07-01",
            domain="coding",
            category_path="source/section",
            source_id="source-pdf",
            tags=("generated",),
            aliases=("Alias",),
            projection_coverage_pointer="coverage.json",
        ),
        body,
    )


def test_add_related_link_is_bounded_and_idempotent() -> None:
    metadata = PageMetadata(page_id="alpha", page_kind="concept", summary="Alpha.")
    first = add_related_link(metadata, "Alpha body.", "beta", "related topic")
    assert first.accepted
    assert first.changed
    assert LINT_LINK_SECTION in first.updated_body
    assert "- [[beta]] - related topic" in first.updated_body

    second = add_related_link(metadata, first.updated_body, "beta", "related topic")
    assert second.accepted
    assert not second.changed
    assert second.updated_body == ""


def test_replace_and_remove_are_exact_link_repairs() -> None:
    metadata = PageMetadata(page_id="alpha", page_kind="concept", summary="Alpha.")
    replaced = replace_link_target(metadata, "See [[betaa]] and beta.", "betaa", "beta", "typo")
    assert replaced.accepted
    assert replaced.updated_body == "See [[beta]] and beta."

    removed = remove_broken_link(
        metadata,
        "Keep this.\n- [[ghost]]\nInline [[ghost]].",
        "ghost",
        "",
    )
    assert removed.accepted
    assert removed.updated_body == "Keep this.\nInline ghost."


def test_generated_pages_reject_link_rewrites_but_allow_navigation_links() -> None:
    metadata = PageMetadata(
        page_id="alpha",
        page_kind="source",
        page_family="section-reference",
        summary="Alpha.",
    )
    replaced = replace_link_target(metadata, "See [[ghost]].", "ghost", "real", "typo")
    assert not replaced.accepted
    assert "bounded navigation links only" in replaced.message

    linked = add_related_link(metadata, "Alpha body.", "real", "related section")
    assert linked.accepted
    assert linked.changed


def test_lint_add_related_link_tool_preserves_metadata(store: WikiStore) -> None:
    store.write_page(_page("alpha", "Alpha body."))
    store.write_page(
        WikiPage.from_metadata(
            PageMetadata(page_id="beta", page_kind="concept", summary="Beta."),
            "Beta body.",
        )
    )
    tool = add_related_link_tool(store, TODAY)

    result = tool.callable(page_id="alpha", target_page_id="beta", reason="related topic")

    assert result.startswith("Applied:")
    page = store.read_wiki_page("alpha")
    assert page.page_metadata.page_family == ""
    assert page.page_metadata.sources == ("raw/source.pdf",)
    assert page.page_metadata.domain == "coding"
    assert page.page_metadata.category_path == "source/section"
    assert page.page_metadata.source_id == "source-pdf"
    assert page.page_metadata.tags == ("generated",)
    assert page.page_metadata.aliases == ("Alias",)
    assert page.page_metadata.projection_coverage_pointer == "coverage.json"
    assert page.page_metadata.updated == TODAY
    assert "Alpha body." in page.page_body
    assert "[[beta]]" in page.page_body


def test_lint_repair_tool_rejects_generated_rewrite(store: WikiStore) -> None:
    store.write_page(
        _page("alpha", "See [[betaa]].", page_kind="source", page_family="source-manifest")
    )
    store.write_page(
        WikiPage.from_metadata(
            PageMetadata(page_id="beta", page_kind="concept", summary="Beta."),
            "Beta body.",
        )
    )
    tool = replace_link_target_tool(store, TODAY)

    result = tool.callable(
        page_id="alpha",
        old_target_page_id="betaa",
        new_target_page_id="beta",
        reason="typo",
    )

    assert result.startswith("Rejected:")
    assert store.read_wiki_page("alpha").page_body == "See [[betaa]]."


def test_lint_workflow_has_no_whole_page_writer(store: WikiStore) -> None:
    workflow = build_lint_workflow(store, TODAY)
    assert "write_page" not in workflow.tools
    assert {
        "search_wiki",
        "read_page",
        "add_related_link",
        "replace_link_target",
        "remove_broken_link",
        "request_source_regeneration",
        "finish_lint",
    } == set(workflow.tools)
