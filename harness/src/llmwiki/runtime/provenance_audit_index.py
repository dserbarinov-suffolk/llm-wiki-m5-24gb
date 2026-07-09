"""Index portable ledger artifacts for provenance auditing."""

from __future__ import annotations

import json
from bisect import bisect_right
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, cast

from llmwiki.runtime.provenance_audit_terms import fragmentary


@dataclass(frozen=True)
class ProvenanceEvidence:
    source_range_id: str
    section_path: str
    excerpt: str
    has_technical_atom: bool
    context_pointer: bool
    fragmentary: bool
    structure_only: bool


class ProvenanceArtifactIndex:
    def __init__(
        self,
        ledger: dict[str, Any],
        structure: dict[str, Any],
        source_coverage: dict[str, Any],
        projection_context: dict[str, Any],
    ) -> None:
        self._nodes = {node["structure_node_id"]: node for node in structure["structure_nodes"]}
        self._nodes_by_range = {
            node.get("source_range_id", ""): node
            for node in structure["structure_nodes"]
            if node.get("source_range_id")
        }
        nodes_by_order = sorted(
            (int(node.get("source_order", 0) or 0), node["structure_node_id"])
            for node in structure["structure_nodes"]
            if int(node.get("source_order", 0) or 0) > 0
        )
        self._node_orders = [item[0] for item in nodes_by_order]
        self._node_ids_by_order = [item[1] for item in nodes_by_order]
        self._entries_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._atoms_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._source_records_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._context_blocks_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._atom_frames_by_range: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._entries_by_id = {
            entry["ledger_entry_id"]: entry
            for entry in ledger["entries"]
            if entry.get("ledger_entry_id")
        }
        self._atoms_by_id = {
            atom["technical_atom_id"]: atom
            for atom in ledger["technical_atoms"]
            if atom.get("technical_atom_id")
        }
        for entry in ledger["entries"]:
            self._entries_by_range[entry["source_range_id"]].append(entry)
        for atom in ledger["technical_atoms"]:
            self._atoms_by_range[atom["source_range_id"]].append(atom)
        for record in source_coverage.get("records", ()):
            for source_range_id in record.get("source_range_ids", ()):
                self._source_records_by_range[source_range_id].append(record)
        for block in projection_context.get("evidence_blocks", ()):
            range_ids = block.get("source_range_ids") or (block.get("source_range_id", ""),)
            for source_range_id in range_ids:
                if source_range_id:
                    self._context_blocks_by_range[source_range_id].append(block)
        for frame in projection_context.get("atom_frames", ()):
            for source_range_id in frame.get("source_range_ids", ()):
                if source_range_id:
                    self._atom_frames_by_range[source_range_id].append(frame)
        self._order_by_range = {
            item["source_range_id"]: item.get("source_order", 0)
            for item in structure.get("dispositions", ())
        }

    def source_order(self, source_range_id: str) -> int:
        return int(self._order_by_range.get(source_range_id, 0) or 0)

    def evidence(self, source_range_id: str) -> ProvenanceEvidence | None:
        entries = self._entries_by_range.get(source_range_id, [])
        atoms = self._atoms_by_range.get(source_range_id, [])
        records = self._source_records_by_range.get(source_range_id, [])
        blocks = self._context_blocks_by_range.get(source_range_id, [])
        frames = self._atom_frames_by_range.get(source_range_id, [])
        entries = _dedupe(
            entries
            + [
                self._entries_by_id[item]
                for item in _record_ids(records, "ledger_entry_ids")
                if item in self._entries_by_id
            ]
        )
        atoms = _dedupe(
            atoms
            + [
                self._atoms_by_id[item]
                for item in _record_ids(records, "technical_atom_ids")
                if item in self._atoms_by_id
            ]
        )
        if (
            not entries
            and not atoms
            and not records
            and not blocks
            and not frames
            and source_range_id not in self._order_by_range
        ):
            return None
        node_ids = [node_id for entry in entries for node_id in entry.get("structure_node_ids", ())]
        section_path = _context_section_path(blocks) or self._section_path(
            node_ids[0] if node_ids else self._structure_node_for_range(source_range_id)
        )
        return ProvenanceEvidence(
            source_range_id=source_range_id,
            section_path=section_path,
            excerpt=_excerpt(entries, atoms) or _context_excerpt(blocks, frames),
            has_technical_atom=bool(
                atoms or frames or any(entry.get("technical_atom_id") for entry in entries)
            ),
            context_pointer=any(_context_pointer(entry) for entry in entries),
            fragmentary=any(fragmentary(_entry_text(entry)) for entry in entries)
            or (
                not entries
                and any(fragmentary(block.get("source_text", "")) for block in blocks)
            ),
            structure_only=not entries and not atoms and not blocks and not frames,
        )

    def _section_path(self, node_id: str) -> str:
        labels: list[str] = []
        seen: set[str] = set()
        current = self._nodes.get(node_id)
        while current is not None and current["structure_node_id"] not in seen:
            seen.add(current["structure_node_id"])
            if current.get("structure_node_kind") != "root":
                labels.append(current.get("heading_text", ""))
            current = self._nodes.get(current.get("parent_structure_node_id", ""))
        return " / ".join(reversed([label for label in labels if label.strip()]))

    def _structure_node_for_range(self, source_range_id: str) -> str:
        exact = self._nodes_by_range.get(source_range_id)
        if exact is not None:
            return str(exact["structure_node_id"])
        order = self.source_order(source_range_id)
        if order <= 0:
            return ""
        index = bisect_right(self._node_orders, order) - 1
        return "" if index < 0 else str(self._node_ids_by_order[index])


