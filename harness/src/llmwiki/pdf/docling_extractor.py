"""Docling adapter for DocumentModel.

This module keeps Docling-specific types out of the PDF domain objects.
"""

from __future__ import annotations

from collections.abc import Callable
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any

import pymupdf

from llmwiki.pdf.document import DocumentElement, DocumentModel

CodeTextResolver = Callable[[Any], str]


def extract_document_model(pdf_path: Path, source_locator: str, source_hash: str) -> DocumentModel:
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import (
        PdfPipelineOptions,
    )
    from docling.document_converter import (
        DocumentConverter,
        PdfFormatOption,
    )

    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = False
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    )
    result = converter.convert(pdf_path)
    with pymupdf.open(pdf_path) as pdf_doc:  # type: ignore[no-untyped-call]
        def code_text_resolver(item: Any) -> str:
            return _pdf_code_text(pdf_doc, item)

        return document_model_from_docling_document(
            result.document,
            source_locator=source_locator,
            source_hash=source_hash,
            extractor_version=_docling_version(),
            code_text_resolver=code_text_resolver,
        )


def document_model_from_docling_document(
    document: Any,
    source_locator: str,
    source_hash: str,
    extractor_version: str,
    code_text_resolver: CodeTextResolver | None = None,
) -> DocumentModel:
    heading_stack: list[str] = []
    elements: list[DocumentElement] = []

    for item, _level in document.iterate_items():
        text = _item_text(item)
        element_kind = _element_kind(item)
        if element_kind == "code_block" and code_text_resolver is not None:
            text = code_text_resolver(item) or text
        if not text and element_kind != "picture":
            continue

        heading_level = _heading_level(item) if element_kind == "heading" else 0
        if element_kind == "heading":
            level = heading_level
            del heading_stack[level - 1 :]
            heading_stack.append(text)
            heading_path = " > ".join(heading_stack)
        else:
            heading_path = " > ".join(heading_stack) or "Document"

        page_start, page_end = _page_span(item)
        body_state = _body_state(item, heading_path, text)
        markdown = _item_markdown(item, element_kind, text)

        elements.append(
            DocumentElement(
                element_id=f"element-{len(elements) + 1:06d}",
                element_kind=element_kind,
                body_state=body_state,
                heading_path=heading_path,
                page_start=page_start,
                page_end=page_end,
                text=text,
                markdown=markdown,
                heading_level=heading_level,
            )
        )

    return DocumentModel(
        source_locator=source_locator,
        source_hash=source_hash,
        extractor_name="docling",
        extractor_version=extractor_version,
        elements=tuple(elements),
    )


def _docling_version() -> str:
    try:
        return version("docling")
    except PackageNotFoundError:
        return "unknown"


def _element_kind(item: Any) -> str:
    label = _enum_value(getattr(item, "label", ""))
    if label == "section_header":
        return "heading"
    if label == "code":
        return "code_block"
    if label == "table":
        return "table"
    if label == "list_item":
        return "list_item"
    if label == "picture":
        return "picture"
    return "paragraph"


def _heading_level(item: Any) -> int:
    raw_level = getattr(item, "level", 1) or 1
    try:
        level = int(raw_level)
    except (TypeError, ValueError):
        level = 1
    return max(1, min(level, 6))


def _item_text(item: Any) -> str:
    text = getattr(item, "text", "")
    if text is None:
        return ""
    return str(text).strip()


def _pdf_code_text(pdf_doc: Any, item: Any) -> str:
    parts: list[str] = []
    for prov in getattr(item, "prov", []) or []:
        page_no = _page_no(prov)
        if page_no <= 0 or page_no > len(pdf_doc):
            continue
        bbox = getattr(prov, "bbox", None)
        if bbox is None:
            continue
        page = pdf_doc[page_no - 1]
        text = _text_from_page_blocks(page, _clip_rect(page, bbox))
        if text:
            parts.append(text)
    return "\n".join(parts).strip()


def _page_no(prov: Any) -> int:
    try:
        return int(getattr(prov, "page_no", 0))
    except (TypeError, ValueError):
        return 0


def _clip_rect(page: Any, bbox: Any) -> pymupdf.Rect:
    left = _float_attr(bbox, "l")
    right = _float_attr(bbox, "r")
    top = _float_attr(bbox, "t")
    bottom = _float_attr(bbox, "b")
    origin = _enum_value(getattr(bbox, "coord_origin", "")).lower()
    if origin == "bottomleft":
        page_height = float(page.rect.height)
        y0 = page_height - max(top, bottom)
        y1 = page_height - min(top, bottom)
    else:
        y0 = min(top, bottom)
        y1 = max(top, bottom)
    x0 = min(left, right)
    x1 = max(left, right)
    pad = 1.0
    return pymupdf.Rect(x0 - pad, y0 - pad, x1 + pad, y1 + pad)  # type: ignore[no-untyped-call]


def _float_attr(value: Any, attr: str) -> float:
    try:
        return float(getattr(value, attr))
    except (TypeError, ValueError):
        return 0.0


def _text_from_page_blocks(page: Any, rect: pymupdf.Rect) -> str:
    blocks = page.get_text("blocks", clip=rect, sort=True)
    parts = [str(block[4]).strip() for block in blocks if len(block) > 4 and str(block[4]).strip()]
    return "\n".join(parts).strip()


def _item_markdown(item: Any, element_kind: str, text: str) -> str:
    exported = _exported_markdown(item)
    if not text:
        return exported
    if element_kind == "heading":
        level = _heading_level(item)
        return f"{'#' * level} {text}"
    if element_kind == "code_block":
        if _has_fence(exported):
            return exported
        return f"```\n{text.rstrip()}\n```"
    if element_kind == "table" and exported:
        return exported
    if element_kind == "list_item" and not text.lstrip().startswith(("-", "*")):
        return f"- {text}"
    return text


def _exported_markdown(item: Any) -> str:
    for name in ("export_to_markdown", "to_markdown"):
        export = getattr(item, name, None)
        if not callable(export):
            continue
        try:
            value = export()
        except TypeError:
            continue
        if value is not None and str(value).strip():
            return str(value).strip()
    return ""


def _has_fence(markdown: str) -> bool:
    stripped = markdown.lstrip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def _page_span(item: Any) -> tuple[int, int]:
    pages: list[int] = []
    for prov in getattr(item, "prov", []) or []:
        page_no = getattr(prov, "page_no", 0)
        try:
            page = int(page_no)
        except (TypeError, ValueError):
            page = 0
        if page > 0:
            pages.append(page)
    if not pages:
        return (0, 0)
    return (min(pages), max(pages))


def _body_state(item: Any, heading_path: str, text: str) -> str:
    content_layer = _enum_value(getattr(item, "content_layer", "body"))
    if content_layer and content_layer != "body":
        return "furniture"
    heading_parts = [part.strip() for part in heading_path.split(">")]
    if _is_table_of_contents(text) or any(_is_table_of_contents(part) for part in heading_parts):
        return "table_of_contents"
    return "body"


def _is_table_of_contents(value: str) -> bool:
    normalized = " ".join(value.lower().split())
    return normalized in {"contents", "table of contents"}


def _enum_value(value: Any) -> str:
    raw = getattr(value, "value", value)
    return str(raw)
