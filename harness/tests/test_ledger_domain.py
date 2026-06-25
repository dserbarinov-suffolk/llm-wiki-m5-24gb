"""Data-in/data-out tests for the pure claim-ledger DomainModule.

These exercise the load-bearing invariants from
docs/2026-06-25-claim-ledger-first-architecture.md: every segment gets exactly
one disposition, one extractor decision per capability, exact atom payload
preservation, claim-like proposition fields, the confidence/needs-review
routing, deterministic output, the quality report + write boundary, and the
Universal Standard (renamed-domain variants behave identically).
"""

from llmwiki.domain.ledger.artifacts import (
    PortableArtifactMember,
    build_portable_artifact_set,
)
from llmwiki.domain.ledger.atoms import TablePayload
from llmwiki.domain.ledger.builder import (
    LedgerBuildResult,
    SegmentInput,
    build_claim_ledger,
    default_schema_bundle,
)
from llmwiki.domain.ledger.canonical import canonical_json
from llmwiki.domain.ledger.features import profile_unit
from llmwiki.domain.ledger.pointers import claim_ledger_pointer, document_structure_pointer
from llmwiki.domain.ledger.projection import ProjectionSourceSupport, plan_source_page
from llmwiki.domain.ledger.quality import (
    build_ledger_quality_report,
    build_projection_quality_report,
    page_write_decision,
)
from llmwiki.domain.ledger.quality_catalog import (
    default_quality_check_catalog,
    default_severity_policy,
)
from llmwiki.domain.ledger.renderer import render_source_page
from llmwiki.domain.ledger.schemas import AtomValidator, default_atom_schema_set
from llmwiki.domain.ledger.segments import SegmentClaim, SourceSegment
from llmwiki.domain.ledger.vocab import (
    CALIBRATION_BUCKETS,
    EXTRACTED_UNIT_DISPOSITIONS,
    EXTRACTOR_CAPABILITY_IDS,
)

_HASH = "0123456789abcdef"


def _build(specs: list[tuple[str, str, list[str]]], source_hash: str = _HASH) -> LedgerBuildResult:
    inputs: list[SegmentInput] = []
    profiles = {}
    for order, (kind, text, claims) in enumerate(specs, start=1):
        seg = SourceSegment(
            segment_id=f"seg-{order:03d}",
            source_range_id=f"sr-{order:03d}",
            source_locator="src.pdf",
            source_hash=source_hash,
            heading_path="H",
            structure_node_id="",
            source_order=order,
            text=text,
            segment_kind=kind,
            evidence_ids=(f"ev-{order:03d}",),
        )
        claim_records = tuple(
            SegmentClaim(f"c-{order}-{i}", statement, (), "eligible", "supported", seg.evidence_ids)
            for i, statement in enumerate(claims)
        )
        inputs.append(SegmentInput(seg, claim_records))
        profiles[seg.segment_id] = profile_unit(
            extracted_unit_id=seg.segment_id,
            source_range_id=seg.source_range_id,
            text=text,
            evidence_ids=seg.evidence_ids,
        )
    return build_claim_ledger(
        source_locator="src.pdf",
        source_hash=source_hash,
        evidence_registry_hash="er-hash",
        segments=tuple(inputs),
        profiles=profiles,
        schema=default_schema_bundle(),
    )


_MIXED = [
    ("heading", "# Combat", []),
    ("paragraph", "A combatant must roll a die.", ["A combatant must roll a die."]),
    ("code-fence", "```python\n  x = 1\n    y = 2\n```", []),
    ("table-block", "1 alpha entry\n2 beta entry\n3 gamma entry", []),
    ("paragraph", "A grimoire contains many spells.", ["A grimoire contains many spells."]),
    (
        "paragraph",
        "Glossary plus assorted notation forms here.",
        ["assorted glossary notation forms"],
    ),
]


