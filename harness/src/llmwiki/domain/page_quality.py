"""Source-neutral page quality scoring for projected wiki pages."""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from statistics import median

from pydantic import BaseModel, ConfigDict, Field

from llmwiki.domain.assertion_graph import (
    Assertion,
    PageProjection,
    SourceUnit,
    TechnicalAtom,
    TopicState,
)

Score = float

_GENERIC_RELATION_LABELS = frozenset(
    {"", "source topic", "contextualizes", "source-supported topic dependency"}
)


class PageQualityRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    page_id: str
    page_family: str
    topic_state_id: str
    source_locality_score: Score = Field(ge=0.0, le=1.0)
    topic_boundary_cohesion: Score = Field(ge=0.0, le=1.0)
    technical_atom_integrity_rate: Score = Field(ge=0.0, le=1.0)
    page_shape_fit: Score = Field(ge=0.0, le=1.0)
    walkability_score: Score = Field(ge=0.0, le=1.0)
    overall_quality_band: str
    positive_reasons: tuple[str, ...] = ()
    negative_reasons: tuple[str, ...] = ()


class PageQualityReport(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)

    source_locator: str
    source_hash: str
    page_quality_records: tuple[PageQualityRecord, ...]


@dataclass(frozen=True)
class _PageEvidence:
    coverage_count: int
    source_unit_ids: frozenset[str]
    page_numbers: frozenset[int]
    atom_ids: frozenset[str]


def build_page_quality_report(
    *,
    source_locator: str,
    source_hash: str,
    pages: tuple[PageProjection, ...],
    topics: tuple[TopicState, ...],
    assertions: tuple[Assertion, ...],
    atoms: tuple[TechnicalAtom, ...],
    source_units: tuple[SourceUnit, ...],
) -> PageQualityReport:
    topic_by_id = {topic.id: topic for topic in topics}
    assertion_units = {
        assertion.id: frozenset(assertion.source_unit_ids) for assertion in assertions
    }
    atom_by_id = {atom.id: atom for atom in atoms}
    atom_units = _atom_source_units(atoms, assertions)
    unit_by_id = {unit.id: unit for unit in source_units}
    records = tuple(
        _score_page(
            page,
            topic_by_id.get(page.topic_state_id),
            assertion_units,
            atom_by_id,
            atom_units,
            unit_by_id,
        )
        for page in pages
        if page.page_family != "source-manifest"
    )
    return PageQualityReport(
        source_locator=source_locator,
        source_hash=source_hash,
        page_quality_records=records,
    )


def quality_band_counts(report: PageQualityReport) -> Counter[str]:
    return Counter(record.overall_quality_band for record in report.page_quality_records)


def median_score(records: tuple[PageQualityRecord, ...], field_name: str) -> float:
    values = [float(getattr(record, field_name)) for record in records]
    return float(median(values)) if values else 0.0


def _score_page(
    page: PageProjection,
    topic: TopicState | None,
    assertion_units: dict[str, frozenset[str]],
    atom_by_id: dict[str, TechnicalAtom],
    atom_units: dict[str, frozenset[str]],
    unit_by_id: dict[str, SourceUnit],
) -> PageQualityRecord:
    evidence = _page_evidence(page, topic, assertion_units, atom_units, unit_by_id)
    scores = {
        "source_locality_score": _source_locality_score(evidence),
        "topic_boundary_cohesion": _topic_boundary_cohesion(page, evidence),
        "technical_atom_integrity_rate": _technical_atom_integrity_rate(evidence, atom_by_id),
        "page_shape_fit": _page_shape_fit(page, topic, evidence),
        "walkability_score": _walkability_score(page, topic),
    }
    positives, negatives = _reasons(page, evidence, scores)
    return PageQualityRecord(
        page_id=page.page_id,
        page_family=page.page_family,
        topic_state_id=page.topic_state_id,
        overall_quality_band=_quality_band(tuple(scores.values())),
        positive_reasons=tuple(positives),
        negative_reasons=tuple(negatives),
        **scores,
    )


def _atom_source_units(
    atoms: tuple[TechnicalAtom, ...], assertions: tuple[Assertion, ...]
) -> dict[str, frozenset[str]]:
    units: dict[str, set[str]] = {atom.id: set() for atom in atoms}
    for assertion in assertions:
        for atom_id in assertion.technical_atom_ids:
            units.setdefault(atom_id, set()).update(assertion.source_unit_ids)
    return {atom_id: frozenset(unit_ids) for atom_id, unit_ids in units.items()}


