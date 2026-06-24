"""Tests for bounded claim-support audit domain objects."""

from llmwiki.domain.citations import SourceInventory, inspect_citations
from llmwiki.domain.claim_support import (
    ClaimSupportAuditReport,
    ClaimSupportCandidate,
    ClaimSupportFinding,
    ClaimSupportSelection,
    ClaimSupportVerdict,
)
from llmwiki.domain.claim_support_evidence import ClaimSupportEvidenceIndex
from llmwiki.domain.claim_support_selection import select_claim_support_candidates
from llmwiki.domain.evidence_registry import (
    EvidenceRecord,
    EvidenceRegistry,
    SourceRange,
    SourceText,
)
from llmwiki.runtime.ingest_confidence import (
    claim_support_gate_from_audit,
    skipped_claim_support_gate,
)


def test_claim_support_report_renders_scope_findings_and_verdict_totals() -> None:
    candidate = ClaimSupportCandidate(
        candidate_id="claim-support-summary-alpha-1",
        page_id="alpha",
        claim_text="Alpha is supported.",
        page_context="Alpha is supported. (raw/alpha.md)",
        citation_texts=("raw/alpha.md",),
        source_claim_ids=("source-claim-alpha",),
        evidence_ids=("evidence-alpha",),
        evidence_excerpts=("evidence-alpha: Alpha is supported.",),
        candidate_kind="source-summary",
    )
    selection = ClaimSupportSelection(
        candidates=(candidate,),
        blocked_candidates=(),
        deterministic_findings=(
            ClaimSupportFinding(
                finding_id="claim-support-finding-alpha",
                candidate_id=candidate.candidate_id,
                page_id="alpha",
                severity="warning",
                category="locator-mismatch",
                message="Evidence appears near the cited locator.",
                evidence_id="evidence-alpha",
            ),
        ),
        candidate_count=2,
        max_claims=5,
    )
    report = ClaimSupportAuditReport(
        run_id="test-run",
        selection=selection,
        verdicts=(
            ClaimSupportVerdict(
                candidate_id=candidate.candidate_id,
                verdict="too_broad",
                rationale="The claim adds a detail absent from the excerpt.",
                recommended_action="Narrow the claim.",
            ),
        ),
        model_report="Done.",
    )

    rendered = report.render()

    assert "Selected for model judgment: 1" in rendered
    assert "locator-mismatch" in rendered
    assert "- too_broad: 1" in rendered
    assert "Free-form model notes" not in rendered


def test_claim_support_gate_fails_when_selected_candidates_lack_verdicts() -> None:
    selection = ClaimSupportSelection(
        candidates=(
            ClaimSupportCandidate(
                candidate_id="claim-support-summary-alpha-1",
                page_id="alpha",
                claim_text="Alpha is supported.",
                page_context="Alpha is supported. (raw/alpha.md)",
                citation_texts=("raw/alpha.md",),
                source_claim_ids=("source-claim-alpha",),
                evidence_ids=("evidence-alpha",),
                evidence_excerpts=("evidence-alpha: Alpha is supported.",),
            ),
        ),
        blocked_candidates=(),
        deterministic_findings=(),
        candidate_count=1,
        max_claims=1,
    )
    audit = ClaimSupportAuditReport(
        run_id="test-run",
        selection=selection,
        verdicts=(),
        model_report="Done.",
    )

    gate, findings = claim_support_gate_from_audit("alpha.md", audit)

    assert gate.status == "fail"
    assert findings[0].severity == "blocker"
    assert "Missing model verdicts" in findings[0].message


def test_skipped_claim_support_gate_is_visible_but_non_blocking() -> None:
    gate, findings = skipped_claim_support_gate("alpha.md", "Not run during ordinary ingest.")

    assert gate.status == "skipped"
    assert gate.gate_kind == "model-assisted"
    assert findings[0].severity == "info"
    assert "Not run" in gate.detail


def test_citation_parser_accepts_pdf_page_ranges_and_unicode_dashes() -> None:
    inventory = SourceInventory.from_raw_relative_paths(("javascriptallonge.pdf",))
    report = inspect_citations(
        "javascriptallonge-value-types",
        "The source discusses value cups. (raw/javascriptallonge.pdf p.20–22)",
        inventory,
    )

    assert report.findings == ()
    assert report.citations[0].source_path == "raw/javascriptallonge.pdf"
    assert report.citations[0].page_range == (20, 22)


