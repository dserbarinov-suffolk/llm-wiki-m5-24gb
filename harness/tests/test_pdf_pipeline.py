"""Extraction pipeline tests against a synthetic PDF."""

from pathlib import Path

import pymupdf  # type: ignore[import-untyped]
import pytest

from llmwiki.pdf import ScannedPdfError
from llmwiki.pdf.document import DocumentElement, DocumentModel
from llmwiki.pdf.pipeline import chunk_file, ensure_extracted, save_manifest
from llmwiki.pdf.recognizer import NullRecognizer

_PAGE_PROSE = "Functions are first-class values. " * 40  # ~1.4K chars/page: classifies TEXT


def _make_pdf(path: Path, n_pages: int = 6, with_image: bool = True) -> None:
    doc = pymupdf.open()
    for i in range(n_pages):
        page = doc.new_page()
        page.insert_text((72, 72), f"Chapter text page {i + 1}.")
        page.insert_textbox(pymupdf.Rect(72, 100, 540, 400), _PAGE_PROSE)
    if with_image:
        # A textured "photo" placed clear of the text — the layout engine
        # silently drops featureless rectangles and overlapped images.
        width, height = 240, 180
        pixmap = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, width, height), False)
        for y in range(0, height, 4):
            for x in range(0, width, 4):
                pixmap.set_pixel(x, y, (x % 256, y % 256, (x * y) % 256))
        doc[0].insert_image(pymupdf.Rect(150, 450, 390, 630), pixmap=pixmap)
    toc = [[1, "One", 1], [1, "Two", 3], [1, "Three", 5]]
    doc.set_toc(toc)
    doc.save(str(path))
    doc.close()


def _make_scanned_pdf(path: Path, n_pages: int = 4) -> None:
    doc = pymupdf.open()
    for _ in range(n_pages):
        doc.new_page()  # no text layer at all
    doc.save(str(path))
    doc.close()


def _make_captioned_table_pdf(path: Path) -> None:
    doc = pymupdf.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Chapter text page 1.")
    page.insert_textbox(pymupdf.Rect(72, 100, 540, 400), _PAGE_PROSE)
    rows = (
        ("Table- Sample Matrix",),
        ("Label", "Score", "Note"),
        ("Alpha", "10", "Stable"),
        ("Beta", "20", "Review"),
        ("Gamma", "30", "Complete"),
    )
    y = 500
    for row in rows:
        if len(row) == 1:
            page.insert_text((72, y), row[0])
        else:
            for x, value in zip((72, 190, 310), row, strict=True):
                page.insert_text((x, y), value)
        y += 18
    page.insert_text((72, y + 20), "Next Section")
    page.insert_text((72, y + 38), "Ordinary prose follows the table.")
    doc.save(str(path))
    doc.close()


class FakeDocumentExtractor:
    def __init__(self, heading: str = "Functions", text: str = "Functions are values.") -> None:
        self.calls = 0
        self.heading = heading
        self.text = text

    def __call__(self, pdf_path: Path, source_rel: str, source_hash: str) -> DocumentModel:
        self.calls += 1
        return DocumentModel(
            source_locator=source_rel,
            source_hash=source_hash,
            extractor_name="docling",
            extractor_version="test",
            elements=(
                DocumentElement(
                    element_id="element-000001",
                    element_kind="heading",
                    body_state="body",
                    heading_path=self.heading,
                    page_start=1,
                    page_end=1,
                    text=self.heading,
                    markdown=f"# {self.heading}",
                ),
                DocumentElement(
                    element_id="element-000002",
                    element_kind="paragraph",
                    body_state="body",
                    heading_path=self.heading,
                    page_start=1,
                    page_end=6,
                    text=self.text,
                    markdown=self.text,
                ),
            ),
        )


class TestEnsureExtracted:
    def test_extracts_chunks_and_manifest(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)
        document_extractor = FakeDocumentExtractor()
        result = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )

        manifest = result.manifest
        assert manifest.source == "book.pdf"
        assert manifest.extractor_name == "docling"
        assert len(manifest.chunks) == 1
        assert manifest.pending == manifest.chunks
        first = manifest.chunks[0]
        text = chunk_file(result.cache_dir, first.chunk_id).read_text(encoding="utf-8")
        assert "Functions are values" in text
        assert (first.start_page, manifest.chunks[-1].end_page) == (1, 6)
        assert (result.cache_dir / "document_model.json").is_file()
        assert (result.cache_dir / "source_sections.json").is_file()
        assert document_extractor.calls == 1

    def test_cache_hit_skips_reextraction(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)
        document_extractor = FakeDocumentExtractor()
        first = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )
        marked = first.manifest.mark_done(1, "notes")
        save_manifest(type(first)(manifest=marked, cache_dir=first.cache_dir))

        again = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )
        assert again.manifest.chunks[0].status == "done"  # resume state survived
        assert document_extractor.calls == 1

    def test_reextract_rebuilds_pending_manifest(self, tmp_path: Path) -> None:
        pdf = tmp_path / "book.pdf"
        _make_pdf(pdf)
        document_extractor = FakeDocumentExtractor()
        first = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )
        save_manifest(
            type(first)(manifest=first.manifest.mark_done(1, "n"), cache_dir=first.cache_dir)
        )
        redone = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            reextract=True,
            document_extractor=document_extractor,
        )
        assert redone.manifest.pending == redone.manifest.chunks
        assert document_extractor.calls == 2

    def test_scanned_pdf_is_refused_cleanly(self, tmp_path: Path) -> None:
        pdf = tmp_path / "scan.pdf"
        _make_scanned_pdf(pdf)
        with pytest.raises(ScannedPdfError, match="scanned"):
            ensure_extracted(
                pdf,
                "scan.pdf",
                tmp_path / "cache",
                NullRecognizer(),
                document_extractor=FakeDocumentExtractor(),
            )

    def test_recovers_captioned_layout_table_when_primary_extractor_misses_it(
        self, tmp_path: Path
    ) -> None:
        pdf = tmp_path / "book.pdf"
        _make_captioned_table_pdf(pdf)
        document_extractor = FakeDocumentExtractor(
            heading="Measurements",
            text="Table- Sample Matrix\n\n20",
        )

        result = ensure_extracted(
            pdf,
            "book.pdf",
            tmp_path / "cache",
            NullRecognizer(),
            document_extractor=document_extractor,
        )

        model = (result.cache_dir / "document_model.json").read_text(encoding="utf-8")
        chunk = "\n\n".join(
            chunk_file(result.cache_dir, chunk_record.chunk_id).read_text(encoding="utf-8")
            for chunk_record in result.manifest.chunks
        )
        assert '"element_kind": "table"' in model
        assert model.count('"element_kind": "table"') == 1
        assert chunk.count("Table- Sample Matrix") == 1
        assert "Label" in chunk
        assert "Alpha" in chunk
        assert "Gamma" in chunk
        assert "Next Section" not in chunk
