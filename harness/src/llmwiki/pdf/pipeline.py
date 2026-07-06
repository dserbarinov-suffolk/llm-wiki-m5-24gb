"""Extraction pipeline orchestrator: PDF -> cached DocumentModel + chunks + manifest.

Derived artifacts live under <cache_root>/<sha256-prefix>/.
They are disposable, reproducible, and outside the wiki's three layers.
Re-running with a complete existing artifact set is a cache hit.
"""

from __future__ import annotations

import hashlib
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile
from llmwiki.pdf import ScannedPdfError
from llmwiki.pdf.classify import PdfKind, classify_pdf
from llmwiki.pdf.docling_extractor import extract_document_model
from llmwiki.pdf.document import (
    DocumentModel,
    SourceChunk,
    build_source_chunks,
    build_source_sections,
    document_model_from_json,
    document_model_to_json,
    source_sections_to_json,
)
from llmwiki.pdf.extractor import read_page_char_counts
from llmwiki.pdf.manifest import ChunkRecord, Manifest, from_json, to_json
from llmwiki.pdf.recognizer import TextRecognizer
from llmwiki.pdf.table_extractor import enrich_document_model_with_tables

_MANIFEST_FILE = "manifest.json"
_DOCUMENT_MODEL_FILE = "document_model.json"
_SOURCE_SECTIONS_FILE = "source_sections.json"
_CHUNK_DIR = "chunks"

DocumentExtractFn = Callable[[Path, str, str], DocumentModel]


@dataclass(frozen=True)
class ExtractionResult:
    manifest: Manifest
    cache_dir: Path


def chunk_file(cache_dir: Path, chunk_id: int) -> Path:
    return cache_dir / _CHUNK_DIR / f"{chunk_id:04d}.md"


def read_source_text(cache_dir: Path) -> str:
    """The whole extracted source (all chunks) — salience's mention corpus."""
    chunk_dir = cache_dir / _CHUNK_DIR
    if not chunk_dir.is_dir():
        return ""
    return "\n\n".join(p.read_text(encoding="utf-8") for p in sorted(chunk_dir.glob("*.md")))


def save_manifest(result: ExtractionResult) -> None:
    (result.cache_dir / _MANIFEST_FILE).write_text(to_json(result.manifest), encoding="utf-8")


def read_document_model(cache_dir: Path) -> DocumentModel | None:
    path = cache_dir / _DOCUMENT_MODEL_FILE
    if not path.is_file():
        return None
    return document_model_from_json(path.read_text(encoding="utf-8"))


def cache_has_current_pdf_artifacts(cache_dir: Path) -> bool:
    return (
        (cache_dir / _MANIFEST_FILE).is_file()
        and (cache_dir / _DOCUMENT_MODEL_FILE).is_file()
        and (cache_dir / _SOURCE_SECTIONS_FILE).is_file()
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def ensure_extracted(
    pdf_path: Path,
    source_rel: str,
    cache_root: Path,
    recognizer: TextRecognizer,
    reextract: bool = False,
    document_extractor: DocumentExtractFn = extract_document_model,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> ExtractionResult:
    """Extract + chunk the PDF, or return the cached manifest (resume)."""
    _ = recognizer
    sha = _sha256(pdf_path)
    cache_dir = cache_root / sha[:16]
    manifest_path = cache_dir / _MANIFEST_FILE

    if cache_has_current_pdf_artifacts(cache_dir) and not reextract:
        document_model = read_document_model(cache_dir)
        if document_model is not None:
            manifest = from_json(manifest_path.read_text(encoding="utf-8"))
            return _write_derived_artifacts(
                cache_dir,
                source_rel,
                document_model,
                previous_manifest=manifest,
                model_profile=model_profile,
            )
        manifest = from_json(manifest_path.read_text(encoding="utf-8"))
        if _chunk_files_present(cache_dir, manifest):
            return ExtractionResult(manifest=manifest, cache_dir=cache_dir)

    if classify_pdf(read_page_char_counts(pdf_path)) is PdfKind.SCANNED:
        raise ScannedPdfError(
            f"raw/{source_rel} looks like a scanned (image-only) PDF; "
            "whole-document OCR is not enabled yet "
            "(docs/2026-06-11-pdf-ingestion-design.md)."
        )

    cache_dir.mkdir(parents=True, exist_ok=True)
    document_model = enrich_document_model_with_tables(
        pdf_path, document_extractor(pdf_path, source_rel, sha)
    )
    return _write_derived_artifacts(
        cache_dir, source_rel, document_model, model_profile=model_profile
    )


def _write_derived_artifacts(
    cache_dir: Path,
    source_rel: str,
    document_model: DocumentModel,
    *,
    previous_manifest: Manifest | None = None,
    model_profile: ModelProfile = DEFAULT_MODEL_PROFILE,
) -> ExtractionResult:
    source_sections = build_source_sections(document_model)
    source_chunks = build_source_chunks(
        document_model, source_sections, model_profile=model_profile
    )

    (cache_dir / _DOCUMENT_MODEL_FILE).write_text(
        document_model_to_json(document_model), encoding="utf-8"
    )
    (cache_dir / _SOURCE_SECTIONS_FILE).write_text(
        source_sections_to_json(source_sections), encoding="utf-8"
    )

    chunk_dir = cache_dir / _CHUNK_DIR
    chunk_dir.mkdir(parents=True, exist_ok=True)
    for old_chunk in chunk_dir.glob("*.md"):
        old_chunk.unlink()
    for chunk in source_chunks:
        chunk_file(cache_dir, chunk.chunk_id).write_text(chunk.text, encoding="utf-8")

    manifest = Manifest(
        source=source_rel,
        sha256=document_model.source_hash,
        extractor_name=document_model.extractor_name,
        chunks=tuple(_record(c, previous_manifest) for c in source_chunks),
    )
    result = ExtractionResult(manifest=manifest, cache_dir=cache_dir)
    save_manifest(result)
    return result


def _chunk_files_present(cache_dir: Path, manifest: Manifest) -> bool:
    return all(chunk_file(cache_dir, record.chunk_id).is_file() for record in manifest.chunks)


def _record(chunk: SourceChunk, previous_manifest: Manifest | None = None) -> ChunkRecord:
    base = ChunkRecord(
        chunk_id=chunk.chunk_id,
        heading=chunk.heading_path,
        start_page=chunk.page_start,
        end_page=chunk.page_end,
        token_estimate=chunk.token_estimate,
    )
    if previous_manifest is None:
        return base
    previous = _matching_previous_record(base, previous_manifest)
    if previous is None:
        return base
    return ChunkRecord(
        chunk_id=base.chunk_id,
        heading=base.heading,
        start_page=base.start_page,
        end_page=base.end_page,
        token_estimate=base.token_estimate,
        status=previous.status,
        notes=previous.notes,
        pages_written=previous.pages_written,
    )


def _matching_previous_record(
    record: ChunkRecord, previous_manifest: Manifest
) -> ChunkRecord | None:
    for previous in previous_manifest.chunks:
        if (
            previous.chunk_id == record.chunk_id
            and previous.heading == record.heading
            and previous.start_page == record.start_page
            and previous.end_page == record.end_page
        ):
            return previous
    return None
