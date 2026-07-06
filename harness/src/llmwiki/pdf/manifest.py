"""PDF source-unit manifest: the on-disk resume cursor for a PDF ingest (pure).

Source-unit state lives here, not in the model's context — the design's
"control flow is not memory" applied at the orchestration level.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, replace

from llmwiki.domain.model_profile import DEFAULT_MODEL_PROFILE

_STATUSES = ("pending", "done")


@dataclass(frozen=True)
class SourceUnitRecord:
    unit_id: str
    heading: str
    start_page: int
    end_page: int
    token_estimate: int
    status: str = "pending"
    notes: str = ""
    # Machine record of pages the source-unit run actually wrote (captured at the
    # write_page tool) — ground truth where notes have over-claimed.
    pages_written: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.status not in _STATUSES:
            raise ValueError(f"invalid source-unit status {self.status!r}")


@dataclass(frozen=True)
class Manifest:
    source: str  # path relative to raw/
    sha256: str
    source_units: tuple[SourceUnitRecord, ...]
    extractor_name: str = "docling"
    integrated: bool = field(default=False)

    @property
    def pending(self) -> tuple[SourceUnitRecord, ...]:
        return tuple(unit for unit in self.source_units if unit.status == "pending")

    @property
    def all_done(self) -> bool:
        return not self.pending

    def mark_done(
        self,
        unit_id: str,
        notes: str,
        pages_written: tuple[str, ...] = (),
        note_cap_chars: int = DEFAULT_MODEL_PROFILE.pdf_manifest_note_chars,
    ) -> Manifest:
        capped = notes if len(notes) <= note_cap_chars else notes[: note_cap_chars - 1] + "…"
        source_units = tuple(
            replace(unit, status="done", notes=capped, pages_written=pages_written)
            if unit.unit_id == unit_id
            else unit
            for unit in self.source_units
        )
        if source_units == self.source_units:
            raise ValueError(f"no pending source unit with id {unit_id}")
        return replace(self, source_units=source_units)

    def mark_integrated(self) -> Manifest:
        return replace(self, integrated=True)

    def digest(self) -> str:
        """Concatenated per-source-unit notes for the integrate run.

        The recorded pages_written line is the machine record; the notes
        above it are the model's own account.
        """
        parts = []
        for unit in self.source_units:
            if unit.status != "done" or not unit.notes:
                continue
            entry = (
                f"Source unit {unit.unit_id} — {unit.heading} "
                f"(p.{unit.start_page}-{unit.end_page}):\n{unit.notes}"
            )
            if unit.pages_written:
                entry += "\nPages written (recorded): " + ", ".join(
                    f"[[{page}]]" for page in unit.pages_written
                )
            parts.append(entry)
        return "\n\n".join(parts)

    def write_counts(self) -> dict[str, int]:
        """Per-page write totals across done source units (salience input)."""
        counts: dict[str, int] = {}
        for unit in self.source_units:
            for page in unit.pages_written:
                counts[page] = counts.get(page, 0) + 1
        return counts


def to_json(manifest: Manifest) -> str:
    return json.dumps(
        {
            "source": manifest.source,
            "sha256": manifest.sha256,
            "extractor_name": manifest.extractor_name,
            "integrated": manifest.integrated,
            "source_units": [
                {
                    "id": unit.unit_id,
                    "heading": unit.heading,
                    "pages": [unit.start_page, unit.end_page],
                    "tokens": unit.token_estimate,
                    "status": unit.status,
                    "notes": unit.notes,
                    "pages_written": list(unit.pages_written),
                }
                for unit in manifest.source_units
            ],
        },
        indent=2,
        ensure_ascii=False,
    )


def from_json(text: str) -> Manifest:
    data = json.loads(text)
    return Manifest(
        source=data["source"],
        sha256=data["sha256"],
        extractor_name=data["extractor_name"],
        integrated=data["integrated"],
        source_units=tuple(
            SourceUnitRecord(
                unit_id=unit["id"],
                heading=unit["heading"],
                start_page=unit["pages"][0],
                end_page=unit["pages"][1],
                token_estimate=unit["tokens"],
                status=unit["status"],
                notes=unit["notes"],
                pages_written=tuple(unit["pages_written"]),
            )
            for unit in data["source_units"]
        ),
    )
