"""End-to-end planned PDF ingest: real WorkflowRunner + store, fake LLM,
fake extractor. Covers global PagePlan creation before writes, serial
PlannedPageWrite execution, manifest recording, and observation output.
"""

from pathlib import Path

from fakes import FakeClient
from forge.context import ContextManager, NoCompact
from forge.core.workflow import LLMResponse, ToolCall

from llmwiki.config import WikiPaths
from llmwiki.domain.objects import IngestRun
from llmwiki.domain.pages import WikiPage
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json
from llmwiki.pdf.pipeline import ExtractionResult
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-06-11"


def _fake_extraction(
    paths: WikiPaths, statuses: tuple[str, str] = ("pending", "pending")
) -> ExtractionResult:
    cache_dir = paths.cache_dir / "deadbeef"
    chunks_dir = cache_dir / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    (chunks_dir / "0001.md").write_text("Chunk one: functions are values.", encoding="utf-8")
    (chunks_dir / "0002.md").write_text("Chunk two: closures capture scope.", encoding="utf-8")
    manifest = Manifest(
        source="book.pdf",
        sha256="deadbeef" * 8,
        chunks=(
            ChunkRecord(1, "Functions", 1, 10, 4000, status=statuses[0]),
            ChunkRecord(2, "Closures", 11, 20, 3800, status=statuses[1]),
        ),
    )
    return ExtractionResult(manifest=manifest, cache_dir=cache_dir)


def _write_page_call(name: str, content: str = "Body.") -> ToolCall:
    return ToolCall(
        tool="write_page",
        args={"name": name, "category": "source", "summary": f"About {name}.", "content": content},
    )


def _planned_turns(
    page: str,
    report: str,
    *,
    read_first: bool = False,
    content: str = "Body.",
) -> list[LLMResponse]:
    turns: list[LLMResponse] = []
    if read_first:
        turns.append([ToolCall(tool="read_page", args={"name": page})])
    turns.extend(
        [
            [_write_page_call(page, content)],
            [ToolCall(tool="finish_planned_write", args={"report": report})],
        ]
    )
    return turns


def _session(
    store: WikiStore,
    script: list[LLMResponse],
    paths: WikiPaths,
    extraction: ExtractionResult,
) -> Session:
    notes_seen: list[str] = []
    session = Session(
        store=store,
        client=FakeClient(script),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-test",
        extract_pdf=lambda pdf, rel, reextract: extraction,
        on_chunk_note=notes_seen.append,
    )
    object.__setattr__(session, "_notes_seen", notes_seen)  # test-side capture
    return session


class PlanAwareStore(WikiStore):
    def __init__(self, paths: WikiPaths, plan_path: Path) -> None:
        super().__init__(paths)
        self._plan_path = plan_path

    def write_page(self, page: WikiPage) -> None:
        assert self._plan_path.exists()
        super().write_page(page)


class TestPlannedPdfIngest:
    async def test_plan_exists_before_any_wiki_write(self, paths: WikiPaths) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        plan_path = extraction.cache_dir / "page_plan.json"
        store = PlanAwareStore(paths, plan_path)
        script = (
            _planned_turns("book-functions", "functions written")
            + _planned_turns("book-closures", "closures written")
            + _planned_turns("book", "hub written")
        )
        result = await _session(store, script, paths, extraction).ingest("book.pdf")

        assert "Planned ingest completed" in result.output
        assert plan_path.exists()
        assert {"book-functions", "book-closures", "book"} <= set(store.list_pages())

    async def test_page_plan_and_manifest_record_planned_writes(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        script = (
            _planned_turns("book-functions", "functions written")
            + _planned_turns("book-closures", "closures written")
            + _planned_turns("book", "hub written")
        )
        session = _session(store, script, paths, extraction)
        result = await session.ingest("book.pdf")

        assert isinstance(result.run, IngestRun)
        assert result.run.page_plan is not None
        assert len(result.run.page_plan.extracted_units) == 2
        assert [p.source_classification for p in result.run.source_plans] == [
            "planned pdf write",
            "planned pdf write",
            "planned pdf write",
        ]
        saved = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert saved.all_done and saved.integrated
        assert saved.chunks[0].pages_written == ("book-functions",)
        assert saved.chunks[1].pages_written == ("book-closures",)

    async def test_existing_source_page_is_enriched_instead_of_duplicated(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            WikiPage(
                name="functions",
                category="source",
                summary="Existing function source page.",
                body="functions are values from raw/book.pdf p.1-10",
                sources=("raw/book.pdf p.1-10",),
                updated=TODAY,
            )
        )
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        script = (
            _planned_turns("functions", "functions enriched")
            + _planned_turns("book-closures", "closures written")
            + _planned_turns("book", "hub written")
        )
        result = await _session(store, script, paths, extraction).ingest("book.pdf")

        assert isinstance(result.run, IngestRun)
        assert result.run.page_plan is not None
        first_write = result.run.page_plan.planned_writes[0]
        assert first_write.action == "enrich-existing"
        assert first_write.page_metadata.page_id == "functions"
        assert "book-functions" not in store.list_pages()

    async def test_observation_report_lists_counts_and_paths(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        script = (
            _planned_turns("book-functions", "functions written")
            + _planned_turns("book-closures", "closures written")
            + _planned_turns("book", "hub written")
        )
        await _session(store, script, paths, extraction).ingest("book.pdf")

        report = (extraction.cache_dir / "observation.md").read_text(encoding="utf-8")
        assert "ExtractedUnits: 2" in report
        assert "TopicClusters:" in report
        assert "`book-functions` -> `book-functions.md`" in report
        assert "Observation:" in paths.log_path.read_text(encoding="utf-8")

    async def test_hub_key_lists_reconciled_after_planned_writes(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        store.write_page(
            WikiPage(
                name="iterable",
                category="concept",
                summary="Core protocol.",
                body="Central.",
                sources=("raw/book.pdf",),
                updated=TODAY,
            )
        )
        (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.5 fake")
        extraction = _fake_extraction(paths)
        (extraction.cache_dir / "chunks" / "0001.md").write_text(
            "iterable " * 12,
            encoding="utf-8",
        )
        script = (
            _planned_turns(
                "book-functions",
                "functions written",
                content="Functions build on [[iterable]].",
            )
            + _planned_turns(
                "book-closures",
                "closures written",
                content="Closures build on [[iterable]].",
            )
            + [
                [
                    _write_page_call(
                        "book",
                        "Hub prose with [[iterable]].\n\n**Key entities**: [[stale-person]].",
                    )
                ],
                [ToolCall(tool="finish_planned_write", args={"report": "hub written"})],
            ]
        )
        await _session(store, script, paths, extraction).ingest("book.pdf")

        hub_text = store.read_page("book")
        assert "stale-person" not in hub_text
        assert "**Key concepts:** [[iterable]]" in hub_text