def test_every_segment_has_exactly_one_disposition() -> None:
    result = _build(_MIXED)
    dispositions = result.document_structure.dispositions
    assert len(dispositions) == len(_MIXED)
    assert all(record.disposition in EXTRACTED_UNIT_DISPOSITIONS for record in dispositions)
    # Headings are structural, never non-claim.
    heading = next(r for r in dispositions if r.source_range_id == "sr-001")
    assert heading.disposition == "structural"


def test_one_extractor_decision_per_capability_per_content_segment() -> None:
    result = _build(_MIXED)
    by_range: dict[str, set[str]] = {}
    for decision in result.ledger.extractor_decisions:
        by_range.setdefault(decision.source_range_id, set()).add(decision.extractor_capability_id)
    for capabilities in by_range.values():
        assert capabilities == set(EXTRACTOR_CAPABILITY_IDS)


def test_code_block_preserves_exact_text_including_whitespace() -> None:
    result = _build(_MIXED)
    code = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "code-block")
    assert code.payload.raw_code_text == "  x = 1\n    y = 2"
    assert code.parse_status == "parsed"


def test_table_block_preserves_raw_text_with_partial_parse_review() -> None:
    result = _build(_MIXED)
    table = next(a for a in result.ledger.technical_atoms if a.technical_atom_kind == "table")
    assert table.payload.raw_table_text == "1 alpha entry\n2 beta entry\n3 gamma entry"
    assert table.parse_status == "partially-parsed"
    assert table.review_reason is not None
    assert table.payload.cells  # logical model recovered as enumerated rows


def test_deontic_sentence_becomes_rule_atom_not_duplicate_claim() -> None:
    result = _build(_MIXED)
    rules = [a for a in result.ledger.technical_atoms if a.technical_atom_kind == "rule"]
    assert any(a.payload.rule_force == "required" for a in rules)
    claim_texts = [e.normalized_text for e in result.ledger.entries if e.is_claim_like]
    assert not any("must roll a die" in text for text in claim_texts)


def test_claim_like_entry_carries_required_proposition_fields() -> None:
    result = _build(_MIXED)
    claim = next(e for e in result.ledger.usable_entries if "grimoire" in e.normalized_text)
    assert claim.subject and claim.predicate and claim.object_value
    assert claim.polarity in ("affirmative", "negative")
    assert claim.claim_force


def test_fragmentary_statement_is_needs_review_not_usable() -> None:
    result = _build(_MIXED)
    fragment = next(
        e for e in result.ledger.entries if "glossary notation" in e.normalized_text.lower()
    )
    assert fragment.ledger_entry_status == "needs-review"
    assert fragment.review_reason is not None


def test_atom_validator_rejects_incomplete_payload() -> None:
    validator = AtomValidator(default_atom_schema_set())
    invalid = TablePayload(raw_table_text="", parse_status="parsed", source_locator="src.pdf")
    valid = TablePayload(raw_table_text="x", parse_status="parsed", source_locator="src.pdf")
    assert validator.validate("table", invalid).status == "invalid"
    assert validator.validate("table", valid).status == "valid"


def test_ranker_scores_in_range_and_buckets_controlled() -> None:
    result = _build(_MIXED)
    for decision in result.ledger.extractor_decisions:
        assert 0.0 <= decision.ranker_score <= 1.0
        if decision.extractor_decision_status == "abstained":
            assert decision.calibration_bucket in CALIBRATION_BUCKETS
            assert decision.abstain_reason is not None


def test_domain_is_deterministic_for_same_input() -> None:
    first = _build(_MIXED)
    second = _build(_MIXED)
    assert canonical_json(first.ledger) == canonical_json(second.ledger)
    assert canonical_json(first.document_structure) == canonical_json(second.document_structure)


