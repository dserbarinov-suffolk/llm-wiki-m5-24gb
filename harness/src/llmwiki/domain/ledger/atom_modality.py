"""Source-structure policy for technical atom extractor eligibility."""

from __future__ import annotations

from llmwiki.domain.ledger.notation import standalone_formula_candidate_line
from llmwiki.domain.ledger.segments import SourceSegment

_PROSE_CAPABILITIES = frozenset(
    {"rule-extractor", "procedure-extractor", "worked-example-extractor"}
)
_BLOCK_KIND_CAPABILITIES: dict[str, frozenset[str]] = {
    "code_block": frozenset({"code-block-extractor"}),
    "table": frozenset({"table-extractor"}),
    "formula": frozenset({"formula-extractor"}),
    "picture": frozenset({"figure-extractor"}),
}
_SEGMENT_KIND_CAPABILITIES: dict[str, frozenset[str]] = {
    "code-fence": frozenset({"code-block-extractor"}),
    "table-block": frozenset({"table-extractor"}),
    "formula": frozenset({"formula-extractor"}),
    "figure": frozenset({"figure-extractor"}),
    "paragraph": _PROSE_CAPABILITIES,
    "list": _PROSE_CAPABILITIES,
    "heading": frozenset(),
    "blank": frozenset(),
}


def allowed_capability_ids(segment: SourceSegment) -> frozenset[str]:
    """Return extractors compatible with the segment's source modality."""
    if segment.code_text.strip():
        return frozenset({"code-block-extractor"})
    if segment.table_text.strip():
        return frozenset({"table-extractor"})
    if segment.formula_text.strip():
        return frozenset({"formula-extractor"})
    if segment.block_kind in _BLOCK_KIND_CAPABILITIES:
        return _BLOCK_KIND_CAPABILITIES[segment.block_kind]
    allowed = _SEGMENT_KIND_CAPABILITIES.get(segment.segment_kind, _PROSE_CAPABILITIES)
    if segment.segment_kind in {"paragraph", "list"} and _has_standalone_formula(segment):
        return allowed | frozenset({"formula-extractor"})
    return allowed


def capability_allowed(segment: SourceSegment, capability_id: str) -> bool:
    return capability_id in allowed_capability_ids(segment)


def _has_standalone_formula(segment: SourceSegment) -> bool:
    return standalone_formula_candidate_line(segment.text) is not None
