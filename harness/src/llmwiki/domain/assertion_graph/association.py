"""Association graph records for page grouping experiments."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field, model_validator

from llmwiki.domain.assertion_graph.common import Confidence, DomainRecord, NonEmptyStr


class AssociationNodeKind(StrEnum):
    SOURCE_UNIT = "source_unit"
    EVIDENCE_SPAN = "evidence_span"
    ASSERTION = "assertion"
    TECHNICAL_ATOM = "technical_atom"
    CONCEPT_LABEL = "concept_label"


class AssociationEdgeKind(StrEnum):
    SOURCE_CONTAINS_EVIDENCE = "source_contains_evidence"
    ASSERTION_HAS_EVIDENCE = "assertion_has_evidence"
    ATOM_HAS_EVIDENCE = "atom_has_evidence"
    ASSERTION_USES_ATOM = "assertion_uses_atom"
    EXPLICIT_RELATIONSHIP = "explicit_relationship"
    ARGUMENT_EDGE = "argument_edge"
    SHARED_SOURCE_UNIT = "shared_source_unit"
    SHARED_SUBJECT = "shared_subject"
    HEADING_ANCESTRY = "heading_ancestry"


class AssociationClusterShape(StrEnum):
    CONCEPT = "concept"
    PROCEDURE = "procedure"
    RULE_SET = "rule_set"
    CATALOG_RECORD = "catalog_record"
    TECHNICAL_ATOM_SET = "technical_atom_set"
    MIXED = "mixed"


class AssociationNode(DomainRecord):
    id: NonEmptyStr
    node_kind: AssociationNodeKind
    record_id: str = ""
    label: NonEmptyStr
    source_order: int = Field(ge=0)


class AssociationEdge(DomainRecord):
    id: NonEmptyStr
    edge_kind: AssociationEdgeKind
    from_node_id: NonEmptyStr
    to_node_id: NonEmptyStr
    weight: Confidence
    rationale: NonEmptyStr
    support_record_ids: tuple[str, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_edge(self) -> AssociationEdge:
        if self.from_node_id == self.to_node_id:
            raise ValueError("association edge endpoints must differ")
        return self


class AssociationCluster(DomainRecord):
    id: NonEmptyStr
    label: NonEmptyStr
    member_node_ids: tuple[NonEmptyStr, ...] = Field(min_length=1)
    assertion_ids: tuple[str, ...] = ()
    technical_atom_ids: tuple[str, ...] = ()
    source_unit_ids: tuple[str, ...] = ()
    dominant_shape: AssociationClusterShape
    cohesion_score: Confidence
    separation_score: Confidence
    ambiguous: bool = False
    oversized: bool = False


class AssociationGraph(DomainRecord):
    source_locator: NonEmptyStr
    source_hash: NonEmptyStr
    nodes: tuple[AssociationNode, ...]
    edges: tuple[AssociationEdge, ...]
    clusters: tuple[AssociationCluster, ...]
