"""CLI argument contract and explicit config resolution."""

import asyncio
import json
import signal
from pathlib import Path

import pytest
from fakes import FakeClient
from forge.context import ContextManager, NoCompact

from llmwiki.application.ingestion_trace_builder import build_ingestion_trace
from llmwiki.application.ingestion_trace_records import ingestion_trace_artifact_to_json
from llmwiki.cli import _build_parser, _read_chat_line, _run, _run_chat
from llmwiki.config import ConfigError, WikiPaths, load_backend_config
from llmwiki.domain.graph import GraphStatus
from llmwiki.domain.ledger.artifacts import PortableArtifactMember
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore


class TestParser:
    def test_ingest_args(self) -> None:
        args = _build_parser().parse_args(["ingest", "article.md"])
        assert (args.op, args.source) == ("ingest", "article.md")

    def test_query_args(self) -> None:
        args = _build_parser().parse_args(["query", "what happened?"])
        assert (args.op, args.question) == ("query", "what happened?")

    def test_lint_args_and_root_override(self, tmp_path: Path) -> None:
        args = _build_parser().parse_args(["--root", str(tmp_path), "lint"])
        assert args.op == "lint"
        assert args.root == tmp_path

    def test_graph_check_args(self) -> None:
        args = _build_parser().parse_args(["graph", "--check"])
        assert args.op == "graph"
        assert args.check

    def test_inspect_ingest_args(self) -> None:
        args = _build_parser().parse_args(
            ["inspect-ingest", "article.pdf", "--stage", "topic-state"]
        )
        assert args.op == "inspect-ingest"
        assert args.source == "article.pdf"
        assert args.stage == "topic-state"

    def test_op_is_required(self) -> None:
        with pytest.raises(SystemExit):
            _build_parser().parse_args([])


