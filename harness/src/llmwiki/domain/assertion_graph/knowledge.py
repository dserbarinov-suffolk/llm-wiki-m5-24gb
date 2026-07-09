"""Assertion, relationship, and argument-edge domain records."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field, model_validator

from llmwiki.domain.assertion_graph.common import (
    ArgumentEdgeId,
    AssertionId,
    Confidence,
    DomainRecord,
    DomainReferenceId,
    EvidenceSpanId,
    NonEmptyStr,
    ProvenanceActivityId,
    RelationshipId,
    SourceUnitId,
    TechnicalAtomId,
)


class AssertionKind(StrEnum):
    SOURCE_CLAIM = "source_claim"
    DEFINITION = "definition"
    RULE_STATEMENT = "rule_statement"
    PROCEDURE_STEP = "procedure_step"
    EXAMPLE_STATEMENT = "example_statement"
    EVENT_STATEMENT = "event_statement"
    ENTITY_FACT = "entity_fact"
    TECHNICAL_FACT = "technical_fact"
    ANALYTIC_INFERENCE = "analytic_inference"
    CORROBORATION = "corroboration"
    CONTRADICTION = "contradiction"
    STATUS_UPDATE = "status_update"


class AssertionStatus(StrEnum):
    PROPOSED = "proposed"
    ACCEPTED = "accepted"
    NEEDS_REVIEW = "needs_review"
    REJECTED = "rejected"
    CONTRADICTED = "contradicted"
    SUPERSEDED = "superseded"


class RelationshipKind(StrEnum):
    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    WEAKENS = "weakens"
    CONTEXTUALIZES = "contextualizes"
    NARROWS = "narrows"
    ELABORATES = "elaborates"
    DEPENDS_ON = "depends_on"
    PART_OF = "part_of"
    EXAMPLE_OF = "example_of"
    EXCEPTION_TO = "exception_to"
    INFERS = "infers"
    CONTRASTS_WITH = "contrasts_with"
    EQUIVALENT_TO = "equivalent_to"
    CAUSED_BY = "caused_by"
    COINCIDES_WITH = "coincides_with"


class Qualifier(DomainRecord):
    """Reusable qualifier attached to an assertion."""

    key: NonEmptyStr
    value: NonEmptyStr


class Assertion(DomainRecord):
    """One atomic statement with explicit source support and lifecycle state."""

    id: AssertionId
    kind: AssertionKind
    subject: NonEmptyStr
    predicate: NonEmptyStr
    object_entity_id: DomainReferenceId | None = None
    object_value: NonEmptyStr | None = None
    qualifiers: tuple[Qualifier, ...] = ()
    status: AssertionStatus
    confidence: Confidence
    source_backed: bool = True
    source_unit_ids: tuple[SourceUnitId, ...] = ()
    evidence_span_ids: tuple[EvidenceSpanId, ...] = ()
    technical_atom_ids: tuple[TechnicalAtomId, ...] = ()
    provenance_activity_ids: tuple[ProvenanceActivityId, ...] = ()

    @model_validator(mode="after")
    def validate_assertion_support(self) -> Assertion:
        has_entity = self.object_entity_id is not None
        has_value = self.object_value is not None
        if has_entity == has_value:
            raise ValueError("assertion must have exactly one object")
        if not self.source_backed and self.kind != AssertionKind.ANALYTIC_INFERENCE:
            raise ValueError("only analytic inference assertions can be non-source-backed")
        if self.status == AssertionStatus.ACCEPTED and not self.provenance_activity_ids:
            raise ValueError("accepted assertions require provenance")
        if self.status == AssertionStatus.ACCEPTED and self.source_backed:
            if not self.source_unit_ids:
                raise ValueError("accepted source-backed assertions require source units")
            if not self.evidence_span_ids:
                raise ValueError("accepted source-backed assertions require evidence spans")
        return self


class Relationship(DomainRecord):
    """A typed edge between domain records, never between wiki pages."""

    id: RelationshipId
    subject_id: DomainReferenceId
    predicate: RelationshipKind
    object_id: DomainReferenceId
    assertion_ids: tuple[AssertionId, ...] = Field(min_length=1)
    confidence: Confidence
    provenance_activity_ids: tuple[ProvenanceActivityId, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_relationship(self) -> Relationship:
        if self.subject_id == self.object_id:
            raise ValueError("relationship subject and object must differ")
        return self


class ArgumentEdge(DomainRecord):
    """A typed argument edge between two assertions."""

    id: ArgumentEdgeId
    from_assertion_id: AssertionId
    to_assertion_id: AssertionId
    relation: RelationshipKind
    rationale: NonEmptyStr
    evidence_span_ids: tuple[EvidenceSpanId, ...] = ()
    confidence: Confidence
    provenance_activity_id: ProvenanceActivityId

    @model_validator(mode="after")
    def validate_argument_edge(self) -> ArgumentEdge:
        if self.from_assertion_id == self.to_assertion_id:
            raise ValueError("argument edge assertions must differ")
        return self
