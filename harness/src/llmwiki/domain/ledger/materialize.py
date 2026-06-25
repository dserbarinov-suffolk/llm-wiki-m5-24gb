"""Materialize technical-atom payloads from a source segment.

Each builder preserves the exact source text and adds logical structure only
when reusable structural parsing succeeds. When parsing partially or fully
fails, the raw text is still preserved and a ``ReviewReason`` is attached — an
atom is never dropped because its structure could not be modeled.
"""

from __future__ import annotations

import re

from llmwiki.domain.ledger.atoms import (
    CodeBlockPayload,
    FormulaPayload,
    ProcedurePayload,
    RulePayload,
    TableCell,
    TableColumn,
    TablePayload,
    TableRow,
    WorkedExamplePayload,
)
from llmwiki.domain.ledger.common import ReviewReason
from llmwiki.domain.ledger.segments import SourceSegment

_FENCE = re.compile(r"^[ \t]*(```|~~~)[ \t]*([A-Za-z0-9_+-]*)[ \t]*$")
_DEONTIC_FORCE = (
    (("must", "shall", "required", "have to"), "required"),
    (("cannot", "can not", "forbidden", "prohibited", "never", "may not"), "forbidden"),
    (("may", "allowed", "permitted", "can"), "permitted"),
    (("should", "recommended", "ought"), "recommended"),
)
_STEP = re.compile(
    r"^\s*(?:\d+[.)]\s|[-*]\s*\d+[.)\s]|step\b|then\b|next\b|finally\b)", re.IGNORECASE
)
_EXAMPLE = re.compile(
    r"\bfor example\b|\bexample[:.]|\be\.g\.|\bsuppose\b|\bconsider\b", re.IGNORECASE
)
_SENTENCE = re.compile(r"(?<=[.!?])\s+")
_MAX_RULE_WORDS = 60


def materialize_code_block(segment: SourceSegment) -> tuple[CodeBlockPayload, str] | None:
    block = _fenced_block(segment.text)
    if block is None:
        return None
    raw_code_text, language_tag = block
    return (
        CodeBlockPayload(
            raw_code_text=raw_code_text,
            parse_status="parsed",
            source_locator=segment.source_locator,
            language_tag=language_tag,
            language_detected=False,
            code_fence="```",
            line_count=raw_code_text.count("\n") + 1 if raw_code_text else 0,
            surrounding_explanation_locator=segment.source_range_id,
        ),
        "parsed",
    )


def materialize_table(segment: SourceSegment) -> tuple[TablePayload, ReviewReason | None]:
    raw = segment.text
    columns, rows, cells, status = _parse_pipe_table(raw)
    if status == "parsed":
        return TablePayload(raw, status, segment.source_locator, columns, rows, cells), None
    columns, rows, cells = _parse_enumerated_table(raw)
    if cells:
        reason = ReviewReason(
            "partial-parse", "table parsed as enumerated rows", segment.evidence_ids
        )
        return (
            TablePayload(raw, "partially-parsed", segment.source_locator, columns, rows, cells),
            reason,
        )
    reason = ReviewReason(
        "unparsed", "table structure not recovered; raw text preserved", segment.evidence_ids
    )
    return TablePayload(raw, "unparsed", segment.source_locator), reason


def materialize_formula(segment: SourceSegment) -> FormulaPayload | None:
    line = _first_match(segment.text, _FORMULA_LINE)
    if line is None:
        return None
    has_equation = "=" in line
    symbolic = bool(_SYMBOLIC.search(line)) and len(line.split()) <= 12
    return FormulaPayload(
        raw_formula_text=line.strip(),
        formula_subtype="symbolic-formula" if symbolic else "procedural-formula",
        formula_surface_form="equation" if has_equation else "prose",
        source_locator=segment.source_locator,
        notation_context_locator=segment.source_range_id,
    )


def materialize_rule(segment: SourceSegment) -> RulePayload | None:
    for sentence in _sentences(segment.text):
        # A rule is one statement, not a page of run-on text (e.g. a contents
        # list with a stray modal). Bound the length as a reusable structural cue.
        if len(sentence.split()) > _MAX_RULE_WORDS:
            continue
        force = _rule_force(sentence)
        if force is not None:
            return RulePayload(
                rule_text=sentence.strip(),
                rule_force=force,
                source_locator=segment.source_locator,
            )
    return None


