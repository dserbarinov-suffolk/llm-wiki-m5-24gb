"""Markdown render helpers for source section pages."""

from __future__ import annotations

from llmwiki.domain.ledger.atom_addressing import technical_atom_anchor
from llmwiki.domain.ledger.atom_context import best_atom_context
from llmwiki.domain.ledger.atoms import TechnicalAtom
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.projection_context import ProjectionContext
from llmwiki.domain.ledger.projection_context_render import (
    atom_frame_markdown,
    evidence_block_line,
)
from llmwiki.domain.ledger.renderer import atom_block, atom_context_block


def claim_entries(entries: tuple[LedgerEntry, ...]) -> tuple[LedgerEntry, ...]:
    return tuple(entry for entry in entries if entry.ledger_entry_kind != "technical-atom")


def append_claims(
    lines: list[str],
    claims: tuple[LedgerEntry, ...],
    projection_context: ProjectionContext | None,
) -> None:
    rendered: set[str] = set()
    if projection_context is not None:
        claim_ids = tuple(entry.ledger_entry_id for entry in claims)
        for block in projection_context.blocks_for_entries(claim_ids):
            selected = tuple(entry_id for entry_id in block.entry_ids if entry_id in claim_ids)
            if not selected:
                continue
            lines.append(evidence_block_line(block))
            rendered.update(selected)
    for entry in claims:
        if entry.ledger_entry_id in rendered:
            continue
        text = entry.normalized_text or entry.source_text
        citation = f"{entry.source_locator} ({entry.source_range_id})"
        lines.append(f"- {text.strip()} _({citation})_")


def append_atoms(
    lines: list[str],
    ledger: ClaimLedger,
    atoms: tuple[TechnicalAtom, ...],
    projection_context: ProjectionContext | None,
) -> None:
    rendered: set[str] = set()
    rendered_frame_count = 0
    if projection_context is not None:
        atom_ids = tuple(atom.technical_atom_id for atom in atoms)
        for index, frame in enumerate(projection_context.frames_for_atoms(atom_ids), start=1):
            selected = tuple(atom_id for atom_id in frame.atom_ids if atom_id in atom_ids)
            if not selected:
                continue
            lines.extend(atom_frame_markdown(frame, ledger, projection_context, index).splitlines())
            lines.append("")
            rendered_frame_count = index
            rendered.update(selected)
    next_index = rendered_frame_count + 1
    for atom in atoms:
        if atom.technical_atom_id in rendered:
            continue
        lines.extend((f"### Technical atom {next_index}", ""))
        next_index += 1
        lines.extend((technical_atom_anchor(atom.technical_atom_id), ""))
        context = best_atom_context(ledger.atom_contexts(atom.technical_atom_id))
        if context is not None:
            lines.extend(atom_context_block(context, atom.source_locator).strip().splitlines())
            lines.append("")
        rendered_block = atom_block(atom.technical_atom_kind, atom.payload)
        citation = f"{atom.source_locator} ({atom.source_range_id})"
        lines.extend((f"**Atom:** _({citation})_", "", rendered_block, ""))
