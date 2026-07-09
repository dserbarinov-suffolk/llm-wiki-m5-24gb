"""JSON schema helpers for assertion graph domain records."""

from __future__ import annotations

from typing import cast

from llmwiki.domain.assertion_graph.association import (
    AssociationCluster,
    AssociationEdge,
    AssociationGraph,
    AssociationNode,
)
from llmwiki.domain.assertion_graph.common import DomainRecord, EvidenceSelector, LayoutBox
from llmwiki.domain.assertion_graph.knowledge import (
    ArgumentEdge,
    Assertion,
    Qualifier,
    Relationship,
)
from llmwiki.domain.assertion_graph.lifecycle import (
    PageCoverageRecord,
    PageProjection,
    ProjectionFinding,
    ProposedChange,
    ProvenanceActivity,
    RecordPayload,
    RenderedRelatedLink,
)
from llmwiki.domain.assertion_graph.source import EvidenceSpan, SourceUnit, TechnicalAtom
from llmwiki.domain.assertion_graph.topic import (
    ProjectionPolicy,
    TopicDependency,
    TopicGap,
    TopicState,
)

JsonSchema = dict[str, object]

PUBLIC_DOMAIN_RECORDS: tuple[type[DomainRecord], ...] = (
    LayoutBox,
    EvidenceSelector,
    SourceUnit,
    EvidenceSpan,
    TechnicalAtom,
    Qualifier,
    Assertion,
    Relationship,
    ArgumentEdge,
    ProjectionPolicy,
    TopicDependency,
    TopicGap,
    TopicState,
    RecordPayload,
    ProvenanceActivity,
    ProposedChange,
    PageCoverageRecord,
    RenderedRelatedLink,
    ProjectionFinding,
    PageProjection,
    AssociationNode,
    AssociationEdge,
    AssociationCluster,
    AssociationGraph,
)


def schema_for(record_type: type[DomainRecord]) -> JsonSchema:
    """Return a JSON schema for one public domain record type."""

    return cast(JsonSchema, record_type.model_json_schema())


def domain_json_schemas() -> dict[str, JsonSchema]:
    """Return JSON schemas for every public assertion graph record."""

    return {record_type.__name__: schema_for(record_type) for record_type in PUBLIC_DOMAIN_RECORDS}
