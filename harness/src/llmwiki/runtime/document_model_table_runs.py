"""Detect table runs in structured document model elements."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.tabular import row_marker_count
from llmwiki.pdf.document import DocumentElement

_ROW_CONTINUATION_LOOKAHEAD = 10
_TABLE_RUN_ELEMENT_LIMIT = 80


def table_run_end(elements: tuple[DocumentElement, ...], start: int) -> int:
    element = elements[start]
    if element.element_kind == "table":
        return start + 1
    if element.element_kind == "heading":
        return _heading_table_end(elements, start)
    if row_marker_count(element.text or element.markdown) > 0:
        return _row_run_end(elements, start)
    return start


def table_text(elements: tuple[DocumentElement, ...]) -> str:
    return "\n".join(
        text for element in elements if (text := _table_element_text(element).strip())
    ).strip()


def preserve_table_section_heading(elements: tuple[DocumentElement, ...]) -> bool:
    if not elements or elements[0].element_kind != "heading":
        return False
    heading = _collapse_spaces(elements[0].text)
    return bool(heading and not _table_caption_heading(heading))


def _heading_table_end(elements: tuple[DocumentElement, ...], start: int) -> int:
    if start + 1 < len(elements) and elements[start + 1].element_kind == "heading":
        return start
    row_count = 0
    non_row_before_rows = 0
    end = start + 1
    index = start + 1
    while index < len(elements) and index <= start + _TABLE_RUN_ELEMENT_LIMIT:
        element = elements[index]
        if element.element_kind in {"heading", "code_block", "picture"}:
            break
        if not _same_table_scope(elements[start], element):
            break
        count = row_marker_count(element.text or element.markdown)
        if count:
            row_count += count
            end = index + 1
            index += 1
            continue
        if row_count and _row_continues_ahead(elements, index):
            end = index + 1
            index += 1
            continue
        if row_count:
            break
        non_row_before_rows += 1
        if non_row_before_rows > 3:
            return start
        end = index + 1
        index += 1
    return end if row_count >= 2 else start


def _row_run_end(elements: tuple[DocumentElement, ...], start: int) -> int:
    row_count = 0
    index = start
    heading_path = elements[start].heading_path
    while index < len(elements):
        element = elements[index]
        if element.element_kind in {"heading", "code_block", "picture"}:
            break
        if element.heading_path != heading_path:
            break
        count = row_marker_count(element.text or element.markdown)
        if not count:
            if row_count and _row_continues_ahead(elements, index):
                index += 1
                continue
            break
        row_count += count
        index += 1
    return index if row_count >= 2 else start


def _table_element_text(element: DocumentElement) -> str:
    if element.element_kind == "heading":
        return _collapse_spaces(element.text)
    if element.element_kind == "table" and element.markdown:
        return element.markdown
    return element.text or element.markdown


def _same_table_scope(start: DocumentElement, element: DocumentElement) -> bool:
    if element.heading_path == start.heading_path:
        return True
    if start.element_kind != "heading":
        return False
    heading = _collapse_spaces(start.text)
    if _table_caption_heading(heading):
        return True
    return element.heading_path.endswith(f" > {heading}")


def _table_caption_heading(text: str) -> bool:
    lowered = text.casefold()
    return lowered.startswith(("table-", "table ", "tab. ")) or "table below" in lowered


def _row_continues_ahead(elements: tuple[DocumentElement, ...], index: int) -> bool:
    element = elements[index]
    if element.element_kind in {"heading", "code_block", "picture"}:
        return False
    for next_element in elements[index + 1 : index + _ROW_CONTINUATION_LOOKAHEAD + 1]:
        if next_element.element_kind in {"heading", "code_block", "picture"}:
            return False
        if next_element.heading_path != element.heading_path:
            return False
        if row_marker_count(next_element.text or next_element.markdown) > 0:
            return True
    return False


def _collapse_spaces(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()