def test_targeted_selection_includes_known_scope_claim_for_model_judgment() -> None:
    registry = _registry_for_value_types(page_range=(20, 22))
    selection = select_claim_support_candidates(
        {
            "javascriptallonge-value-types": _page_text(
                "javascriptallonge-value-types",
                "- Same-type, same-content value cups can still be distinguished. "
                "(raw/javascriptallonge.pdf p.22)",
            ),
            "javascriptallonge-reference-types": _page_text(
                "javascriptallonge-reference-types",
                "- Reference cups can be distinct even with matching contents. "
                "(raw/javascriptallonge.pdf p.24)",
            ),
        },
        SourceInventory.from_raw_relative_paths(("javascriptallonge.pdf",)),
        (registry,),
        max_claims=1,
        source="javascriptallonge.pdf",
        sample_strategy="ordered",
        page_ids=("javascriptallonge-value-types",),
        claim_contains="distinguish",
    )

    assert selection.candidate_count == 1
    assert selection.selected_count == 1
    candidate = selection.candidates[0]
    assert candidate.page_id == "javascriptallonge-value-types"
    assert candidate.candidate_kind == "source-summary"
    assert "same-content value cups" in candidate.claim_text
    assert candidate.evidence_excerpts == (
        "evidence-value-cups: Value cups with the same value are undistinguishable.",
    )


def test_selection_blocks_claim_when_citation_is_outside_planned_source_range() -> None:
    selection = select_claim_support_candidates(
        {
            "javascriptallonge-value-types": _page_text(
                "javascriptallonge-value-types",
                "- Value cups are discussed outside the selected page range. "
                "(raw/javascriptallonge.pdf p.23)",
            )
        },
        SourceInventory.from_raw_relative_paths(("javascriptallonge.pdf",)),
        (_registry_for_value_types(page_range=(20, 22)),),
        max_claims=1,
        source="javascriptallonge.pdf",
        sample_strategy="ordered",
        page_ids=("javascriptallonge-value-types",),
    )

    assert selection.candidates == ()
    assert selection.blocked_candidates[0].page_id == "javascriptallonge-value-types"
    assert {finding.category for finding in selection.deterministic_findings} >= {
        "missing-evidence",
        "source-range",
    }


def test_evidence_excerpts_include_source_order_context_around_strong_match() -> None:
    registry = _registry_with_contextual_claims()
    evidence_ids = tuple(record.evidence_id for record in registry.evidence_records)
    excerpts = ClaimSupportEvidenceIndex((registry,)).excerpts_for_claim(
        evidence_ids,
        "same kind of cup same contents can still distinguish",
        limit=5,
    )

    rendered = "\n".join(excerpts)
    assert "no way to tell the difference" in rendered
    assert "We haven't encountered the fourth possibility yet" in rendered
    assert "serial number on the bottom" in rendered
    assert "you can still distinguish between them" in rendered


def test_selection_blocks_source_summary_claim_that_crosses_scope_shift() -> None:
    selection = select_claim_support_candidates(
        {
            "javascriptallonge-value-types": _page_text(
                "javascriptallonge-value-types",
                "- Even with identical content and type, two cups (values) can still "
                "be distinguished. (raw/javascriptallonge.pdf p.22)",
            )
        },
        SourceInventory.from_raw_relative_paths(("javascriptallonge.pdf",)),
        (_registry_with_contextual_claims(),),
        max_claims=1,
        source="javascriptallonge.pdf",
        sample_strategy="ordered",
        page_ids=("javascriptallonge-value-types",),
    )

    assert selection.candidates == ()
    assert selection.blocked_candidates[0].page_id == "javascriptallonge-value-types"
    assert [finding.category for finding in selection.deterministic_findings] == ["support-verdict"]


def test_selection_blocks_source_scope_shift_with_renamed_fixture_terms() -> None:
    selection = select_claim_support_candidates(
        {
            "field-guide-primary-protocol": _page_text(
                "field-guide-primary-protocol",
                "- The secondary protocol uses archival keys to distinguish duplicate "
                "measurements. (raw/field-guide.pdf p.7)",
            )
        },
        SourceInventory.from_raw_relative_paths(("field-guide.pdf",)),
        (_registry_with_synthetic_scope_context(),),
        max_claims=1,
        source="field-guide.pdf",
        sample_strategy="ordered",
        page_ids=("field-guide-primary-protocol",),
    )

    assert selection.candidates == ()
    assert selection.blocked_candidates[0].page_id == "field-guide-primary-protocol"
    assert [finding.category for finding in selection.deterministic_findings] == [
        "support-verdict"
    ]


def _page_text(page_id: str, bullet: str) -> str:
    return "\n".join(
        (
            "---",
            f"page_id: {page_id}",
            "page_kind: concept",
            "summary: Test page.",
            "---",
            "",
            "## Key supported claims",
            "",
            bullet,
        )
    )


