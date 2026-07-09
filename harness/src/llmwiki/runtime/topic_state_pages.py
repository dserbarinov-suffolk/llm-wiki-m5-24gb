"""Project admitted topic states into source-scoped wiki pages."""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.topic_state_artifacts import TopicStateArtifact
from llmwiki.domain.assertion_graph import (
    Assertion,
    EvidenceSpan,
    TechnicalAtom,
    TopicKind,
    TopicState,
)
from llmwiki.domain.ledger.artifacts import (
    LedgerQualityReportArtifact,
    ProjectionCoverageArtifact,
    build_projection_coverage_artifact,
)
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.ledger.coverage import ProjectionCoverage, RenderedPage
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.pointers import ledger_quality_report_pointer
from llmwiki.domain.ledger.projection import ProjectionSourceSupport
from llmwiki.domain.ledger.source_manifest_navigation import (
    build_source_navigation_plan,
    render_source_manifest,
    source_review_section,
)
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify
from llmwiki.runtime.ledger_pages import build_source_wiki_page, ledger_summary


@dataclass(frozen=True)
class TopicStatePageProjection:
    source_page: WikiPage
    linked_pages: tuple[WikiPage, ...]
    coverage_artifact: ProjectionCoverageArtifact


def build_topic_state_page_projection(
    *,
    ledger: ClaimLedger,
    structure: DocumentStructure,
    page_id: str,
    title: str,
    source_locator: str,
    today: str,
    decision: str,
    rendered: RenderedPage,
    support: ProjectionSourceSupport,
    projection_report_artifact: LedgerQualityReportArtifact,
    assertion_graph_artifact: AssertionGraphArtifact,
    topic_state_artifact: TopicStateArtifact,
) -> TopicStatePageProjection:
    linked_pages = _linked_pages(
        source_page_id=page_id,
        source_locator=source_locator,
        today=today,
        graph=assertion_graph_artifact,
        topic_artifact=topic_state_artifact,
    )
    navigation = build_source_navigation_plan(
        source_page_id=page_id,
        title=title,
        source_locator=source_locator,
        ledger_summary=ledger_summary(ledger, decision, len(linked_pages)),
        linked_pages=linked_pages,
        structure=structure,
        collection_plans=(),
    )
    source_body = render_source_manifest(navigation)
    review = source_review_section(rendered.page_body)
    if review:
        source_body = f"{source_body.rstrip()}\n\n{review}\n"
    coverage_artifact = build_projection_coverage_artifact(
        wiki_page_locator=page_id,
        page_body_hash=short_digest(source_body, 32),
        support_set=(support,),
        coverage=ProjectionCoverage(()),
        ledger_quality_report_pointer=ledger_quality_report_pointer(
            projection_report_artifact.ledger_quality_report_artifact_id,
            projection_report_artifact.ledger_quality_report_fingerprint,
        ),
    )
    source_page = build_source_wiki_page(
        page_id,
        source_locator,
        title,
        ledger_summary(ledger, decision, len(linked_pages)),
        today,
        source_body,
        coverage_artifact,
    )
    return TopicStatePageProjection(source_page, linked_pages, coverage_artifact)


def _linked_pages(
    *,
    source_page_id: str,
    source_locator: str,
    today: str,
    graph: AssertionGraphArtifact,
    topic_artifact: TopicStateArtifact,
) -> tuple[WikiPage, ...]:
    pages: list[WikiPage] = []
    page_id_by_topic = {
        topic.id: _topic_page_id(source_page_id, topic)
        for topic in topic_artifact.topic_states
        if topic.topic_kind != TopicKind.SOURCE_MANIFEST
    }
    for topic in topic_artifact.topic_states:
        if topic.topic_kind == TopicKind.SOURCE_MANIFEST:
            continue
        pages.append(
            _topic_page(
                source_page_id=source_page_id,
                source_locator=source_locator,
                today=today,
                topic=topic,
                graph=graph,
                topic_artifact=topic_artifact,
                page_id_by_topic=page_id_by_topic,
            )
        )
    return tuple(sorted(pages, key=lambda page: page.page_id))


def _topic_page(
    *,
    source_page_id: str,
    source_locator: str,
    today: str,
    topic: TopicState,
    graph: AssertionGraphArtifact,
    topic_artifact: TopicStateArtifact,
    page_id_by_topic: dict[str, str],
) -> WikiPage:
    page_id = page_id_by_topic[topic.id]
    assertions = _assertions(topic, graph)
    atoms = _atoms(topic, graph)
    body = _body(topic, assertions, atoms, graph, topic_artifact, page_id_by_topic, source_page_id)
    metadata = PageMetadata(
        page_id=page_id,
        page_kind=topic.projection_policy.page_kind,
        summary=_summary(topic, assertions, atoms, source_locator),
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=source_page_id,
        category_path=f"{topic.projection_policy.page_kind}s",
        projection_coverage_pointer=f"topic-state-{topic.id}@{short_digest(body, 32)}",
        page_family=topic.projection_policy.page_family,
    )
    return WikiPage.from_metadata(metadata, body)


