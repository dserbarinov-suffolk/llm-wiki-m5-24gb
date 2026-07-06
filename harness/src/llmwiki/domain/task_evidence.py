"""Deterministic evidence packs for task-shaped chat turns."""

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass

from llmwiki.domain.chat_grounding import ChatTaskMode
from llmwiki.domain.links import extract_links
from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile
from llmwiki.domain.pages import PageError, parse_page
from llmwiki.domain.search import SearchHit
from llmwiki.domain.structured_evidence import (
    StructuredEvidenceArtifact,
    select_structured_evidence_artifacts,
)

_STEP_RE = re.compile(
    r"^\s*(?P<sequence>\d+)\.\s+\*\*(?P<title>[^*]+)\*\*.*?\[\[(?P<page_id>[a-z0-9-]+)\]\]",
    re.MULTILINE,
)

@dataclass(frozen=True)
class ProcedureStepRequirement:
    sequence: int
    title: str
    evidence_page_id: str


@dataclass(frozen=True)
class TaskEvidencePage:
    page_id: str
    page_kind: str
    page_family: str
    summary: str
    excerpt: str


@dataclass(frozen=True)
class TaskEvidencePack:
    """Bounded, deterministic evidence selected before a task is executed."""

    procedure_id: str
    procedure_title: str
    steps: tuple[ProcedureStepRequirement, ...]
    pages: tuple[TaskEvidencePage, ...]
    structured_artifacts: tuple[StructuredEvidenceArtifact, ...] = ()

    @property
    def page_ids(self) -> frozenset[str]:
        page_ids = frozenset(page.page_id for page in self.pages)
        artifact_ids = frozenset(artifact.page_id for artifact in self.structured_artifacts)
        return page_ids | artifact_ids

    @property
    def evidence_texts(self) -> dict[str, str]:
        texts = {page.page_id: page.excerpt for page in self.pages}
        for artifact in self.structured_artifacts:
            existing = texts.get(artifact.page_id, "")
            texts[artifact.page_id] = f"{existing}\n\n{artifact.excerpt}".strip()
        return texts

    def render(self, *, require_procedure_execution: bool = True) -> str:
        lines = [
            "Deterministic task evidence pack:",
            f"- Procedure: [[{self.procedure_id}]] {self.procedure_title}",
            "- Required procedure steps:",
        ]
        for step in self.steps:
            lines.append(f"  {step.sequence}. {step.title} - evidence [[{step.evidence_page_id}]]")
        lines.append("")
        if require_procedure_execution:
            lines.extend(_execution_checklist(self.procedure_id))
        else:
            lines.extend(_explanation_checklist())
        if self.structured_artifacts:
            lines.append("Deterministic structured evidence artifacts:")
            for artifact in self.structured_artifacts:
                lines.extend(
                    (
                        f"### [[{artifact.page_id}]] {artifact.category}: {artifact.heading}",
                        artifact.excerpt.strip(),
                        "",
                    )
                )
        lines.append("Evidence pages:")
        for page in self.pages:
            family = f"/{page.page_family}" if page.page_family else ""
            lines.extend(
                (
                    f"### [[{page.page_id}]] ({page.page_kind}{family})",
                    page.summary,
                    "",
                    page.excerpt.strip(),
                    "",
                )
            )
        lines.extend(_closing_reminder(require_procedure_execution))
        return "\n".join(lines).strip()


