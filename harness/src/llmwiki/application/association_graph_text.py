"""Shared text normalization for AssociationGraph builders."""

from __future__ import annotations


def canonical_label(text: str) -> str:
    return " ".join(text.casefold().strip().split())
