"""llmwiki CLI: ingest, query, lint.

Thin entry point — parses arguments, boots the backend, delegates to a
Session, prints the result. All wiki logic lives in domain/store/workflows.
"""

from __future__ import annotations

import argparse
import asyncio
import signal
import sys
from datetime import datetime
from pathlib import Path

from forge.context import ContextManager, NoCompact

from llmwiki.application.ingestion_trace_records import (
    ingestion_trace_artifact_from_json,
    ingestion_trace_artifact_to_json,
)
from llmwiki.config import ConfigError, WikiPaths, load_backend_config, load_model_profile
from llmwiki.domain.citations import SourceInventory
from llmwiki.domain.claim_support import (
    DEFAULT_CLAIM_SUPPORT_SAMPLE_STRATEGY,
    DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS,
)
from llmwiki.domain.claim_support_selection import select_claim_support_candidates
from llmwiki.domain.evidence_registry_io import registry_from_json
from llmwiki.domain.graph import build_wiki_graph, graph_status
from llmwiki.domain.model_profile import ModelProfile
from llmwiki.pdf import PdfError
from llmwiki.pdf.pipeline import ExtractionResult, ensure_extracted
from llmwiki.pdf.vision import AppleVisionRecognizer
from llmwiki.runtime.backend import start_backend
from llmwiki.runtime.chat_repl import ChatRepl
from llmwiki.runtime.ingestion_trace_inspect import render_trace_stage, render_trace_summary
from llmwiki.runtime.session import ExtractFn, OperationResult, Session
from llmwiki.store import WikiStore
from llmwiki.store.chat_store import ChatStore


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="llmwiki",
        description="LLM-maintained local wiki (Qwen3-14B via forge + llama-server).",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Project root containing raw/, wiki/, SCHEMA.md (default: cwd).",
    )
    sub = parser.add_subparsers(dest="op", required=True)

    ingest = sub.add_parser("ingest", help="Integrate one raw source into the wiki.")
    ingest.add_argument("source", help="Source path relative to raw/, e.g. article.md")
    ingest.add_argument(
        "--reextract",
        action="store_true",
        help="PDF only: discard the cached extraction/manifest and start over "
        "(default resumes a partial ingest).",
    )
    ingest.add_argument(
        "--reintegrate",
        action="store_true",
        help="PDF only: rerun just the integrate pass of a completed ingest "
        "(rebuilds the hub with current salience).",
    )

    query = sub.add_parser("query", help="Answer a question from the wiki.")
    query.add_argument("question", help="The question to answer.")

    sub.add_parser("lint", help="Health-check the wiki.")

    inspect_ingest = sub.add_parser(
        "inspect-ingest",
        help="Inspect one source ingest trace without starting the model backend.",
    )
    inspect_ingest.add_argument("source", help="Source path relative to raw/.")
    inspect_ingest.add_argument("--stage", default="", help="Restrict output to one trace stage.")
    inspect_ingest.add_argument("--json", action="store_true", help="Print canonical trace JSON.")

    graph = sub.add_parser("graph", help="Write or check the deterministic wiki graph export.")
    graph.add_argument(
        "--check",
        action="store_true",
        help="Fail if wiki/wiki-graph.json is missing, invalid, or stale.",
    )

    chat = sub.add_parser("chat", help="Converse with the wiki (model stays loaded).")
    chat.add_argument(
        "--resume",
        nargs="?",
        const="latest",
        default=None,
        metavar="SESSION_ID",
        help="Continue a conversation (default: the most recent one).",
    )
    claim_support = sub.add_parser(
        "claim-support",
        help="Audit selected generated claims against ingest EvidenceRecords.",
    )
    claim_support.add_argument(
        "--source",
        required=True,
        help="Source path relative to raw/ whose evidence registry should be used.",
    )
    claim_support.add_argument(
        "--max-claims",
        type=int,
        default=DEFAULT_MAX_CLAIM_SUPPORT_CLAIMS,
        help="Maximum selected claims to send for model judgment.",
    )
    claim_support.add_argument(
        "--sample-strategy",
        choices=("ordered", "stratified"),
        default=DEFAULT_CLAIM_SUPPORT_SAMPLE_STRATEGY,
        help="Candidate sampling strategy.",
    )
    claim_support.add_argument(
        "--page",
        action="append",
        default=[],
        help="Restrict the audit to a page_id; repeat to include multiple pages.",
    )
    claim_support.add_argument(
        "--claim-contains",
        default="",
        help="Restrict the audit to candidate claims containing this text.",
    )
    return parser


