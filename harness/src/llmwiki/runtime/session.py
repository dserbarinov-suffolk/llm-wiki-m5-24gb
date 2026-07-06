"""Operation orchestrator: arranges workflow, runner, transcript, and log.

Side effects are coordinated here; content decisions belong to the model
and bookkeeping formats to the domain layer. The LLM client and context
manager are injected, so tests drive the real WorkflowRunner with a fake
client and no network.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from forge.context import ContextManager
from forge.core.messages import Message
from forge.core.runner import WorkflowRunner

from llmwiki.domain.chatwindow import QAPair
from llmwiki.domain.claim_support import (
    ClaimSupportAuditReport,
    ClaimSupportSelection,
    ClaimSupportVerdict,
)
from llmwiki.domain.evidence_registry import SourceText, source_text_from_text
from llmwiki.domain.evidence_registry_io import registry_to_json
from llmwiki.domain.graph import GraphStatus, build_wiki_graph, graph_status
from llmwiki.domain.ledger.canonical import short_digest
from llmwiki.domain.links import compute_findings
from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile
from llmwiki.domain.objects import (
    ExtractedUnit,
    ExtractionPrompt,
    IngestRun,
    LintRun,
    PagePlan,
    QueryRun,
    RawSource,
    Schema,
    SourceBundle,
    SourcePlan,
    SourcePlanContractSelection,
)
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify
from llmwiki.domain.planning import (
    build_page_plan,
    observation_report,
    page_plan_to_json,
)
from llmwiki.domain.salience import compute_salience
from llmwiki.domain.source_batching import SourceTextChunk, markdown_source_chunks
from llmwiki.pdf import PdfError
from llmwiki.pdf.document import DocumentModel
from llmwiki.pdf.pipeline import (
    ExtractionResult,
    chunk_file,
    read_document_model,
    read_source_text,
    save_manifest,
)
from llmwiki.runtime.chat_turn import prepare_chat_turn
from llmwiki.runtime.cross_source_pipeline import build_cross_source_pages
from llmwiki.runtime.ingest_confidence import record_post_ingest_confidence
from llmwiki.runtime.ledger_pipeline import build_source_ledger
from llmwiki.runtime.ledger_segmentation import ChunkText
from llmwiki.runtime.provenance_audit import build_provenance_audit, report_to_json
from llmwiki.runtime.provenance_audit_render import render_markdown
from llmwiki.runtime.transcript import TranscriptWriter
from llmwiki.store import WikiStore
from llmwiki.workflows import (
    build_claim_support_workflow,
    build_lint_workflow,
    build_query_workflow,
)

_MAX_ITERATIONS = {
    "ingest": 24,
    "query": 12,
    "lint": 24,
    "pdf-chunk": 24,
    "pdf-integrate": 20,
    "pdf-planned-write": 16,
    "planned-write": 16,
    "chat": 12,
    "claim-support": 8,
}

_MAX_TOOL_ERRORS = {
    "pdf-planned-write": 5,
    "planned-write": 5,
}

# (pdf_path, source_rel, reextract) -> ExtractionResult; injectable for tests.
ExtractFn = Callable[[Path, str, bool], ExtractionResult]

# Harness-maintained health report page: rewritten by every lint pass, so it
# never accumulates inbound links and is exempted from orphan findings.
# History lives in log.md (and git), not in dated page copies.
HEALTH_PAGE = "wiki-health"
_LINT_PROMPT_MAX_FINDINGS_PER_SECTION = 25
_LINT_MODEL_MAX_FINDINGS = 50

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
    "planned-write": (
        "Reply with exactly one tool call. If the planned target page is "
        "written, call finish_planned_write with your report; otherwise call "
        "the next tool you need."
    ),
    "chat": ("Reply with exactly one tool call. Use respond to deliver your answer to the user."),
    "claim-support": (
        "Reply with exactly one tool call. If every selected candidate has a "
        "record_claim_support_verdict call, call finish_claim_support; otherwise "
        "record the next missing verdict."
    ),
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
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE
    runs_dir: Path | None = None
    run_id: str = ""  # unique per run (e.g. timestamp); falls back to date
    extract_pdf: ExtractFn | None = None  # required for PDF ingest; CLI wires it
    on_chunk_note: Callable[[str], None] | None = None  # per-chunk supervision

    async def ingest(
        self, source_locator: str, reextract: bool = False, reintegrate: bool = False
    ) -> OperationResult:
        if source_locator.lower().endswith(".pdf"):
            return await self._ingest_pdf(source_locator, reextract, reintegrate)
        if reintegrate:
            raise PdfError("--reintegrate applies to chunked (PDF) sources only.")
        return await self._ingest_markdown(source_locator)

    async def _ingest_markdown(self, source_locator: str) -> OperationResult:
        raw_source = self.store.raw_source(source_locator)
        source_bundle = SourceBundle.one(raw_source)
        source_text = self.store.read_source_for_ingest(source_locator)
        source_text_record = source_text_from_text(source_locator, source_text)
        title = _markdown_title(source_locator)
        source_chunks = markdown_source_chunks(
            source_text, title, model_profile=self.model_profile
        )
        extracted_units = self._markdown_extracted_units(
            raw_source,
            source_chunks,
            source_hash=source_text_record.source_hash,
            fallback_title=title,
            fallback_text=source_text,
        )
        page_plan = build_page_plan(
            plan_id=f"{slugify(Path(source_locator).stem)}-page-plan",
            source_bundle=source_bundle,
            raw_source=raw_source,
            extracted_units=extracted_units,
            existing_pages=self.store.page_texts(),
            wiki_structure=self.store.structure,
            today=self.today,
            schema=self._schema_object(),
            model_profile=self.model_profile,
        )
        chunks = tuple(
            ChunkText(unit.unit_id, unit.locator, unit.heading_path, unit.text)
            for unit in extracted_units
        )
        return self._finish_ledger_ingest(
            source_locator=source_locator,
            page_plan=page_plan,
            chunks=chunks,
            document_model=None,
            source_text=source_text_record,
            run=self._markdown_ingest_run(source_locator, page_plan),
        )

    async def _ingest_pdf(
        self, source_locator: str, reextract: bool, reintegrate: bool = False
    ) -> OperationResult:
        if self.extract_pdf is None:
            raise RuntimeError("Session has no PDF extractor wired (extract_pdf).")
        result = self.extract_pdf(
            self.store.raw_source_path(source_locator),
            source_locator,
            reextract,
        )
        manifest = result.manifest
        raw_source = self.store.raw_source(source_locator)
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
            schema=self._schema_object(),
            model_profile=self.model_profile,
        )
        self._write_page_plan(result.cache_dir, page_plan)
        self._write_observation(result.cache_dir, page_plan)
        chunks = tuple(
            ChunkText(unit.unit_id, unit.locator, unit.heading_path, unit.text)
            for unit in extracted_units
        )
        save_manifest(
            ExtractionResult(manifest=manifest.mark_integrated(), cache_dir=result.cache_dir)
        )
        return self._finish_ledger_ingest(
            source_locator=source_locator,
            page_plan=page_plan,
            chunks=chunks,
            document_model=read_document_model(result.cache_dir),
            source_text=source_text_from_text(
                source_locator, read_source_text(result.cache_dir), "pdf-cache"
            ),
            run=self._pdf_ingest_run(source_locator, page_plan),
        )

    def _finish_ledger_ingest(
        self,
        *,
        source_locator: str,
        page_plan: PagePlan,
        chunks: tuple[ChunkText, ...],
        document_model: DocumentModel | None,
        source_text: SourceText,
        run: IngestRun,
    ) -> OperationResult:
        confidence = record_post_ingest_confidence(
            store=self.store,
            today=self.today,
            run_id=self.run_id or self.today,
            source_locator=source_locator,
            page_plan=page_plan,
            source_text=source_text,
        )
        registry_hash = short_digest(registry_to_json(confidence.evidence_registry), 32)
        ledger = build_source_ledger(
            source_locator=source_locator,
            source_hash=source_text.source_hash,
            evidence_registry_hash=registry_hash,
            chunks=chunks,
            document_model=document_model,
            today=self.today,
            schema=self._schema_object(),
        )
        self.store.write_ledger_artifacts(source_locator, ledger.artifact_files)
        if ledger.wiki_page is not None:
            self.store.write_page(ledger.wiki_page)
            written = f"[[{ledger.page_id}]]"
        else:
            written = "none (authoritative write blocked — see blocked-write-diagnostic.json)"
        for topic_page in ledger.topic_pages:
            self.store.write_page(topic_page)
        if ledger.wiki_page is not None:
            keep_page_ids = {
                ledger.wiki_page.page_id,
                *(page.page_id for page in ledger.topic_pages),
            }
            self.store.delete_source_pages_not_in(source_locator, keep_page_ids)
        provenance_line = "Provenance audit: skipped because authoritative write was blocked."
        if ledger.wiki_page is not None:
            audit = build_provenance_audit(
                self.store.page_texts(),
                source_page_id=ledger.page_id,
                artifact_files=ledger.artifact_files,
            )
            self.store.write_ledger_artifacts(
                source_locator,
                {
                    "provenance-audit.json": report_to_json(audit),
                    "provenance-audit.md": render_markdown(audit),
                },
            )
            provenance_line = (
                f"Provenance audit: {audit.finding_count} finding(s), "
                f"{audit.non_manifest_finding_count} outside source manifests."
            )
        graph = self._write_graph_export()
        if self.on_chunk_note is not None:
            self.on_chunk_note(ledger.summary)
        report = (
            f"Claim-ledger ingest of raw/{source_locator} ({len(chunks)} chunk(s)).\n"
            f"{ledger.summary}\n"
            f"Source page: {written}; linked pages: {len(ledger.topic_pages)}. "
            f"Ledger artifacts: {self.store.page_plan_artifact_dir(source_locator)}/ledger.\n"
            f"{provenance_line}\n"
            f"{_graph_summary_line(graph)}\n"
            f"{_confidence_summary_line(confidence.report)}"
        )
        self.store.append_log(self.today, "ingest", source_locator, report)
        return OperationResult("ingest", source_locator, report, None, run)

    async def synthesize(self) -> OperationResult:
        """Build canonical concept pages from stored topic indexes.

        Deterministic and model-free: per-source topics (headings + key terms)
        that recur across sources become canonical concept pages with source
        evidence sections and typed cross-source relation sections.
        """
        topic_jsons = tuple(self.store.list_topic_index_artifacts())
        claim_ledger_jsons = tuple(self.store.list_claim_ledger_artifacts())
        if len(topic_jsons) < 2:
            report = (
                "Cross-source synthesis needs at least two ingested sources; "
                f"found {len(topic_jsons)}."
            )
            self.store.append_log(self.today, "synthesize", "cross-source", report)
            return OperationResult("synthesize", "cross-source", report, None)
        result = build_cross_source_pages(topic_jsons, claim_ledger_jsons, today=self.today)
        for page in result.pages:
            self.store.write_page(page)
        self.store.delete_cross_source_pages_not_in({page.page_id for page in result.pages})
        graph = self._write_graph_export()
        summary = f"{result.summary}\n{_graph_summary_line(graph)}"
        self.store.append_log(self.today, "synthesize", "cross-source", summary)
        return OperationResult("synthesize", "cross-source", summary, None)

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
        prepared = prepare_chat_turn(
            self.store,
            question=question,
            window=window,
            grounded=grounded,
            model_profile=self.model_profile,
        )
        return await self._run(
            prepared.workflow,
            prepared.message,
            "chat",
            tag=tag,
            initial_messages=list(prepared.initial_messages),
        )

    async def lint(self) -> OperationResult:
        findings = compute_findings(
            self.store.page_texts(),
            self.store.index_page_ids(),
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
        if findings.is_clean or len(findings.lint_findings) > _LINT_MODEL_MAX_FINDINGS:
            report = _deterministic_lint_report(findings)
            self._file_lint_report(report)
            self.store.append_log(self.today, "lint", "wiki health", report)
            return OperationResult("lint", "wiki health", report, None, findings)
        workflow = build_lint_workflow(self.store, self.today)
        salience_block = compute_salience(self.store.page_texts()).render()
        message = (
            "Run a lint pass. Deterministic findings from the harness:\n\n"
            f"{findings.render(max_items_per_section=_LINT_PROMPT_MAX_FINDINGS_PER_SECTION)}\n\n"
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
            self._lint_run(),
        )

    async def claim_support(
        self,
        selection: ClaimSupportSelection,
        *,
        subject: str = "selected claims",
        source_locator: str = "",
    ) -> OperationResult:
        verdicts: list[ClaimSupportVerdict] = []
        transcript: Path | None = None
        model_report = "No model candidates selected."
        if selection.candidates:
            message = (
                "Run a bounded claim-support audit for the selected generated "
                "wiki claims. For each candidate, compare the full generated "
                "claim to the supplied evidence excerpts and record exactly one "
                "structured verdict.\n\n"
                f"{selection.render_for_prompt()}"
            )
            model_report, transcript = await self._run(
                build_claim_support_workflow(
                    self.store,
                    verdicts,
                    selection.candidates,
                    selection.deterministic_findings,
                ),
                message,
                "claim-support",
            )
        audit = ClaimSupportAuditReport(
            run_id=self.run_id or self.today,
            selection=selection,
            verdicts=tuple(verdicts),
            model_report=model_report,
        )
        report = audit.render()
        self._file_claim_support_report(report, source_locator=source_locator)
        self.store.append_log(
            self.today,
            "claim-support",
            subject,
            _claim_support_summary_line(audit),
        )
        return OperationResult("claim-support", subject, report, transcript)

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
            max_tool_errors=_MAX_TOOL_ERRORS.get(op, 2),
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
            WikiPage.from_metadata(
                PageMetadata(
                    page_id=HEALTH_PAGE,
                    page_kind="synthesis",
                    summary=f"Wiki health report from the latest lint pass ({self.today}).",
                    updated=self.today,
                ),
                report,
            )
        )

    def _file_claim_support_report(self, report: str, *, source_locator: str = "") -> None:
        self.store.write_page(
            WikiPage.from_metadata(
                PageMetadata(
                    page_id="wiki-claim-support",
                    page_kind="synthesis",
                    summary=f"Latest bounded claim-support audit ({self.today}).",
                    updated=self.today,
                ),
                report,
            )
        )
        if source_locator:
            self.store.write_claim_support_report_artifact(source_locator, report)

    def _schema_object(self) -> Schema:
        return Schema(page_contracts=self.store.read_schema())

    def _extraction_prompt(self, subject: str) -> ExtractionPrompt:
        return ExtractionPrompt(
            instruction_text=(
                f"Use the local LLM-Wiki ingest workflow from Schema. Run subject: raw/{subject}."
            )
        )

    def _source_bundle(self, source_locator: str) -> SourceBundle:
        return SourceBundle.one(self.store.raw_source(source_locator))

    def _markdown_ingest_run(self, source_locator: str, page_plan: PagePlan) -> IngestRun:
        raw_source = self.store.raw_source(source_locator)
        plans = tuple(
            SourcePlan(
                raw_source=raw_source,
                source_classification="planned markdown write",
                ingest_disposition=write.action,
                planned_page_write_ids=(write.write_id,),
                page_body_contract_selections=(
                    SourcePlanContractSelection(
                        contract_id=write.resolved_page_body_contract.contract_id,
                        page_ids=(write.page_metadata.page_id,),
                    ),
                ),
                handling_notes="PagePlan write.",
            )
            for write in page_plan.planned_writes
        )
        return IngestRun(
            source_bundle=SourceBundle.one(raw_source),
            wiki_structure=self.store.structure,
            schema=self._schema_object(),
            extraction_prompt=self._extraction_prompt(source_locator),
            source_plans=plans,
            page_plan=page_plan,
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

    def _markdown_extracted_units(
        self,
        raw_source: RawSource,
        source_chunks: tuple[SourceTextChunk, ...],
        *,
        source_hash: str,
        fallback_title: str,
        fallback_text: str,
    ) -> tuple[ExtractedUnit, ...]:
        if not source_chunks:
            return (
                ExtractedUnit(
                    unit_id="unit-0001",
                    raw_source=raw_source,
                    locator="document",
                    heading_path=fallback_title,
                    text=fallback_text,
                    extraction_status="ok",
                    source_hash=source_hash,
                ),
            )
        return tuple(
            ExtractedUnit(
                unit_id=f"unit-{chunk.chunk_id:04d}",
                raw_source=raw_source,
                locator=chunk.locator,
                heading_path=chunk.heading_path,
                text=chunk.text,
                extraction_status="ok",
                source_hash=source_hash,
            )
            for chunk in source_chunks
        )

    def _write_page_plan(self, cache_dir: Path, page_plan: PagePlan) -> Path:
        path = cache_dir / "page_plan.json"
        path.write_text(page_plan_to_json(page_plan), encoding="utf-8")
        return path

    def _write_observation(self, cache_dir: Path, page_plan: PagePlan) -> str:
        path = cache_dir / "observation.md"
        path.write_text(observation_report(page_plan), encoding="utf-8")
        return str(path)

    def _pdf_ingest_run(self, source_locator: str, page_plan: PagePlan) -> IngestRun:
        raw_source = self.store.raw_source(source_locator)
        plans = tuple(
            SourcePlan(
                raw_source=raw_source,
                source_classification="planned pdf write",
                ingest_disposition=write.action,
                planned_page_write_ids=(write.write_id,),
                page_body_contract_selections=(
                    SourcePlanContractSelection(
                        contract_id=write.resolved_page_body_contract.contract_id,
                        page_ids=(write.page_metadata.page_id,),
                    ),
                ),
                handling_notes="Global PagePlan write.",
            )
            for write in page_plan.planned_writes
        )
        return IngestRun(
            source_bundle=SourceBundle.one(raw_source),
            wiki_structure=self.store.structure,
            schema=self._schema_object(),
            extraction_prompt=self._extraction_prompt(source_locator),
            source_plans=plans,
            page_plan=page_plan,
        )

    def _lint_run(self) -> LintRun:
        return compute_findings(
            self.store.page_texts(),
            self.store.index_page_ids(),
            exempt_from_orphans=frozenset({HEALTH_PAGE}),
        )

    def _write_graph_export(self) -> GraphStatus:
        graph = build_wiki_graph(self.store.page_texts(), generated_date=self.today)
        self.store.write_graph_json(graph.to_json_text())
        return graph_status(graph, self.store.read_graph_json())


def _markdown_title(source_locator: str) -> str:
    stem = Path(source_locator).stem.replace("_", " ").replace("-", " ")
    return " ".join(word if word.isupper() else word.capitalize() for word in stem.split())


def _confidence_summary_line(report: Any) -> str:
    status_line = next(
        (
            line
            for line in report.computed_summary.splitlines()
            if line.startswith("Confidence status:")
        ),
        "Confidence status: unknown",
    )
    artifact_dir_note = "Report filed as [[wiki-ingest-confidence]]."
    status = status_line.removeprefix("Confidence status: ")
    return f"Ingest confidence: {status}. {artifact_dir_note}"


def _graph_summary_line(status: GraphStatus) -> str:
    return (
        f"Graph export: {status.status}; nodes={status.node_count}; "
        f"edges={status.edge_count}; unresolved={status.unresolved_edge_count}."
    )


def _deterministic_lint_report(findings: LintRun) -> str:
    if findings.is_clean:
        return findings.render()
    return (
        "Deterministic lint report.\n\n"
        f"{findings.render(max_items_per_section=_LINT_PROMPT_MAX_FINDINGS_PER_SECTION)}\n\n"
        "Model repair loop skipped because the deterministic finding set "
        f"contains {len(findings.lint_findings)} issue(s), above the "
        f"{_LINT_MODEL_MAX_FINDINGS}-issue interactive repair budget."
    )


def _claim_support_summary_line(audit: ClaimSupportAuditReport) -> str:
    verdict_counts = {"too_broad": 0, "not_supported": 0, "unclear": 0}
    for verdict in audit.verdicts:
        if verdict.verdict in verdict_counts:
            verdict_counts[verdict.verdict] += 1
    issue_count = sum(verdict_counts.values())
    return (
        "Claim-support audit filed as [[wiki-claim-support]]. "
        f"Selected for model judgment: {audit.selection.selected_count}. "
        f"Structured verdicts: {len(audit.verdicts)}. "
        f"Model-raised issues: {issue_count}. "
        f"Deterministic blockers: {audit.selection.deterministic_skipped_count}. "
        f"Missing verdicts: {len(audit.missing_verdict_candidate_ids)}."
    )
