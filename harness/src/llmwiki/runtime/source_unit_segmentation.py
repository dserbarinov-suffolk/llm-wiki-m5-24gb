"""Segment structured source units for the claim-ledger adapter."""

from __future__ import annotations

import re

from llmwiki.domain.evidence_locator_index import EvidenceIdentity
from llmwiki.domain.ledger.builder import SegmentInput
from llmwiki.domain.ledger.extraction import ExtractedUnitProfile
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.objects import Schema
from llmwiki.domain.planning import derive_segment_claims
from llmwiki.pdf.document import SourceUnit, SourceUnitBlock
from llmwiki.runtime.source_unit_table_runs import (
    block_raw_text,
    preserve_table_section_heading,
    table_run_end,
    table_text,
)

_PROSE_KINDS = ("paragraph", "list")


def segment_source_units(
    units: tuple[SourceUnit, ...],
    *,
    source_locator: str,
    source_hash: str,
    schema: Schema,
) -> tuple[tuple[SegmentInput, ...], dict[str, ExtractedUnitProfile]]:
    inputs: list[SegmentInput] = []
    profiles: dict[str, ExtractedUnitProfile] = {}
    order = 0
    for unit in units:
        body_blocks = tuple(block for block in unit.blocks if _body_block(block))
        index = 0
        while index < len(body_blocks):
            table_end = table_run_end(body_blocks, index)
            if table_end > index:
                group = body_blocks[index:table_end]
                if preserve_table_section_heading(group):
                    order = _append_segment(
                        inputs,
                        profiles,
                        order=order,
                        kind="heading",
                        text=_block_segment_text(group[0], "heading"),
                        blocks=(group[0],),
                        unit=unit,
                        source_locator=source_locator,
                        source_hash=source_hash,
                        schema=schema,
                    )
                kind = "table-block"
                text = table_text(group)
                index = table_end
            else:
                group = (body_blocks[index],)
                kind = _block_segment_kind(body_blocks[index])
                text = _block_segment_text(body_blocks[index], kind)
                index += 1
            if not text:
                continue
            order = _append_segment(
                inputs,
                profiles,
                order=order,
                kind=kind,
                text=text,
                blocks=group,
                unit=unit,
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
    blocks: tuple[SourceUnitBlock, ...],
    unit: SourceUnit,
    source_locator: str,
    source_hash: str,
    schema: Schema,
) -> int:
    next_order = order + 1
    range_id = f"source-range-{source_hash[:8]}-{next_order:05d}"
    evidence_id = EvidenceIdentity.from_excerpt(
        source_locator, source_hash, _page_locator(blocks, unit), text
    ).evidence_id
    segment = SourceSegment(
        segment_id=f"segment-{next_order:05d}",
        source_range_id=range_id,
        source_locator=source_locator,
        source_hash=source_hash,
        heading_path=blocks[-1].heading_path or unit.heading_path,
        structure_node_id="",
        source_order=next_order,
        text=text,
        segment_kind=kind,
        evidence_ids=(evidence_id,),
        source_element_ids=tuple(block.element_id for block in blocks),
        source_unit_id=unit.unit_id,
        source_block_ids=tuple(block.element_id for block in blocks),
        source_blocks=blocks,
        block_kind=blocks[0].block_kind if len({b.block_kind for b in blocks}) == 1 else "group",
    )
    inputs.append(SegmentInput(segment=segment, claims=_claims(kind, text, (evidence_id,), schema)))
    profiles[segment.segment_id] = profile_unit(
        extracted_unit_id=segment.segment_id,
        source_range_id=range_id,
        text=text,
        evidence_ids=(evidence_id,),
    )
    return next_order


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


def _body_block(block: SourceUnitBlock) -> bool:
    if block.block_kind == "picture":
        return True
    return bool(block_raw_text(block).strip())


def _block_segment_kind(block: SourceUnitBlock) -> str:
    if block.block_kind == "heading":
        return "heading"
    if block.block_kind == "code_block":
        return "code-fence"
    if block.block_kind == "table":
        return "table-block"
    if block.block_kind == "picture":
        return "figure"
    if block.block_kind == "list_item":
        return "list"
    return "paragraph"


def _block_segment_text(block: SourceUnitBlock, kind: str) -> str:
    if kind == "heading":
        return f"# {_collapse_spaces(block.text)}".strip()
    if kind == "code-fence":
        code = (block.code_text or block.text).rstrip()
        return f"```\n{code}\n```" if code.strip() else ""
    if kind == "table-block":
        return table_text((block,))
    if kind == "figure":
        caption = _collapse_spaces(block.text)
        label = f"[Figure: {caption}]" if caption else "[Figure]"
        return f"{label} ({_page_locator((block,), None)})"
    if kind == "list":
        return _collapse_spaces(block.text)
    return _collapse_spaces(block.text)


def _page_locator(blocks: tuple[SourceUnitBlock, ...], unit: SourceUnit | None) -> str:
    starts = [block.page_start for block in blocks if block.page_start > 0]
    ends = [block.page_end for block in blocks if block.page_end > 0]
    if not starts and unit is not None and unit.page_start > 0:
        starts = [unit.page_start]
    if not ends and unit is not None and unit.page_end > 0:
        ends = [unit.page_end]
    if not starts or not ends:
        return "document"
    start, end = min(starts), max(ends)
    return f"p.{start}" if start == end else f"p.{start}-{end}"


def _collapse_spaces(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()
