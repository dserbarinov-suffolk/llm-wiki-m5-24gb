"""Wiki-page helper functions for claim-ledger ingest."""

from __future__ import annotations

from pathlib import Path

from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.source_coverage import SourceElementRecord
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.pdf.document import DocumentModel


def source_element_records(model: DocumentModel) -> tuple[SourceElementRecord, ...]:
    return tuple(
        SourceElementRecord(
            source_element_id=element.element_id,
            element_kind=element.element_kind,
            body_state=element.body_state,
            heading_path=element.heading_path,
            page_locator=_page_locator(element.page_start, element.page_end),
            has_source_text=bool((element.text or element.markdown).strip()),
        )
        for element in model.elements
    )


def source_title(source_locator: str, structure: DocumentStructure) -> str:
    _ = structure
    stem = Path(source_locator).stem.replace("_", " ").replace("-", " ")
    return " ".join(_title_word(word) for word in stem.split())


def _title_word(word: str) -> str:
    return word if word.isupper() else word.capitalize()


def ledger_summary(ledger: ClaimLedger, decision: str, linked_page_count: int = 0) -> str:
    usable = len(ledger.usable_entries)
    atoms = len(ledger.technical_atoms)
    review = len(ledger.needs_review_entries)
    label = ledger.source_family_assignment.top_label
    return (
        f"Claim-ledger projection ({label}): {usable} usable entries, {atoms} technical atoms, "
        f"{review} needs-review, {linked_page_count} linked page(s); write decision {decision}."
    )


def _page_locator(page_start: int, page_end: int) -> str:
    if page_start <= 0 or page_end <= 0:
        return "document"
    return f"p.{page_start}" if page_start == page_end else f"p.{page_start}-{page_end}"
