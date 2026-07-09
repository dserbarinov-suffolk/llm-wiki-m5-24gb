"""Source-neutral topic-state admission helpers."""

from __future__ import annotations

import re

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.domain.assertion_graph import (
    Assertion,
    AssertionKind,
    GapKind,
    ProjectionPolicy,
    ProvenanceActivity,
    ProvenanceActivityKind,
    Relationship,
    SourceUnit,
    SourceUnitKind,
    TechnicalAtom,
    TopicGap,
    TopicKind,
    TopicState,
)
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.page_families import (
    PAGE_FAMILY_BROAD_TOPIC,
    PAGE_FAMILY_PROCEDURE_GUIDE,
    PAGE_FAMILY_SOURCE_MANIFEST,
    PAGE_FAMILY_TOPIC_CONCEPT,
)
from llmwiki.domain.pages import slugify

_MIN_ASSERTIONS_FOR_TOPIC = 2
_LOCAL_SPAN_RATIO = 0.01
_LOCAL_SPAN_FLOOR = 12


def admitted_topic_states(
    graph: AssertionGraphArtifact,
) -> tuple[tuple[TopicState, ...], tuple[TopicGap, ...]]:
    assertions_by_subject: dict[str, list[Assertion]] = {}
    labels_by_key: dict[str, str] = {}
    gaps: list[TopicGap] = []
    units_by_id = {unit.id: unit for unit in graph.source_units}
    for assertion in graph.assertions:
        if not _has_topic_identity(assertion.subject):
            gaps.append(
                _weak_topic_gap(_digest_key(assertion.subject), assertion.subject, [assertion])
            )
            continue
        label = _owner_heading_label(assertion, units_by_id) or assertion.subject
        key = _topic_key(label)
        assertions_by_subject.setdefault(key, []).append(assertion)
        labels_by_key.setdefault(key, label)
    relationships_by_assertion = _relationships_by_assertion(graph.relationships)
    atoms_by_id = {atom.id: atom for atom in graph.technical_atoms}
    states: list[TopicState] = [_source_manifest_state(graph)]
    for key, assertions in sorted(assertions_by_subject.items()):
        atom_ids = _accepted_atom_ids(assertions, relationships_by_assertion, atoms_by_id)
        relationship_ids = tuple(
            relation.id
            for assertion in assertions
            for relation in relationships_by_assertion.get(assertion.id, ())
        )
        edge_ids = tuple(
            edge.id
            for edge in graph.argument_edges
            if edge.from_assertion_id in {item.id for item in assertions}
            and edge.to_assertion_id in {item.id for item in assertions}
        )
        if not _is_admissible_topic(assertions, edge_ids, labels_by_key[key], graph):
            gaps.append(_weak_topic_gap(key, labels_by_key[key], assertions))
            continue
        states.append(
            TopicState(
                id=_topic_state_id(graph.source_hash, key),
                topic_key=key,
                label=labels_by_key[key],
                topic_kind=_topic_kind(assertions),
                accepted_assertion_ids=tuple(assertion.id for assertion in assertions),
                accepted_technical_atom_ids=atom_ids,
                relationship_ids=tuple(dict.fromkeys(relationship_ids)),
                argument_edge_ids=tuple(dict.fromkeys(edge_ids)),
                source_unit_ids=_source_unit_ids(assertions, atom_ids, atoms_by_id, graph),
                projection_policy=_projection_policy(assertions),
            )
        )
    return tuple(states), tuple(gaps)


def topic_state_build_activity(graph: AssertionGraphArtifact) -> ProvenanceActivity:
    return ProvenanceActivity(
        id=f"prv_{short_digest(graph.assertion_graph_artifact_id + '|topic-state')}",
        activity_kind=ProvenanceActivityKind.TOPIC_STATE_BUILD,
        actor="llmwiki-topic-state-builder",
        source_locator=graph.source_locator,
    )


def _source_manifest_state(graph: AssertionGraphArtifact) -> TopicState:
    return TopicState(
        id=_topic_state_id(graph.source_hash, "source-manifest"),
        topic_key="source-manifest",
        label=graph.source_locator,
        topic_kind=TopicKind.SOURCE_MANIFEST,
        accepted_assertion_ids=tuple(assertion.id for assertion in graph.assertions),
        accepted_technical_atom_ids=tuple(atom.id for atom in graph.technical_atoms),
        relationship_ids=tuple(relation.id for relation in graph.relationships),
        argument_edge_ids=tuple(edge.id for edge in graph.argument_edges),
        source_unit_ids=tuple(unit.id for unit in graph.source_units),
        projection_policy=ProjectionPolicy(
            page_kind="source",
            page_family=PAGE_FAMILY_SOURCE_MANIFEST,
        ),
    )


def _relationships_by_assertion(
    relationships: tuple[Relationship, ...],
) -> dict[str, tuple[Relationship, ...]]:
    grouped: dict[str, list[Relationship]] = {}
    for relationship in relationships:
        for assertion_id in relationship.assertion_ids:
            grouped.setdefault(assertion_id, []).append(relationship)
    return {key: tuple(value) for key, value in grouped.items()}


