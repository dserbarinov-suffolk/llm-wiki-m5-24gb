"""Reusable source-authored numbering helpers for document structure."""

from __future__ import annotations

import re

_MARKDOWN_DECORATION = re.compile(r"[*_`]+")
_TRAILING_MARKER = re.compile(r"\s+#+\s*$")
_WHITESPACE = re.compile(r"\s+")
_LEADING_NUMBER = re.compile(
    r"^(?:(?:chapter|section|part|appendix|book)\s+)?\d+(?:\.\d+)*\s*[-:.]?\s*",
    re.IGNORECASE,
)
_NUMBER_PATH = re.compile(
    r"^(?:(?:chapter|section|part|appendix|book)\s+)?(\d+(?:\.\d+)*)\b",
    re.IGNORECASE,
)


def heading_text(text: str) -> str:
    stripped = text.lstrip()
    without_opening = stripped.lstrip("#").strip()
    return _TRAILING_MARKER.sub("", without_opening).strip()


def canonical_heading_label(text: str) -> str:
    without_decoration = _MARKDOWN_DECORATION.sub("", text)
    return _WHITESPACE.sub(" ", without_decoration).strip().casefold()


def heading_number_path(label: str) -> tuple[int, ...]:
    match = _NUMBER_PATH.match(label.strip())
    if match is None:
        return ()
    return tuple(int(part) for part in match.group(1).split("."))


def is_number_marker(label: str, number_path: tuple[int, ...]) -> bool:
    marker = ".".join(str(part) for part in number_path)
    return label == marker


def structural_path_labels(labels: tuple[str, ...]) -> tuple[str, ...]:
    merged: list[str] = []
    index = 0
    while index < len(labels):
        label = labels[index]
        number_path = heading_number_path(label)
        if (
            number_path
            and is_number_marker(label, number_path)
            and index + 1 < len(labels)
            and not heading_number_path(labels[index + 1])
        ):
            merged.append(canonical_heading_label(numbered_title(number_path, labels[index + 1])))
            index += 2
            continue
        merged.append(label)
        index += 1
    return tuple(merged)


def number_conflicts(parent: tuple[int, ...], child: tuple[int, ...]) -> bool:
    if not parent or not child or parent == child:
        return False
    return not number_parent(parent, child)


def number_parent(parent: tuple[int, ...], child: tuple[int, ...]) -> bool:
    return bool(parent and child and len(parent) < len(child) and child[: len(parent)] == parent)


def same_heading(parent_label: str, child_label: str) -> bool:
    if parent_label == child_label or without_leading_number(parent_label) == child_label:
        return True
    parent_path = heading_number_path(parent_label)
    child_path = heading_number_path(child_label)
    return bool(
        parent_path
        and parent_path == child_path
        and without_leading_number(parent_label) == without_leading_number(child_label)
    )


def without_leading_number(label: str) -> str:
    return _LEADING_NUMBER.sub("", label, count=1).strip()


def numbered_title(number_path: tuple[int, ...], title: str) -> str:
    return f"{'.'.join(str(part) for part in number_path)} {title}".strip()
