"""Wiki tools exposed to the model, bound to a WikiStore.

Each callable validates its arguments with the same Pydantic model that the
LLM sees as the tool schema, then delegates to the store. Domain/store
errors either return corrective draft feedback or raise with corrective
messages, depending on whether the failed write can safely be retried.
"""

from __future__ import annotations

import re
from dataclasses import replace

from forge.core.workflow import ToolDef, ToolSpec
from forge.tools.respond import RESPOND_DESCRIPTION, RespondParams
from pydantic import BaseModel, Field

from llmwiki.domain.objects import PlannedPageWrite, SourceSummaryBullet, SourceSummaryDraft
from llmwiki.domain.page_body_contracts import (
    canonicalize_source_summary_draft,
    canonicalize_source_summary_page_body,
    render_page_body_findings,
    render_source_summary_draft,
    validate_page_body,
    validate_source_summary_draft,
)
from llmwiki.domain.page_inspection import inspect_page_text, render_page_map
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.retrieval import render_context_pack, retrieve_wiki_context
from llmwiki.pdf.intermediate import OCR_MARKER
from llmwiki.store import WikiStore, WikiStoreError

_READ_PAGE_DEFAULT_CHARS = 3_000
_READ_PAGE_MAX_CHARS = 5_000
type _FocusKey = tuple[tuple[str, ...], str]
_WIKI_LINK_RE = re.compile(r"\[\[[a-z0-9][a-z0-9-]*\]\]")
_SOURCE_CITATION_RE = re.compile(r"\braw/[a-zA-Z0-9_./-]+|source-range-[a-z0-9]+-\d+")


def _strip_pipeline_markers(content: str) -> str:
    """Content hygiene at the wiki boundary: extraction-pipeline markers
    (e.g. the OCR caveat tag) are internal plumbing, never wiki content —
    observed quoted verbatim into a page despite the schema forbidding it."""
    return "\n".join(line for line in content.splitlines() if OCR_MARKER not in line)


def _page_body_contract_source_text(store: WikiStore, planned_write: PlannedPageWrite) -> str:
    if not planned_write.evidence:
        return ""
    raw_source = planned_write.evidence[0].raw_source
    if raw_source.source_format != "markdown":
        return ""
    return store.read_source(raw_source.source_locator)


def _validate_planned_page_body(
    store: WikiStore, planned_write: PlannedPageWrite, page_body: str
) -> None:
    source_text = _page_body_contract_source_text(store, planned_write)
    findings = validate_page_body(
        page_body,
        planned_write.resolved_page_body_contract,
        source_text=source_text,
    )
    if findings:
        raise WikiStoreError(
            render_page_body_findings(findings, planned_write.resolved_page_body_contract)
        )


class ReadSourceParams(BaseModel):
    source_locator: str = Field(
        description="RawSource locator relative to raw/, e.g. 'article.md'."
    )


class SearchWikiParams(BaseModel):
    query: str = Field(
        description="Search question or terms to match against the wiki index, page metadata, "
        "headings, links, and content."
    )


class ReadIndexParams(BaseModel):
    """No parameters — the index is one document."""


class InspectPageParams(BaseModel):
    page_id: str = Field(description="WikiPage page_id, e.g. 'bronze-age-collapse'.")
    max_sections: int = Field(
        default=40,
        ge=1,
        le=80,
        description="Maximum number of headings/sections to include in the compact page map.",
    )
    focus_query: str | None = Field(
        default=None,
        description=(
            "Optional topic or procedure phrase. When provided, the page map prioritizes "
            "matching section headings plus their ancestors and nearby siblings; if no "
            "headings match, treat that as missing coverage unless another page names "
            "the target directly."
        ),
    )


class ReadPageParams(BaseModel):
    page_id: str = Field(description="WikiPage page_id, e.g. 'bronze-age-collapse'.")
    offset: int = Field(
        default=0,
        ge=0,
        description="Character offset for chunked reads of large WikiPages.",
    )
    max_chars: int = Field(
        default=_READ_PAGE_DEFAULT_CHARS,
        ge=1,
        le=_READ_PAGE_MAX_CHARS,
        description=(
            "Maximum characters to return. Keep reads targeted; use offset for additional "
            "chunks only when the first chunk does not contain enough evidence."
        ),
    )


