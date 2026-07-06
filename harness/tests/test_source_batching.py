from llmwiki.domain.source_batching import (
    chunk_source_sections,
    markdown_source_chunks,
    markdown_source_sections,
)


def test_markdown_headings_produce_source_sections() -> None:
    sections = markdown_source_sections(
        "# Alpha\n\nFirst claim.\n\n## Beta\n\nSecond claim.",
        "Document",
    )

    assert [section.heading_path for section in sections] == ["Alpha", "Alpha > Beta"]
    assert [section.locator for section in sections] == ["lines:1-3", "lines:5-7"]


def test_fenced_code_block_stays_in_one_chunk_when_budget_is_tiny() -> None:
    text = "# Example\n\n```js\nconst one = 1;\nconst two = 2;\n```\n\nAfterward."

    chunks = markdown_source_chunks(text, "Document", budget_tokens=1)

    code_chunks = [chunk for chunk in chunks if "const one" in chunk.text]
    assert len(code_chunks) == 1
    assert code_chunks[0].text == "```js\nconst one = 1;\nconst two = 2;\n```"
    assert code_chunks[0].locator == "lines:3-6"


def test_markdown_table_stays_in_one_chunk_when_budget_is_tiny() -> None:
    text = "# Table\n\n| Name | Value |\n| --- | --- |\n| A | 1 |\n| B | 2 |\n\nAfterward."

    chunks = markdown_source_chunks(text, "Document", budget_tokens=1)

    table_chunks = [chunk for chunk in chunks if "| Name | Value |" in chunk.text]
    assert len(table_chunks) == 1
    assert "| B | 2 |" in table_chunks[0].text
    assert table_chunks[0].locator == "lines:3-6"


def test_oversized_prose_splits_only_between_paragraph_blocks() -> None:
    sections = markdown_source_sections(
        "# Long\n\n"
        "First paragraph has enough words to exceed the small budget.\n\n"
        "Second paragraph has enough words to become another chunk.",
        "Document",
    )

    chunks = chunk_source_sections(sections, budget_tokens=3)

    assert [chunk.locator for chunk in chunks] == ["lines:1", "lines:3", "lines:5"]
    assert chunks[1].text.startswith("First paragraph")
    assert chunks[2].text.startswith("Second paragraph")


def test_chunking_preserves_every_non_empty_source_block_once() -> None:
    text = "# A\n\nAlpha.\n\n# B\n\nBeta.\n\n```go\nfmt.Println(\"gamma\")\n```"
    sections = markdown_source_sections(text, "Document")
    chunks = chunk_source_sections(sections, budget_tokens=2)

    rendered = "\n\n".join(chunk.text for chunk in chunks)

    assert "# A" in rendered
    assert "Alpha." in rendered
    assert "# B" in rendered
    assert "Beta." in rendered
    assert "fmt.Println" in rendered
