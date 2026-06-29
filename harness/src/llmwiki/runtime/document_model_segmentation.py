"""Segment structured PDF document models for the claim-ledger adapter."""

from __future__ import annotations

import re

from llmwiki.domain.evidence_locator_index import EvidenceIdentity
from llmwiki.domain.ledger.builder import SegmentInput
from llmwiki.domain.ledger.extraction import ExtractedUnitProfile
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.objects import Schema
from llmwiki.domain.planning import derive_segment_claims
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.runtime.document_model_table_runs import (
    preserve_table_section_heading,
    table_run_end,
    table_text,
)

_FENCE = re.compile(r"^\s*(```|~~~)")
_PROSE_KINDS = ("paragraph", "list")


def segment_document_model(
    model: DocumentModel,
    *,
    source_locator: str,
    source_hash: str,
    schema: Schema,
) -> tuple[tuple[SegmentInput, ...], dict[str, ExtractedUnitProfile]]:
    elements = tuple(element for element in model.elements if _body_element(element))
    inputs: list[SegmentInput] = []
    profiles: dict[str, ExtractedUnitProfile] = {}
    order = 0
    index = 0
    while index < len(elements):
        table_end = table_run_end(elements, index)
        if table_end > index:
            group = elements[index:table_end]
            if preserve_table_section_heading(group):
                order += 1
                _append_segment(
                    inputs,
                    profiles,
                    order=order,
                    kind="heading",
                    text=_element_segment_text(group[0], "heading"),
                    heading_path=group[0].heading_path,
                    page_locator=_page_locator((group[0],)),
                    source_element_ids=(group[0].element_id,),
                    source_locator=source_locator,
                    source_hash=source_hash,
                    schema=schema,
                )
            kind = "table-block"
            text = table_text(group)
            index = table_end
        else:
            group = (elements[index],)
            kind = _element_segment_kind(elements[index])
            text = _element_segment_text(elements[index], kind)
            index += 1
        if not text:
            continue
        order += 1
        _append_segment(
            inputs,
            profiles,
            order=order,
            kind=kind,
            text=text,
            heading_path=group[-1].heading_path,
            page_locator=_page_locator(group),
            source_element_ids=tuple(element.element_id for element in group),
            source_locator=source_locator,
            source_hash=source_hash,
            schema=schema,
        )
    return tuple(inputs), profiles


def _append_segment(
    inputs: list[SegmentInput],
    profiles: dict[str, ExtractedUnitProfile],
    *,
    order: int,
    kind: str,
    text: str,
    heading_path: str,
    page_locator: str,
    source_locator: str,
    source_hash: str,
    source_element_ids: tuple[str, ...],
    schema: Schema,
) -> None:
    range_id = f"source-range-{source_hash[:8]}-{order:05d}"
    evidence_id = EvidenceIdentity.from_excerpt(
        source_locator, source_hash, page_locator, text
    ).evidence_id
    segment = SourceSegment(
        segment_id=f"segment-{order:05d}",
        source_range_id=range_id,
        source_locator=source_locator,
        source_hash=source_hash,
        heading_path=heading_path,
        structure_node_id="",
        source_order=order,
        text=text,
        segment_kind=kind,
        evidence_ids=(evidence_id,),
        source_element_ids=source_element_ids,
    )
    inputs.append(SegmentInput(segment=segment, claims=_claims(kind, text, (evidence_id,), schema)))
    profiles[segment.segment_id] = profile_unit(
        extracted_unit_id=segment.segment_id,
        source_range_id=range_id,
        text=text,
        evidence_ids=(evidence_id,),
    )


def _claims(
    kind: str, text: str, evidence_ids: tuple[str, ...], schema: Schema
) -> tuple[SegmentClaim, ...]:
    if kind not in _PROSE_KINDS:
        return ()
    records = derive_segment_claims(text, schema)
    return tuple(
        SegmentClaim(
            claim_id=f"segment-claim-{index:03d}-{evidence_ids[0]}",
            statement=record.statement,
            role_tags=record.role_tags,
            eligibility=record.eligibility,
            certainty=record.certainty,
            evidence_ids=evidence_ids,
        )
        for index, record in enumerate(records, start=1)
    )


def _body_element(element: DocumentElement) -> bool:
    if element.body_state != "body":
        return False
    if element.element_kind == "picture":
        return True
    return bool((element.text or element.markdown).strip())


def _element_segment_kind(element: DocumentElement) -> str:
    if element.element_kind == "heading":
        return "heading"
    if element.element_kind == "code_block":
        return "code-fence"
    if element.element_kind == "table":
        return "table-block"
    if element.element_kind == "picture":
        return "figure"
    if element.element_kind == "list_item":
        return "list"
    return "paragraph"


def _element_segment_text(element: DocumentElement, kind: str) -> str:
    if kind == "heading":
        level = element.heading_level or _markdown_heading_level(element.markdown) or 1
        return f"{'#' * level} {_collapse_spaces(element.text)}".strip()
    if kind == "code-fence":
        first_line = (element.markdown or "").splitlines()[0] if element.markdown else ""
        if _FENCE.match(first_line):
            return element.markdown.strip()
        return f"```\n{element.text.rstrip()}\n```"
    if kind == "list":
        return _collapse_spaces(element.markdown or element.text)
    if kind == "figure":
        caption = _collapse_spaces(element.text or element.markdown)
        locator = _page_locator((element,))
        label = f"[Figure: {caption}]" if caption else "[Figure]"
        return f"{label} ({locator})"
    return _collapse_spaces(element.text)


def _markdown_heading_level(markdown: str) -> int:
    match = re.match(r"^\s{0,3}(#{1,6})\s", markdown)
    return len(match.group(1)) if match else 0


def _page_locator(elements: tuple[DocumentElement, ...]) -> str:
    starts = [element.page_start for element in elements if element.page_start > 0]
    ends = [element.page_end for element in elements if element.page_end > 0]
    if not starts or not ends:
        return "document"
    start, end = min(starts), max(ends)
    return f"p.{start}" if start == end else f"p.{start}-{end}"


def _collapse_spaces(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()
