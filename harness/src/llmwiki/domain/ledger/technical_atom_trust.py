"""Source-neutral trust decisions for technical atoms.

The trust gate decides whether a materialized atom can be projected as an
authoritative table/code/formula/etc. It never keys off a source title, domain
noun, or known passage; all signals come from payload shape and source-derived
structure.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import (
    CodeBlockPayload,
    FormulaPayload,
    ProcedurePayload,
    RulePayload,
    TablePayload,
    TechnicalAtom,
    WorkedExamplePayload,
    atom_raw_text,
)
from llmwiki.domain.ledger.common import ReviewReason

TRUSTED = "trusted"
REVIEW_ONLY = "review-only"
REJECTED = "rejected"
AUTHORITATIVE = "authoritative"
RAW_REVIEW_ONLY = "raw-review-only"
DO_NOT_PROJECT = "do-not-project"

_SENTENCE_END = re.compile(r"[.!?;:]\s*$")
_CODE_MARKER = re.compile(r"[{}()[\];=]|=>|->|//|#|</?|\\|::|:=|\b(?:const|let|var|def|fn)\b")
_FENCE = re.compile(r"^\s*(```|~~~)")


@dataclass(frozen=True)
class TechnicalAtomTrustDecision:
    technical_atom_id: str
    trust_status: str
    trust_reasons: tuple[str, ...]
    projection_policy: str
    review_reason: ReviewReason | None = None


def atom_is_authoritative(atom: TechnicalAtom) -> bool:
    return atom.trust_status == TRUSTED and atom.projection_policy == AUTHORITATIVE


def assess_technical_atom_trust(atom: TechnicalAtom) -> TechnicalAtomTrustDecision:
    raw = atom_raw_text(atom.payload).strip()
    if not raw:
        return _decision(atom, REJECTED, ("empty-payload",), DO_NOT_PROJECT)
    if atom.technical_atom_kind == "table" and isinstance(atom.payload, TablePayload):
        return _table_decision(atom, atom.payload)
    if atom.technical_atom_kind == "code-block" and isinstance(atom.payload, CodeBlockPayload):
        return _code_decision(atom, atom.payload)
    if isinstance(atom.payload, FormulaPayload):
        if not atom.payload.raw_formula_text.strip():
            return _decision(atom, REVIEW_ONLY, ("formula-empty",), RAW_REVIEW_ONLY)
        return _decision(atom, TRUSTED, (), AUTHORITATIVE)
    if isinstance(atom.payload, ProcedurePayload) and len(atom.payload.steps) < 2:
        return _decision(atom, REVIEW_ONLY, ("procedure-steps-incomplete",), RAW_REVIEW_ONLY)
    if isinstance(atom.payload, RulePayload) and (
        not atom.payload.rule_text.strip() or not atom.payload.rule_force.strip()
    ):
        return _decision(atom, REVIEW_ONLY, ("rule-structure-incomplete",), RAW_REVIEW_ONLY)
    if isinstance(atom.payload, WorkedExamplePayload) and not atom.payload.example_text.strip():
        return _decision(atom, REVIEW_ONLY, ("worked-example-empty",), RAW_REVIEW_ONLY)
    return _decision(atom, TRUSTED, (), AUTHORITATIVE)


def _table_decision(atom: TechnicalAtom, payload: TablePayload) -> TechnicalAtomTrustDecision:
    reasons: list[str] = []
    raw = payload.raw_table_text.strip()
    if payload.parse_status != "parsed" and not _partial_grid_is_authoritative(payload, raw):
        reasons.append("table-parse-incomplete")
    if payload.parse_status == "unparsed" and not _raw_table_like(raw):
        reasons.append("table-unparsed")
    if payload.parse_status in {"parsed", "partially-parsed"}:
        if not payload.columns or not payload.rows or not payload.cells:
            reasons.append("table-grid-missing")
        if _headers_suspicious(payload):
            reasons.append("table-header-suspicious")
        if _row_coverage_suspicious(payload):
            reasons.append("table-row-coverage-suspicious")
    if _raw_table_has_prose_contamination(raw):
        reasons.append("table-raw-text-contaminated-by-prose")
    if _cell_prose_contamination(payload):
        reasons.append("table-cells-contaminated-by-prose")
    if reasons:
        return _decision(atom, REVIEW_ONLY, tuple(dict.fromkeys(reasons)), RAW_REVIEW_ONLY)
    return _decision(atom, TRUSTED, (), AUTHORITATIVE)


def _code_decision(atom: TechnicalAtom, payload: CodeBlockPayload) -> TechnicalAtomTrustDecision:
    reasons: list[str] = []
    raw = payload.raw_code_text.strip()
    if payload.parse_status == "unparsed":
        reasons.append("code-unparsed")
    if _contains_fence(raw):
        reasons.append("code-contains-nested-fence")
    if _prose_lines_inside_code(raw):
        reasons.append("code-block-contaminated-by-prose")
    if payload.line_count and payload.line_count != raw.count("\n") + 1:
        reasons.append("code-line-count-mismatch")
    if reasons:
        return _decision(atom, REVIEW_ONLY, tuple(dict.fromkeys(reasons)), RAW_REVIEW_ONLY)
    return _decision(atom, TRUSTED, (), AUTHORITATIVE)


def _headers_suspicious(payload: TablePayload) -> bool:
    headers = tuple(column.header_text.strip() for column in payload.columns)
    if not headers:
        return True
    if _generic_entry_content_headers(headers) and len(payload.rows) >= 2:
        return False
    meaningful = [header for header in headers if any(char.isalnum() for char in header)]
    if len(meaningful) < max(1, len(headers) // 2):
        return True
    fragments = [header for header in meaningful if _fragment_like(header)]
    return len(fragments) >= max(2, len(meaningful) // 2)


def _row_coverage_suspicious(payload: TablePayload) -> bool:
    if not payload.rows or not payload.columns:
        return True
    width = len(payload.columns)
    filled_by_row: dict[int, int] = {row.row_index: 0 for row in payload.rows}
    for cell in payload.cells:
        if cell.column_index >= width:
            return True
        if cell.value.strip():
            filled_by_row[cell.row_index] = filled_by_row.get(cell.row_index, 0) + 1
    sparse = sum(1 for count in filled_by_row.values() if count < max(1, width // 2))
    return sparse > max(1, len(filled_by_row) // 2)


def _raw_table_has_prose_contamination(raw: str) -> bool:
    prose_lines = [
        line
        for line in raw.splitlines()
        if not _table_markup_line(line)
        and len(_words(line)) >= 7
        and (_SENTENCE_END.search(line.strip()) or _lowercase_sentence_start(line))
    ]
    return len(prose_lines) >= 2


def _raw_table_like(raw: str) -> bool:
    lines = [line for line in raw.splitlines() if line.strip()]
    table_like = sum(1 for line in lines if _table_markup_line(line) or _aligned_text_row(line))
    enumerated = sum(1 for line in lines if re.match(r"^\s*\d{1,3}\b\s+\S+", line))
    return table_like >= 2 or enumerated >= 2


def _partial_grid_is_authoritative(payload: TablePayload, raw: str) -> bool:
    if payload.parse_status != "partially-parsed":
        return False
    headers = tuple(column.header_text.strip() for column in payload.columns)
    if _generic_entry_content_headers(headers) and not _raw_has_implicit_header_before_rows(raw):
        return False
    if len(payload.columns) < 2 or len(payload.rows) < 2:
        return False
    if _headers_suspicious(payload) or _row_coverage_suspicious(payload):
        return False
    if _partial_row_coverage_suspicious(payload, raw):
        return False
    if _raw_table_has_prose_contamination(raw) or _cell_prose_contamination(payload):
        return False
    return _raw_table_like(raw)


def _partial_row_coverage_suspicious(payload: TablePayload, raw: str) -> bool:
    lines = [
        line.strip()
        for line in raw.splitlines()
        if line.strip() and not line.strip().lower().startswith(("table ", "table-", "tab. "))
    ]
    expected_data_lines = max(1, len(lines) - 1)
    return len(payload.rows) / expected_data_lines < 0.5


def _cell_prose_contamination(payload: TablePayload) -> bool:
    values = [cell.value for cell in payload.cells if cell.value.strip()]
    if len(values) < 4:
        return False
    prose = [
        value
        for value in values
        if len(_words(value)) >= 8
        and (_SENTENCE_END.search(value.strip()) or _lowercase_sentence_start(value))
    ]
    return len(prose) >= 3 and len(prose) / len(values) >= 0.18


def _prose_lines_inside_code(raw: str) -> bool:
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    code_lines = sum(1 for line in lines if _code_line(line))
    prose_lines = sum(1 for line in lines if _prose_line_in_code(line))
    return code_lines > 0 and prose_lines > 0


def _code_line(line: str) -> bool:
    stripped = line.strip()
    return bool(_CODE_MARKER.search(stripped)) or stripped.startswith(("//", "#", "/*", "*"))


def _prose_line_in_code(line: str) -> bool:
    stripped = line.strip()
    if not stripped or _code_line(stripped):
        return False
    words = _words(stripped)
    return len(words) >= 5 or (len(words) >= 3 and _SENTENCE_END.search(stripped) is not None)


def _contains_fence(raw: str) -> bool:
    return any(_FENCE.match(line) for line in raw.splitlines())


def _table_markup_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith("|") or "|" in stripped:
        return True
    return stripped.lower().startswith(("table ", "table-", "tab. "))


def _aligned_text_row(line: str) -> bool:
    return len(re.split(r"\s{2,}", line.strip())) >= 2


def _fragment_like(text: str) -> bool:
    words = _words(text)
    if not words:
        return True
    return text[:1].islower() or text.rstrip().endswith((",", "and", "or", "to"))


def _generic_entry_content_headers(headers: tuple[str, ...]) -> bool:
    return tuple(header.lower() for header in headers) == ("entry", "content")


def _raw_has_implicit_header_before_rows(raw: str) -> bool:
    candidates: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r"^\d{1,3}\b\s+\S+", stripped):
            break
        if stripped.lower().startswith(("table ", "table-", "tab. ")):
            continue
        candidates.append(stripped)
    return any(len(_words(line)) >= 2 for line in candidates)


def _lowercase_sentence_start(text: str) -> bool:
    stripped = text.strip()
    return bool(stripped[:1] and stripped[:1].islower())


def _words(text: str) -> tuple[str, ...]:
    return tuple(re.findall(r"[A-Za-z0-9]+", text))


def _decision(
    atom: TechnicalAtom,
    status: str,
    reasons: tuple[str, ...],
    policy: str,
) -> TechnicalAtomTrustDecision:
    review = None
    if status != TRUSTED:
        review = ReviewReason(
            "technical-atom-trust",
            ", ".join(reasons) if reasons else "technical atom is not authoritative",
            atom.evidence_ids,
        )
    return TechnicalAtomTrustDecision(
        technical_atom_id=atom.technical_atom_id,
        trust_status=status,
        trust_reasons=reasons,
        projection_policy=policy,
        review_reason=review,
    )