def _page_evidence(
    page: PageProjection,
    topic: TopicState | None,
    assertion_units: dict[str, frozenset[str]],
    atom_units: dict[str, frozenset[str]],
    unit_by_id: dict[str, SourceUnit],
) -> _PageEvidence:
    unit_ids: set[str] = set(topic.source_unit_ids if topic else ())
    atom_ids: set[str] = set(topic.accepted_technical_atom_ids if topic else ())
    for coverage in page.coverage_records:
        support_id = coverage.support_record_id
        unit_ids.update(assertion_units.get(support_id, ()))
        if support_id in atom_units:
            atom_ids.add(support_id)
            unit_ids.update(atom_units[support_id])
    page_numbers = {
        page_number
        for unit_id in unit_ids
        if (unit := unit_by_id.get(unit_id)) is not None
        for page_number in _page_numbers(unit)
    }
    return _PageEvidence(
        coverage_count=len(page.coverage_records),
        source_unit_ids=frozenset(unit_ids),
        page_numbers=frozenset(page_numbers),
        atom_ids=frozenset(atom_ids),
    )


def _source_locality_score(evidence: _PageEvidence) -> float:
    if not evidence.source_unit_ids:
        return 0.3
    span = (
        max(evidence.page_numbers) - min(evidence.page_numbers) + 1
        if evidence.page_numbers
        else 1
    )
    span_factor = _clamp(1.0 - max(0, span - 2) / 20)
    unit_factor = min(1.0, 30 / max(len(evidence.source_unit_ids), 1))
    coverage_factor = min(1.0, 40 / max(evidence.coverage_count, 1))
    return _round(min(span_factor, unit_factor, coverage_factor))


def _topic_boundary_cohesion(page: PageProjection, evidence: _PageEvidence) -> float:
    score = 1.0
    if page.page_family == "broad-topic":
        score -= 0.25
    score -= min(0.5, max(0, evidence.coverage_count - 40) / 160)
    score -= min(0.3, max(0, len(evidence.source_unit_ids) - 40) / 200)
    return _round(score)


def _technical_atom_integrity_rate(
    evidence: _PageEvidence, atom_by_id: dict[str, TechnicalAtom]
) -> float:
    if not evidence.atom_ids:
        return 1.0
    scores = [_atom_integrity(atom_by_id.get(atom_id)) for atom_id in evidence.atom_ids]
    return _round(sum(scores) / len(scores))


def _atom_integrity(atom: TechnicalAtom | None) -> float:
    if atom is None or not atom.exact_payload.strip():
        return 0.0
    if atom.parse_status == "parsed":
        return 1.0
    if atom.parse_status == "partial":
        return 0.45
    return 0.0


def _page_shape_fit(
    page: PageProjection, topic: TopicState | None, evidence: _PageEvidence
) -> float:
    score = 1.0
    has_procedure = "\n## Procedure\n" in f"\n{page.page_body}\n"
    topic_kind = str(topic.topic_kind) if topic is not None else ""
    if _weak_page_title(page.page_body):
        score -= 0.5
    if has_procedure and topic_kind != "procedure":
        score -= 0.45
    if page.page_family == "broad-topic" and has_procedure:
        score -= 0.2
    score -= min(0.35, max(0, evidence.coverage_count - 80) / 400)
    return _round(score)


def _walkability_score(page: PageProjection, topic: TopicState | None) -> float:
    links = page.rendered_related_links
    dependency_count = len(topic.required_dependency_ids) if topic is not None else 0
    if not links:
        return 0.85 if dependency_count == 0 and len(page.coverage_records) < 8 else 0.35
    support_rate = sum(bool(link.support_record_ids) for link in links) / len(links)
    typed_rate = sum(
        link.relation_label.casefold() not in _GENERIC_RELATION_LABELS for link in links
    ) / len(links)
    description_rate = sum(len(link.description.split()) >= 4 for link in links) / len(links)
    return _round((support_rate * 0.6) + (typed_rate * 0.25) + (description_rate * 0.15))


def _quality_band(scores: tuple[float, ...]) -> str:
    min_score = min(scores, default=0.0)
    med = float(median(scores)) if scores else 0.0
    if min_score >= 0.85:
        return "exemplary"
    if med >= 0.75 and min_score >= 0.60:
        return "good"
    if med >= 0.55 and min_score >= 0.35:
        return "usable"
    if min_score < 0.20:
        return "bad"
    return "suspect"


def _reasons(
    page: PageProjection, evidence: _PageEvidence, scores: dict[str, float]
) -> tuple[list[str], list[str]]:
    positives: list[str] = []
    negatives: list[str] = []
    for name, value in scores.items():
        if value >= 0.85:
            positives.append(f"{name}:strong")
        elif value < 0.4:
            negatives.append(f"{name}:weak")
    if not evidence.atom_ids:
        positives.append("no-technical-atoms-required")
    if page.coverage_records and len(page.coverage_records) >= 120:
        negatives.append("extreme-projection-coverage")
    return positives, negatives


def _page_numbers(unit: SourceUnit) -> tuple[int, ...]:
    start, end = unit.page_span
    if start <= 0 or end <= 0:
        return ()
    return tuple(range(start, end + 1))


def _weak_page_title(page_body: str) -> bool:
    first_line = page_body.splitlines()[0] if page_body.splitlines() else ""
    title = first_line.removeprefix("#").strip()
    return bool(re.fullmatch(r"\d+(?:[.-]\d+)*", title))


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def _round(value: float) -> float:
    return round(_clamp(value), 3)
