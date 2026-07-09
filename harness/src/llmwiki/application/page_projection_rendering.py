"""Markdown rendering helpers for page projection records."""

from __future__ import annotations

from collections.abc import Callable

from llmwiki.application.assertion_graph_artifacts import AssertionGraphArtifact
from llmwiki.application.page_projection_artifacts import related_link
from llmwiki.domain.assertion_graph import (
    Assertion,
    AssertionKind,
    EvidenceSpan,
    PageCoverageRecord,
    PageProjection,
    RenderedRelatedLink,
    TechnicalAtom,
    TechnicalAtomKind,
    TopicGap,
    TopicKind,
    TopicState,
)
from llmwiki.domain.ledger.canonical import short_digest


def topic_body(
    *,
    topic: TopicState,
    assertions: tuple[Assertion, ...],
    atoms: tuple[TechnicalAtom, ...],
    gaps: tuple[TopicGap, ...],
    related: tuple[RenderedRelatedLink, ...],
    graph: AssertionGraphArtifact,
    source_page_id: str,
) -> tuple[str, list[PageCoverageRecord]]:
    coverage: list[PageCoverageRecord] = []
    lines = [f"# {topic.label}", "", f"Source: [[{source_page_id}]]"]
    if _procedure_like(topic, assertions, atoms):
        _append_assertion_group(lines, coverage, "Procedure", assertions, graph)
        _append_assertion_group(
            lines, coverage, "Steps", assertions, graph, AssertionKind.PROCEDURE_STEP
        )
        _append_atoms(lines, coverage, "Required tables and formulas", atoms, graph, _required_atom)
        _append_assertion_group(
            lines,
            coverage,
            "Rules and exceptions",
            assertions,
            graph,
            AssertionKind.RULE_STATEMENT,
        )
        _append_assertion_group(
            lines, coverage, "Examples", assertions, graph, AssertionKind.EXAMPLE_STATEMENT
        )
    else:
        _append_assertion_group(lines, coverage, "Statements", assertions, graph)
        _append_assertion_group(
            lines, coverage, "Rules", assertions, graph, AssertionKind.RULE_STATEMENT
        )
        _append_assertion_group(
            lines, coverage, "Examples", assertions, graph, AssertionKind.EXAMPLE_STATEMENT
        )
        _append_atoms(lines, coverage, "Technical atoms", atoms, graph, lambda atom: True)
    _append_related(lines, coverage, related)
    _append_gaps(lines, coverage, gaps)
    if not coverage:
        text = f"{topic.label}: admitted topic with no renderable assertions or atoms."
        lines.extend(("", "## Status", "", f"- {text}"))
        coverage.append(_coverage("Status", topic.id, text))
    return "\n".join(lines).strip() + "\n", coverage


def source_manifest_body(
    topic: TopicState,
    topic_pages: tuple[PageProjection, ...],
    topic_by_id: dict[str, TopicState],
    page_id_by_topic: dict[str, str],
    source_title: str,
    source_locator: str,
    source_summary: str,
    source_review: str,
) -> tuple[str, list[PageCoverageRecord], tuple[RenderedRelatedLink, ...]]:
    coverage = [_coverage("Source", topic.id, f"Raw source: raw/{source_locator}")]
    lines = [
        f"# {source_title}",
        "",
        "## Source",
        "",
        f"- Raw source: `raw/{source_locator}`",
        f"- {source_summary}",
        "",
        "## Page Families",
        "",
    ]
    for family, count in _family_counts(topic_pages):
        text = f"- {family}: {count} page(s) - generated topic-state projections"
        lines.append(text)
        coverage.append(_coverage("Page Families", topic.id, text))
    lines.extend(("", "## Concept Entry Points", ""))
    links = []
    for projection in sorted(topic_pages, key=lambda item: _projection_title(item).casefold()):
        topic_id = projection.topic_state_id
        target_topic = topic_by_id[topic_id]
        page_id = page_id_by_topic[topic_id]
        summary = _projection_summary(target_topic, projection)
        text = f"- [[{page_id}]] - {target_topic.projection_policy.page_family}: {summary}"
        lines.append(text)
        coverage.append(_coverage("Concept Entry Points", topic_id, text))
        links.append(related_link(page_id, "source topic", summary, (topic_id,)))
    if source_review:
        lines.extend(("", source_review.strip()))
        coverage.append(_coverage("Source review", topic.id, source_review.strip()))
    return "\n".join(lines).strip() + "\n", coverage, tuple(links)


