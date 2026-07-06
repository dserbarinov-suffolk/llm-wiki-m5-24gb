"""Extraction pipeline orchestrator: PDF -> cached DocumentModel + source units + manifest.

Derived artifacts live under <cache_root>/<sha256-prefix>/.
They are disposable, reproducible, and outside the wiki's three layers.
Re-running with a complete existing artifact set is a cache hit.
"""

from __future__ import annotations

import hashlib
import shutil
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE, ModelProfile
from llmwiki.pdf import ScannedPdfError
from llmwiki.pdf.classify import PdfKind, classify_pdf
from llmwiki.pdf.docling_extractor import extract_document_model
from llmwiki.pdf.document import (
    DocumentModel,
    SourceUnit,
    build_source_sections,
    build_source_units,
    document_model_from_json,
    document_model_to_json,
    render_source_units,
    source_sections_to_json,
    source_units_from_jsonl,
    source_units_to_jsonl,
)
from llmwiki.pdf.extractor import read_page_char_counts
from llmwiki.pdf.manifest import Manifest, SourceUnitRecord, from_json, to_json
from llmwiki.pdf.recognizer import TextRecognizer
from llmwiki.pdf.table_extractor import enrich_document_model_with_tables

_MANIFEST_FILE = "manifest.json"
_DOCUMENT_MODEL_FILE = "document_model.json"
_SOURCE_SECTIONS_FILE = "source_sections.json"
_SOURCE_UNITS_FILE = "source_units.jsonl"
_OBSOLETE_CHUNK_DIR = "chunks"

DocumentExtractFn = Callable[[Path, str, str], DocumentModel]


@dataclass(frozen=True)
class ExtractionResult:
    manifest: Manifest
    cache_dir: Path


def source_units_file(cache_dir: Path) -> Path:
    return cache_dir / _SOURCE_UNITS_FILE


def read_source_text(cache_dir: Path) -> str:
    """The whole extracted source rendered from structured source units."""
    units = read_source_units(cache_dir)
    if not units:
        return ""
    return render_source_units(units)


def save_manifest(result: ExtractionResult) -> None:
    (result.cache_dir / _MANIFEST_FILE).write_text(to_json(result.manifest), encoding="utf-8")


def read_document_model(cache_dir: Path) -> DocumentModel | None:
    path = cache_dir / _DOCUMENT_MODEL_FILE
    if not path.is_file():
        return None
    return document_model_from_json(path.read_text(encoding="utf-8"))


def read_source_units(cache_dir: Path) -> tuple[SourceUnit, ...]:
    path = source_units_file(cache_dir)
    if not path.is_file():
        return ()
    return source_units_from_jsonl(path.read_text(encoding="utf-8"))


def cache_has_current_pdf_artifacts(cache_dir: Path) -> bool:
    return (
        (cache_dir / _MANIFEST_FILE).is_file()
        and (cache_dir / _DOCUMENT_MODEL_FILE).is_file()
        and (cache_dir / _SOURCE_SECTIONS_FILE).is_file()
        and source_units_file(cache_dir).is_file()
        and _read_manifest_if_current(cache_dir) is not None
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
    """Extract + structure the PDF, or return the cached manifest (resume)."""
    _ = recognizer
    sha = _sha256(pdf_path)
    cache_dir = cache_root / sha[:16]

    if not reextract:
        document_model = read_document_model(cache_dir)
        if document_model is not None:
            return _write_derived_artifacts(
                cache_dir,
                source_rel,
                document_model,
                previous_manifest=_read_manifest_if_current(cache_dir),
                model_profile=model_profile,
            )

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
    source_units = build_source_units(
        document_model, source_sections, model_profile=model_profile
    )

    (cache_dir / _DOCUMENT_MODEL_FILE).write_text(
        document_model_to_json(document_model), encoding="utf-8"
    )
    (cache_dir / _SOURCE_SECTIONS_FILE).write_text(
        source_sections_to_json(source_sections), encoding="utf-8"
    )

    source_units_file(cache_dir).write_text(
        source_units_to_jsonl(source_units), encoding="utf-8"
    )
    obsolete_chunk_dir = cache_dir / _OBSOLETE_CHUNK_DIR
    if obsolete_chunk_dir.is_dir():
        shutil.rmtree(obsolete_chunk_dir)

    manifest = Manifest(
        source=source_rel,
        sha256=document_model.source_hash,
        extractor_name=document_model.extractor_name,
        source_units=tuple(_record(unit, previous_manifest) for unit in source_units),
    )
    result = ExtractionResult(manifest=manifest, cache_dir=cache_dir)
    save_manifest(result)
    return result


def _source_units_file_present(cache_dir: Path) -> bool:
    return source_units_file(cache_dir).is_file()


def _read_manifest_if_current(cache_dir: Path) -> Manifest | None:
    path = cache_dir / _MANIFEST_FILE
    if not path.is_file() or not _source_units_file_present(cache_dir):
        return None
    try:
        return from_json(path.read_text(encoding="utf-8"))
    except (KeyError, TypeError, ValueError):
        return None


def _record(
    source_unit: SourceUnit, previous_manifest: Manifest | None = None
) -> SourceUnitRecord:
    base = SourceUnitRecord(
        unit_id=source_unit.unit_id,
        heading=source_unit.heading_path,
        start_page=source_unit.page_start,
        end_page=source_unit.page_end,
        token_estimate=source_unit.token_estimate,
    )
    if previous_manifest is None:
        return base
    previous = _matching_previous_record(base, previous_manifest)
    if previous is None:
        return base
    return SourceUnitRecord(
        unit_id=base.unit_id,
        heading=base.heading,
        start_page=base.start_page,
        end_page=base.end_page,
        token_estimate=base.token_estimate,
        status=previous.status,
        notes=previous.notes,
        pages_written=previous.pages_written,
    )


def _matching_previous_record(
    record: SourceUnitRecord, previous_manifest: Manifest
) -> SourceUnitRecord | None:
    for previous in previous_manifest.source_units:
        if (
            previous.unit_id == record.unit_id
            and previous.heading == record.heading
            and previous.start_page == record.start_page
            and previous.end_page == record.end_page
        ):
            return previous
    return None
