"""Source-derived assertion graph records."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field, field_validator, model_validator

from llmwiki.domain.assertion_graph.common import (
    Confidence,
    DomainRecord,
    EvidenceSelector,
    EvidenceSpanId,
    LayoutBox,
    NonEmptyStr,
    NonNegativeInt,
    PageSpan,
    ProvenanceActivityId,
    SourceHash,
    SourceUnitId,
    TechnicalAtomId,
    validate_page_span,
)


class SourceUnitKind(StrEnum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    LIST = "list"
    TABLE = "table"
    CODE = "code"
    FORMULA = "formula"
    FIGURE = "figure"
    CAPTION = "caption"
    FOOTNOTE = "footnote"
    INDEX_ENTRY = "index_entry"
    GLOSSARY_ENTRY = "glossary_entry"
    UNKNOWN = "unknown"


class TechnicalAtomKind(StrEnum):
    TABLE = "table"
    CODE_BLOCK = "code_block"
    FORMULA = "formula"
    RULE = "rule"
    PROCEDURE = "procedure"
    EXAMPLE = "example"
    DIAGRAM = "diagram"
    STRUCTURED_RECORD = "structured_record"


class ParseStatus(StrEnum):
    PARSED = "parsed"
    PARTIAL = "partial"
    UNPARSED = "unparsed"
    FAILED = "failed"


class SourceUnit(DomainRecord):
    """One ordered source-derived block or structured source item."""

    id: SourceUnitId
    source_locator: NonEmptyStr
    source_hash: SourceHash
    source_order: NonNegativeInt
    kind: SourceUnitKind
    parent_id: SourceUnitId | None = None
    child_ids: tuple[SourceUnitId, ...] = ()
    sibling_ids: tuple[SourceUnitId, ...] = ()
    text: str = ""
    page_span: PageSpan = (0, 0)
    layout_boxes: tuple[LayoutBox, ...] = ()

    @field_validator("page_span")
    @classmethod
    def validate_source_page_span(cls, page_span: PageSpan) -> PageSpan:
        return validate_page_span(page_span)

    @model_validator(mode="after")
    def validate_structure_links(self) -> SourceUnit:
        linked_ids = (self.parent_id,) + self.child_ids + self.sibling_ids
        if self.id in linked_ids:
            raise ValueError("source unit cannot link to itself")
        return self


class EvidenceSpan(DomainRecord):
    """Exact source support span tied to source units, never wiki text."""

    id: EvidenceSpanId
    source_locator: NonEmptyStr
    source_hash: SourceHash
    source_unit_ids: tuple[SourceUnitId, ...] = Field(min_length=1)
    exact_text: NonEmptyStr
    prefix_text: str = ""
    suffix_text: str = ""
    page_span: PageSpan = (0, 0)
    selectors: tuple[EvidenceSelector, ...] = ()
    layout_boxes: tuple[LayoutBox, ...] = ()
    text_fingerprint: NonEmptyStr
    confidence: Confidence
    provenance_activity_ids: tuple[ProvenanceActivityId, ...] = Field(min_length=1)

    @field_validator("page_span")
    @classmethod
    def validate_evidence_page_span(cls, page_span: PageSpan) -> PageSpan:
        return validate_page_span(page_span)


class TechnicalAtom(DomainRecord):
    """A complete table, code block, formula, rule, example, or similar atom."""

    id: TechnicalAtomId
    atom_kind: TechnicalAtomKind
    evidence_span_ids: tuple[EvidenceSpanId, ...] = Field(min_length=1)
    exact_payload: NonEmptyStr
    normalized_payload: str = ""
    parse_status: ParseStatus
    context_span_ids: tuple[EvidenceSpanId, ...] = ()
    source_order: NonNegativeInt
    provenance_activity_ids: tuple[ProvenanceActivityId, ...] = Field(min_length=1)
