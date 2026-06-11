"""Operation orchestrator: arranges workflow, runner, transcript, and log.

Side effects are coordinated here; content decisions belong to the model
and bookkeeping formats to the domain layer. The LLM client and context
manager are injected, so tests drive the real WorkflowRunner with a fake
client and no network.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from forge.context import ContextManager
from forge.core.runner import WorkflowRunner

from llmwiki.domain.links import compute_findings
from llmwiki.domain.pages import WikiPage
from llmwiki.runtime.transcript import TranscriptWriter
from llmwiki.store import WikiStore
from llmwiki.workflows import (
    build_ingest_workflow,
    build_lint_workflow,
    build_query_workflow,
)

_MAX_ITERATIONS = {"ingest": 24, "query": 12, "lint": 16}

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
}


@dataclass(frozen=True)
class OperationResult:
    op: str
    subject: str
    output: str
    transcript_path: Path | None


@dataclass(frozen=True)
class Session:
    """One operation run: explicit dependencies, one public method per op."""

    store: WikiStore
    client: Any  # forge LLMClient protocol
    context_manager: ContextManager
    today: str
    runs_dir: Path | None = None
    run_id: str = ""  # unique per run (e.g. timestamp); falls back to date

    async def ingest(self, source_path: str) -> OperationResult:
        workflow = build_ingest_workflow(self.store, self.today)
        message = (
            f"Ingest the source 'raw/{source_path}' into the wiki. "
            f"Pass path='{source_path}' to read_source."
        )
        report, transcript = await self._run(workflow, message, "ingest")
        self.store.append_log(self.today, "ingest", source_path, report)
        return OperationResult("ingest", source_path, report, transcript)

    async def query(self, question: str) -> OperationResult:
        workflow = build_query_workflow(self.store, self.today)
        # Factual lookups don't benefit from Qwen3's thinking preamble.
        answer, transcript = await self._run(workflow, question + " /no_think", "query")
        self.store.append_log(self.today, "query", question, answer)
        return OperationResult("query", question, answer, transcript)

    async def lint(self) -> OperationResult:
        findings = compute_findings(
            self.store.page_texts(),
            self.store.index_names(),
            exempt_from_orphans=frozenset({HEALTH_PAGE}),
        )
        if not self.store.list_pages():
            report = "Wiki is empty — nothing to lint."
            self.store.append_log(self.today, "lint", "empty wiki", report)
            return OperationResult("lint", "wiki health", report, None)
        workflow = build_lint_workflow(self.store, self.today)
        message = (
            "Run a lint pass. Deterministic findings from the harness:\n\n"
            f"{findings.render()}\n\n"
            "Review the affected pages (and spot-check others), then call "
            "finish_lint with the health report."
        )
        report, transcript = await self._run(workflow, message, "lint")
        self._file_lint_report(report)
        self.store.append_log(self.today, "lint", "wiki health", report)
        return OperationResult("lint", "wiki health", report, transcript)

    async def _run(self, workflow: Any, message: str, op: str) -> tuple[str, Path | None]:
        writer = (
            TranscriptWriter(self.runs_dir / f"{self.run_id or self.today}-{op}.jsonl")
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
                workflow, message, prompt_vars={"schema": self.store.read_schema()}
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
