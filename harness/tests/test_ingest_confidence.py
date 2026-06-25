"""Tests for source-level ingest confidence domain objects."""

from llmwiki.domain.ingest_confidence import (
    ArtifactFingerprint,
    ArtifactReuseDecision,
    IngestConfidenceGate,
    IngestConfidenceReport,
    decide_artifact_reuse,
    validation_finding,
)
from llmwiki.domain.objects import PageBodyContract, Schema


def test_artifact_fingerprint_tracks_schema_contracts() -> None:
    baseline = ArtifactFingerprint.from_schema(
        source_locator="alpha.md",
        source_hash="hash-alpha",
        schema=Schema(),
    )
    changed = ArtifactFingerprint.from_schema(
        source_locator="alpha.md",
        source_hash="hash-alpha",
        schema=Schema(
            page_body_contracts=(
                PageBodyContract(
                    contract_id="source-summary",
                    match_page_kinds=("source",),
                    max_words=120,
                ),
            )
        ),
    )

    assert baseline.digest == ArtifactFingerprint.from_json_text(baseline.to_json_text()).digest
    assert baseline.page_body_contract_digest != changed.page_body_contract_digest


def test_artifact_reuse_requires_matching_fingerprint() -> None:
    current = _fingerprint("hash-alpha")

    assert (
        decide_artifact_reuse(
            artifact_kind="page-plan",
            artifact_path="cache/page-plan.json",
            current=current,
            stored=_fingerprint("hash-alpha"),
            artifact_exists=True,
        ).decision
        == "reuse"
    )
    assert (
        decide_artifact_reuse(
            artifact_kind="page-plan",
            artifact_path="cache/page-plan.json",
            current=current,
            stored=_fingerprint("stale-hash"),
            artifact_exists=True,
        ).decision
        == "rebuild"
    )
    assert (
        decide_artifact_reuse(
            artifact_kind="page-plan",
            artifact_path="cache/page-plan.json",
            current=current,
            stored=current,
            artifact_exists=False,
        ).decision
        == "missing"
    )
    assert (
        decide_artifact_reuse(
            artifact_kind="page-plan",
            artifact_path="cache/page-plan.json",
            current=current,
            stored=current,
            artifact_exists=True,
            fresh=True,
        ).decision
        == "rebuild"
    )


def test_report_rendering_keeps_skipped_gate_visible() -> None:
    finding = validation_finding(
        severity="info",
        category="claim-support",
        source_locator="alpha.md",
        message="Skipped because there are no candidates.",
    )
    report = IngestConfidenceReport(
        run_id="test-run",
        source_locator="alpha.md",
        artifact_decisions=(
            ArtifactReuseDecision(
                "page-plan",
                "cache/page-plan.json",
                "reuse",
                "fingerprint matches",
                "abc123",
            ),
        ),
        gates=(
            IngestConfidenceGate(
                "claim-support",
                "model-assisted",
                "raw/alpha.md",
                "skipped",
                (finding.finding_id,),
                finding.message,
            ),
        ),
        findings=(finding,),
    )

    rendered = report.render()

    assert "Confidence status: passed" in rendered
    assert "### claim-support" in rendered
    assert "Status: skipped" in rendered
    assert "Skipped because there are no candidates." in rendered


def _fingerprint(source_hash: str) -> ArtifactFingerprint:
    return ArtifactFingerprint.from_schema(
        source_locator="alpha.md",
        source_hash=source_hash,
        schema=Schema(),
    )