def test_universal_standard_renamed_domain_variants_behave_identically() -> None:
    spells = [
        ("heading", "# Spells", []),
        ("paragraph", "The wizard must cast a spell.", ["The wizard must cast a spell."]),
        ("paragraph", "A grimoire contains many spells.", ["A grimoire contains many spells."]),
    ]
    modules = [
        ("heading", "# Modules", []),
        (
            "paragraph",
            "The engineer must compile a module.",
            ["The engineer must compile a module."],
        ),
        ("paragraph", "A library contains many modules.", ["A library contains many modules."]),
    ]
    a = _build(spells, source_hash="a" * 16)
    b = _build(modules, source_hash="b" * 16)

    def shape(result: LedgerBuildResult) -> tuple:
        kinds = tuple(e.ledger_entry_kind for e in result.ledger.entries)
        statuses = tuple(e.ledger_entry_status for e in result.ledger.entries)
        atoms = tuple(a.technical_atom_kind for a in result.ledger.technical_atoms)
        dispositions = tuple(r.disposition for r in result.document_structure.dispositions)
        return kinds, statuses, atoms, dispositions

    assert shape(a) == shape(b)


def test_quality_report_warns_on_review_and_write_boundary_allows_with_work() -> None:
    result = _build(_MIXED)
    catalog = default_quality_check_catalog()
    severity = default_severity_policy()
    pointer = claim_ledger_pointer("qcc", "fp")  # any pointer for the report header
    report = build_ledger_quality_report(
        result.ledger,
        result.document_structure,
        catalog=catalog,
        severity=severity,
        catalog_pointer=pointer,
    )
    assert report.has_severity("warning")  # the fragment is review work
    assert not report.has_severity("blocking")
    assert page_write_decision(report) == "write-with-review-work"


def test_projection_renders_only_usable_entries_and_no_internal_ids() -> None:
    result = _build(_MIXED)
    support = ProjectionSourceSupport(
        "pss",
        _HASH,
        "src.pdf",
        claim_ledger_pointer("cl", "f"),
        document_structure_pointer("ds", "g"),
    )
    plan = plan_source_page(
        result.ledger,
        result.document_structure,
        wiki_page_locator="src",
        title="Src",
        source_support=support,
    )
    page = render_source_page(plan, result.ledger)
    catalog = default_quality_check_catalog()
    report = build_projection_quality_report(
        plan,
        page.coverage,
        page.page_body,
        result.ledger,
        catalog=catalog,
        severity=default_severity_policy(),
        catalog_pointer=claim_ledger_pointer("qcc", "fp"),
    )
    assert not report.has_severity("blocking")
    for prefix in ("ledger-entry-", "projection-coverage-entry-"):
        assert prefix not in page.page_body
    # Generated page claims select only usable entries.
    usable = {e.ledger_entry_id for e in result.ledger.usable_entries}
    for entry in page.coverage.entries:
        if entry.projection_coverage_unit_kind == "generated-page-claim":
            assert set(entry.selected_ledger_entry_ids) <= usable


def test_portable_artifact_set_excludes_self_and_tracks_membership() -> None:
    members = (
        PortableArtifactMember("claim-ledger-artifact", "cl-1", "f1"),
        PortableArtifactMember("document-structure-artifact", "ds-1", "f2"),
    )
    first = build_portable_artifact_set(members)
    assert all(m.portable_artifact_kind != "portable-artifact-set" for m in first.members)
    extra = (*members, PortableArtifactMember("projection-coverage-artifact", "pc-1", "f3"))
    second = build_portable_artifact_set(extra)
    assert first.portable_artifact_set_fingerprint != second.portable_artifact_set_fingerprint


def test_reading_source_close_text_is_the_source_statement() -> None:
    # The projection cites source-close normalized text, never a broadened paraphrase.
    result = _build(_MIXED)
    claim = next(e for e in result.ledger.usable_entries if "grimoire" in e.normalized_text)
    assert claim.normalized_text == "A grimoire contains many spells."
    assert claim.resolution_basis == "source-close-statement"