def _registry_for_value_types(page_range: tuple[int, int]) -> EvidenceRegistry:
    return EvidenceRegistry(
        registry_id="evidence-registry-allonge",
        source_texts=(
            SourceText(
                source_locator="javascriptallonge.pdf",
                source_hash="hash",
                source_text_kind="pdf-cache",
                lines=("Value cups with the same value are undistinguishable.",),
            ),
        ),
        source_ranges=(
            SourceRange(
                source_range_id="source-range-javascriptallonge-value-types",
                page_id="javascriptallonge-value-types",
                source_locator="javascriptallonge.pdf",
                page_range=page_range,
                line_range=(1, 1),
                heading_path="Value Types",
            ),
        ),
        evidence_records=(
            EvidenceRecord(
                evidence_id="evidence-value-cups",
                source_locator="javascriptallonge.pdf",
                source_hash="hash",
                source_range_id="source-range-javascriptallonge-value-types",
                line_range=(1, 1),
                excerpt="Value cups with the same value are undistinguishable.",
                excerpt_digest="digest",
                evidence_kind="source-claim",
                source_claim_id="source-claim-value-cups",
            ),
        ),
    )


def _registry_with_contextual_claims() -> EvidenceRegistry:
    source_text = SourceText(
        source_locator="javascriptallonge.pdf",
        source_hash="hash",
        source_text_kind="pdf-cache",
        lines=("value type excerpt",),
    )
    source_range = SourceRange(
        source_range_id="source-range-javascriptallonge-value-types",
        page_id="javascriptallonge-value-types",
        source_locator="javascriptallonge.pdf",
        page_range=(22, 22),
        line_range=(1, 1),
        heading_path="Value Types",
    )
    excerpts = (
        "Third, some types of cups have no distinguishing marks on them.",
        "If they are the same kind of cup, and they hold the same contents, "
        "we have no way to tell the difference between them.",
        "This is the case with the strings, numbers, and booleans we have seen so far.",
        "Strings, numbers, and booleans are examples of value or primitive types.",
        "We'll use both terms interchangeably.",
        "We haven't encountered the fourth possibility yet.",
        "Some types of cups have a serial number on the bottom.",
        "So even if you have two cups of the same type, and their contents are the same, "
        "you can still distinguish between them.",
    )
    return EvidenceRegistry(
        registry_id="evidence-registry-allonge-context",
        source_texts=(source_text,),
        source_ranges=(source_range,),
        evidence_records=tuple(
            EvidenceRecord(
                evidence_id=f"evidence-context-{index:04d}",
                source_locator="javascriptallonge.pdf",
                source_hash="hash",
                source_range_id=source_range.source_range_id,
                line_range=(1, 1),
                excerpt=excerpt,
                excerpt_digest=f"digest-{index}",
                evidence_kind="source-claim",
                source_claim_id=f"source-claim-context-{index:04d}",
            )
            for index, excerpt in enumerate(excerpts, start=1)
        ),
    )


def _registry_with_synthetic_scope_context() -> EvidenceRegistry:
    source_text = SourceText(
        source_locator="field-guide.pdf",
        source_hash="hash",
        source_text_kind="pdf-cache",
        lines=("primary protocol excerpt",),
    )
    source_range = SourceRange(
        source_range_id="source-range-field-guide-primary-protocol",
        page_id="field-guide-primary-protocol",
        source_locator="field-guide.pdf",
        page_range=(7, 7),
        line_range=(1, 1),
        heading_path="Primary Protocol",
    )
    excerpts = (
        "The primary protocol normalizes sensor readings before storage.",
        "It keeps stable measurements in the active buffer.",
        "We have not introduced the secondary protocol yet.",
        "The secondary protocol uses archival keys to distinguish duplicate measurements.",
    )
    return EvidenceRegistry(
        registry_id="evidence-registry-field-guide-context",
        source_texts=(source_text,),
        source_ranges=(source_range,),
        evidence_records=tuple(
            EvidenceRecord(
                evidence_id=f"evidence-field-guide-context-{index:04d}",
                source_locator="field-guide.pdf",
                source_hash="hash",
                source_range_id=source_range.source_range_id,
                line_range=(1, 1),
                excerpt=excerpt,
                excerpt_digest=f"digest-{index}",
                evidence_kind="source-claim",
                source_claim_id=f"source-claim-field-guide-context-{index:04d}",
            )
            for index, excerpt in enumerate(excerpts, start=1)
        ),
    )
