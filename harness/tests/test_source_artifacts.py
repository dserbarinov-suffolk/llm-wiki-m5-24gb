from __future__ import annotations

import json
from types import SimpleNamespace

import pytest

from llmwiki.application.source_artifacts import (
    build_canonical_ledger_source,
    canonical_source_artifact_from_json,
    canonical_source_artifact_to_json,
)
from llmwiki.domain.ledger.builder import SegmentInput
from llmwiki.domain.ledger.extraction import ExtractedUnitProfile
from llmwiki.domain.ledger.segments import SourceSegment

SOURCE_HASH = "b" * 64


def test_canonical_source_artifact_preserves_source_order_and_evidence() -> None:
    source = _canonical_source(
        (
            _input("segment-00001", 1, "heading", "# Root"),
            _input("segment-00002", 2, "paragraph", "A supported sentence."),
            _input("segment-00003", 3, "code-fence", "```\nconst answer = 42;\n```"),
        )
    )
    artifact = source.artifact

    assert [unit.source_order for unit in artifact.source_units] == [1, 2, 3]
    assert all(span.source_unit_ids for span in artifact.evidence_spans)
    assert all(
        "wiki" not in selector.value
        for span in artifact.evidence_spans
        for selector in span.selectors
    )
    assert artifact.source_units[1].parent_id == artifact.source_units[0].id
    assert artifact.technical_atoms[0].atom_kind == "code_block"
    assert artifact.technical_atoms[0].context_span_ids == (artifact.evidence_spans[0].id,)


def test_canonical_source_artifact_preserves_complete_table_and_formula_atoms() -> None:
    table = "| Name | Value |\n| --- | --- |\n| Size | 5 |"
    formula = "speed = distance / time"
    source = _canonical_source(
        (
            _input("segment-00001", 1, "table-block", table),
            _input("segment-00002", 2, "formula", formula),
        )
    )

    atoms = {atom.atom_kind.value: atom.exact_payload for atom in source.artifact.technical_atoms}

    assert atoms["table"] == table
    assert atoms["formula"] == formula


def test_canonical_source_artifact_round_trips_json() -> None:
    source = _canonical_source((_input("segment-00001", 1, "paragraph", "A sentence."),))
    text = canonical_source_artifact_to_json(source.artifact)

    roundtripped = canonical_source_artifact_from_json(text)

    assert roundtripped == source.artifact
    assert json.loads(text)["source_artifact_fingerprint"]


def test_canonical_source_artifact_requires_segments() -> None:
    with pytest.raises(ValueError, match="at least one segment"):
        build_canonical_ledger_source(
            source_locator="source.pdf",
            source_hash=SOURCE_HASH,
            segment_inputs=(),
            profiles={},
        )


def _canonical_source(inputs: tuple[SegmentInput, ...]):
    return build_canonical_ledger_source(
        source_locator="source.pdf",
        source_hash=SOURCE_HASH,
        segment_inputs=inputs,
        profiles={
            item.segment.segment_id: ExtractedUnitProfile(
                item.segment.segment_id,
                item.segment.source_range_id,
                (),
            )
            for item in inputs
        },
    )


def _input(segment_id: str, order: int, kind: str, text: str) -> SegmentInput:
    source_range_id = f"source-range-{order:05d}"
    return SegmentInput(
        SourceSegment(
            segment_id=segment_id,
            source_range_id=source_range_id,
            source_locator="source.pdf",
            source_hash=SOURCE_HASH,
            heading_path="Root",
            structure_node_id="",
            source_order=order,
            text=text,
            segment_kind=kind,
            evidence_ids=(f"evidence-{order}",),
            source_unit_id=f"unit-{order:04d}",
            source_blocks=(_block(kind, text),),
        )
    )


def _block(kind: str, text: str) -> SimpleNamespace:
    return SimpleNamespace(
        page_start=1,
        page_end=1,
        code_text=text if kind == "code-fence" else "",
        table_text=text if kind == "table-block" else "",
        formula_text=text if kind == "formula" else "",
    )
