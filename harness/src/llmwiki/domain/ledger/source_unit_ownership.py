"""Source-neutral ownership decisions for extracted source units.

The gate decides which source-structure node owns each extracted segment before
claims and technical atoms are assembled into the ledger. It uses only reusable
signals recovered from the source: heading paths, source order, and labels
inside structured atom text.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger import structure_numbers
from llmwiki.domain.ledger.common import ReviewReason
from llmwiki.domain.ledger.segments import SourceSegment
from llmwiki.domain.ledger.structure import StructureNode
from llmwiki.domain.ledger.structure_build import StructurePlan

_STRUCTURED_SEGMENTS = {"table-block", "code-fence", "formula", "figure"}
_BOUNDARY_REVIEW_WINDOW = 3
_LABEL_MATCH_WINDOW = 16


@dataclass(frozen=True)
class SourceUnitOwnershipDecision:
    segment_id: str
    owner_node_id: str
    status: str
    reason_codes: tuple[str, ...] = ()

    @property
    def needs_atom_review(self) -> bool:
        return self.status == "review-only" or "boundary-adjacent-prose" in self.reason_codes

    def review_reason(self, evidence_ids: tuple[str, ...]) -> ReviewReason | None:
        if not self.needs_atom_review:
            return None
        detail = "source unit ownership is ambiguous for authoritative atom projection"
        if self.reason_codes:
            detail = f"{detail}: {', '.join(self.reason_codes)}"
        return ReviewReason("source-unit-ownership", detail, evidence_ids)


@dataclass(frozen=True)
class SourceUnitOwnershipPlan:
    decisions: tuple[SourceUnitOwnershipDecision, ...]

    def decision_for(self, segment_id: str) -> SourceUnitOwnershipDecision | None:
        return next((item for item in self.decisions if item.segment_id == segment_id), None)

    def owner_for(self, segment_id: str, default_node_id: str) -> str:
        decision = self.decision_for(segment_id)
        return decision.owner_node_id if decision is not None else default_node_id

    def same_owner(self, left_segment_id: str, right_segment_id: str) -> bool:
        left = self.decision_for(left_segment_id)
        right = self.decision_for(right_segment_id)
        return left is not None and right is not None and left.owner_node_id == right.owner_node_id


def build_source_unit_ownership_plan(
    segments: tuple[SourceSegment, ...],
    structure_plan: StructurePlan,
) -> SourceUnitOwnershipPlan:
    decisions: list[SourceUnitOwnershipDecision] = []
    nodes = tuple(structure_plan.nodes)
    for index, segment in enumerate(segments):
        default_node_id = structure_plan.node_for_segment.get(segment.segment_id, "")
        owner_node_id = default_node_id
        status = "owned"
        reasons: list[str] = []

        label_node = _label_owner(segment, nodes)
        if label_node is not None and label_node.structure_node_id != default_node_id:
            owner_node_id = label_node.structure_node_id
            status = "reassigned"
            reasons.append("internal-label-owner")

        if _boundary_adjacent_prose(segment, segments, index):
            status = "review-only" if status == "owned" else status
            reasons.append("boundary-adjacent-prose")

        decisions.append(
            SourceUnitOwnershipDecision(
                segment.segment_id,
                owner_node_id,
                status,
                tuple(dict.fromkeys(reasons)),
            )
        )
    return SourceUnitOwnershipPlan(tuple(decisions))


def _label_owner(segment: SourceSegment, nodes: tuple[StructureNode, ...]) -> StructureNode | None:
    if segment.segment_kind not in _STRUCTURED_SEGMENTS:
        return None
    label = _internal_label(segment.text)
    if not label:
        return None
    candidates = tuple(
        node for node in nodes if node.structure_node_kind != "root" and _labels_match(label, node)
    )
    if not candidates:
        return None
    nearby = tuple(
        node
        for node in candidates
        if abs(node.source_order - segment.source_order) <= _LABEL_MATCH_WINDOW
    )
    return min(
        nearby or candidates,
        key=lambda node: (abs(node.source_order - segment.source_order), node.source_order),
    )


def _internal_label(text: str) -> str:
    for raw_line in text.splitlines():
        line = structure_numbers.heading_text(raw_line).strip(" |")
        if not line:
            continue
        if _table_delimiter(line):
            continue
        if _looks_like_heading_label(line):
            return structure_numbers.canonical_heading_label(line)
        return ""
    return ""


def _looks_like_heading_label(text: str) -> bool:
    label = structure_numbers.canonical_heading_label(text)
    if structure_numbers.heading_number_path(label):
        return True
    return len(label.split()) <= 8 and any(char.isalpha() for char in label)


def _labels_match(label: str, node: StructureNode) -> bool:
    node_label = structure_numbers.canonical_heading_label(node.heading_text)
    return structure_numbers.same_heading(node_label, label) or structure_numbers.same_heading(
        label, node_label
    )


def _boundary_adjacent_prose(
    segment: SourceSegment, segments: tuple[SourceSegment, ...], index: int
) -> bool:
    if segment.segment_kind not in {"paragraph", "list"}:
        return False
    if not segment.text.strip():
        return False
    for next_segment in segments[index + 1 : index + _BOUNDARY_REVIEW_WINDOW + 1]:
        if next_segment.segment_kind == "heading":
            return True
        if next_segment.segment_kind not in {"blank"}:
            continue
    return False


def _table_delimiter(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and set(stripped) <= {"|", "-", ":", " "}
