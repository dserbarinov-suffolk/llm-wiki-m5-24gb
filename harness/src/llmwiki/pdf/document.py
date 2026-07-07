"""Structured PDF extraction domain objects.

DoclingExtractor creates DocumentModel.
SourceSectionBuilder creates SourceSection.
SourceUnitBuilder creates SourceUnit.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass

from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile


@dataclass(frozen=True)
class DocumentElement:
    element_id: str
    element_kind: str
    body_state: str
    heading_path: str
    page_start: int
    page_end: int
    text: str
    markdown: str
    heading_level: int = 0
    layout_font_size: float = 0.0
    layout_x0: float = 0.0
    layout_y0: float = 0.0


@dataclass(frozen=True)
class DocumentModel:
    source_locator: str
    source_hash: str
    extractor_name: str
    extractor_version: str
    elements: tuple[DocumentElement, ...]


@dataclass(frozen=True)
class SourceSection:
    section_id: str
    heading_path: str
    page_start: int
    page_end: int
    element_ids: tuple[str, ...]
    text: str


@dataclass(frozen=True)
class SourceUnitBlock:
    element_id: str
    block_kind: str
    heading_path: str
    page_start: int
    page_end: int
    text: str
    code_text: str = ""
    table_text: str = ""
    formula_text: str = ""
    heading_level: int = 0


@dataclass(frozen=True)
class SourceUnit:
    unit_id: str
    source_section_id: str
    heading_path: str
    page_start: int
    page_end: int
    element_ids: tuple[str, ...]
    blocks: tuple[SourceUnitBlock, ...]
    token_estimate: int


def document_model_to_json(model: DocumentModel) -> str:
    return json.dumps(asdict(model), indent=2, ensure_ascii=False)


def document_model_from_json(text: str) -> DocumentModel:
    data = json.loads(text)
    return DocumentModel(
        source_locator=data["source_locator"],
        source_hash=data["source_hash"],
        extractor_name=data["extractor_name"],
        extractor_version=data["extractor_version"],
        elements=tuple(DocumentElement(**element) for element in data["elements"]),
    )


def source_sections_to_json(sections: tuple[SourceSection, ...]) -> str:
    return json.dumps([asdict(section) for section in sections], indent=2, ensure_ascii=False)


def source_sections_from_json(text: str) -> tuple[SourceSection, ...]:
    data = json.loads(text)
    return tuple(
        SourceSection(
            section_id=section["section_id"],
            heading_path=section["heading_path"],
            page_start=section["page_start"],
            page_end=section["page_end"],
            element_ids=tuple(section["element_ids"]),
            text=section["text"],
        )
        for section in data
    )


def source_units_to_jsonl(units: tuple[SourceUnit, ...]) -> str:
    return "\n".join(json.dumps(asdict(unit), ensure_ascii=False) for unit in units) + "\n"


def source_units_from_jsonl(text: str) -> tuple[SourceUnit, ...]:
    units = []
    for line in text.splitlines():
        if not line.strip():
            continue
        data = json.loads(line)
        units.append(
            SourceUnit(
                unit_id=data["unit_id"],
                source_section_id=data["source_section_id"],
                heading_path=data["heading_path"],
                page_start=data["page_start"],
                page_end=data["page_end"],
                element_ids=tuple(data["element_ids"]),
                blocks=tuple(SourceUnitBlock(**block) for block in data["blocks"]),
                token_estimate=data["token_estimate"],
            )
        )
    return tuple(units)


def build_source_sections(model: DocumentModel) -> tuple[SourceSection, ...]:
    sections: list[SourceSection] = []
    current_heading = "Document"
    current_elements: list[DocumentElement] = []

    def flush() -> None:
        nonlocal current_elements
        section = _make_section(current_heading, current_elements, len(sections) + 1)
        if section is not None:
            sections.append(section)
        current_elements = []

    for element in model.elements:
        if element.body_state != "body":
            continue
        if not _element_markdown(element):
            continue
        if element.element_kind == "heading":
            flush()
            current_heading = element.heading_path or element.text or "Document"
            current_elements.append(element)
            continue
        element_heading = element.heading_path or current_heading
        if current_elements and element_heading != current_heading:
            flush()
            current_heading = element_heading
        elif not current_elements:
            current_heading = element_heading
        current_elements.append(element)

    flush()
    return tuple(sections)


def build_source_units(
    model: DocumentModel,
    sections: tuple[SourceSection, ...],
    budget_tokens: int | None = None,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> tuple[SourceUnit, ...]:
    resolved_budget = budget_tokens or model_profile.source_chunk_tokens
    units: list[SourceUnit] = []
    elements_by_id = {element.element_id: element for element in model.elements}

    for section in sections:
        section_elements = tuple(
            elements_by_id[element_id]
            for element_id in section.element_ids
            if element_id in elements_by_id
        )
        if not section_elements:
            _append_unit(units, section, (), model_profile=model_profile)
            continue

        current: list[DocumentElement] = []
        part_no = 1

        def flush(flush_section: SourceSection) -> None:
            nonlocal current, part_no
            if not current:
                return
            _append_unit(units, flush_section, current, model_profile=model_profile)
            current = []
            part_no += 1

        for element in section_elements:
            element_text = _element_render_text(element)
            if not element_text:
                continue
            candidate = _join_element_render_text((*current, element))
            if current and model_profile.estimate_tokens(candidate) > resolved_budget:
                flush(section)
            current.append(element)
        flush(section)

    return tuple(units)


def render_source_unit(unit: SourceUnit) -> str:
    return "\n\n".join(
        text for block in unit.blocks if (text := _render_source_unit_block(block))
    ).strip()


def render_source_units(units: tuple[SourceUnit, ...]) -> str:
    return "\n\n".join(rendered for unit in units if (rendered := render_source_unit(unit)))


def _append_unit(
    units: list[SourceUnit],
    section: SourceSection,
    elements: tuple[DocumentElement, ...] | list[DocumentElement],
    *,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> None:
    page_start, page_end = (
        _element_page_span(elements) if elements else (section.page_start, section.page_end)
    )
    blocks = tuple(_source_unit_block(element) for element in elements)
    text = "\n\n".join(_render_source_unit_block(block) for block in blocks).strip()
    units.append(
        SourceUnit(
            unit_id=f"unit-{len(units) + 1:04d}",
            source_section_id=section.section_id,
            heading_path=section.heading_path,
            page_start=page_start,
            page_end=page_end,
            element_ids=tuple(element.element_id for element in elements),
            blocks=blocks,
            token_estimate=model_profile.estimate_tokens(text),
        )
    )


def _make_section(
    heading_path: str, elements: list[DocumentElement], section_number: int
) -> SourceSection | None:
    text = _join_element_markdown(elements)
    if not text:
        return None
    page_start, page_end = _element_page_span(elements)
    return SourceSection(
        section_id=f"section-{section_number:04d}-{_slug(heading_path)}",
        heading_path=heading_path,
        page_start=page_start,
        page_end=page_end,
        element_ids=tuple(element.element_id for element in elements),
        text=text,
    )


def _join_element_markdown(elements: tuple[DocumentElement, ...] | list[DocumentElement]) -> str:
    return "\n\n".join(
        element_text for element in elements if (element_text := _element_markdown(element))
    ).strip()


def _join_element_render_text(
    elements: tuple[DocumentElement, ...] | list[DocumentElement],
) -> str:
    return "\n\n".join(
        element_text for element in elements if (element_text := _element_render_text(element))
    ).strip()


def _element_markdown(element: DocumentElement) -> str:
    return (element.markdown or element.text).strip()


def _element_render_text(element: DocumentElement) -> str:
    if element.element_kind == "heading":
        return f"{'#' * max(1, element.heading_level or 1)} {element.text}".strip()
    if element.element_kind == "code_block":
        text = element.text.strip()
        if not text:
            return ""
        return f"```\n{text.rstrip()}\n```"
    if element.element_kind == "table":
        return (element.markdown or element.text).strip()
    return (element.text or element.markdown).strip()


def _source_unit_block(element: DocumentElement) -> SourceUnitBlock:
    text = (element.text or "").strip()
    return SourceUnitBlock(
        element_id=element.element_id,
        block_kind=element.element_kind,
        heading_path=element.heading_path,
        page_start=element.page_start,
        page_end=element.page_end,
        text=text,
        code_text=text if element.element_kind == "code_block" else "",
        table_text=(element.markdown or text).strip() if element.element_kind == "table" else "",
        formula_text=text if element.element_kind == "formula" else "",
        heading_level=element.heading_level if element.element_kind == "heading" else 0,
    )


def _render_source_unit_block(block: SourceUnitBlock) -> str:
    if block.block_kind == "heading":
        text = block.text.strip()
        level = max(1, block.heading_level or 1)
        return f"{'#' * level} {text}" if text else ""
    if block.block_kind == "code_block":
        code = (block.code_text or block.text).strip()
        return f"```\n{code.rstrip()}\n```" if code else ""
    if block.block_kind == "table":
        return (block.table_text or block.text).strip()
    return block.text.strip()


def _element_page_span(
    elements: tuple[DocumentElement, ...] | list[DocumentElement],
) -> tuple[int, int]:
    page_starts = [element.page_start for element in elements if element.page_start > 0]
    page_ends = [element.page_end for element in elements if element.page_end > 0]
    if not page_starts or not page_ends:
        return (0, 0)
    return (min(page_starts), max(page_ends))


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:80] or "document"