class WritePageParams(BaseModel):
    page_id: str = Field(
        description="WikiPage page_id as a kebab-case slug. Reuse an existing page_id to update."
    )
    page_kind: str = Field(description="WikiPage page_kind: source, entity, concept, or synthesis.")
    summary: str = Field(description="One-line summary of the page, used in the wiki index.")
    page_body: str = Field(
        description="Full PageBody markdown. Link related pages inline with [[page_id]]. "
        "Cite evidence as (raw/<source_locator>). Do not include frontmatter."
    )
    sources: list[str] = Field(
        default_factory=list,
        description="RawSource locators this page draws on, e.g. ['article.md'].",
    )


class FinishParams(BaseModel):
    report: str = Field(description="Short report of what was done and what changed.")


class PlannedWritePageParams(BaseModel):
    page_body: str = Field(
        description="Full PageBody markdown for the planned target page. "
        "Link related pages inline with [[page_id]]. Do not include frontmatter."
    )


class SourceSummaryBulletParams(BaseModel):
    bullet_text: str = Field(
        description="One concise source-summary claim bullet without a leading dash."
    )
    covered_source_claims: list[str] = Field(
        description="SourceClaim ids from SourceSummaryPlan covered by this bullet."
    )


class PlannedWriteSourceSummaryParams(BaseModel):
    source_record_text: str = Field(
        description="One source-record sentence with required wikilink and citation."
    )
    claim_bullets: list[SourceSummaryBulletParams] = Field(
        description="Three to five source-summary bullets with SourceClaim coverage ids."
    )


def read_source_tool(store: WikiStore) -> ToolDef:
    def _read_source(**kwargs: object) -> str:
        params = ReadSourceParams(**kwargs)  # type: ignore[arg-type]
        return store.read_source(params.source_locator)

    return ToolDef(
        spec=ToolSpec(
            name="read_source",
            description="Read one immutable source document from raw/.",
            parameters=ReadSourceParams,
        ),
        callable=_read_source,
    )


def search_wiki_tool(store: WikiStore) -> ToolDef:
    def _search_wiki(**kwargs: object) -> str:
        params = SearchWikiParams(**kwargs)  # type: ignore[arg-type]
        pack = retrieve_wiki_context(
            query=params.query,
            index_text=store.read_index(),
            page_texts=store.page_texts(),
        )
        return render_context_pack(pack)

    return ToolDef(
        spec=ToolSpec(
            name="search_wiki",
            description="Search the wiki's compiled navigation artifacts; returns matching "
            "page_ids with snippets, nearby links, and why each page matched.",
            parameters=SearchWikiParams,
        ),
        callable=_search_wiki,
    )


def read_index_tool(store: WikiStore) -> ToolDef:
    """Index-first navigation (pattern doc): the catalog answers questions
    about the wiki itself and its coverage that content search cannot."""

    def _read_index(**kwargs: object) -> str:
        ReadIndexParams(**kwargs)
        return store.read_index()

    return ToolDef(
        spec=ToolSpec(
            name="read_index",
            description="Read the wiki's index: the catalog of every page "
            "with a one-line summary, grouped by page_kind. Use this for "
            "questions about the wiki itself or what it covers.",
            parameters=ReadIndexParams,
        ),
        callable=_read_index,
    )


def inspect_page_tool(
    store: WikiStore, missing_focus_reports: set[str] | None = None
) -> ToolDef:
    missing_focus_by_source: set[_FocusKey] = set()

    def _inspect_page(**kwargs: object) -> str:
        params = InspectPageParams(**kwargs)  # type: ignore[arg-type]
        page_map = inspect_page_text(
            params.page_id,
            store.read_page(params.page_id),
            max_sections=params.max_sections,
            focus_query=params.focus_query,
        )
        focus_key = _focus_key(page_map.sources, params.focus_query)
        if focus_key is not None and focus_key in missing_focus_by_source:
            return _render_missing_focus_stop(page_map.sources, params.focus_query or "")
        if (
            focus_key is not None
            and page_map.page_family == "source-manifest"
            and page_map.focus_matched_sections == 0
        ):
            missing_focus_by_source.add(focus_key)
            if missing_focus_reports is not None:
                missing_focus_reports.add(
                    _missing_focus_label(page_map.sources, params.focus_query)
                )
        return render_page_map(page_map)

    return ToolDef(
        spec=ToolSpec(
            name="inspect_page",
            description=(
                "Return a compact map of one wiki page: metadata, related pages, headings, "
                "section character ranges, and source-range ids. Use this before read_page "
                "for complex procedures or large pages."
            ),
            parameters=InspectPageParams,
        ),
        callable=_inspect_page,
    )