def _pdf_extractor(paths: WikiPaths, model_profile: ModelProfile) -> ExtractFn:
    def extract(pdf_path: Path, source_rel: str, reextract: bool) -> ExtractionResult:
        return ensure_extracted(
            pdf_path,
            source_rel,
            cache_root=paths.cache_dir,
            recognizer=AppleVisionRecognizer(),
            reextract=reextract,
            model_profile=model_profile,
        )

    return extract


async def _run(args: argparse.Namespace) -> OperationResult:
    paths = WikiPaths(root=args.root.resolve())
    paths.validate()
    now = datetime.now()
    if args.op == "claim-support":
        return await _run_claim_support(paths, args, now)

    if args.op == "inspect-ingest":
        return _run_inspect_ingest(args, paths)

    if args.op == "graph":
        return _run_graph(args, paths, now.date().isoformat())

    model_profile = load_model_profile()
    if args.op == "ingest":
        # Claim-ledger ingest is a deterministic projection, so no backend starts.
        session = Session(
            store=WikiStore(paths, model_profile=model_profile),
            client=None,
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
            model_profile=model_profile,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
            extract_pdf=_pdf_extractor(paths, model_profile),
            on_chunk_note=lambda note: print(note, flush=True),
        )
        return await session.ingest(
            args.source, reextract=args.reextract, reintegrate=args.reintegrate
        )
    if args.op == "lint":
        session = Session(
            store=WikiStore(paths, model_profile=model_profile),
            client=None,
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
            model_profile=model_profile,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
            extract_pdf=_pdf_extractor(paths, model_profile),
            on_chunk_note=lambda note: print(note, flush=True),
        )
        if not session.lint_needs_model_review():
            return await session.lint()

    backend_config = load_backend_config()
    backend = await start_backend(backend_config)
    try:
        session = Session(
            store=WikiStore(paths, model_profile=backend_config.model_profile),
            client=backend.client,
            context_manager=backend.context_manager,
            model_profile=backend_config.model_profile,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
            extract_pdf=_pdf_extractor(paths, backend_config.model_profile),
            on_chunk_note=lambda note: print(note, flush=True),
        )
        if args.op == "query":
            return await session.query(args.question)
        if args.op == "chat":
            return await _run_chat(session, paths, args.resume)
        return await session.lint()
    finally:
        await backend.aclose()


def _run_graph(args: argparse.Namespace, paths: WikiPaths, today: str) -> OperationResult:
    store = WikiStore(paths)
    graph = build_wiki_graph(store.page_texts(), generated_date=today)
    status = graph_status(graph, store.read_graph_json())
    if args.check:
        if not status.is_current:
            raise ConfigError(status.render())
        return OperationResult("graph", "wiki graph", status.render(), None)
    store.write_graph_json(graph.to_json_text())
    status = graph_status(graph, store.read_graph_json())
    report = status.render()
    store.append_log(today, "graph", "wiki graph", report)
    return OperationResult("graph", "wiki graph", report, None)


def _run_inspect_ingest(args: argparse.Namespace, paths: WikiPaths) -> OperationResult:
    store = WikiStore(paths)
    source = args.source.removeprefix("raw/")
    text = store.read_ingestion_trace_artifact(source)
    if text is None:
        raise ConfigError(
            "No ingestion-trace artifact found for "
            f"raw/{source}. Run `uv run llmwiki ingest {source}` first."
        )
    trace = ingestion_trace_artifact_from_json(text)
    if args.json:
        output = ingestion_trace_artifact_to_json(trace)
    elif args.stage:
        try:
            output = render_trace_stage(trace, args.stage)
        except ValueError as exc:
            raise ConfigError(str(exc)) from exc
    else:
        output = render_trace_summary(trace)
    return OperationResult("inspect-ingest", source, output, None)


