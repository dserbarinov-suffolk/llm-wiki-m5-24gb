from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.runtime.ledger_pages import append_source_page_links, source_title


def test_source_title_uses_source_locator_stem_and_preserves_abbreviations() -> None:
    structure = DocumentStructure("root", ())
    title = source_title("Sword World RPG - Complete Edition.pdf", structure=structure)

    assert title == "Sword World RPG Complete Edition"


def test_append_source_page_links_adds_walkable_derived_pages() -> None:
    page = WikiPage.from_metadata(
        PageMetadata(
            page_id="source-procedure-build-item",
            page_kind="procedure",
            summary="Build Item: 3 ordered step(s) from raw/source.pdf.",
        ),
        "# Build Item\n",
    )

    body = append_source_page_links("# Source\n", "Procedure Guides", (page,))

    assert "## Procedure Guides" in body
    assert (
        "- [[source-procedure-build-item]] - Build Item: 3 ordered step(s) from raw/source.pdf."
        in body
    )
