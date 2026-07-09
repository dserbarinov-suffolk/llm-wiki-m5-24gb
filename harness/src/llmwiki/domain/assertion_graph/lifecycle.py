"""Lifecycle and page-projection domain records."""

from __future__ import annotations

import json
from enum import StrEnum

from pydantic import Field, field_validator, model_validator

from llmwiki.domain.assertion_graph.common import (
    DomainRecord,
    DomainReferenceId,
    NonEmptyStr,
    PageProjectionId,
    ProposedChangeId,
    ProvenanceActivityId,
    SourceUnitId,
    TopicStateId,
)


class ReviewStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    EDITED = "edited"
    REJECTED = "rejected"


class ProvenanceActivityKind(StrEnum):
    SOURCE_INGEST = "source_ingest"
    SOURCE_UNIT_EXTRACTION = "source_unit_extraction"
    ASSERTION_PROPOSAL = "assertion_proposal"
    PROPOSED_CHANGE_REVIEW = "proposed_change_review"
    RELATIONSHIP_MINING = "relationship_mining"
    TOPIC_STATE_BUILD = "topic_state_build"
    PAGE_PROJECTION = "page_projection"
    LINT = "lint"
    QUERY_FILING = "query_filing"


class RecordPayload(DomainRecord):
    """Serialized model-proposed or accepted record payload."""

    record_type: NonEmptyStr
    json_text: NonEmptyStr

    @field_validator("json_text")
    @classmethod
    def validate_json_object(cls, json_text: str) -> str:
        decoded = json.loads(json_text)
        if not isinstance(decoded, dict):
            raise ValueError("record payload JSON must decode to an object")
        return json_text


class ProvenanceActivity(DomainRecord):
    """A recorded action that created or changed domain records."""

    id: ProvenanceActivityId
    activity_kind: ProvenanceActivityKind
    actor: NonEmptyStr
    input_record_ids: tuple[DomainReferenceId, ...] = ()
    output_record_ids: tuple[DomainReferenceId, ...] = ()
    source_locator: str = ""
    model_name: str = ""
    prompt_id: str = ""


class ProposedChange(DomainRecord):
    """A proposed record change awaiting validation and review."""

    id: ProposedChangeId
    review_status: ReviewStatus
    proposed_record: RecordPayload
    accepted_record: RecordPayload | None = None
    source_locator: NonEmptyStr
    source_unit_ids: tuple[SourceUnitId, ...] = ()
    model_name: NonEmptyStr
    prompt_id: NonEmptyStr
    provenance_activity_id: ProvenanceActivityId

    @model_validator(mode="after")
    def validate_review_state(self) -> ProposedChange:
        if (
            self.review_status in (ReviewStatus.APPROVED, ReviewStatus.EDITED)
            and self.accepted_record is None
        ):
            raise ValueError("approved or edited proposed changes require accepted record")
        if (
            self.review_status in (ReviewStatus.PENDING, ReviewStatus.REJECTED)
            and self.accepted_record is not None
        ):
            raise ValueError("pending or rejected proposed changes cannot have accepted record")
        return self


class PageCoverageRecord(DomainRecord):
    """One projected page fragment tied back to a supporting domain record."""

    coverage_id: NonEmptyStr
    page_section: NonEmptyStr
    support_record_id: DomainReferenceId
    rendered_text: NonEmptyStr


class RenderedRelatedLink(DomainRecord):
    """A rendered related link with a reason grounded in domain records."""

    target_page_id: NonEmptyStr
    relation_label: NonEmptyStr
    description: NonEmptyStr
    support_record_ids: tuple[DomainReferenceId, ...] = ()


class ProjectionFinding(DomainRecord):
    """Visible finding produced during page projection."""

    finding_kind: NonEmptyStr
    detail: NonEmptyStr
    support_record_ids: tuple[DomainReferenceId, ...] = ()


class PageProjection(DomainRecord):
    """A disposable markdown view derived from one topic state."""

    id: PageProjectionId
    topic_state_id: TopicStateId
    page_id: NonEmptyStr
    page_kind: NonEmptyStr
    page_family: NonEmptyStr
    page_body: NonEmptyStr
    coverage_records: tuple[PageCoverageRecord, ...] = Field(min_length=1)
    source_locators: tuple[NonEmptyStr, ...] = ()
    rendered_related_links: tuple[RenderedRelatedLink, ...] = ()
    projection_findings: tuple[ProjectionFinding, ...] = ()
