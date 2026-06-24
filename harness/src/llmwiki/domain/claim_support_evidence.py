"""Evidence lookup service for claim-support audits."""

from __future__ import annotations

import re
from collections.abc import Sequence

from llmwiki.domain.citations import Citation
from llmwiki.domain.evidence_registry import EvidenceRecord, EvidenceRegistry, SourceRange

_TERM_RE = re.compile(r"[a-z][a-z0-9-]{2,}")


class ClaimSupportEvidenceIndex:
    def __init__(self, registries: Sequence[EvidenceRegistry]) -> None:
        self.registries = registries
        self.records = _records_by_id(registries)
        self.records_by_claim = _records_by_claim(registries)
        self.ranges = _ranges_by_id(registries)
        self.registries_by_source = {
            registry.source_texts[0].source_path: registry
            for registry in registries
            if registry.source_texts
        }

    def registry_for_source(self, source_path: str) -> EvidenceRegistry | None:
        return self.registries_by_source.get(source_path)

    def evidence_ids_for_claims(self, claim_ids: Sequence[str]) -> tuple[str, ...]:
        ids: list[str] = []
        for claim_id in claim_ids:
            ids.extend(record.evidence_id for record in self.records_by_claim.get(claim_id, ()))
        return tuple(dict.fromkeys(ids))

    def evidence_ids_for_citations(
        self, page_id: str, citations: Sequence[Citation]
    ) -> tuple[str, ...]:
        ids: list[str] = []
        for citation in citations:
            registry = self.registry_for_source(citation.source_path)
            if registry is None:
                continue
            for source_range in registry.ranges_for_page(page_id, citation.source_path):
                if source_range.contains_source_span(
                    source_path=citation.source_path,
                    page_range=citation.page_range,
                    line_range=citation.line_range,
                ):
                    ids.extend(
                        record.evidence_id
                        for record in registry.evidence_records
                        if record.source_range_id == source_range.source_range_id
                    )
        return tuple(dict.fromkeys(ids))

    def page_id_for_evidence(self, evidence_ids: Sequence[str]) -> str:
        for evidence_id in evidence_ids:
            record = self.records.get(evidence_id)
            if record is None:
                continue
            source_range = self.ranges.get(record.source_range_id)
            if source_range is not None:
                return source_range.page_id
        return ""

    def excerpts(self, evidence_ids: Sequence[str], limit: int = 3) -> tuple[str, ...]:
        excerpts: list[str] = []
        for evidence_id in evidence_ids[:limit]:
            record = self.records.get(evidence_id)
            if record is not None:
                excerpts.append(f"{evidence_id}: {record.excerpt}")
        return tuple(excerpts)

    def excerpts_for_claim(
        self, evidence_ids: Sequence[str], claim_text: str, limit: int = 3
    ) -> tuple[str, ...]:
        query_terms = _terms(claim_text)
        indexed: list[tuple[int, str, EvidenceRecord, int, int]] = []
        for position, evidence_id in enumerate(dict.fromkeys(evidence_ids)):
            record = self.records.get(evidence_id)
            if record is None:
                continue
            overlap = len(query_terms & _terms(record.excerpt)) if query_terms else 0
            source_claim_bonus = 1 if record.source_claim_id else 0
            indexed.append((position, evidence_id, record, overlap, source_claim_bonus))
        selected = _contextual_excerpt_positions(indexed, limit)
        return tuple(
            f"{evidence_id}: {record.excerpt}"
            for position, evidence_id, record, _overlap, _bonus in indexed
            if position in selected
        )


def _contextual_excerpt_positions(
    indexed: Sequence[tuple[int, str, EvidenceRecord, int, int]], limit: int
) -> frozenset[int]:
    if limit < 1:
        return frozenset()
    if len(indexed) <= limit:
        return frozenset(position for position, *_rest in indexed)
    ranked = sorted(
        indexed,
        key=lambda item: (item[3], item[4], -item[0]),
        reverse=True,
    )
    selected: set[int] = set()
    anchor = ranked[0]
    if anchor[3] > 0:
        anchor_position = anchor[0]
        for position in range(max(0, anchor_position - 2), anchor_position + 1):
            if _has_position(indexed, position):
                selected.add(position)
    for position, _evidence_id, _record, _overlap, _bonus in ranked:
        if len(selected) >= limit:
            break
        selected.add(position)
    for position, *_rest in indexed:
        if len(selected) >= limit:
            break
        selected.add(position)
    return frozenset(sorted(selected)[:limit])


def _has_position(
    indexed: Sequence[tuple[int, str, EvidenceRecord, int, int]], position: int
) -> bool:
    return any(item[0] == position for item in indexed)


def _records_by_id(registries: Sequence[EvidenceRegistry]) -> dict[str, EvidenceRecord]:
    return {
        record.evidence_id: record
        for registry in registries
        for record in registry.evidence_records
    }


def _records_by_claim(
    registries: Sequence[EvidenceRegistry],
) -> dict[str, tuple[EvidenceRecord, ...]]:
    result: dict[str, list[EvidenceRecord]] = {}
    for registry in registries:
        for record in registry.evidence_records:
            if record.source_claim_id:
                result.setdefault(record.source_claim_id, []).append(record)
    return {claim_id: tuple(records) for claim_id, records in result.items()}


def _ranges_by_id(registries: Sequence[EvidenceRegistry]) -> dict[str, SourceRange]:
    return {
        source_range.source_range_id: source_range
        for registry in registries
        for source_range in registry.source_ranges
    }


def _terms(text: str) -> frozenset[str]:
    return frozenset(_TERM_RE.findall(text.lower()))
