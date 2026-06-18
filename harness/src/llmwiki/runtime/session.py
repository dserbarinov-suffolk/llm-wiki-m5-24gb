"""Operation orchestrator: arranges workflow, runner, transcript, and log.

Side effects are coordinated here; content decisions belong to the model
and bookkeeping formats to the domain layer. The LLM client and context
manager are injected, so tests drive the real WorkflowRunner with a fake
client and no network.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from forge.context import ContextManager
from forge.core.messages import Message, MessageMeta, MessageRole, MessageType
from forge.core.runner import WorkflowRunner

from llmwiki.domain.chatwindow import QAPair
from llmwiki.domain.links import compute_findings
from llmwiki.domain.objects import (
    ExtractedUnit,
    ExtractionPrompt,
    IngestRun,
    LintFinding,
    LintRun,
    PagePlan,
    QueryRun,
    RawSource,
    Schema,
    SourceBundle,
    SourcePlan,
)
from llmwiki.domain.pages import WikiPage, parse_page, slugify
from llmwiki.domain.planning import (
    build_page_plan,
    observation_report,
    page_plan_to_json,
    planned_write_message,
)
from llmwiki.domain.salience import SalienceReport, compute_salience, reconcile_key_lists
from llmwiki.pdf import PdfError
from llmwiki.pdf.pipeline import (
    ExtractionResult,
    chunk_file,
    read_source_text,
    save_manifest,
)
from llmwiki.runtime.transcript import TranscriptWriter
from llmwiki.store import WikiStore
from llmwiki.workflows import (
    build_chat_workflow,
    build_ingest_workflow,
    build_lint_workflow,
    build_query_workflow,
)
from llmwiki.workflows.pdf_ingest import build_planned_write_workflow

_MAX_ITERATIONS = {
    "ingest": 24,
    "query": 12,
    "lint": 24,
    "pdf-chunk": 24,
    "pdf-integrate": 20,
    "pdf-planned-write": 16,
    "chat": 12,
}

# (pdf_path, source_rel, reextract) -> ExtractionResult; injectable for tests.
ExtractFn = Callable[[Path, str, bool], ExtractionResult]

# Harness-maintained health report page: rewritten by every lint pass, so it
# never accumulates inbound links and is exempted from orphan findings.
# History lives in log.md (and git), not in dated page copies.
HEALTH_PAGE = "wiki-health"

# Bare text usually means the model finished its work and wants to report.
# Name the terminal tool in the retry nudge so the model can exit the loop
# (forge ADR-013: small models need the structured way out spelled out).
_RETRY_NUDGES = {
    "ingest": (
        "Reply with exactly one tool call. If the wiki now fully reflects the "
        "source, call finish_ingest with your report; otherwise call the next "
        "tool you need."
    ),
    "query": ("Reply with exactly one tool call. Use respond to deliver your answer to the user."),
    "lint": (
        "Reply with exactly one tool call. If the review is complete, call "
        "finish_lint with the health report; otherwise call the next tool you need."
    ),
    "pdf-chunk": (
        "Reply with exactly one tool call. If the wiki now reflects this "
        "chunk, call finish_chunk with your notes; otherwise call the next "
        "tool you need."
    ),
    "pdf-integrate": (
        "Reply with exactly one tool call. If the hub page and cross-links "
        "are in place, call finish_ingest with your report; otherwise call "
        "the next tool you need."
    ),
    "pdf-planned-write": (
        "Reply with exactly one tool call. If the planned target page is "
        "written, call finish_planned_write with your report; otherwise call "
        "the next tool you need."
    ),
    "chat": ("Reply with exactly one tool call. Use respond to deliver your answer to the user."),
}


@dataclass(frozen=True)
class OperationResult:
    op: str
    subject: str
    output: str
    transcript_path: Path | None
    run: IngestRun | QueryRun | LintRun | None = None


@dataclass(frozen=True)
class Session:
    """One operation run: explicit dependencies, one public method per op."""

    store: WikiStore
    client: Any  # forge LLMClient protocol
    context_manager: ContextManager
    today: str
    runs_dir: Path | None = None
    run_id: str = ""  # unique per run (e.g. timestamp); falls back to date
    extract_pdf: ExtractFn | None = None  # required for PDF ingest; CLI wires it
    on_chunk_note: Callable[[str], None] | None = None  # per-chunk supervision

    async def ingest(
        self, source_path: str, reextract: bool = False, reintegrate: bool = False
    ) -> OperationResult:
        if source_path.lower().endswith(".pdf"):
            return await self._ingest_pdf(source_path, reextract, reintegrate)
        if reintegrate:
            raise PdfError("--reintegrate applies to chunked (PDF) sources only.")
        workflow = build_ingest_workflow(self.store, self.today)
        message = (
            f"Ingest the source 'raw/{source_path}' into the wiki. "
            f"Pass path='{source_path}' to read_source."
        )
        report, transcript = await self._run(workflow, message, "ingest")
        self.store.append_log(self.today, "ingest", source_path, report)
        return OperationResult(
            "ingest",
            source_path,
            report,
            transcript,
            self._markdown_ingest_run(source_path),
        )

    async def _ingest_pdf(
        self, source_path: str, reextract: bool, reintegrate: bool = False
    ) -> OperationResult:
        if self.extract_pdf is None:
            raise RuntimeError("Session has no PDF extractor wired (extract_pdf).")
        result = self.extract_pdf(self.store.source_path(source_path), source_path, reextract)
        manifest, total = result.manifest, len(result.manifest.chunks)
        raw_source = self.store.raw_source(source_path)
        source_bundle = SourceBundle.one(raw_source)
        extracted_units = self._extracted_units(result, raw_source)
        page_plan = build_page_plan(
            plan_id=f"{manifest.sha256[:16]}-page-plan",
            source_bundle=source_bundle,
            raw_source=raw_source,
            extracted_units=extracted_units,
            existing_pages=self.store.page_texts(),
            wiki_structure=self.store.structure,
            today=self.today,
        )
        self._write_page_plan(result.cache_dir, page_plan)

        units = {unit.unit_id: unit for unit in extracted_units}
        actual_pages_by_unit: dict[str, list[str]] = {}
        reports: list[str] = []
        last_transcript: Path | None = None
        hub = slugify(Path(source_path).stem)
        for planned_write in page_plan.planned_writes:
            write_log: list[str] = []
            report, last_transcript = await self._run(
                build_planned_write_workflow(
                    self.store,
                    self.today,
                    planned_write,
                    write_log=write_log,
                ),
                planned_write_message(planned_write, units),
                "pdf-planned-write",
                tag=f"pdf-plan-{planned_write.write_id}",
            )
            reports.append(f"{planned_write.page_metadata.page_id}: {report}")
            if planned_write.page_metadata.page_id != hub:
                for unit_id in planned_write.extracted_units:
                    actual_pages_by_unit.setdefault(unit_id, []).extend(write_log)
            if self.on_chunk_note is not None:
                self.on_chunk_note(
                    f"[planned write {len(reports)}/{len(page_plan.planned_writes)}] "
                    f"{planned_write.page_metadata.page_id}: {report}"
                )

        salience = compute_salience(
            self.store.page_texts(),
            self._write_counts(actual_pages_by_unit),
            source_text=read_source_text(result.cache_dir),
            scope_source=source_path,
            exclude_inbound_from=frozenset({hub}),
        )
        self._reconcile_hub_key_lists(hub, salience)
        manifest = self._mark_manifest_planned(manifest, actual_pages_by_unit).mark_integrated()
        save_manifest(ExtractionResult(manifest=manifest, cache_dir=result.cache_dir))
        observation_path = self._write_observation(result.cache_dir, page_plan)
        report = (
            f"Planned ingest completed for {total} extracted unit(s) from "
            f"raw/{source_path}. Executed {len(page_plan.planned_writes)} planned "
            f"page write(s). Observation: {observation_path}."
        )
        self.store.append_log(self.today, "ingest", source_path, report)
        return OperationResult(
            "ingest",
            source_path,
            report,
            last_transcript,
            self._pdf_ingest_run(source_path, page_plan),
        )

    def _reconcile_hub_key_lists(self, hub: str, salience: SalienceReport) -> None:
        """Harness-owned bookkeeping: the hub's key-lists mirror the salience
        report by construction (same contract as index.md entries)."""
        if hub not in self.store.list_pages():
            return  # no hub page; lint's findings will surface it
        page = parse_page(hub, self.store.read_page(hub))
        body = reconcile_key_lists(page.body, salience)
        if body != page.body:
            self.store.write_page(replace(page, body=body, updated=self.today))

    async def query(self, question: str) -> OperationResult:
        workflow = build_query_workflow(self.store, self.today)
        # Factual lookups don't benefit from Qwen3's thinking preamble.
        answer, transcript = await self._run(workflow, question + " /no_think", "query")
        self.store.append_log(self.today, "query", question, answer)
        return OperationResult("query", question, answer, transcript, QueryRun(question))

    async def chat_turn(
        self, question: str, window: Sequence[QAPair], grounded: bool, tag: str
    ) -> tuple[str, Path | None]:
        """One read-only conversation turn, seeded with windowed Q/A pairs.

        The seed carries question/answer text only — prior tool calls and
        page contents are never replayed; evidence is re-fetched on demand.
        *grounded* (a conversation's first turn) provisions the wiki index
        with the question, so the opening answer starts from the catalog
        and drills into pages — grounding by provisioning, not enforcement.
        """
        workflow = build_chat_workflow(self.store)
        rendered = workflow.build_system_prompt(schema=self.store.read_schema())
        seed = [Message(MessageRole.SYSTEM, rendered, MessageMeta(MessageType.SYSTEM_PROMPT))]
        for pair in window:
            seed.append(
                Message(MessageRole.USER, pair.question, MessageMeta(MessageType.USER_INPUT))
            )
            seed.append(
                Message(MessageRole.ASSISTANT, pair.answer, MessageMeta(MessageType.TEXT_RESPONSE))
            )
        message = question + " /no_think"
        if grounded:
            message = (
                "The wiki's index — the catalog of every page:\n\n"
                f"{self.store.read_index()}\n\n"
                f"Question: {message}"
            )
        seed.append(Message(MessageRole.USER, message, MessageMeta(MessageType.USER_INPUT)))
        return await self._run(workflow, message, "chat", tag=tag, initial_messages=seed)

    async def lint(self) -> OperationResult:
        findings = compute_findings(
            self.store.page_texts(),
            self.store.index_names(),
            exempt_from_orphans=frozenset({HEALTH_PAGE}),
        )
        if not self.store.list_pages():
            report = "Wiki is empty — nothing to lint."
            self.store.append_log(self.today, "lint", "empty wiki", report)
            return OperationResult(
                "lint",
                "wiki health",
                report,
                None,
                LintRun(lint_findings=()),
            )
        workflow = build_lint_workflow(self.store, self.today)
        salience_block = compute_salience(self.store.page_texts()).render()
        message = (
            "Run a lint pass. Deterministic findings from the harness:\n\n"
            f"{findings.render()}\n\n"
            f"{salience_block}\n"
            "The salience report names the most load-bearing pages — protect "
            "their content. Review the affected pages (and spot-check "
            "others), then call finish_lint with the health report."
        )
        report, transcript = await self._run(workflow, message, "lint")
        self._file_lint_report(report)
        self.store.append_log(self.today, "lint", "wiki health", report)
        return OperationResult(
            "lint",
            "wiki health",
            report,
            transcript,
            LintRun(lint_findings=self._lint_findings()),
        )

    async def _run(
        self,
        workflow: Any,
        message: str,
        op: str,
        tag: str = "",
        initial_messages: list[Message] | None = None,
    ) -> tuple[str, Path | None]:
        writer = (
            TranscriptWriter(self.runs_dir / f"{self.run_id or self.today}-{tag or op}.jsonl")
            if self.runs_dir is not None
            else None
        )
        runner = WorkflowRunner(
            client=self.client,
            context_manager=self.context_manager,
            max_iterations=_MAX_ITERATIONS[op],
            on_message=writer.on_message if writer else None,
            retry_nudge=_RETRY_NUDGES[op],
        )
        try:
            result = await runner.run(
                workflow,
                message,
                prompt_vars={"schema": self.store.read_schema()},
                initial_messages=initial_messages,
            )
        finally:
            if writer:
                writer.close()
        return str(result), writer.path if writer else None

    def _file_lint_report(self, report: str) -> None:
        self.store.write_page(
            WikiPage(
                name=HEALTH_PAGE,
                category="synthesis",
                summary=f"Wiki health report from the latest lint pass ({self.today}).",
                body=report,
                updated=self.today,
            )
        )

    def _schema_object(self) -> Schema:
        return Schema(page_contracts=self.store.read_schema())

    def _extraction_prompt(self, subject: str) -> ExtractionPrompt:
        return ExtractionPrompt(
            instruction_text=(
                "Use the local LLM-Wiki ingest workflow from Schema. "
                f"Run subject: raw/{subject}."
            )
        )

    def _source_bundle(self, source_path: str) -> SourceBundle:
        return SourceBundle.one(self.store.raw_source(source_path))

    def _markdown_ingest_run(self, source_path: str) -> IngestRun:
        raw_source = self.store.raw_source(source_path)
        page_id = slugify(Path(source_path).stem)
        metadata = WikiPage(
            name=page_id,
            category="source",
            summary=f"Source page for raw/{source_path}.",
            body="",
            sources=(source_path,),
            updated=self.today,
        ).page_metadata
        source_plan = SourcePlan(
            raw_source=raw_source,
            source_classification=raw_source.source_format,
            ingest_disposition="create-or-update",
            target_page_metadata=metadata,
            target_page_paths=(str(self.store.structure.render_path(metadata)),),
            handling_notes="Default one-source ingest plan.",
        )
        return IngestRun(
            source_bundle=SourceBundle.one(raw_source),
            wiki_structure=self.store.structure,
            schema=self._schema_object(),
            extraction_prompt=self._extraction_prompt(source_path),
            source_plans=(source_plan,),
        )

    def _extracted_units(
        self, result: ExtractionResult, raw_source: RawSource
    ) -> tuple[ExtractedUnit, ...]:
        units = []
        for record in result.manifest.chunks:
            text = chunk_file(result.cache_dir, record.chunk_id).read_text(encoding="utf-8")
            units.append(
                ExtractedUnit(
                    unit_id=f"unit-{record.chunk_id:04d}",
                    raw_source=raw_source,
                    locator=f"p.{record.start_page}-{record.end_page}",
                    heading_path=record.heading,
                    text=text,
                    extraction_status="ok",
                    source_hash=result.manifest.sha256,
                )
            )
        return tuple(units)

    def _write_page_plan(self, cache_dir: Path, page_plan: PagePlan) -> Path:
        path = cache_dir / "page_plan.json"
        path.write_text(page_plan_to_json(page_plan), encoding="utf-8")
        return path

    def _write_observation(self, cache_dir: Path, page_plan: PagePlan) -> str:
        path = cache_dir / "observation.md"
        path.write_text(observation_report(page_plan), encoding="utf-8")
        return str(path)

    def _mark_manifest_planned(self, manifest: Any, pages_by_unit: dict[str, list[str]]) -> Any:
        updated = manifest
        for record in manifest.chunks:
            unit_id = f"unit-{record.chunk_id:04d}"
            pages = tuple(dict.fromkeys(pages_by_unit.get(unit_id, ())))
            notes = "Global PagePlan executed"
            if pages:
                notes += ": " + ", ".join(f"[[{page}]]" for page in pages)
            if record.status == "done" and record.notes == notes and record.pages_written == pages:
                continue
            updated = updated.mark_done(record.chunk_id, notes, pages_written=pages)
        return updated

    def _write_counts(self, pages_by_unit: dict[str, list[str]]) -> dict[str, int]:
        counts: dict[str, int] = {}
        for pages in pages_by_unit.values():
            for page in pages:
                counts[page] = counts.get(page, 0) + 1
        return counts

    def _pdf_ingest_run(self, source_path: str, page_plan: PagePlan) -> IngestRun:
        raw_source = self.store.raw_source(source_path)
        plans = tuple(
            SourcePlan(
                raw_source=raw_source,
                source_classification="planned pdf write",
                ingest_disposition=write.action,
                target_page_metadata=write.page_metadata,
                target_page_paths=(
                    (write.projection.page_path if write.projection else ""),
                ),
                expected_wiki_pages=(write.page_metadata.page_id,),
                handling_notes="Global PagePlan write.",
            )
            for write in page_plan.planned_writes
        )
        return IngestRun(
            source_bundle=SourceBundle.one(raw_source),
            wiki_structure=self.store.structure,
            schema=self._schema_object(),
            extraction_prompt=self._extraction_prompt(source_path),
            source_plans=plans,
            page_plan=page_plan,
        )

    def _lint_findings(self) -> tuple[LintFinding, ...]:
        findings = compute_findings(
            self.store.page_texts(),
            self.store.index_names(),
            exempt_from_orphans=frozenset({HEALTH_PAGE}),
        )
        converted: list[LintFinding] = []
        for page, links in findings.broken_links.items():
            converted.extend(
                LintFinding("broken link", wiki_page=page, cross_reference=link)
                for link in links
            )
        converted.extend(
            LintFinding("orphan page", wiki_page=page) for page in findings.orphan_pages
        )
        converted.extend(
            LintFinding("missing from index", wiki_page=page)
            for page in findings.missing_from_index
        )
        converted.extend(
            LintFinding("stale index entry", wiki_page=page)
            for page in findings.stale_index_entries
        )
        return tuple(converted)