class TestBackendConfig:
    def test_env_override_wins(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        gguf = tmp_path / "model.gguf"
        gguf.write_bytes(b"GGUF")
        monkeypatch.setenv("LLMWIKI_GGUF", str(gguf))
        monkeypatch.setenv("LLMWIKI_PORT", "9001")
        monkeypatch.setenv("LLMWIKI_CTX", "8192")
        config = load_backend_config()
        assert config.gguf_path == gguf
        assert config.port == 9001
        assert config.model_profile.context_window_tokens == 8192

    def test_missing_model_fails_loudly(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("LLMWIKI_GGUF", str(tmp_path / "absent.gguf"))
        with pytest.raises(ConfigError, match="GGUF not found"):
            load_backend_config()


class TestWikiPathsValidation:
    def test_complete_tree_validates(self, paths: WikiPaths) -> None:
        paths.validate()

    def test_missing_layer_raises(self, tmp_path: Path) -> None:
        with pytest.raises(ConfigError, match="Wiki layer missing"):
            WikiPaths(root=tmp_path).validate()


class TestGraphCommand:
    async def test_graph_write_then_check_current(self, paths: WikiPaths) -> None:
        store = WikiStore(paths)
        store.write_page(
            WikiPage.from_metadata(
                PageMetadata("alpha", "concept", "Alpha summary."),
                "See [[alpha]].",
            )
        )

        write_args = _build_parser().parse_args(["--root", str(paths.root), "graph"])
        check_args = _build_parser().parse_args(["--root", str(paths.root), "graph", "--check"])

        written = await _run(write_args)
        checked = await _run(check_args)

        assert "Graph export: current" in written.output
        assert "Graph export: current" in checked.output


class TestInspectIngestCommand:
    async def test_inspect_ingest_reads_trace_without_backend(
        self, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        store = WikiStore(paths)
        store.write_ledger_artifacts("article.pdf", {"ingestion-trace.json": _trace_json()})

        async def fail_start_backend(_config: object) -> None:
            raise AssertionError("inspect-ingest must not start the backend")

        monkeypatch.setattr("llmwiki.cli.start_backend", fail_start_backend)
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "inspect-ingest", "article.pdf"]
        )

        result = await _run(args)

        assert "Ingestion trace for raw/article.pdf" in result.output
        assert "topic-state" in result.output

    async def test_inspect_ingest_stage_and_json_modes(self, paths: WikiPaths) -> None:
        store = WikiStore(paths)
        store.write_ledger_artifacts("article.pdf", {"ingestion-trace.json": _trace_json()})
        stage_args = _build_parser().parse_args(
            [
                "--root",
                str(paths.root),
                "inspect-ingest",
                "article.pdf",
                "--stage",
                "topic-state",
            ]
        )
        json_args = _build_parser().parse_args(
            ["--root", str(paths.root), "inspect-ingest", "article.pdf", "--json"]
        )

        stage = await _run(stage_args)
        rendered_json = await _run(json_args)

        assert "Ingestion trace stage: topic-state" in stage.output
        assert json.loads(rendered_json.output)["source_locator"] == "article.pdf"

    async def test_inspect_ingest_missing_trace_fails(self, paths: WikiPaths) -> None:
        args = _build_parser().parse_args(
            ["--root", str(paths.root), "inspect-ingest", "missing.pdf"]
        )

        with pytest.raises(ConfigError, match="No ingestion-trace artifact"):
            await _run(args)


class TestLintCommand:
    async def test_large_lint_set_does_not_start_backend(
        self, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        store = WikiStore(paths)
        for index in range(55):
            store.write_page(
                WikiPage.from_metadata(
                    PageMetadata(
                        f"orphan-{index:02d}",
                        "concept",
                        f"Orphan {index}.",
                    ),
                    "No inbound links.",
                )
            )

        async def fail_start_backend(_config: object) -> None:
            raise AssertionError("large deterministic lint pass must not start the backend")

        monkeypatch.setattr("llmwiki.cli.start_backend", fail_start_backend)
        args = _build_parser().parse_args(["--root", str(paths.root), "lint"])

        result = await _run(args)

        assert "Model repair loop skipped" in result.output
        assert "55 issue(s)" in result.output
        assert "wiki-health" in store.list_pages()


class TestChatInputLoop:
    def test_prompt_restores_default_sigint_handler(self, monkeypatch: pytest.MonkeyPatch) -> None:
        asyncio_handler = object()
        calls: list[tuple[int, object]] = []

        def fake_signal(signum: int, handler: object) -> None:
            calls.append((signum, handler))

        def fake_input(_prompt: str) -> str:
            assert calls[-1] == (signal.SIGINT, signal.default_int_handler)
            raise KeyboardInterrupt

        monkeypatch.setattr(signal, "getsignal", lambda _signum: asyncio_handler)
        monkeypatch.setattr(signal, "signal", fake_signal)
        monkeypatch.setattr("builtins.input", fake_input)

        with pytest.raises(KeyboardInterrupt):
            _read_chat_line()

        assert calls == [
            (signal.SIGINT, signal.default_int_handler),
            (signal.SIGINT, asyncio_handler),
        ]

    async def test_ctrl_c_at_prompt_exits_without_to_thread(
        self, paths: WikiPaths, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        session = Session(
            store=WikiStore(paths),
            client=FakeClient([]),
            context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
            today="2026-06-18",
        )

        def fail_to_thread(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("chat prompt must not use asyncio.to_thread")

        def interrupt_input(_prompt: str) -> str:
            raise KeyboardInterrupt

        monkeypatch.setattr(asyncio, "to_thread", fail_to_thread)
        monkeypatch.setattr("builtins.input", interrupt_input)

        result = await _run_chat(session, paths, resume=None)

        assert result.output == "chat ended: 0 turns across 0 conversation(s)"
        assert "chat |" not in paths.log_path.read_text(encoding="utf-8")


def _trace_json() -> str:
    trace = build_ingestion_trace(
        source_locator="article.pdf",
        source_hash="a" * 64,
        run_id="cli-test",
        artifact_files={
            "source-plan.json": "{}",
            "extraction-result.json": "{}",
            "assertion-graph-source-artifact.json": "{}",
            "document-structure.json": "{}",
            "claim-ledger.json": '{"ledger": {}}',
            "proposed-change-review.json": "{}",
            "assertion-graph.json": "{}",
            "topic-states.json": '{"topic_states": [], "topic_dependencies": [], "topic_gaps": []}',
            "page-projections.json": '{"page_projections": []}',
            "staged-pages.json": '{"pages": []}',
            "lint-run.json": json.dumps(
                {"status": "accepted", "accepted_page_ids": [], "rejected_page_ids": []}
            ),
            "publish-run.json": json.dumps(
                {"status": "published", "accepted_page_ids": [], "rejected_page_ids": []}
            ),
            "projection-coverage.json": "{}",
            "provenance-audit.json": "{}",
        },
        artifact_members=(PortableArtifactMember("source-plan-artifact", "source-plan", "fp"),),
        graph_status=GraphStatus("current", 0, 0, 0, "current"),
        metric_providers=(),
    )
    return ingestion_trace_artifact_to_json(trace)