def _body(
    topic: TopicState,
    assertions: tuple[Assertion, ...],
    atoms: tuple[TechnicalAtom, ...],
    graph: AssertionGraphArtifact,
    topic_artifact: TopicStateArtifact,
    page_id_by_topic: dict[str, str],
    source_page_id: str,
) -> str:
    lines = [f"# {topic.label}", "", f"Source: [[{source_page_id}]]", "", "## Statements", ""]
    for assertion in assertions:
        citation = _citation(assertion.evidence_span_ids, graph)
        lines.append(f"- {_assertion_text(assertion)} {citation}")
    _append_technical_atoms(lines, atoms, graph)
    _append_related(lines, topic, topic_artifact, page_id_by_topic)
    _append_gaps(lines, topic, topic_artifact)
    return "\n".join(lines).strip() + "\n"


def _append_technical_atoms(
    lines: list[str], atoms: tuple[TechnicalAtom, ...], graph: AssertionGraphArtifact
) -> None:
    if not atoms:
        return
    lines.extend(("", "## Technical atoms", ""))
    for index, atom in enumerate(atoms, start=1):
        lines.append(f'<a id="atom-{index}"></a>')
        lines.append(f"**Atom:** {atom.atom_kind.value.replace('_', ' ')}")
        context = _context(atom, graph)
        if context:
            lines.append(f"Context: {context}")
        lines.append("")
        fence = _fence(atom)
        lines.extend((f"```{fence}", atom.exact_payload.strip(), "```", ""))


def _append_related(
    lines: list[str],
    topic: TopicState,
    topic_artifact: TopicStateArtifact,
    page_id_by_topic: dict[str, str],
) -> None:
    dependencies = [
        dependency
        for dependency in topic_artifact.topic_dependencies
        if dependency.id in topic.required_dependency_ids
        and dependency.to_topic_state_id in page_id_by_topic
    ]
    if not dependencies:
        return
    lines.extend(("", "## Related pages", ""))
    for dependency in dependencies:
        target_page_id = page_id_by_topic[dependency.to_topic_state_id]
        label = dependency.relation.value.replace("_", " ")
        lines.append(f"- [[{target_page_id}]] - {label}: source-supported topic dependency")


def _append_gaps(
    lines: list[str], topic: TopicState, topic_artifact: TopicStateArtifact
) -> None:
    gaps = [gap for gap in topic_artifact.topic_gaps if gap.id in topic.unresolved_gap_ids]
    if not gaps:
        return
    lines.extend(("", "## Open gaps", ""))
    for gap in gaps:
        lines.append(f"- {gap.description}")


def _assertions(topic: TopicState, graph: AssertionGraphArtifact) -> tuple[Assertion, ...]:
    by_id = {assertion.id: assertion for assertion in graph.assertions}
    return tuple(by_id[item] for item in topic.accepted_assertion_ids if item in by_id)


def _atoms(topic: TopicState, graph: AssertionGraphArtifact) -> tuple[TechnicalAtom, ...]:
    by_id = {atom.id: atom for atom in graph.technical_atoms}
    return tuple(by_id[item] for item in topic.accepted_technical_atom_ids if item in by_id)


def _assertion_text(assertion: Assertion) -> str:
    obj = assertion.object_value or assertion.object_entity_id or ""
    return f"{assertion.subject} {assertion.predicate} {obj}.".replace("..", ".")


def _citation(span_ids: tuple[str, ...], graph: AssertionGraphArtifact) -> str:
    spans = {span.id: span for span in graph.evidence_spans}
    page_labels = tuple(
        dict.fromkeys(_page_label(spans[item]) for item in span_ids if item in spans)
    )
    if not page_labels:
        return ""
    return f"({graph.source_locator} {', '.join(page_labels)})"


def _context(atom: TechnicalAtom, graph: AssertionGraphArtifact) -> str:
    spans = {span.id: span for span in graph.evidence_spans}
    texts = [spans[item].exact_text.strip() for item in atom.context_span_ids if item in spans]
    return " ".join(texts)[:220]


def _page_label(span: EvidenceSpan) -> str:
    start, end = span.page_span
    if start <= 0 or end <= 0:
        return "document"
    return f"p.{start}" if start == end else f"p.{start}-{end}"


def _fence(atom: TechnicalAtom) -> str:
    if atom.atom_kind.value == "code_block":
        return ""
    if atom.atom_kind.value == "table":
        return "text"
    return ""


def _summary(
    topic: TopicState,
    assertions: tuple[Assertion, ...],
    atoms: tuple[TechnicalAtom, ...],
    source_locator: str,
) -> str:
    return (
        f"{topic.label}: {len(assertions)} accepted assertion(s) and "
        f"{len(atoms)} technical atom(s) from raw/{source_locator}."
    )


def _topic_page_id(source_page_id: str, topic: TopicState) -> str:
    return slugify(f"{source_page_id}-{topic.topic_key}")[:180]
