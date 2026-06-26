"""Source-local topic evidence tests.

These prove topic planning rejects unsupported lexical headings without relying
on source-specific passages, while preserving valid headings and definitions.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.builder import (
    LedgerBuildResult,
    SegmentInput,
    build_claim_ledger,
    default_schema_bundle,
)
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.topics import SourceTopic, plan_source_topics

_HASH = "fedcba9876543210"


@dataclass(frozen=True)
class _ClaimSpec:
    statement: str
    role_tags: tuple[str, ...] = ()


def _claim(statement: str, role_tags: tuple[str, ...] = ()) -> _ClaimSpec:
    return _ClaimSpec(statement, role_tags)


def _build(specs: list[tuple[str, str, tuple[_ClaimSpec, ...]]]) -> LedgerBuildResult:
    inputs: list[SegmentInput] = []
    profiles = {}
    for order, (kind, text, claims) in enumerate(specs, start=1):
        segment = SourceSegment(
            segment_id=f"seg-{order:03d}",
            source_range_id=f"sr-{order:03d}",
            source_locator="source.pdf",
            source_hash=_HASH,
            heading_path="H",
            structure_node_id="",
            source_order=order,
            text=text,
            segment_kind=kind,
            evidence_ids=(f"ev-{order:03d}",),
        )
        claim_records = tuple(
            SegmentClaim(
                claim_id=f"c-{order}-{index}",
                statement=claim.statement,
                role_tags=claim.role_tags,
                eligibility="eligible",
                certainty="supported",
                evidence_ids=segment.evidence_ids,
            )
            for index, claim in enumerate(claims)
        )
        inputs.append(SegmentInput(segment, claim_records))
        profiles[segment.segment_id] = profile_unit(
            extracted_unit_id=segment.segment_id,
            source_range_id=segment.source_range_id,
            text=text,
            evidence_ids=segment.evidence_ids,
        )
    return build_claim_ledger(
        source_locator="source.pdf",
        source_hash=_HASH,
        evidence_registry_hash="er",
        segments=tuple(inputs),
        profiles=profiles,
        schema=default_schema_bundle(),
    )


def _topics(specs: list[tuple[str, str, tuple[_ClaimSpec, ...]]]) -> tuple[SourceTopic, ...]:
    result = _build(specs)
    return plan_source_topics(result.ledger, result.document_structure)


def _topic(
    specs: list[tuple[str, str, tuple[_ClaimSpec, ...]]], key: str
) -> tuple[LedgerBuildResult, SourceTopic | None]:
    result = _build(specs)
    topic = next(
        (
            item
            for item in plan_source_topics(result.ledger, result.document_structure)
            if item.topic_key == key
        ),
        None,
    )
    return result, topic


def test_discourse_heading_without_source_evidence_does_not_create_topic() -> None:
    topics = _topics(
        [
            ("heading", "# But in our case", ()),
            (
                "paragraph",
                "Widget has a Draw method so it satisfies the Shape interface.",
                (_claim("Widget has a Draw method so it satisfies the Shape interface."),),
            ),
        ]
    )

    assert "case" not in {topic.topic_key for topic in topics}


def test_renamed_heading_without_source_evidence_does_not_create_topic() -> None:
    topics = _topics(
        [
            ("heading", "# Around this orbit", ()),
            (
                "paragraph",
                "Marbler has a Draw method so it satisfies the Shape interface.",
                (_claim("Marbler has a Draw method so it satisfies the Shape interface."),),
            ),
        ]
    )

    assert "orbit" not in {topic.topic_key for topic in topics}


def test_domain_heading_with_source_evidence_survives() -> None:
    result, topic = _topic(
        [
            ("heading", "# Gliders", ()),
            ("paragraph", "A glider holds lift.", (_claim("A glider holds lift."),)),
            ("paragraph", "A glider uses trim.", (_claim("A glider uses trim."),)),
        ],
        "glider",
    )

    assert topic is not None
    texts = []
    for entry_id in topic.entry_ids:
        entry = result.ledger.entry(entry_id)
        assert entry is not None
        texts.append(entry.normalized_text)
    assert "A glider holds lift." in texts


def test_repeated_container_subject_does_not_anchor_single_term_topic() -> None:
    topics = _topics(
        [
            (
                "paragraph",
                f"The case of Riverland cannot be considered alone in passage {index}.",
                (_claim(f"The case of Riverland cannot be considered alone in passage {index}."),),
            )
            for index in range(1, 5)
        ]
    )

    assert "case" not in {topic.topic_key for topic in topics}


def test_defined_container_term_can_anchor_topic() -> None:
    _result, topic = _topic(
        [
            ("heading", "# Legal Terms", ()),
            (
                "paragraph",
                "A case is defined as a reviewed dispute.",
                (_claim("A case is defined as a reviewed dispute.", ("definition",)),),
            ),
        ],
        "case",
    )

    assert topic is not None
    assert topic.label == "Case"


def test_heading_representative_prefers_topic_support_over_source_order() -> None:
    result, topic = _topic(
        [
            ("heading", "# Interfaces", ()),
            ("paragraph", "A rectangle holds width.", (_claim("A rectangle holds width."),)),
            (
                "paragraph",
                "An interface specifies required methods.",
                (_claim("An interface specifies required methods."),),
            ),
        ],
        "interface",
    )

    assert topic is not None
    first = result.ledger.entry(topic.entry_ids[0])
    assert first is not None
    assert first.normalized_text == "An interface specifies required methods."
