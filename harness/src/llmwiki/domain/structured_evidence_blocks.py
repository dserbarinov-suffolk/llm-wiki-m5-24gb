"""Block-level structured evidence extraction."""

from __future__ import annotations

import re

from llmwiki.domain.structured_evidence_types import StructuredEvidenceArtifact

_ARITHMETIC_RE = re.compile(r"\b\d+\s*(?:[+\-*/xX]|x)\s*\d+.*=")
_CODE_FENCE_RE = re.compile(r"^\s*```")
_DICE_RE = re.compile(r"\b\d+d(?:\s*[+xX]\s*\d+)?\b", re.IGNORECASE)
_EXAMPLE_RE = re.compile(
    r"\b(?:example|worked example|for example|this character|our|we(?:'ll|'ve|'re)?)\b",
    re.IGNORECASE,
)
_MARKDOWN_TABLE_RE = re.compile(r"^\s*\|.+\|\s*$", re.MULTILINE)
_TABLE_RE = re.compile(r"\btable\b", re.IGNORECASE)


def extract_structured_artifacts(page_id: str, body: str) -> tuple[StructuredEvidenceArtifact, ...]:
    artifacts: list[StructuredEvidenceArtifact] = []
    artifacts.extend(_raw_table_artifacts(page_id, body))
    artifacts.extend(_markdown_table_artifacts(page_id, body))
    artifacts.extend(_code_block_artifacts(page_id, body))
    artifacts.extend(_technical_frame_artifacts(page_id, body))
    artifacts.extend(_statement_artifacts(page_id, body))
    return tuple(artifacts)


def has_structured_signal(text: str) -> bool:
    return bool(
        _MARKDOWN_TABLE_RE.search(text)
        or _TABLE_RE.search(text)
        or _ARITHMETIC_RE.search(text)
        or _DICE_RE.search(text)
        or _EXAMPLE_RE.search(text)
        or _CODE_FENCE_RE.search(text)
    )


def category(text: str) -> str:
    if _MARKDOWN_TABLE_RE.search(text) or _TABLE_RE.search(text):
        return "table"
    if _CODE_FENCE_RE.search(text):
        return "code"
    if _ARITHMETIC_RE.search(text) or _DICE_RE.search(text):
        return "formula"
    if _EXAMPLE_RE.search(text):
        return "worked-example"
    return "structured-evidence"


def _raw_table_artifacts(page_id: str, body: str) -> list[StructuredEvidenceArtifact]:
    lines = body.splitlines()
    artifacts: list[StructuredEvidenceArtifact] = []
    heading = ""
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("# ").strip()
        if "<summary>Raw table text</summary>" not in stripped:
            index += 1
            continue
        start = max(0, index - 1)
        end = index + 1
        while end < len(lines) and "</details>" not in lines[end]:
            end += 1
        end = min(len(lines), end + 1)
        artifacts.append(
            StructuredEvidenceArtifact(
                page_id=page_id,
                category="raw-table-text",
                heading=heading,
                excerpt="\n".join(lines[start:end]).strip(),
            )
        )
        index = end
    return artifacts


def _markdown_table_artifacts(page_id: str, body: str) -> list[StructuredEvidenceArtifact]:
    lines = body.splitlines()
    artifacts: list[StructuredEvidenceArtifact] = []
    heading = ""
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("# ").strip()
        if "|" not in line:
            index += 1
            continue
        start = index
        while index < len(lines) and "|" in lines[index]:
            index += 1
        block = "\n".join(lines[start:index]).strip()
        if len(block.splitlines()) >= 2 and _MARKDOWN_TABLE_RE.search(block):
            artifacts.append(
                StructuredEvidenceArtifact(
                    page_id=page_id,
                    category="markdown-table",
                    heading=heading,
                    excerpt=block,
                )
            )
        continue
    return artifacts


def _code_block_artifacts(page_id: str, body: str) -> list[StructuredEvidenceArtifact]:
    lines = body.splitlines()
    artifacts: list[StructuredEvidenceArtifact] = []
    heading = ""
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("# ").strip()
        if not _CODE_FENCE_RE.match(stripped):
            index += 1
            continue
        start = index
        index += 1
        while index < len(lines) and not _CODE_FENCE_RE.match(lines[index].strip()):
            index += 1
        if index < len(lines):
            index += 1
        artifacts.append(
            StructuredEvidenceArtifact(
                page_id=page_id,
                category="code-block",
                heading=heading,
                excerpt="\n".join(lines[start:index]).strip(),
            )
        )
    return artifacts


def _technical_frame_artifacts(page_id: str, body: str) -> list[StructuredEvidenceArtifact]:
    lines = body.splitlines()
    artifacts: list[StructuredEvidenceArtifact] = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line.startswith("### Technical frame"):
            index += 1
            continue
        heading = line.removeprefix("### ").strip()
        start = index
        index += 1
        while index < len(lines) and not lines[index].startswith(("## ", "### ")):
            index += 1
        block = "\n".join(lines[start:index]).strip()
        if has_structured_signal(block):
            artifacts.append(
                StructuredEvidenceArtifact(
                    page_id=page_id,
                    category=category(block),
                    heading=heading,
                    excerpt=block,
                )
            )
    return artifacts


def _statement_artifacts(page_id: str, body: str) -> list[StructuredEvidenceArtifact]:
    artifacts: list[StructuredEvidenceArtifact] = []
    heading = ""
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("### "):
            heading = stripped.removeprefix("### ").strip()
        if not stripped.startswith("- ") or not has_structured_signal(stripped):
            continue
        artifacts.append(
            StructuredEvidenceArtifact(
                page_id=page_id,
                category=category(stripped),
                heading=heading,
                excerpt=stripped,
            )
        )
    return artifacts
