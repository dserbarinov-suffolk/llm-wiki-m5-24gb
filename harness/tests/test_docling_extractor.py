from types import SimpleNamespace
from typing import Any

from llmwiki.pdf.docling_extractor import (
    _pdf_code_text,
    document_model_from_docling_document,
)


class _Doc:
    def __init__(self, items: tuple[Any, ...]) -> None:
        self.items = items

    def iterate_items(self) -> tuple[tuple[Any, int], ...]:
        return tuple((item, 1) for item in self.items)


class _PdfDoc:
    def __init__(self, page: Any) -> None:
        self.page = page

    def __len__(self) -> int:
        return 1

    def __getitem__(self, index: int) -> Any:
        assert index == 0
        return self.page


class _Page:
    def __init__(self) -> None:
        self.rect = SimpleNamespace(height=100.0)
        self.clip = None

    def get_text(self, kind: str, *, clip: Any, sort: bool) -> list[tuple[Any, ...]]:
        assert kind == "blocks"
        assert sort is True
        self.clip = clip
        return [
            (0, 0, 0, 0, "line one\nline two", 0, 0),
            (0, 0, 0, 0, "}", 0, 0),
        ]


def test_docling_code_block_uses_resolved_multiline_source_text() -> None:
    item = SimpleNamespace(
        label="code",
        text="line one line two }",
        prov=(SimpleNamespace(page_no=1),),
    )

    model = document_model_from_docling_document(
        _Doc((item,)),
        source_locator="source.pdf",
        source_hash="abc",
        extractor_version="test",
        code_text_resolver=lambda _: "line one\nline two\n}",
    )

    assert len(model.elements) == 1
    element = model.elements[0]
    assert element.element_kind == "code_block"
    assert element.text == "line one\nline two\n}"
    assert element.markdown == "```\nline one\nline two\n}\n```"


def test_pdf_code_text_joins_block_text_inside_docling_bbox() -> None:
    page = _Page()
    pdf_doc = _PdfDoc(page)
    bbox = SimpleNamespace(
        l=10,
        r=20,
        t=60,
        b=50,
        coord_origin=SimpleNamespace(value="BOTTOMLEFT"),
    )
    item = SimpleNamespace(prov=(SimpleNamespace(page_no=1, bbox=bbox),))

    text = _pdf_code_text(pdf_doc, item)

    assert text == "line one\nline two\n}"
    assert page.clip is not None
    assert page.clip.x0 == 9.0
    assert page.clip.y0 == 39.0
    assert page.clip.x1 == 21.0
    assert page.clip.y1 == 51.0
