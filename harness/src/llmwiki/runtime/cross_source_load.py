"""Load persisted per-source topic indexes into the cross-source read model.

Each source's ``topics.json`` (built at ingest from headings + key terms)
becomes one ``SourcePosition`` per topic: the topic key is the cross-source
grouping key, and the topic's representative statement carries the proposition
fields used to classify relationships. Grouping these by shared key across
sources is what produces real cross-source concept pages.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from llmwiki.domain.ledger.cross_source import SourcePosition


@dataclass(frozen=True)
class LoadedSource:
    source_locator: str
    source_hash: str
    projection_source_support_id: str
    positions: tuple[SourcePosition, ...]


def load_source_positions(topic_index_json: str) -> LoadedSource:
    index = json.loads(topic_index_json)
    source_locator = index["source_locator"]
    source_hash = index["source_hash"]
    support_id = index["projection_source_support_id"]
    positions = tuple(
        _position(topic, source_locator, source_hash, support_id)
        for topic in index.get("topics", ())
        if topic.get("topic_key")
    )
    return LoadedSource(source_locator, source_hash, support_id, positions)


def _position(
    topic: dict[str, Any], source_locator: str, source_hash: str, support_id: str
) -> SourcePosition:
    representative = topic.get("representative") or {}
    return SourcePosition(
        source_locator=source_locator,
        source_hash=source_hash,
        projection_source_support_id=support_id,
        ledger_entry_id=representative.get("ledger_entry_id", f"topic-{topic['topic_key']}"),
        ledger_entry_kind="concept",
        subject=representative.get("subject", ""),
        predicate=representative.get("predicate", ""),
        polarity=representative.get("polarity", ""),
        claim_force=representative.get("claim_force", ""),
        condition_scope=representative.get("condition_scope", "unconditional"),
        has_scope=bool(representative.get("has_scope", False)),
        normalized_text=representative.get("normalized_text", topic.get("label", "")),
        concept_facets=(topic["topic_key"],),
        topic_keys=(topic["topic_key"],),
        evidence_ids=(),
        citation_label=representative.get("citation_label", source_locator),
    )