def provenance_index_from_artifacts(artifact_files: dict[str, str]) -> ProvenanceArtifactIndex:
    return ProvenanceArtifactIndex(
        _artifact_json(artifact_files, "claim-ledger.json", "ledger"),
        _artifact_json(artifact_files, "document-structure.json", "document_structure"),
        _artifact_json(artifact_files, "source-coverage.json", "source_coverage"),
        {},
    )


def _artifact_json(files: dict[str, str], filename: str, key: str) -> dict[str, Any]:
    if filename not in files:
        return {}
    data = cast(dict[str, Any], json.loads(files[filename]))
    return cast(dict[str, Any], data.get(key, data))


def _entry_text(entry: dict[str, Any]) -> str:
    return str(entry.get("normalized_text") or entry.get("source_text", ""))


def _excerpt(entries: list[dict[str, Any]], atoms: list[dict[str, Any]]) -> str:
    texts = [_entry_text(entry) for entry in entries]
    if not texts:
        texts = [json.dumps(atom.get("payload", {}), sort_keys=True) for atom in atoms]
    return " ".join(text.strip() for text in texts if text.strip())[:320]


def _context_excerpt(blocks: list[dict[str, Any]], frames: list[dict[str, Any]]) -> str:
    texts = [str(block.get("source_text", "")).strip() for block in blocks]
    if not texts:
        texts = [
            " ".join(
                text
                for text in (str(frame.get("label", "")), str(frame.get("technical_atom_kind", "")))
                if text
            )
            for frame in frames
        ]
    return " ".join(text for text in texts if text)[:320]


def _record_ids(records: list[dict[str, Any]], key: str) -> tuple[str, ...]:
    return tuple(str(item) for record in records for item in record.get(key, ()) if item)


def _dedupe(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[int] = set()
    deduped: list[dict[str, Any]] = []
    for record in records:
        if id(record) in seen:
            continue
        seen.add(id(record))
        deduped.append(record)
    return deduped


def _context_section_path(blocks: list[dict[str, Any]]) -> str:
    for block in blocks:
        section = str(block.get("section_label", "")).strip()
        if section:
            return section
    return ""


def _context_pointer(entry: dict[str, Any]) -> bool:
    scope = entry.get("spatial_scope") or {}
    return bool(
        entry.get("ledger_entry_kind") in {"claim", "event"}
        and scope.get("spatial_kind") == "relative-location"
        and not scope.get("normalized_spatial_value")
        and "identity" in entry.get("claim_role_tags", ())
    )