def build_task_evidence_pack(
    pages: Mapping[str, str],
    hits: Sequence[SearchHit],
    *,
    task_mode: ChatTaskMode,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> TaskEvidencePack | None:
    """Build a task evidence pack from search hits and procedure-page links."""

    if task_mode not in {
        ChatTaskMode.EXPLAIN_PROCEDURE,
        ChatTaskMode.EXECUTE_PROCEDURE,
        ChatTaskMode.SOURCE_AUDIT,
    }:
        return None
    procedure_id = _best_procedure_page(pages, hits)
    if procedure_id is None:
        return None
    procedure_text = pages[procedure_id]
    procedure_page = parse_page(procedure_text)
    steps = _procedure_steps(procedure_page.page_body)
    if not steps:
        return None
    page_ids = _candidate_page_ids(procedure_id, procedure_page.page_body, steps, hits, pages)
    structured_artifacts = select_structured_evidence_artifacts(
        pages,
        page_ids,
        (procedure_page.page_body, *(step.title for step in steps)),
        model_profile=model_profile,
    )
    evidence_pages = _pack_pages(pages, page_ids, model_profile)
    if not evidence_pages:
        return None
    return TaskEvidencePack(
        procedure_id=procedure_id,
        procedure_title=_title(procedure_page.page_body) or procedure_page.summary,
        steps=steps,
        pages=evidence_pages,
        structured_artifacts=structured_artifacts,
    )


def _best_procedure_page(pages: Mapping[str, str], hits: Sequence[SearchHit]) -> str | None:
    for hit in hits:
        text = pages.get(hit.page_id)
        if text is None:
            continue
        try:
            page = parse_page(text)
        except PageError:
            continue
        metadata = page.page_metadata
        if metadata.page_kind == "procedure" or metadata.page_family == "procedure-guide":
            return metadata.page_id
    return None


def _procedure_steps(body: str) -> tuple[ProcedureStepRequirement, ...]:
    steps: list[ProcedureStepRequirement] = []
    for match in _STEP_RE.finditer(body):
        steps.append(
            ProcedureStepRequirement(
                sequence=int(match.group("sequence")),
                title=" ".join(match.group("title").split()),
                evidence_page_id=match.group("page_id"),
            )
        )
    return tuple(steps)


def _candidate_page_ids(
    procedure_id: str,
    procedure_body: str,
    steps: tuple[ProcedureStepRequirement, ...],
    hits: Sequence[SearchHit],
    pages: Mapping[str, str],
) -> tuple[str, ...]:
    ordered: list[str] = [procedure_id]
    ordered.extend(step.evidence_page_id for step in steps)
    ordered.extend(_prioritized_page_links(extract_links(procedure_body), pages))
    ordered.extend(hit.page_id for hit in hits)
    return tuple(dict.fromkeys(page_id for page_id in ordered if page_id in pages))


def _prioritized_page_links(page_ids: Iterable[str], pages: Mapping[str, str]) -> tuple[str, ...]:
    existing = tuple(dict.fromkeys(page_id for page_id in page_ids if page_id in pages))
    return tuple(sorted(existing, key=lambda page_id: _page_link_priority(page_id, pages)))


def _page_link_priority(page_id: str, pages: Mapping[str, str]) -> tuple[int, str]:
    try:
        page = parse_page(pages[page_id])
    except PageError:
        return (2, page_id)
    if page.page_metadata.page_family == "source-manifest":
        return (2, page_id)
    if page.page_kind == "source":
        return (0, page_id)
    return (1, page_id)


def _pack_pages(
    pages: Mapping[str, str], page_ids: tuple[str, ...], model_profile: ModelProfile
) -> tuple[TaskEvidencePage, ...]:
    packed: list[TaskEvidencePage] = []
    total = 0
    for page_id in page_ids:
        text = pages[page_id]
        try:
            page = parse_page(text)
        except PageError:
            continue
        if page_id != page_ids[0] and page.page_metadata.page_family == "source-manifest":
            continue
        cap = (
            model_profile.task_evidence_procedure_chars
            if page_id == page_ids[0]
            else model_profile.task_evidence_page_chars
        )
        remaining = model_profile.task_evidence_total_chars - total
        if remaining <= 0:
            break
        excerpt = _clip(page.page_body, min(cap, remaining))
        total += len(excerpt)
        packed.append(
            TaskEvidencePage(
                page_id=page.page_id,
                page_kind=page.page_kind,
                page_family=page.page_metadata.page_family,
                summary=page.summary,
                excerpt=excerpt,
            )
        )
    return tuple(packed)


def _clip(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    clipped = text[:max_chars].rstrip()
    return f"{clipped}\n\n[TRUNCATED: task evidence pack excerpt]"


def _title(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return ""


def _execution_checklist(procedure_id: str) -> list[str]:
    return [
        "ProcedureExecution submission checklist:",
        "- Call submit_procedure_execution before respond.",
        f"- procedure_id must be {procedure_id}.",
        "- step_results must include every sequence/title listed above.",
        "- For each output, set support to evidence, derived, assumption, or unresolved.",
        "- For broad steps, status=partial is acceptable when nested outputs are too large.",
        "- Put user-independent choices in assumptions; mark missing rule details unresolved.",
        "",
    ]


def _explanation_checklist() -> list[str]:
    return [
        "Procedure explanation checklist:",
        "- Walk through every required step listed above.",
        "- Name relevant table, code, formula, and worked-example artifacts exactly.",
        "- Treat the table-index artifact as the authoritative list of table titles.",
        "- Say plainly when a detail is a free choice or unresolved.",
        "",
    ]


def _closing_reminder(require_procedure_execution: bool) -> list[str]:
    if require_procedure_execution:
        return [
            "ProcedureExecution tool reminder:",
            "- For an execution request, the next tool call must be submit_procedure_execution.",
            "- Include every required step result.",
            "- Use unresolved outputs for missing details instead of inventing them.",
        ]
    return [
        "Procedure explanation reminder:",
        "- Explain the required steps and cite the structured table/code/formula evidence above.",
        "- Do not answer with a meta-summary that the steps were provided.",
    ]
