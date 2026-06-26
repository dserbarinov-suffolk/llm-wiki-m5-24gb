"""Concept-entry tests for claim-ledger topic keys.

These prevent cross-source pages from being rescued by a downstream blocklist:
only explicit, source-derived defined terms become concept facets.
"""

from llmwiki.domain.ledger.confidence import ConfidencePolicy
from llmwiki.domain.ledger.entries import LedgerEntry
from llmwiki.domain.ledger.entry_build import build_claim_entry
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment


def _entry(statement: str) -> LedgerEntry:
    segment = SourceSegment(
        segment_id="seg-001",
        source_range_id="sr-001",
        source_locator="src.pdf",
        source_hash="0123456789abcdef",
        heading_path="H",
        structure_node_id="",
        source_order=1,
        text=statement,
        segment_kind="paragraph",
        evidence_ids=("ev-001",),
    )
    claim = SegmentClaim(
        "claim-001",
        statement,
        ("definition",),
        "eligible",
        "supported",
        ("ev-001",),
    )
    return build_claim_entry(
        segment=segment,
        claim=claim,
        statement_id="source-statement-001",
        structure_node_ids=(),
        policy=ConfidencePolicy(),
    )


def test_definition_with_lexical_frame_uses_defined_term_not_frame_noun() -> None:
    entry = _entry('The word "monk" means solitude.')

    assert entry.ledger_entry_kind == "concept"
    assert entry.concept_facets == ("monk",)


def test_definition_with_concise_subject_becomes_concept() -> None:
    entry = _entry("A closure refers to a function plus its environment.")

    assert entry.ledger_entry_kind == "concept"
    assert entry.concept_facets == ("closure",)


def test_deictic_definition_stays_claim_not_concept() -> None:
    entry = _entry("In broad terms, this means that a value can be reused.")

    assert entry.ledger_entry_kind == "claim"
    assert entry.concept_facets == ()


def test_means_of_is_not_a_definition_cue() -> None:
    entry = _entry("Roads are a means of communication.")

    assert entry.ledger_entry_kind == "claim"
    assert entry.concept_facets == ()


def test_later_lexical_frame_supplies_defined_term() -> None:
    entry = _entry("The motto is old, but the word minister merely means servant.")

    assert entry.ledger_entry_kind == "concept"
    assert entry.concept_facets == ("minister",)