def _append_assertion_group(
    lines: list[str],
    coverage: list[PageCoverageRecord],
    heading: str,
    assertions: tuple[Assertion, ...],
    graph: AssertionGraphArtifact,
    kind: AssertionKind | None = None,
) -> None:
    selected = tuple(
        assertion for assertion in assertions if kind is None or assertion.kind == kind
    )
    if not selected:
        return
    lines.extend(("", f"## {heading}", ""))
    for assertion in selected:
        text = f"- {_assertion_text(assertion)} {_citation(assertion.evidence_span_ids, graph)}"
        lines.append(text)
        coverage.append(_coverage(heading, assertion.id, text))


def _append_atoms(
    lines: list[str],
    coverage: list[PageCoverageRecord],
    heading: str,
    atoms: tuple[TechnicalAtom, ...],
    graph: AssertionGraphArtifact,
    include: Callable[[TechnicalAtom], bool],
) -> None:
    selected = tuple(atom for atom in atoms if include(atom))
    if not selected:
        return
    lines.extend(("", f"## {heading}", ""))
    for index, atom in enumerate(selected, start=1):
        rendered = _atom_block(index, atom, graph)
        lines.extend(rendered.splitlines())
        lines.append("")
        coverage.append(_coverage(heading, atom.id, rendered))


def _append_related(
    lines: list[str],
    coverage: list[PageCoverageRecord],
    related: tuple[RenderedRelatedLink, ...],
) -> None:
    if not related:
        return
    lines.extend(("", "## Related pages", ""))
    for link in related:
        support = link.support_record_ids[0]
        text = f"- [[{link.target_page_id}]] - {link.relation_label}: {link.description}"
        lines.append(text)
        coverage.append(_coverage("Related pages", support, text))


def _append_gaps(
    lines: list[str], coverage: list[PageCoverageRecord], gaps: tuple[TopicGap, ...]
) -> None:
    if not gaps:
        return
    lines.extend(("", "## Open gaps", ""))
    for gap in gaps:
        text = f"- {gap.description}"
        lines.append(text)
        coverage.append(_coverage("Open gaps", gap.id, text))


def _procedure_like(
    topic: TopicState, assertions: tuple[Assertion, ...], atoms: tuple[TechnicalAtom, ...]
) -> bool:
    if topic.topic_kind == TopicKind.PROCEDURE or "recipe" in topic.projection_policy.page_family:
        return True
    has_steps = any(assertion.kind == AssertionKind.PROCEDURE_STEP for assertion in assertions)
    has_required_atoms = any(
        atom.atom_kind in {TechnicalAtomKind.TABLE, TechnicalAtomKind.FORMULA} for atom in atoms
    )
    return has_steps or has_required_atoms


def _required_atom(atom: TechnicalAtom) -> bool:
    return atom.atom_kind in {TechnicalAtomKind.TABLE, TechnicalAtomKind.FORMULA}


def _atom_block(index: int, atom: TechnicalAtom, graph: AssertionGraphArtifact) -> str:
    lines = [f'<a id="atom-{index}"></a>', f"**Atom:** {atom.atom_kind.value.replace('_', ' ')}"]
    context = _context(atom, graph)
    if context:
        lines.append(f"Context: {context}")
    lines.extend(("", f"```{_fence(atom)}", atom.exact_payload.strip(), "```"))
    return "\n".join(lines)


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
    return "text" if atom.atom_kind == TechnicalAtomKind.TABLE else ""


def _family_counts(topic_pages: tuple[PageProjection, ...]) -> tuple[tuple[str, int], ...]:
    counts: dict[str, int] = {}
    for projection in topic_pages:
        counts[projection.page_family] = counts.get(projection.page_family, 0) + 1
    return tuple(sorted(counts.items(), key=lambda item: item[0].casefold()))


def _projection_title(projection: PageProjection) -> str:
    return projection.page_body.splitlines()[0].lstrip("# ").strip()


def _projection_summary(topic: TopicState, projection: PageProjection) -> str:
    return (
        f"{topic.label}; {len(projection.coverage_records)} projected supported fragment(s), "
        f"{len(projection.rendered_related_links)} related link(s)."
    )


def _coverage(section: str, support_record_id: str, rendered: str) -> PageCoverageRecord:
    return PageCoverageRecord(
        coverage_id=f"coverage-{short_digest(section + '|' + support_record_id + '|' + rendered)}",
        page_section=section,
        support_record_id=support_record_id,
        rendered_text=rendered.strip(),
    )
