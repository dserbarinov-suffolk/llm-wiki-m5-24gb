from llmwiki.domain.objects import Schema
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.runtime.document_model_segmentation import segment_document_model


def _element(
    element_id: str,
    element_kind: str,
    heading_path: str,
    text: str,
    *,
    page: int = 1,
    heading_level: int = 0,
    body_state: str = "body",
) -> DocumentElement:
    markdown = f"{'#' * heading_level} {text}" if element_kind == "heading" else text
    return DocumentElement(
        element_id=element_id,
        element_kind=element_kind,
        body_state=body_state,
        heading_path=heading_path,
        page_start=page,
        page_end=page,
        text=text,
        markdown=markdown,
        heading_level=heading_level,
    )


def _model(elements: tuple[DocumentElement, ...]) -> DocumentModel:
    return DocumentModel(
        source_locator="generic.pdf",
        source_hash="a" * 64,
        extractor_name="test",
        extractor_version="test",
        elements=elements,
    )


def test_document_model_segmentation_groups_heading_scoped_table_rows() -> None:
    model = _model(
        (
            _element("e1", "heading", "Outcome Matrix", "Outcome Matrix", heading_level=1),
            _element("e2", "heading", "Score Result", "Score Result", heading_level=2),
            _element(
                "e3",
                "paragraph",
                "Outcome Matrix > Score Result",
                "The row number identifies the result.",
            ),
            _element("e4", "list_item", "Outcome Matrix > Score Result", "2 Fractured axle"),
            _element("e5", "paragraph", "Outcome Matrix > Score Result", "Loose wheel"),
            _element("e6", "list_item", "Outcome Matrix > Score Result", "3 requires a repair"),
            _element("e7", "list_item", "Outcome Matrix > Score Result", "4 Stable frame"),
            _element("e8", "heading", "Aftermath", "Aftermath", heading_level=1),
        )
    )

    inputs, _profiles = segment_document_model(
        model, source_locator="generic.pdf", source_hash="b" * 64, schema=Schema()
    )

    kinds = [item.segment.segment_kind for item in inputs]
    assert kinds == ["heading", "table-block", "heading"]
    table = inputs[1].segment.text
    assert "Score Result" in table
    assert "2 Fractured axle" in table
    assert "Loose wheel" in table
    assert "4 Stable frame" in table


def test_document_model_segmentation_groups_inline_enumerated_rows() -> None:
    model = _model(
        (
            _element("e1", "heading", "Catalog", "Catalog", heading_level=1),
            _element(
                "e2",
                "paragraph",
                "Catalog",
                "9 Alpha entry. 10 Beta entry. 11 Gamma entry. 12 Delta entry.",
            ),
        )
    )

    inputs, _profiles = segment_document_model(
        model, source_locator="generic.pdf", source_hash="c" * 64, schema=Schema()
    )

    assert [item.segment.segment_kind for item in inputs] == ["table-block"]
    assert "9 Alpha entry" in inputs[0].segment.text


def test_document_model_segmentation_groups_range_value_rows() -> None:
    model = _model(
        (
            _element(
                "e1",
                "paragraph",
                "Range Table",
                "18-19 +4 20-21 +5 22-23 +6 24-25 +7",
            ),
        )
    )

    inputs, _profiles = segment_document_model(
        model, source_locator="generic.pdf", source_hash="f" * 64, schema=Schema()
    )

    assert [item.segment.segment_kind for item in inputs] == ["table-block"]


def test_document_model_segmentation_rejects_incidental_prose_numbers_as_table() -> None:
    model = _model(
        (
            _element(
                "e1",
                "paragraph",
                "Combat Example",
                "The operator rolled a 1 and a 3. The target has 5 HP and 11 STR. "
                "The result causes 6 damage.",
            ),
        )
    )

    inputs, _profiles = segment_document_model(
        model, source_locator="generic.pdf", source_hash="d" * 64, schema=Schema()
    )

    assert [item.segment.segment_kind for item in inputs] == ["paragraph"]


def test_document_model_segmentation_preserves_body_picture_as_figure() -> None:
    model = _model((_element("e1", "picture", "Illustrations", "", page=2),))

    inputs, _profiles = segment_document_model(
        model, source_locator="generic.pdf", source_hash="e" * 64, schema=Schema()
    )

    assert [item.segment.segment_kind for item in inputs] == ["figure"]
    assert inputs[0].segment.source_element_ids == ("e1",)
    assert inputs[0].segment.text == "[Figure] (p.2)"
