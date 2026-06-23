"""Tests for bounded claim-support audit domain objects."""

from llmwiki.domain.claim_support import (
    ClaimSupportAuditReport,
    ClaimSupportCandidate,
    ClaimSupportFinding,
    ClaimSupportSelection,
    ClaimSupportVerdict,
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