def _accepted_atom_ids(
    assertions: list[Assertion],
    relationships_by_assertion: dict[str, tuple[Relationship, ...]],
    atoms_by_id: dict[str, TechnicalAtom],
) -> tuple[str, ...]:
    assertion_ids = {assertion.id for assertion in assertions}
    ids: list[str] = []
    for assertion in assertions:
        ids.extend(assertion.technical_atom_ids)
        for relation in relationships_by_assertion.get(assertion.id, ()):
            for endpoint in (relation.subject_id, relation.object_id):
                if endpoint in atoms_by_id and relation.assertion_ids[0] in assertion_ids:
                    ids.append(endpoint)
    return tuple(dict.fromkeys(atom_id for atom_id in ids if atom_id in atoms_by_id))


def _source_unit_ids(
    assertions: list[Assertion],
    atom_ids: tuple[str, ...],
    atoms_by_id: dict[str, TechnicalAtom],
    graph: AssertionGraphArtifact,
) -> tuple[str, ...]:
    span_units = {span.id: span.source_unit_ids for span in graph.evidence_spans}
    units = [unit_id for assertion in assertions for unit_id in assertion.source_unit_ids]
    for atom_id in atom_ids:
        for span_id in atoms_by_id[atom_id].evidence_span_ids:
            units.extend(span_units.get(span_id, ()))
    return tuple(dict.fromkeys(units))


def _is_admissible_topic(
    assertions: list[Assertion],
    edge_ids: tuple[str, ...],
    label: str,
    graph: AssertionGraphArtifact,
) -> bool:
    if len(assertions) < _MIN_ASSERTIONS_FOR_TOPIC and not edge_ids:
        return False
    return _has_heading_anchor(label, graph.source_units) or _has_local_source_span(
        assertions, graph.source_units
    )


def _has_heading_anchor(label: str, units: tuple[SourceUnit, ...]) -> bool:
    key = _topic_key(label)
    if len(key) < 3:
        return False
    for unit in units:
        if unit.kind != SourceUnitKind.HEADING or not _has_topic_identity(unit.text):
            continue
        heading_key = _topic_key(unit.text)
        if key in heading_key or heading_key in key:
            return True
    return False


def _has_local_source_span(assertions: list[Assertion], units: tuple[SourceUnit, ...]) -> bool:
    order_by_id = {unit.id: unit.source_order for unit in units}
    orders = [
        order_by_id[unit_id]
        for assertion in assertions
        for unit_id in assertion.source_unit_ids
        if unit_id in order_by_id
    ]
    if not orders:
        return False
    max_span = max(_LOCAL_SPAN_FLOOR, int(len(units) * _LOCAL_SPAN_RATIO))
    return max(orders) - min(orders) <= max_span


def _owner_heading_label(assertion: Assertion, units_by_id: dict[str, SourceUnit]) -> str:
    for unit_id in assertion.source_unit_ids:
        unit = units_by_id.get(unit_id)
        while unit is not None:
            if unit.kind == SourceUnitKind.HEADING and _has_topic_identity(unit.text):
                return _clean_heading(unit.text)
            unit = units_by_id.get(unit.parent_id) if unit.parent_id is not None else None
    return ""


def _clean_heading(text: str) -> str:
    return text.lstrip("#").strip()


def _topic_kind(assertions: list[Assertion]) -> TopicKind:
    kinds = {assertion.kind for assertion in assertions}
    if AssertionKind.PROCEDURE_STEP in kinds:
        return TopicKind.PROCEDURE
    if AssertionKind.RULE_STATEMENT in kinds:
        return TopicKind.RULE_SET
    if AssertionKind.ENTITY_FACT in kinds:
        return TopicKind.ENTITY
    return TopicKind.CONCEPT


def _projection_policy(assertions: list[Assertion]) -> ProjectionPolicy:
    topic_kind = _topic_kind(assertions)
    if topic_kind == TopicKind.PROCEDURE:
        return ProjectionPolicy(page_kind="procedure", page_family=PAGE_FAMILY_PROCEDURE_GUIDE)
    page_family = PAGE_FAMILY_BROAD_TOPIC if len(assertions) >= 48 else PAGE_FAMILY_TOPIC_CONCEPT
    return ProjectionPolicy(page_kind="concept", page_family=page_family)


def _weak_topic_gap(key: str, label: str, assertions: list[Assertion]) -> TopicGap:
    return TopicGap(
        id=f"tgp_{short_digest('weak-topic|' + key + '|' + '|'.join(a.id for a in assertions))}",
        gap_kind=GapKind.WEAK_TOPIC_IDENTITY,
        description=f"Candidate topic '{label}' has insufficient accepted closure for projection.",
        source_unit_ids=tuple(dict.fromkeys(u for a in assertions for u in a.source_unit_ids)),
        evidence_span_ids=tuple(dict.fromkeys(e for a in assertions for e in a.evidence_span_ids)),
    )


def _topic_key(subject: str) -> str:
    canonical = _canonical_subject(subject)
    try:
        return slugify(canonical)[:120]
    except ValueError:
        return _digest_key(canonical)


def _digest_key(subject: str) -> str:
    return f"subject-{short_digest(subject)}"


def _has_topic_identity(subject: str) -> bool:
    return bool(re.search(r"\w", subject, re.UNICODE))


def _canonical_subject(subject: str) -> str:
    text = " ".join(subject.strip().split())
    text = re.sub(r"^(?:a|an|the)\s+", "", text, flags=re.IGNORECASE)
    words = text.split()
    if len(words) == 1 and len(words[0]) > 3 and words[0].lower().endswith("s"):
        return words[0][:-1]
    return text


def _topic_state_id(source_hash: str, key: str) -> str:
    return f"tps_{short_digest(source_hash + '|topic|' + key)}"
