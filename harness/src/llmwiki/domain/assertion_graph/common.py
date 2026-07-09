"""Shared value types for the assertion graph domain core."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, model_validator


class DomainRecord(BaseModel):
    """Base for pure, validated, immutable domain records."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True)


NonEmptyStr = Annotated[str, Field(min_length=1)]
Confidence = Annotated[float, Field(ge=0.0, le=1.0)]
NonNegativeInt = Annotated[int, Field(ge=0)]
SourceHash = Annotated[str, Field(pattern=r"^[a-f0-9]{64}$")]

SourceUnitId = Annotated[str, Field(pattern=r"^su_[A-Za-z0-9][A-Za-z0-9_-]*$")]
EvidenceSpanId = Annotated[str, Field(pattern=r"^evs_[A-Za-z0-9][A-Za-z0-9_-]*$")]
TechnicalAtomId = Annotated[str, Field(pattern=r"^tat_[A-Za-z0-9][A-Za-z0-9_-]*$")]
AssertionId = Annotated[str, Field(pattern=r"^ast_[A-Za-z0-9][A-Za-z0-9_-]*$")]
RelationshipId = Annotated[str, Field(pattern=r"^rel_[A-Za-z0-9][A-Za-z0-9_-]*$")]
ArgumentEdgeId = Annotated[str, Field(pattern=r"^arg_[A-Za-z0-9][A-Za-z0-9_-]*$")]
TopicStateId = Annotated[str, Field(pattern=r"^tps_[A-Za-z0-9][A-Za-z0-9_-]*$")]
TopicDependencyId = Annotated[str, Field(pattern=r"^tdp_[A-Za-z0-9][A-Za-z0-9_-]*$")]
TopicGapId = Annotated[str, Field(pattern=r"^tgp_[A-Za-z0-9][A-Za-z0-9_-]*$")]
ProposedChangeId = Annotated[str, Field(pattern=r"^pcg_[A-Za-z0-9][A-Za-z0-9_-]*$")]
ProvenanceActivityId = Annotated[str, Field(pattern=r"^prv_[A-Za-z0-9][A-Za-z0-9_-]*$")]
PageProjectionId = Annotated[str, Field(pattern=r"^pgp_[A-Za-z0-9][A-Za-z0-9_-]*$")]

DomainReferenceId = Annotated[
    str,
    Field(pattern=r"^(su|evs|tat|ast|rel|arg|tps|tdp|tgp|pcg|prv)_[A-Za-z0-9][A-Za-z0-9_-]*$"),
]

PageSpan = tuple[NonNegativeInt, NonNegativeInt]


class LayoutBox(DomainRecord):
    """Source-layout rectangle in a source coordinate system."""

    page: NonNegativeInt
    x0: float
    y0: float
    x1: float
    y1: float

    @model_validator(mode="after")
    def validate_ordered_box(self) -> LayoutBox:
        if self.x0 > self.x1:
            raise ValueError("layout box x0 must be <= x1")
        if self.y0 > self.y1:
            raise ValueError("layout box y0 must be <= y1")
        return self


class SelectorType(StrEnum):
    EXACT_TEXT = "exact_text"
    TEXT_POSITION = "text_position"
    PAGE = "page"
    LAYOUT_BOX = "layout_box"


class EvidenceSelector(DomainRecord):
    """Portable selector for finding an evidence span in a source artifact."""

    selector_type: SelectorType
    value: NonEmptyStr


def validate_page_span(page_span: PageSpan) -> PageSpan:
    """Validate the shared page-span convention."""

    start, end = page_span
    if start > end:
        raise ValueError("page span start must be <= end")
    return page_span