def _focus_key(sources: tuple[str, ...], focus_query: str | None) -> _FocusKey | None:
    if not focus_query or not sources:
        return None
    return (tuple(sorted(sources)), " ".join(focus_query.lower().split()))


def _render_missing_focus_stop(sources: tuple[str, ...], focus_query: str) -> str:
    source_text = ", ".join(sources)
    return (
        "Focused source coverage was already checked on the source manifest.\n"
        f"source scope: {source_text}\n"
        f"focus query: {focus_query!r}\n"
        "No manifest section headings matched this focus. Stop inspecting related "
        "pages for this same source/procedure and answer that the wiki lacks "
        "source-backed procedure coverage unless another retrieved source page "
        "names it directly."
    )


def _missing_focus_label(sources: tuple[str, ...], focus_query: str | None) -> str:
    query = " ".join((focus_query or "").split())
    return f"{','.join(sorted(sources))}::{query}"


def grounded_chat_respond_tool(missing_focus_reports: set[str]) -> ToolDef:
    def _respond(**kwargs: object) -> str:
        params = RespondParams(**kwargs)  # type: ignore[arg-type]
        if missing_focus_reports:
            findings = _chat_response_findings(params.message)
            if findings:
                raise WikiStoreError(
                    "Chat answer violates missing-coverage grounding:\n"
                    + "\n".join(f"- {finding}" for finding in findings)
                    + "\nReplace the answer with a cited limitation. Include the inspected "
                    "[[PageId]], raw source locator or source-range id, and do not ask "
                    "the user to continue outside the wiki."
                )
        return params.message

    return ToolDef(
        spec=ToolSpec(
            name="respond",
            description=RESPOND_DESCRIPTION,
            parameters=RespondParams,
        ),
        callable=_respond,
    )


def _chat_response_findings(message: str) -> tuple[str, ...]:
    findings: list[str] = []
    if _WIKI_LINK_RE.search(message) is None:
        findings.append("missing inspected wiki page citation like [[page-id]]")
    if _SOURCE_CITATION_RE.search(message) is None:
        findings.append("missing raw source locator or source-range id")
    if message.rstrip().endswith("?"):
        findings.append("ends with a follow-up question after reporting missing coverage")
    return tuple(findings)


def read_page_tool(store: WikiStore, read_tracker: set[str] | None = None) -> ToolDef:
    def _read_page(**kwargs: object) -> str:
        params = ReadPageParams(**kwargs)  # type: ignore[arg-type]
        text = store.read_page(params.page_id)
        if read_tracker is not None:
            read_tracker.add(params.page_id)
        return _read_page_chunk(params.page_id, text, params.offset, params.max_chars)

    return ToolDef(
        spec=ToolSpec(
            name="read_page",
            description=(
                "Read a bounded chunk of one wiki page. Use search_wiki first, then read only "
                "the most relevant page chunks needed to answer."
            ),
            parameters=ReadPageParams,
        ),
        callable=_read_page,
    )


def _read_page_chunk(page_id: str, text: str, offset: int, max_chars: int) -> str:
    start = min(offset, len(text))
    end = min(start + max_chars, len(text))
    chunk = text[start:end]
    if start == 0 and end == len(text):
        return chunk
    lines = [
        f"[Showing wiki/{page_id}.md characters {start}-{end} of {len(text)}.]",
        "",
        chunk,
    ]
    if end < len(text):
        lines.extend(["", f"[Truncated. Continue with read_page offset={end}.]"])
    return "\n".join(lines)


