"""Source-neutral text batching for ingest.

The batching contract is coverage-preserving: every non-empty source block is
assigned to exactly one chunk. The budget is a packing target, not a reason to
truncate source text.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile

_HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")
_FENCE = re.compile(r"^\s*(```|~~~)")
_PIPE = re.compile(r"\|")


@dataclass(frozen=True)
class SourceTextBlock:
    block_kind: str
    heading_path: str
    start_line: int
    end_line: int
    text: str


@dataclass(frozen=True)
class SourceTextSection:
    source_section_id: str
    heading_path: str
    start_line: int
    end_line: int
    blocks: tuple[SourceTextBlock, ...]

    @property
    def text(self) -> str:
        return "\n\n".join(block.text for block in self.blocks).strip()

    @property
    def locator(self) -> str:
        return line_locator(self.start_line, self.end_line)


@dataclass(frozen=True)
class SourceTextChunk:
    chunk_id: int
    source_section_id: str
    heading_path: str
    locator: str
    text: str
    token_estimate: int


def estimate_tokens(
    text: str, model_profile: ModelProfile = DEFAULT_MODEL_PROFILE
) -> int:
    return model_profile.estimate_tokens(text)


def line_locator(start_line: int, end_line: int) -> str:
    return f"lines:{start_line}" if start_line == end_line else f"lines:{start_line}-{end_line}"


def markdown_source_sections(
    text: str, default_heading: str = "Document"
) -> tuple[SourceTextSection, ...]:
    lines = text.splitlines()
    sections: list[SourceTextSection] = []
    blocks: list[SourceTextBlock] = []
    heading_stack: list[str] = []
    current_heading = default_heading or "Document"
    index = 0

    def flush_section(end_line: int) -> None:
        nonlocal blocks
        if not blocks:
            return
        start = blocks[0].start_line
        end = blocks[-1].end_line
        sections.append(
            SourceTextSection(
                source_section_id=f"section-{len(sections) + 1:04d}-{_slug(current_heading)}",
                heading_path=current_heading,
                start_line=start,
                end_line=end,
                blocks=tuple(blocks),
            )
        )
        blocks = []

    while index < len(lines):
        line = lines[index]
        line_number = index + 1
        heading_match = _HEADING.match(line)
        if heading_match is not None:
            flush_section(line_number - 1)
            level = len(heading_match.group(1))
            title = _collapse_spaces(heading_match.group(2))
            heading_stack = heading_stack[: level - 1]
            heading_stack.append(title)
            current_heading = " > ".join(heading_stack) or title or default_heading
            blocks.append(
                SourceTextBlock("heading", current_heading, line_number, line_number, line.strip())
            )
            index += 1
            continue
        if _FENCE.match(line):
            block, index = _consume_fence(lines, index, current_heading)
            blocks.append(block)
            continue
        if not line.strip():
            index += 1
            continue
        if _is_table_start(lines, index):
            block, index = _consume_table(lines, index, current_heading)
            blocks.append(block)
            continue
        block, index = _consume_paragraph(lines, index, current_heading)
        blocks.append(block)

    flush_section(len(lines))
    return tuple(sections)


def chunk_source_sections(
    sections: tuple[SourceTextSection, ...],
    *,
    budget_tokens: int | None = None,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> tuple[SourceTextChunk, ...]:
    resolved_budget = budget_tokens or model_profile.source_chunk_tokens
    chunks: list[SourceTextChunk] = []
    for section in sections:
        current: list[SourceTextBlock] = []

        def flush(source_section: SourceTextSection) -> None:
            nonlocal current
            if not current:
                return
            text = "\n\n".join(block.text for block in current).strip()
            chunks.append(
                SourceTextChunk(
                    chunk_id=len(chunks) + 1,
                    source_section_id=source_section.source_section_id,
                    heading_path=source_section.heading_path,
                    locator=line_locator(current[0].start_line, current[-1].end_line),
                    text=text,
                    token_estimate=model_profile.estimate_tokens(text),
                )
            )
            current = []

        for block in section.blocks:
            candidate = "\n\n".join((*[item.text for item in current], block.text))
            if current and model_profile.estimate_tokens(candidate) > resolved_budget:
                flush(section)
            current.append(block)
        flush(section)
    return tuple(chunks)


def markdown_source_chunks(
    text: str,
    default_heading: str = "Document",
    *,
    budget_tokens: int | None = None,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> tuple[SourceTextChunk, ...]:
    return chunk_source_sections(
        markdown_source_sections(text, default_heading),
        budget_tokens=budget_tokens,
        model_profile=model_profile,
    )


def _consume_fence(
    lines: list[str], start: int, heading_path: str
) -> tuple[SourceTextBlock, int]:
    index = start + 1
    while index < len(lines) and not _FENCE.match(lines[index]):
        index += 1
    end = min(index, len(lines) - 1)
    return (
        SourceTextBlock(
            "code-fence",
            heading_path,
            start + 1,
            end + 1,
            "\n".join(lines[start : end + 1]).strip(),
        ),
        end + 1,
    )


def _is_table_start(lines: list[str], index: int) -> bool:
    if not _PIPE.search(lines[index]):
        return False
    if index + 1 >= len(lines):
        return False
    return _PIPE.search(lines[index + 1]) is not None


def _consume_table(
    lines: list[str], start: int, heading_path: str
) -> tuple[SourceTextBlock, int]:
    index = start
    while index < len(lines) and lines[index].strip() and _PIPE.search(lines[index]):
        index += 1
    return (
        SourceTextBlock(
            "table",
            heading_path,
            start + 1,
            index,
            "\n".join(lines[start:index]).strip(),
        ),
        index,
    )


def _consume_paragraph(
    lines: list[str], start: int, heading_path: str
) -> tuple[SourceTextBlock, int]:
    index = start
    collected: list[str] = []
    while index < len(lines):
        line = lines[index]
        if (
            not line.strip()
            or _HEADING.match(line)
            or _FENCE.match(line)
            or _is_table_start(lines, index)
        ):
            break
        collected.append(line)
        index += 1
    text = "\n".join(_collapse_spaces(line) for line in collected).strip()
    return SourceTextBlock("paragraph", heading_path, start + 1, index, text), index


def _collapse_spaces(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:80] or "document"
