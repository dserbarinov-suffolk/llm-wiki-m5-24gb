"""Chunk manifest: the on-disk resume cursor for a PDF ingest (pure).

Chunk state lives here, not in the model's context — the design's
"control flow is not memory" applied at the orchestration level.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, replace

# Cap carried-forward notes so 20 chunks of digest fit the integrate run
# (~1.5K chars ≈ 375 tokens each). Awaiting experimentation.
NOTE_CAP_CHARS = 1500

_STATUSES = ("pending", "done")


@dataclass(frozen=True)
class ChunkRecord:
    chunk_id: int
    heading: str
    start_page: int
    end_page: int
    token_estimate: int
    status: str = "pending"
    notes: str = ""

    def __post_init__(self) -> None:
        if self.status not in _STATUSES:
            raise ValueError(f"invalid chunk status {self.status!r}")


@dataclass(frozen=True)
class Manifest:
    source: str  # path relative to raw/
    sha256: str
    chunks: tuple[ChunkRecord, ...]
    integrated: bool = field(default=False)

    @property
    def pending(self) -> tuple[ChunkRecord, ...]:
        return tuple(c for c in self.chunks if c.status == "pending")

    @property
    def all_done(self) -> bool:
        return not self.pending

    def mark_done(self, chunk_id: int, notes: str) -> Manifest:
        capped = notes if len(notes) <= NOTE_CAP_CHARS else notes[: NOTE_CAP_CHARS - 1] + "…"
        chunks = tuple(
            replace(c, status="done", notes=capped) if c.chunk_id == chunk_id else c
            for c in self.chunks
        )
        if chunks == self.chunks:
            raise ValueError(f"no pending chunk with id {chunk_id}")
        return replace(self, chunks=chunks)

    def mark_integrated(self) -> Manifest:
        return replace(self, integrated=True)

    def digest(self) -> str:
        """Concatenated per-chunk notes for the integrate run."""
        parts = [
            f"Chunk {c.chunk_id} — {c.heading} (p.{c.start_page}-{c.end_page}):\n{c.notes}"
            for c in self.chunks
            if c.status == "done" and c.notes
        ]
        return "\n\n".join(parts)


def to_json(manifest: Manifest) -> str:
    return json.dumps(
        {
            "source": manifest.source,
            "sha256": manifest.sha256,
            "integrated": manifest.integrated,
            "chunks": [
                {
                    "id": c.chunk_id,
                    "heading": c.heading,
                    "pages": [c.start_page, c.end_page],
                    "tokens": c.token_estimate,
                    "status": c.status,
                    "notes": c.notes,
                }
                for c in manifest.chunks
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
        integrated=data["integrated"],
        chunks=tuple(
            ChunkRecord(
                chunk_id=c["id"],
                heading=c["heading"],
                start_page=c["pages"][0],
                end_page=c["pages"][1],
                token_estimate=c["tokens"],
                status=c["status"],
                notes=c["notes"],
            )
            for c in data["chunks"]
        ),
    )
