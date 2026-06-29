"""Source-neutral identity names for materialized table atoms."""

from __future__ import annotations

import re
import unicodedata

from llmwiki.domain.ledger.atoms import TablePayload
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.structure import DocumentStructure, StructureNode

_TABLE_CAPTION = re.compile(r"^\s*(?:table|tab\.)\s*(?:[-:.]|\d+\b)?\s*(.+)$", re.IGNORECASE)
_TOC = re.compile(r"\btable\s+of\s+contents\b", re.IGNORECASE)
_TABLE_VERB = r"shows|lists|gives|provides|contains|summarizes|describes"
_NAME_CHARS = r"[A-Za-z0-9/&+() -]"
_NAMED_TABLE_REFS = (
    re.compile(
        rf"\b(?:the|this|that)\s+({_NAME_CHARS}{{1,80}}?)\s+table\s+"
        rf"(?:{_TABLE_VERB})\b",
        re.IGNORECASE,
    ),
    re.compile(rf"\b([A-Z]{_NAME_CHARS}{{1,80}}?)\s+table\s+(?:{_TABLE_VERB})\b"),
    re.compile(
        rf"\b(?:see|consult|using|use)\s+(?:the\s+)?({_NAME_CHARS}{{1,80}}?)\s+table\b",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\b(?:from|in|on)\s+the\s+({_NAME_CHARS}{{1,80}}?)\s+table\b",
        re.IGNORECASE,
    ),
)
_LEADING_WORDS = frozenset({"a", "an", "the", "this", "that", "these", "those", "following"})
_TRAILING_WORDS = frozenset({"table"})


def table_identity_names(
    ledger: ClaimLedger, structure: DocumentStructure | None = None
) -> tuple[str, ...]:
    """All source-derived names attached to materialized table atoms."""
    names: list[str] = []
    for atom_names in table_identity_names_by_atom_id(ledger, structure).values():
        names.extend(atom_names)
    return tuple(dict.fromkeys(names))


def table_identity_names_by_atom_id(
    ledger: ClaimLedger, structure: DocumentStructure | None = None
) -> dict[str, tuple[str, ...]]:
    """Table atom id to source-derived names: captions, headings, and table cues."""
    node_headings = _structure_node_headings(structure)
    atom_node_ids = _table_atom_node_ids(ledger)
    forward_targets = _table_forward_targets_by_atom_id(ledger, structure)
    names_by_atom: dict[str, tuple[str, ...]] = {}
    for atom in ledger.technical_atoms:
        if atom.technical_atom_kind != "table" or not isinstance(atom.payload, TablePayload):
            continue
        heading_names = tuple(
            heading
            for node_id in atom_node_ids.get(atom.technical_atom_id, ())
            if (heading := node_headings.get(node_id, ""))
        )
        names = _normalized_names(
            (
                atom.payload.caption,
                *raw_table_caption_lines(atom.payload),
                *heading_names,
                *_target_node_names(forward_targets.get(atom.technical_atom_id, ())),
            )
        )
        if names:
            names_by_atom[atom.technical_atom_id] = names
    return names_by_atom


def table_structure_node_ids_by_atom_id(ledger: ClaimLedger) -> dict[str, tuple[str, ...]]:
    return _table_atom_node_ids(ledger)


def table_forward_target_node_ids_by_atom_id(
    ledger: ClaimLedger, structure: DocumentStructure | None
) -> dict[str, tuple[str, ...]]:
    return {
        atom_id: tuple(node.structure_node_id for node in nodes)
        for atom_id, nodes in _table_forward_targets_by_atom_id(ledger, structure).items()
    }


def raw_table_caption_lines(payload: TablePayload) -> tuple[str, ...]:
    lines = tuple(line.strip() for line in payload.raw_table_text.splitlines()[:3] if line.strip())
    caption_lines = [line for line in lines if _TABLE_CAPTION.match(line)]
    if caption_lines:
        return tuple(caption_lines)
    if lines and _one_line_table_title(lines[0]):
        return (lines[0],)
    return ()


def named_table_references(text: str) -> tuple[str, ...]:
    if _TOC.search(text):
        return ()
    refs: list[str] = []
    for pattern in _NAMED_TABLE_REFS:
        for match in pattern.finditer(text):
            name = normalize_table_name(match.group(1))
            if name:
                refs.append(name)
    return tuple(dict.fromkeys(refs))


