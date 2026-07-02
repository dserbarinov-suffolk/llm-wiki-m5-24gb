"""End-to-end PDF ingest: real store + claim-ledger domain, fake extractor.

PDF ingest is deterministic — the source page is a projection of the ledger
built from the extracted chunks, with no model call. These tests use a fake
extractor (synthetic manifest + chunks) and assert the projected page, the
ledger artifacts, and atom preservation.
"""

import json

from fakes import FakeClient
from forge.context import ContextManager, NoCompact

from llmwiki.config import WikiPaths
from llmwiki.domain.objects import IngestRun
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json
from llmwiki.pdf.pipeline import ExtractionResult
from llmwiki.runtime.session import Session
from llmwiki.store import WikiStore

TODAY = "2026-06-11"

_CHUNK_ONE = (
    "# Functions\n\nFunctions are ordinary first-class values.\n\n"
    "A function must return a result.\n\n"
    "```js\nconst f = () => 1;\n```\n"
)
_CHUNK_TWO = (
    "# Closures\n\nClosures contain their captured scope.\n\nValue cups are undistinguishable.\n"
)


def _fake_extraction(paths: WikiPaths) -> ExtractionResult:
    cache_dir = paths.cache_dir / "deadbeef"
    chunks_dir = cache_dir / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    (chunks_dir / "0001.md").write_text(_CHUNK_ONE, encoding="utf-8")
    (chunks_dir / "0002.md").write_text(_CHUNK_TWO, encoding="utf-8")
    manifest = Manifest(
        source="book.pdf",
        sha256="deadbeef" * 8,
        chunks=(
            ChunkRecord(1, "Functions", 1, 10, 4000),
            ChunkRecord(2, "Closures", 11, 20, 3800),
        ),
    )
    return ExtractionResult(manifest=manifest, cache_dir=cache_dir)


def _session(store: WikiStore, paths: WikiPaths, extraction: ExtractionResult) -> Session:
    return Session(
        store=store,
        client=FakeClient([]),
        context_manager=ContextManager(strategy=NoCompact(), budget_tokens=32768),
        today=TODAY,
        runs_dir=paths.root / "runs",
        run_id="pdf-test",
        extract_pdf=lambda pdf, rel, reextract: extraction,
    )


def _raw_pdf(paths: WikiPaths) -> str:
    (paths.raw_dir / "book.pdf").write_bytes(b"%PDF-1.4 fake source bytes")
    return "book.pdf"


def _page_containing(store: WikiStore, text: str) -> str:
    for page_id in store.list_pages():
        body = store.read_page(page_id)
        if text in body:
            return body
    raise AssertionError(f"No page contains {text!r}.")


class TestLedgerPdfIngest:
    async def test_pdf_ingest_projects_single_source_page_from_ledger(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        source = _raw_pdf(paths)
        result = await _session(store, paths, _fake_extraction(paths)).ingest(source)

        assert "Claim-ledger ingest" in result.output
        assert "[[book]]" in result.output
        body = store.read_page("book")
        assert "## Page Families" in body
        assert "## Source Section Index" in body
        assert "Functions are ordinary first-class values." not in body
        assert "Functions are ordinary first-class values." in _page_containing(
            store, "Functions are ordinary first-class values."
        )
        assert "Closures contain their captured scope." in _page_containing(
            store, "Closures contain their captured scope."
        )
        assert isinstance(result.run, IngestRun)
        assert f"## [{TODAY}] ingest | book.pdf" in paths.log_path.read_text(encoding="utf-8")

    async def test_code_block_and_rule_become_atoms(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        source = _raw_pdf(paths)
        await _session(store, paths, _fake_extraction(paths)).ingest(source)
        body = _page_containing(store, "const f = () => 1;")
        assert "const f = () => 1;" in body  # code atom rendered verbatim
        ledger = json.loads(store.read_claim_ledger_artifact(source))["ledger"]
        atom_kinds = {atom["technical_atom_kind"] for atom in ledger["technical_atoms"]}
        assert {"code-block", "rule"} <= atom_kinds

    async def test_ledger_artifacts_and_manifest_written(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        source = _raw_pdf(paths)
        extraction = _fake_extraction(paths)
        await _session(store, paths, extraction).ingest(source)
        ledger_dir = store.page_plan_artifact_dir(source) / "ledger"
        for name in ("claim-ledger.json", "document-structure.json", "portable-artifact-set.json"):
            assert (ledger_dir / name).is_file(), name
        # The manifest is persisted and marked integrated after ingest.
        manifest = from_json((extraction.cache_dir / "manifest.json").read_text(encoding="utf-8"))
        assert manifest.integrated

    async def test_dispositions_account_for_every_segment(
        self, store: WikiStore, paths: WikiPaths
    ) -> None:
        source = _raw_pdf(paths)
        await _session(store, paths, _fake_extraction(paths)).ingest(source)
        structure = json.loads(
            (
                store.page_plan_artifact_dir(source) / "ledger" / "document-structure.json"
            ).read_text()
        )["document_structure"]
        dispositions = structure["dispositions"]
        # Every extracted segment carries exactly one disposition from the
        # controlled vocabulary.
        allowed = {"accepted", "structural", "needs-review", "rejected", "non-claim"}
        assert dispositions
        assert all(record["disposition"] in allowed for record in dispositions)