def materialize_procedure(segment: SourceSegment) -> ProcedurePayload | None:
    steps = tuple(line.strip() for line in segment.text.splitlines() if _STEP.match(line))
    if len(steps) < 2:
        return None
    return ProcedurePayload(
        procedure_text=segment.text,
        steps=steps,
        source_locator=segment.source_locator,
    )


def materialize_worked_example(segment: SourceSegment) -> WorkedExamplePayload | None:
    if not _EXAMPLE.search(segment.text):
        return None
    return WorkedExamplePayload(
        example_text=segment.text,
        source_locator=segment.source_locator,
        explanation="",
    )


# -- helpers ---------------------------------------------------------------

_FORMULA_LINE = re.compile(
    r"[A-Za-z0-9_)\]]\s*=\s*[-+]?[A-Za-z0-9_(\[]|\d+\s*[-+*/×÷]\s*\d+|∑|√|\\frac|\\sum"
)
_SYMBOLIC = re.compile(r"[+\-*/^]|∑|√|×|÷|\\frac|\\sum")


def _fenced_block(text: str) -> tuple[str, str] | None:
    lines = text.splitlines()
    opening: int | None = None
    language = ""
    for index, line in enumerate(lines):
        match = _FENCE.match(line)
        if match is None:
            continue
        if opening is None:
            opening = index
            language = match.group(2)
            continue
        body = "\n".join(lines[opening + 1 : index])
        return (body, language) if body.strip() else None
    return None


def _parse_pipe_table(
    raw: str,
) -> tuple[tuple[TableColumn, ...], tuple[TableRow, ...], tuple[TableCell, ...], str]:
    rows = [line for line in raw.splitlines() if line.strip().startswith("|") or "|" in line]
    grid = [tuple(cell.strip() for cell in line.strip().strip("|").split("|")) for line in rows]
    grid = [row for row in grid if any(cell for cell in row)]
    if len(grid) < 2 or not _is_separator(grid[1]):
        return (), (), (), "failed"
    headers = grid[0]
    columns = tuple(TableColumn(i, header) for i, header in enumerate(headers))
    body = grid[2:]
    table_rows = tuple(TableRow(i) for i in range(len(body)))
    cells = tuple(
        TableCell(r, c, value)
        for r, row in enumerate(body)
        for c, value in enumerate(row)
        if c < len(headers)
    )
    return columns, table_rows, cells, "parsed"


def _is_separator(row: tuple[str, ...]) -> bool:
    return all(set(cell) <= set("-: ") and "-" in cell for cell in row if cell)


def _parse_enumerated_table(
    raw: str,
) -> tuple[tuple[TableColumn, ...], tuple[TableRow, ...], tuple[TableCell, ...]]:
    entries: list[tuple[str, str]] = []
    for line in raw.splitlines():
        match = re.match(r"^\s*(?:[-*]\s*)?(\d+)[\s.)]+(.*)$", line)
        if match and match.group(2).strip():
            entries.append((match.group(1), match.group(2).strip()))
    if len(entries) < 2:
        return (), (), ()
    columns = (TableColumn(0, "entry"), TableColumn(1, "content"))
    rows = tuple(TableRow(i) for i in range(len(entries)))
    cells = tuple(
        cell
        for i, (key, value) in enumerate(entries)
        for cell in (TableCell(i, 0, key), TableCell(i, 1, value))
    )
    return columns, rows, cells


def _rule_force(sentence: str) -> str | None:
    lowered = sentence.lower()
    for cues, force in _DEONTIC_FORCE:
        if any(re.search(rf"\b{re.escape(cue)}\b", lowered) for cue in cues):
            return force
    if re.search(r"\b(always|only|except|unless)\b", lowered):
        return "asserted-constraint"
    return None


def _sentences(text: str) -> list[str]:
    flat = " ".join(text.split())
    return [s for s in _SENTENCE.split(flat) if len(s.split()) >= 3]


def _first_match(text: str, pattern: re.Pattern[str]) -> str | None:
    for line in text.splitlines():
        if pattern.search(line):
            return line
    return None