def normalize_table_name(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    match = _TABLE_CAPTION.match(text.strip())
    if match is not None:
        text = match.group(1)
    text = re.sub(r"[^a-z0-9]+", " ", text.lower())
    words = [word for word in text.split() if word]
    while words and words[0] in _LEADING_WORDS:
        words.pop(0)
    while words and words[-1] in _TRAILING_WORDS:
        words.pop()
    return " ".join(words[:8])


def has_matching_table_name(reference: str, table_names: tuple[str, ...]) -> bool:
    reference_tokens = _match_tokens(reference)
    for name in table_names:
        if reference == name or reference in name or name in reference:
            return True
        name_tokens = _match_tokens(name)
        if (
            reference_tokens
            and name_tokens
            and (reference_tokens.issubset(name_tokens) or name_tokens.issubset(reference_tokens))
        ):
            return True
    return False


def explicit_forward_reference(text: str) -> bool:
    return bool(
        re.search(
            r"\b(?:table\s+(?:below|following|that follows)|following\s+[^.]{0,80}\s+table)\b",
            text,
            re.IGNORECASE,
        )
    )


def _normalized_names(candidates: tuple[str, ...]) -> tuple[str, ...]:
    names = [name for candidate in candidates if (name := normalize_table_name(candidate))]
    return tuple(dict.fromkeys(names))


def _source_order(structure: DocumentStructure | None) -> dict[str, int]:
    if structure is None:
        return {}
    return {
        disposition.source_range_id: disposition.source_order
        for disposition in structure.dispositions
    }


def _structure_node_headings(structure: DocumentStructure | None) -> dict[str, str]:
    if structure is None:
        return {}
    headings: dict[str, str] = {}
    for node in structure.structure_nodes:
        if (
            node.structure_node_kind == "root"
            or node.heading_text.lower().endswith(".pdf")
            or _generic_table_heading_cue(node.heading_text)
        ):
            continue
        name = normalize_table_name(node.heading_text)
        if name:
            headings[node.structure_node_id] = name
    return headings


def _table_atom_node_ids(ledger: ClaimLedger) -> dict[str, tuple[str, ...]]:
    nodes: dict[str, tuple[str, ...]] = {}
    for entry in ledger.entries:
        if entry.ledger_entry_kind != "technical-atom" or entry.technical_atom_kind != "table":
            continue
        if entry.technical_atom_id:
            nodes[entry.technical_atom_id] = entry.structure_node_ids
    return nodes


def _table_forward_targets_by_atom_id(
    ledger: ClaimLedger, structure: DocumentStructure | None
) -> dict[str, tuple[StructureNode, ...]]:
    if structure is None:
        return {}
    source_order = _source_order(structure)
    nodes = tuple(sorted(structure.structure_nodes, key=lambda node: node.source_order))
    targets: dict[str, tuple[StructureNode, ...]] = {}
    for atom in ledger.technical_atoms:
        if atom.technical_atom_kind != "table" or not isinstance(atom.payload, TablePayload):
            continue
        table_order = source_order.get(atom.source_range_id)
        if table_order is None:
            continue
        cue = _nearest_forward_table_cue(nodes, table_order)
        if cue is None:
            continue
        target_nodes = _cue_section_nodes(nodes, cue, structure)
        if target_nodes:
            targets[atom.technical_atom_id] = target_nodes
    return targets


def _nearest_forward_table_cue(
    nodes: tuple[StructureNode, ...], table_order: int
) -> StructureNode | None:
    cues = [
        node
        for node in nodes
        if node.source_order < table_order
        and table_order - node.source_order <= 32
        and _generic_table_heading_cue(node.heading_text)
    ]
    return max(cues, key=lambda node: node.source_order, default=None)


def _cue_section_nodes(
    nodes: tuple[StructureNode, ...], cue: StructureNode, structure: DocumentStructure
) -> tuple[StructureNode, ...]:
    targets: list[StructureNode] = []
    parent = structure.node(cue.parent_structure_node_id) if cue.parent_structure_node_id else None
    if parent is not None and _named_heading(parent.heading_text):
        targets.append(parent)
    for node in sorted(
        (node for node in nodes if node.source_order < cue.source_order),
        key=lambda node: node.source_order,
        reverse=True,
    ):
        if _named_heading(node.heading_text):
            targets.append(node)
            break
    return tuple(dict.fromkeys(targets))


def _target_node_names(nodes: tuple[StructureNode, ...]) -> tuple[str, ...]:
    names: list[str] = []
    for node in nodes:
        names.extend(_named_heading(node.heading_text))
    return tuple(dict.fromkeys(names))


def _named_heading(text: str) -> tuple[str, ...]:
    if not text or _generic_table_heading_cue(text) or text.lower().endswith(".pdf"):
        return ()
    name = normalize_table_name(text)
    return (name,) if name else ()


def _one_line_table_title(line: str) -> bool:
    if "|" in line or "\t" in line or not line.strip():
        return False
    words = line.split()
    if len(words) != 1:
        return False
    word = normalize_table_name(line)
    return bool(word) and not _roll_notation(word)


def _generic_table_heading_cue(text: str) -> bool:
    normalized = " ".join(str(text).lower().split())
    return explicit_forward_reference(normalized) and not named_table_references(normalized)


def _match_tokens(name: str) -> set[str]:
    stopwords = {"table", "tables"}
    return {
        _singularize(word)
        for word in name.split()
        if word not in stopwords and not _roll_notation(word)
    }


def _singularize(word: str) -> str:
    if len(word) > 3 and word.endswith("ies"):
        return f"{word[:-3]}y"
    if len(word) > 3 and word.endswith("s"):
        return word[:-1]
    return word


def _roll_notation(word: str) -> bool:
    return bool(re.fullmatch(r"d\d+|\d+d\d+|\d+", word))
