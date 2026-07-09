"""Topic-state domain records for accumulated wiki knowledge."""

from __future__ import annotations

from enum import StrEnum

from pydantic import model_validator

from llmwiki.domain.assertion_graph.common import (
    ArgumentEdgeId,
    AssertionId,
    Confidence,
    DomainRecord,
    EvidenceSpanId,
    NonEmptyStr,
    NonNegativeInt,
    RelationshipId,
    SourceUnitId,
    TechnicalAtomId,
    TopicDependencyId,
    TopicGapId,
    TopicStateId,
)
from llmwiki.domain.assertion_graph.knowledge import RelationshipKind


class TopicKind(StrEnum):
    CONCEPT = "concept"
    ENTITY = "entity"
    PROCEDURE = "procedure"
    RULE_SET = "rule_set"
    COLLECTION = "collection"
    SOURCE_MANIFEST = "source_manifest"
    COMPARISON = "comparison"
    SYNTHESIS = "synthesis"


class DependencyStatus(StrEnum):
    REQUIRED = "required"
    OPTIONAL = "optional"
    BLOCKED = "blocked"


class GapKind(StrEnum):
    MISSING_SOURCE_SUPPORT = "missing_source_support"
    MISSING_DEPENDENCY = "missing_dependency"
    UNRESOLVED_CONTRADICTION = "unresolved_contradiction"
    AMBIGUOUS_SOURCE_STRUCTURE = "ambiguous_source_structure"
    WEAK_TOPIC_IDENTITY = "weak_topic_identity"


class ProjectionPolicy(DomainRecord):
    """Topic-local instructions for projecting accepted topic state."""

    page_kind: NonEmptyStr
    page_family: NonEmptyStr
    include_gaps: bool = True
    minimum_confidence: Confidence = 0.0


class TopicDependency(DomainRecord):
    """A source-supported dependency between topic states."""

    id: TopicDependencyId
    from_topic_state_id: TopicStateId
    to_topic_state_id: TopicStateId
    relation: RelationshipKind
    required_status: DependencyStatus
    rationale_assertion_ids: tuple[AssertionId, ...] = ()
    source_order: NonNegativeInt

    @model_validator(mode="after")
    def validate_dependency(self) -> TopicDependency:
        if self.from_topic_state_id == self.to_topic_state_id:
            raise ValueError("topic dependency endpoints must differ")
        return self


class TopicGap(DomainRecord):
    """Visible missing, ambiguous, or unresolved knowledge state."""

    id: TopicGapId
    gap_kind: GapKind
    description: NonEmptyStr
    source_unit_ids: tuple[SourceUnitId, ...] = ()
    evidence_span_ids: tuple[EvidenceSpanId, ...] = ()
    blocking: bool = True


class TopicState(DomainRecord):
    """Durable accumulated state for one coherent wiki topic."""

    id: TopicStateId
    topic_key: NonEmptyStr
    label: NonEmptyStr
    topic_kind: TopicKind
    accepted_assertion_ids: tuple[AssertionId, ...] = ()
    accepted_technical_atom_ids: tuple[TechnicalAtomId, ...] = ()
    relationship_ids: tuple[RelationshipId, ...] = ()
    argument_edge_ids: tuple[ArgumentEdgeId, ...] = ()
    source_unit_ids: tuple[SourceUnitId, ...] = ()
    required_dependency_ids: tuple[TopicDependencyId, ...] = ()
    unresolved_gap_ids: tuple[TopicGapId, ...] = ()
    projection_policy: ProjectionPolicy

    @model_validator(mode="after")
    def validate_topic_content(self) -> TopicState:
        has_content = any(
            (
                self.accepted_assertion_ids,
                self.accepted_technical_atom_ids,
                self.relationship_ids,
                self.argument_edge_ids,
            )
        )
        if not has_content and not self.unresolved_gap_ids:
            raise ValueError("topic state requires accepted content or explicit gaps")
        return self