def write_page_tool(
    store: WikiStore,
    today: str,
    prerequisites: list[str | dict[str, str]] | None = None,
    read_tracker: set[str] | None = None,
    write_log: list[str] | None = None,
) -> ToolDef:
    """write_page, optionally guarded by a read-before-rewrite contract.

    When *read_tracker* is shared with read_page_tool, rewriting an existing
    page that wasn't read this run raises — write_page replaces the whole
    page, and a 14B reliably "reconstructs" content it never saw (observed
    live twice; docs/open-questions.md #10). New pages are unaffected.

    *write_log*, when provided, records each successfully written page_id
    — the machine record behind manifest.pages_written and the salience
    write-count signal.
    """

    def _write_page(**kwargs: object) -> str:
        params = WritePageParams(**kwargs)  # type: ignore[arg-type]
        if (
            read_tracker is not None
            and params.page_id not in read_tracker
            and params.page_id in store.list_pages()
        ):
            raise WikiStoreError(
                f"WikiPage '{params.page_id}' already exists and write_page replaces "
                f"it entirely. Call read_page(page_id='{params.page_id}') first, "
                "then rewrite it carrying forward the content you keep."
            )
        metadata = PageMetadata(
            page_id=params.page_id,
            page_kind=params.page_kind,
            summary=params.summary,
            sources=tuple(params.sources),
            updated=today,
        )
        page = WikiPage.from_metadata(metadata, _strip_pipeline_markers(params.page_body))
        store.write_page(page)
        if write_log is not None:
            write_log.append(params.page_id)
        return f"Wrote wiki/{store.rendered_page_path(page)} and updated its index entry."

    return ToolDef(
        spec=ToolSpec(
            name="write_page",
            description="Create a new wiki page, or update one you have "
            "already read this run (write replaces the whole page); the "
            "index entry is maintained automatically.",
            parameters=WritePageParams,
        ),
        callable=_write_page,
        prerequisites=prerequisites or [],
    )


def planned_write_page_tool(
    store: WikiStore,
    today: str,
    planned_write: PlannedPageWrite,
    read_tracker: set[str] | None = None,
    write_log: list[str] | None = None,
) -> ToolDef:
    """write_page variant for PagePlan execution.

    PagePlan owns PageId, PageKind, PageMetadata, and projection fields.
    The model supplies only PageBody.
    """

    target_page = planned_write.page_metadata.page_id

    def _write_page_body(page_body: str) -> str:
        page_body = _strip_pipeline_markers(page_body)
        page_body = canonicalize_source_summary_page_body(
            page_body, planned_write.resolved_page_body_contract
        )
        _validate_planned_page_body(store, planned_write, page_body)
        if (
            read_tracker is not None
            and target_page not in read_tracker
            and target_page in store.list_pages()
        ):
            raise WikiStoreError(
                f"WikiPage '{target_page}' already exists and write_page replaces "
                f"it entirely. Call read_page(page_id='{target_page}') first, "
                "then rewrite it carrying forward the content you keep."
            )
        metadata = replace(planned_write.page_metadata, updated=today)
        page = WikiPage.from_metadata(metadata, page_body)
        store.write_page(page)
        if write_log is not None:
            write_log.append(target_page)
        return f"Wrote wiki/{store.rendered_page_path(page)} and updated its index entry."

    def _write_page(**kwargs: object) -> str:
        params = PlannedWritePageParams(**kwargs)  # type: ignore[arg-type]
        return _write_page_body(params.page_body)

    def _write_source_summary(**kwargs: object) -> str:
        if planned_write.source_summary_plan is None:
            raise WikiStoreError("PlannedPageWrite has no SourceSummaryPlan.")
        params = PlannedWriteSourceSummaryParams(**kwargs)  # type: ignore[arg-type]
        draft = SourceSummaryDraft(
            source_record_text=params.source_record_text,
            claim_bullets=tuple(
                SourceSummaryBullet(
                    bullet_text=item.bullet_text,
                    covered_source_claims=tuple(item.covered_source_claims),
                )
                for item in params.claim_bullets
            ),
        )
        draft = canonicalize_source_summary_draft(draft)
        source_text = _page_body_contract_source_text(store, planned_write)
        findings = validate_source_summary_draft(
            draft, planned_write.source_summary_plan, source_text=source_text
        )
        if findings:
            return render_page_body_findings(findings, planned_write.resolved_page_body_contract)
        return _write_page_body(render_source_summary_draft(draft))

    is_source_summary = planned_write.source_summary_plan is not None
    return ToolDef(
        spec=ToolSpec(
            name="write_page",
            description=f"Write the planned target page [[{target_page}]]. "
            "The PagePlan supplies PageId, PageKind, PageMetadata, and PagePath.",
            parameters=PlannedWriteSourceSummaryParams
            if is_source_summary
            else PlannedWritePageParams,
        ),
        callable=_write_source_summary if is_source_summary else _write_page,
    )


def finish_tool(name: str, description: str) -> ToolDef:
    def _finish(**kwargs: object) -> str:
        params = FinishParams(**kwargs)  # type: ignore[arg-type]
        return params.report

    return ToolDef(
        spec=ToolSpec(name=name, description=description, parameters=FinishParams),
        callable=_finish,
    )