async def _run_claim_support(
    paths: WikiPaths, args: argparse.Namespace, now: datetime
) -> OperationResult:
    model_profile = load_model_profile()
    store = WikiStore(paths, model_profile=model_profile)
    source = args.source.removeprefix("raw/")
    registry_json = store.read_evidence_registry_artifact(source)
    if registry_json is None:
        raise ConfigError(
            "No evidence-registry artifact found for "
            f"raw/{source}. Run `uv run llmwiki ingest {source}` first."
        )
    selection = select_claim_support_candidates(
        store.page_texts(),
        SourceInventory.from_raw_relative_paths(store.list_sources()),
        (registry_from_json(registry_json),),
        max_claims=args.max_claims,
        source=source,
        sample_strategy=args.sample_strategy,
        page_ids=tuple(args.page),
        claim_contains=args.claim_contains,
    )
    subject = _claim_support_subject(source, tuple(args.page), args.claim_contains)
    if not selection.candidates:
        session = Session(
            store=store,
            client=None,
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=1),
            model_profile=model_profile,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
            extract_pdf=_pdf_extractor(paths, model_profile),
            on_chunk_note=lambda note: print(note, flush=True),
        )
        return await session.claim_support(
            selection,
            subject=subject,
            source_locator=source,
        )
    backend_config = load_backend_config()
    backend = await start_backend(backend_config)
    try:
        session = Session(
            store=store,
            client=backend.client,
            context_manager=backend.context_manager,
            model_profile=backend_config.model_profile,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
            extract_pdf=_pdf_extractor(paths, backend_config.model_profile),
            on_chunk_note=lambda note: print(note, flush=True),
        )
        return await session.claim_support(
            selection,
            subject=subject,
            source_locator=source,
        )
    finally:
        await backend.aclose()


def _claim_support_subject(source: str, page_ids: tuple[str, ...], claim_contains: str) -> str:
    detail = [f"raw/{source}"]
    if page_ids:
        detail.append("pages=" + ",".join(page_ids))
    if claim_contains:
        detail.append(f"claim_contains={claim_contains}")
    return " ".join(detail)


async def _run_chat(session: Session, paths: WikiPaths, resume: str | None) -> OperationResult:
    """The thin input loop; all REPL logic lives in ChatRepl (testable)."""
    chat_store = ChatStore(paths.root / "harness" / "chat.db")
    repl = ChatRepl(session=session, chat_store=chat_store)
    try:
        repl.start(resume)
        while True:
            try:
                line = _read_chat_line()
            except (EOFError, KeyboardInterrupt):  # Ctrl-D / Ctrl-C at the prompt
                break
            if not await repl.handle(line):
                break
    except KeyboardInterrupt:  # Ctrl-C: same graceful path as /exit
        pass
    finally:
        repl.finish()
        chat_store.close()
    summary = (
        f"chat ended: {repl.turns} turns across {len(repl.conversations_touched)} conversation(s)"
    )
    return OperationResult("chat", "conversation", summary, None)


def _read_chat_line() -> str:
    """Read a REPL line with normal Ctrl-C behavior under asyncio.run().

    asyncio.run installs a SIGINT handler that cancels the main task. That
    handler does not raise from blocking input(), so Ctrl-C can appear to do
    nothing at the chat prompt. Restore the default handler only while the
    terminal is waiting for input, then put asyncio's handler back.
    """
    previous = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal.default_int_handler)
    try:
        return input("llmwiki> ")
    finally:
        signal.signal(signal.SIGINT, previous)


def main() -> None:
    args = _build_parser().parse_args()
    try:
        result = asyncio.run(_run(args))
    except (ConfigError, PdfError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    print(result.output)
    if result.transcript_path is not None:
        print(f"\n[transcript: {result.transcript_path}]", file=sys.stderr)


if __name__ == "__main__":
    main()
