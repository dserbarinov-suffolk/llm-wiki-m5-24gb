"""Per-source topic index: the searchable subjects a reader would ask about.

Topics come from two source-neutral signals: the author's section headings
(precise, multiword: "Function Declarations", "Character Creation") and salient
recurring subject terms (``function``, ``array``, ``damage``, ``king``). Each
topic aggregates the source's usable claims and technical atoms that mention it,
so a topic page answers "what does this source say about X". No model is used;
the held model pass would later disambiguate and merge near-duplicate topics.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

from llmwiki.domain.ledger.atoms import atom_raw_text
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.stopwords import COMMON_WORDS
from llmwiki.domain.ledger.structure import DocumentStructure

_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9]{2,}")
_HEADING_NUMBER = re.compile(
    r"^(?:chapter|part|section|appendix|book)\s+[\dIVXLC]+\s*[-:.]?\s*", re.IGNORECASE
)
_TOPIC_KINDS = ("claim", "event", "concept")
_MIN_TERM_FREQUENCY = 4
_MIN_MATCHES = 3
_MAX_TOPICS = 32
_HEADING_BONUS = 3.0
# A topic statement is a sentence, not a contents list or run-on paragraph.
_MAX_STATEMENT_WORDS = 45


@dataclass(frozen=True)
class SourceTopic:
    topic_key: str
    label: str
    page_kind: str
    match_terms: tuple[str, ...]
    entry_ids: tuple[str, ...]
    atom_ids: tuple[str, ...]
    from_heading: bool
    salience: float


@dataclass(frozen=True)
class TopicRepresentative:
    """One source's representative statement for a topic, used to classify
    cross-source relationships (shared predicate, polarity, scope)."""

    ledger_entry_id: str
    subject: str
    predicate: str
    polarity: str
    claim_force: str
    condition_scope: str
    has_scope: bool
    normalized_text: str
    citation_label: str


@dataclass(frozen=True)
class PersistedTopic:
    topic_key: str
    label: str
    page_kind: str
    entry_count: int
    atom_count: int
    representative: TopicRepresentative


@dataclass(frozen=True)
class TopicIndex:
    """A source's topics, persisted so cross-source synthesis can group them
    across sources by shared topic key without rehydrating the full ledger."""

    source_locator: str
    source_hash: str
    projection_source_support_id: str
    topics: tuple[PersistedTopic, ...]


def build_topic_index(
    ledger: ClaimLedger,
    topics: tuple[SourceTopic, ...],
    *,
    source_locator: str,
    source_hash: str,
    projection_source_support_id: str,
) -> TopicIndex:
    persisted = tuple(
        PersistedTopic(
            topic_key=topic.topic_key,
            label=topic.label,
            page_kind=topic.page_kind,
            entry_count=len(topic.entry_ids),
            atom_count=len(topic.atom_ids),
            representative=_representative(ledger, topic),
        )
        for topic in topics
    )
    return TopicIndex(source_locator, source_hash, projection_source_support_id, persisted)


def _representative(ledger: ClaimLedger, topic: SourceTopic) -> TopicRepresentative:
    for entry_id in topic.entry_ids:
        entry = ledger.entry(entry_id)
        if entry is None:
            continue
        has_scope = (
            entry.condition_scope in ("conditional", "exception")
            or entry.temporal_scope is not None
            or entry.spatial_scope is not None
        )
        return TopicRepresentative(
            ledger_entry_id=entry.ledger_entry_id,
            subject=entry.subject,
            predicate=entry.predicate,
            polarity=entry.polarity,
            claim_force=entry.claim_force,
            condition_scope=entry.condition_scope,
            has_scope=has_scope,
            normalized_text=entry.normalized_text or entry.source_text,
            citation_label=f"{entry.source_locator} ({entry.source_range_id})",
        )
    return TopicRepresentative(
        ledger_entry_id=f"topic-{topic.topic_key}",
        subject="",
        predicate="",
        polarity="",
        claim_force="",
        condition_scope="unconditional",
        has_scope=False,
        normalized_text=topic.label,
        citation_label=topic.label,
    )


def plan_source_topics(
    ledger: ClaimLedger,
    structure: DocumentStructure,
    *,
    max_topics: int = _MAX_TOPICS,
    min_matches: int = _MIN_MATCHES,
) -> tuple[SourceTopic, ...]:
    entries = [
        entry
        for entry in ledger.usable_entries
        if entry.ledger_entry_kind in _TOPIC_KINDS and (entry.subject or entry.normalized_text)
    ]
    candidates = _heading_candidates(structure) + _term_candidates(entries)
    topics: dict[str, SourceTopic] = {}
    for key, label, terms, from_heading in candidates:
        if key in topics:
            continue
        topic = _aggregate(key, label, terms, from_heading, entries, ledger)
        if topic is not None and len(topic.entry_ids) + len(topic.atom_ids) >= min_matches:
            topics[key] = topic
    ranked = sorted(topics.values(), key=lambda t: (-t.salience, t.topic_key))
    return tuple(ranked[:max_topics])


def _heading_candidates(
    structure: DocumentStructure,
) -> list[tuple[str, str, tuple[str, ...], bool]]:
    candidates: list[tuple[str, str, tuple[str, ...], bool]] = []
    seen: set[str] = set()
    for node in structure.structure_nodes:
        if node.structure_node_kind == "root":
            continue
        label = _HEADING_NUMBER.sub("", node.heading_text).strip()
        terms = _content_terms(label)
        key = "-".join(terms)
        if not terms or len(terms) > 5 or key in seen:
            continue
        seen.add(key)
        candidates.append((key, label, tuple(terms), True))
    return candidates


def _term_candidates(entries: list[LedgerEntry]) -> list[tuple[str, str, tuple[str, ...], bool]]:
    counts: Counter[str] = Counter()
    for entry in entries:
        for token in _content_terms(entry.subject):
            counts[token] += 1
    candidates: list[tuple[str, str, tuple[str, ...], bool]] = []
    for term, frequency in counts.most_common():
        if frequency < _MIN_TERM_FREQUENCY:
            break
        candidates.append((term, term.title(), (term,), False))
    return candidates


def _aggregate(
    key: str,
    label: str,
    terms: tuple[str, ...],
    from_heading: bool,
    entries: list[LedgerEntry],
    ledger: ClaimLedger,
) -> SourceTopic | None:
    matcher = _matcher(terms)
    if matcher is None:
        return None
    matched = [
        entry
        for entry in entries
        if (matcher.search(entry.subject) or matcher.search(entry.normalized_text))
        and len(entry.normalized_text.split()) <= _MAX_STATEMENT_WORDS
    ]
    # Most focused statements first (shorter, more on-topic), so the rendered
    # head of the page reads well even though salience uses the full count.
    matched.sort(key=lambda entry: len(entry.normalized_text))
    entry_ids = tuple(entry.ledger_entry_id for entry in matched)
    atom_ids = tuple(
        atom.technical_atom_id
        for atom in ledger.technical_atoms
        if matcher.search(atom_raw_text(atom.payload))
    )
    salience = len(entry_ids) + 1.5 * len(atom_ids) + (_HEADING_BONUS if from_heading else 0.0)
    return SourceTopic(
        topic_key=key,
        label=label,
        page_kind="concept",
        match_terms=terms,
        entry_ids=entry_ids,
        atom_ids=atom_ids,
        from_heading=from_heading,
        salience=salience,
    )


def _content_terms(text: str) -> list[str]:
    terms = []
    for token in _TOKEN.findall(text):
        lowered = _singular(token.lower())
        if len(lowered) >= 4 and lowered not in COMMON_WORDS:
            terms.append(lowered)
    return list(dict.fromkeys(terms))


def _matcher(terms: tuple[str, ...]) -> re.Pattern[str] | None:
    parts = [re.escape(term) for term in terms if term]
    if not parts:
        return None
    return re.compile(r"\b(?:" + "|".join(parts) + r")", re.IGNORECASE)


def _singular(token: str) -> str:
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith("ss"):
        return token
    return token[:-1] if token.endswith("s") and len(token) > 4 else token
