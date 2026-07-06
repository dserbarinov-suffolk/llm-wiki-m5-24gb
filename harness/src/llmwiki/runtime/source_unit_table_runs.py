"""Detect table runs in structured source-unit blocks."""

from __future__ import annotations

import re

from llmwiki.domain.ledger.tabular import row_marker_count
from llmwiki.pdf.document import SourceUnitBlock

_ROW_CONTINUATION_LOOKAHEAD = 10
_TABLE_RUN_BLOCK_LIMIT = 80


def table_run_end(blocks: tuple[SourceUnitBlock, ...], start: int) -> int:
    block = blocks[start]
    if block.block_kind == "table":
        return start + 1
    if block.block_kind == "heading":
        return _heading_table_end(blocks, start)
    if row_marker_count(block_raw_text(block)) > 0:
        return _row_run_end(blocks, start)
    return start


def table_text(blocks: tuple[SourceUnitBlock, ...]) -> str:
    return "\n".join(
        text for block in blocks if (text := _table_block_text(block).strip())
    ).strip()


def preserve_table_section_heading(blocks: tuple[SourceUnitBlock, ...]) -> bool:
    if not blocks or blocks[0].block_kind != "heading":
        return False
    heading = _collapse_spaces(blocks[0].text)
    return bool(heading and not table_caption_heading(heading))


def block_raw_text(block: SourceUnitBlock) -> str:
    return block.table_text or block.code_text or block.formula_text or block.text


def table_caption_heading(text: str) -> bool:
    lowered = text.casefold()
    return lowered.startswith(("table-", "table ", "tab. ")) or "table below" in lowered


def _heading_table_end(blocks: tuple[SourceUnitBlock, ...], start: int) -> int:
    if start + 1 < len(blocks) and blocks[start + 1].block_kind == "heading":
        return start
    row_count = 0
    non_row_before_rows = 0
    end = start + 1
    index = start + 1
    while index < len(blocks) and index <= start + _TABLE_RUN_BLOCK_LIMIT:
        block = blocks[index]
        if block.block_kind in {"heading", "code_block", "picture"}:
            break
        if not _same_table_scope(blocks[start], block):
            break
        count = row_marker_count(block_raw_text(block))
        if count:
            row_count += count
            end = index + 1
            index += 1
            continue
        if row_count and _row_continues_ahead(blocks, index):
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


def _row_run_end(blocks: tuple[SourceUnitBlock, ...], start: int) -> int:
    row_count = 0
    index = start
    heading_path = blocks[start].heading_path
    while index < len(blocks):
        block = blocks[index]
        if block.block_kind in {"heading", "code_block", "picture"}:
            break
        if block.heading_path != heading_path:
            break
        count = row_marker_count(block_raw_text(block))
        if not count:
            if row_count and _row_continues_ahead(blocks, index):
                index += 1
                continue
            break
        row_count += count
        index += 1
    return index if row_count >= 2 else start


def _row_continues_ahead(blocks: tuple[SourceUnitBlock, ...], index: int) -> bool:
    block = blocks[index]
    if block.block_kind in {"heading", "code_block", "picture"}:
        return False
    for next_block in blocks[index + 1 : index + _ROW_CONTINUATION_LOOKAHEAD + 1]:
        if next_block.block_kind in {"heading", "code_block", "picture"}:
            return False
        if next_block.heading_path != block.heading_path:
            return False
        if row_marker_count(block_raw_text(next_block)) > 0:
            return True
    return False


def _table_block_text(block: SourceUnitBlock) -> str:
    if block.block_kind == "heading":
        return _collapse_spaces(block.text)
    if block.block_kind == "table" and block.table_text:
        return block.table_text
    return block_raw_text(block)


def _same_table_scope(start: SourceUnitBlock, block: SourceUnitBlock) -> bool:
    if block.heading_path == start.heading_path:
        return True
    if start.block_kind != "heading":
        return False
    heading = _collapse_spaces(start.text)
    if table_caption_heading(heading):
        return True
    return block.heading_path.endswith(f" > {heading}")


def _collapse_spaces(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()
