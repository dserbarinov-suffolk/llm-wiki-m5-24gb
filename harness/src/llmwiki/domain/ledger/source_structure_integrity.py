"""Source-neutral integrity rules for authored document structure."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

from llmwiki.domain.ledger import structure_numbers
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode

ADMITTED_HEADING_KINDS = frozenset({"trusted-heading", "container-heading"})
PAGE_DRIVER_DISPOSITIONS = frozenset({"trusted", "container"})
_FIELD_ASSIGNMENT = re.compile(r"\b[\w][\w /()-]{0,36}\s*=")
_ROW_SEPARATOR = re.compile(r"\s(?:=|:|/)\s")
_MARKDOWN_HEADING = re.compile(r"^\s{0,3}#{1,6}\s*")


@dataclass(frozen=True)
class HeadingCandidate:
    candidate_id: str
    text: str
    heading_level: int
    layout_font_size: float
    body_font_size: float
    layout_x0: float = 0.0
    layout_y0: float = 0.0


@dataclass(frozen=True)
class HeadingAdmissionDecision:
    candidate_id: str
    admission_kind: str
    reason_codes: tuple[str, ...]

    @property
    def admitted(self) -> bool:
        return self.admission_kind in ADMITTED_HEADING_KINDS


@dataclass(frozen=True)
class StructureNodeDisposition:
    structure_node_id: str
    disposition: str
    reason_codes: tuple[str, ...]

    @property
    def may_drive_pages(self) -> bool:
        return self.disposition in PAGE_DRIVER_DISPOSITIONS


@dataclass(frozen=True)
class StructureIntegrityFinding:
    structure_node_id: str
    severity: str
    category: str
    message: str


@dataclass(frozen=True)
class SourceStructureIntegrityReport:
    dispositions: tuple[StructureNodeDisposition, ...]
    findings: tuple[StructureIntegrityFinding, ...]


def heading_admission(candidate: HeadingCandidate) -> HeadingAdmissionDecision:
    text = _plain(candidate.text)
    reasons: list[str] = []
    if not text:
        return HeadingAdmissionDecision(candidate.candidate_id, "body-text", ("empty",))
    if not _has_heading_signal(candidate):
        reasons.append("weak-layout-signal")
    if _has_unbalanced_delimiters(text):
        return HeadingAdmissionDecision(
            candidate.candidate_id, "fragment", (*reasons, "unbalanced-delimiters")
        )
    if _is_bracket_wrapped_label(text):
        return HeadingAdmissionDecision(
            candidate.candidate_id, "record-label", (*reasons, "bracket-wrapped-label")
        )
    if _field_density(text) >= 2:
        return HeadingAdmissionDecision(
            candidate.candidate_id, "record-label", (*reasons, "field-dense")
        )
    if _looks_like_table_row(text):
        return HeadingAdmissionDecision(
            candidate.candidate_id, "table-row", (*reasons, "row-shaped")
        )
    if reasons:
        return HeadingAdmissionDecision(candidate.candidate_id, "body-text", tuple(reasons))
    if candidate.heading_level <= 1 and _short_label(text):
        return HeadingAdmissionDecision(candidate.candidate_id, "container-heading", ())
    return HeadingAdmissionDecision(candidate.candidate_id, "trusted-heading", ())


def source_structure_integrity_report(
    structure: DocumentStructure,
) -> SourceStructureIntegrityReport:
    dispositions = tuple(_node_disposition(node) for node in structure.structure_nodes)
    disposition_findings = tuple(
        StructureIntegrityFinding(
            item.structure_node_id,
            "warning",
            "source-structure",
            f"Structure node cannot drive pages: {', '.join(item.reason_codes)}.",
        )
        for item in dispositions
        if not item.may_drive_pages and item.reason_codes
    )
    hierarchy_findings = _hierarchy_findings(structure)
    return SourceStructureIntegrityReport(
        dispositions, (*disposition_findings, *hierarchy_findings)
    )


def structure_node_can_drive_pages(node: StructureNode) -> bool:
    return _node_disposition(node).may_drive_pages


def structure_nodes_that_drive_pages(
    structure: DocumentStructure,
) -> tuple[StructureNode, ...]:
    return tuple(node for node in structure.structure_nodes if structure_node_can_drive_pages(node))


def _node_disposition(node: StructureNode) -> StructureNodeDisposition:
    if node.structure_node_kind == "root":
        return StructureNodeDisposition(node.structure_node_id, "trusted", ())
    if node.structure_node_kind == "record":
        text = _plain(node.heading_text)
        record_reasons: list[str] = []
        if not text:
            record_reasons.append("empty")
        if _has_unbalanced_delimiters(text):
            record_reasons.append("unbalanced-delimiters")
        if _too_long_for_label(text):
            record_reasons.append("label-too-long")
        if record_reasons:
            return StructureNodeDisposition(
                node.structure_node_id, "evidence-only", tuple(record_reasons)
            )
        return StructureNodeDisposition(node.structure_node_id, "trusted", ())
    text = _plain(node.heading_text)
    reasons: list[str] = []
    if not text:
        reasons.append("empty")
    if _has_unbalanced_delimiters(text):
        reasons.append("unbalanced-delimiters")
    if _is_bracket_wrapped_label(text):
        reasons.append("bracket-wrapped-label")
    if _field_density(text) >= 2:
        reasons.append("field-dense")
    if _looks_like_table_row(text):
        reasons.append("row-shaped")
    if _too_long_for_label(text):
        reasons.append("label-too-long")
    if reasons:
        return StructureNodeDisposition(node.structure_node_id, "evidence-only", tuple(reasons))
    if node.depth <= 1:
        return StructureNodeDisposition(node.structure_node_id, "container", ())
    return StructureNodeDisposition(node.structure_node_id, "trusted", ())


def _hierarchy_findings(structure: DocumentStructure) -> tuple[StructureIntegrityFinding, ...]:
    findings: list[StructureIntegrityFinding] = []
    for node in structure.structure_nodes:
        if node.structure_node_kind == "root":
            continue
        nearest = _nearest_numbered_ancestor(structure, node)
        if nearest is None:
            continue
        nearest_node, nearest_path = nearest
        node_path = _number_path(node)
        if node_path and not structure_numbers.number_parent(nearest_path, node_path):
            findings.append(
                StructureIntegrityFinding(
                    node.structure_node_id,
                    "warning",
                    "source-structure",
                    (
                        f"Numbered heading {node.heading_text!r} is under "
                        f"{nearest_node.heading_text!r}, but its number path is not a descendant."
                    ),
                )
            )
            continue
        if not node_path and node.depth <= 1 and nearest_node.depth > 1:
            findings.append(
                StructureIntegrityFinding(
                    node.structure_node_id,
                    "warning",
                    "source-structure",
                    (
                        f"Top-level heading {node.heading_text!r} is under numbered subsection "
                        f"{nearest_node.heading_text!r}."
                    ),
                )
            )
    return tuple(findings)


def _nearest_numbered_ancestor(
    structure: DocumentStructure, node: StructureNode
) -> tuple[StructureNode, tuple[int, ...]] | None:
    for ancestor_id in structure.ancestry(node.structure_node_id)[1:]:
        ancestor = structure.node(ancestor_id)
        if ancestor is None or ancestor.structure_node_kind == "root":
            continue
        path = _number_path(ancestor)
        if path:
            return ancestor, path
    return None


def _number_path(node: StructureNode) -> tuple[int, ...]:
    return structure_numbers.heading_number_path(
        structure_numbers.canonical_heading_label(node.heading_text)
    )


def _has_heading_signal(candidate: HeadingCandidate) -> bool:
    if candidate.heading_level > 1:
        return True
    if candidate.body_font_size <= 0:
        return candidate.heading_level > 0
    return bool(
        candidate.layout_font_size
        and candidate.layout_font_size >= candidate.body_font_size * 1.08
    )


def _plain(text: str) -> str:
    return re.sub(r"\s+", " ", _MARKDOWN_HEADING.sub("", text)).strip()


def _short_label(text: str) -> bool:
    return 0 < len(text.split()) <= 12 and len(text) <= 96


def _too_long_for_label(text: str) -> bool:
    return len(text.split()) > 18 or len(text) > 160


def _field_density(text: str) -> int:
    return len(_FIELD_ASSIGNMENT.findall(text))


def _looks_like_table_row(text: str) -> bool:
    if "|" in text and text.count("|") >= 2:
        return True
    if _field_density(text) >= 1 and len(_ROW_SEPARATOR.findall(text)) >= 3:
        return True
    separators = Counter(char for char in text if char in "=:/;")
    return sum(separators.values()) >= 5 and len(text.split()) >= 8


def _has_unbalanced_delimiters(text: str) -> bool:
    pairs = (("[", "]"), ("(", ")"), ("{", "}"), ("【", "】"), ("《", "》"))
    return any(text.count(left) != text.count(right) for left, right in pairs)


def _is_bracket_wrapped_label(text: str) -> bool:
    if re.match(r"^\d+(?:\.\d+)*\s+", text):
        return False
    pairs = (("[", "]"), ("【", "】"), ("《", "》"))
    stripped = text.strip()
    return any(
        stripped.startswith(left)
        and stripped.endswith(right)
        and len(stripped.split()) <= 8
        for left, right in pairs
    )
