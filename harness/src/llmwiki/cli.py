"""llmwiki CLI: ingest, query, lint.

Thin entry point — parses arguments, boots the backend, delegates to a
Session, prints the result. All wiki logic lives in domain/store/workflows.
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from datetime import datetime
from pathlib import Path

from llmwiki.config import ConfigError, WikiPaths, load_backend_config
from llmwiki.runtime.backend import start_backend
from llmwiki.runtime.session import OperationResult, Session
from llmwiki.store import WikiStore


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

    query = sub.add_parser("query", help="Answer a question from the wiki.")
    query.add_argument("question", help="The question to answer.")

    sub.add_parser("lint", help="Health-check the wiki.")
    return parser


async def _run(args: argparse.Namespace) -> OperationResult:
    paths = WikiPaths(root=args.root.resolve())
    paths.validate()
    backend_config = load_backend_config()

    now = datetime.now()
    backend = await start_backend(backend_config)
    try:
        session = Session(
            store=WikiStore(paths),
            client=backend.client,
            context_manager=backend.context_manager,
            today=now.date().isoformat(),
            runs_dir=paths.runs_dir,
            run_id=now.strftime("%Y-%m-%d-%H%M%S"),
        )
        if args.op == "ingest":
            return await session.ingest(args.source)
        if args.op == "query":
            return await session.query(args.question)
        return await session.lint()
    finally:
        await backend.aclose()


def main() -> None:
    args = _build_parser().parse_args()
    try:
        result = asyncio.run(_run(args))
    except ConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
    print(result.output)
    if result.transcript_path is not None:
        print(f"\n[transcript: {result.transcript_path}]", file=sys.stderr)


if __name__ == "__main__":
    main()
