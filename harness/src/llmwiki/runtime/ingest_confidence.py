"""Post-ingest confidence artifact assembly.

This module is an adapter layer: it arranges store writes around pure domain
objects but does not ask the model to judge content.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass

from llmwiki.domain.claim_support import ClaimSupportAuditReport
from llmwiki.domain.evidence_locator_builder import build_evidence_locator_index
from llmwiki.domain.evidence_locator_index import EvidenceLocatorIndex
from llmwiki.domain.evidence_locator_index_io import evidence_locator_index_to_json
from llmwiki.domain.evidence_registry import (
    EvidenceRegistry,
    SourceText,
    build_evidence_registry,
)
from llmwiki.domain.evidence_registry_io import registry_to_json
from llmwiki.domain.ingest_confidence import (
    ArtifactFingerprint,
    IngestConfidenceGate,
    IngestConfidenceReport,
    ValidationFinding,
    decide_artifact_reuse,
    gate_status,
    validation_finding,
)
from llmwiki.domain.objects import PagePlan, Schema
from llmwiki.domain.pages import PageMetadata, WikiPage
from llmwiki.domain.planning import (
    observation_report,
    page_plan_to_json,
    source_summary_quality_report,
)
from llmwiki.store import WikiStore

INGEST_CONFIDENCE_PAGE = "wiki-ingest-confidence"


@dataclass(frozen=True)
class PostIngestConfidenceArtifacts:
    report: IngestConfidenceReport
    evidence_registry: EvidenceRegistry
    evidence_locator_index: EvidenceLocatorIndex


def record_post_ingest_confidence(
    *,
    store: WikiStore,
    today: str,
    run_id: str,
    source_locator: str,
    page_plan: PagePlan,
    source_text: SourceText,
) -> PostIngestConfidenceArtifacts:
    fingerprint = ArtifactFingerprint.from_schema(
        source_locator=source_locator,
        source_hash=_raw_source_hash(store, source_locator),
        schema=Schema(),
    )
    stored = _stored_fingerprint(store, source_locator)
    artifact_dir = store.page_plan_artifact_dir(source_locator)
    decisions = (
        decide_artifact_reuse(
            artifact_kind="page-plan",
            artifact_path=str(artifact_dir / "page-plan.json"),
            current=fingerprint,
            stored=stored,
            artifact_exists=(artifact_dir / "page-plan.json").is_file(),
        ),
        decide_artifact_reuse(
            artifact_kind="evidence-registry",
            artifact_path=str(artifact_dir / "evidence-registry.json"),
            current=fingerprint,
            stored=stored,
            artifact_exists=(artifact_dir / "evidence-registry.json").is_file(),
        ),
        decide_artifact_reuse(
            artifact_kind="evidence-locators",
            artifact_path=str(artifact_dir / "evidence-locators.json"),
            current=fingerprint,
            stored=stored,
            artifact_exists=(artifact_dir / "evidence-locators.json").is_file(),
        ),
    )
    registry = build_evidence_registry(page_plan, (source_text,))
    locator_index = build_evidence_locator_index(registry)
    scoped_pages = _planned_page_texts(store, page_plan)
    claim_support_gate, claim_support_findings = skipped_claim_support_gate(
        source_locator,
        "ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.",
    )
    deterministic_findings = (
        *_page_plan_findings(source_locator, page_plan),
        *_source_summary_findings(source_locator, page_plan, scoped_pages),
        *_registry_findings(source_locator, registry),
        *_locator_findings(source_locator, locator_index),
    )
    findings = (*deterministic_findings, *claim_support_findings)
    gates = (
        _gate("page-plan", "deterministic", source_locator, deterministic_findings, "planning"),
        _gate(
            "source-summary-quality",
            "deterministic",
            source_locator,
            deterministic_findings,
            "source-summary",
            detail=source_summary_quality_report(page_plan, scoped_pages).render(),
        ),
        _gate(
            "evidence-registry",
            "deterministic",
            source_locator,
            deterministic_findings,
            "evidence",
            detail=(
                f"Source texts: {len(registry.source_texts)}\n"
                f"Source ranges: {len(registry.source_ranges)}\n"
                f"Evidence records: {len(registry.evidence_records)}"
            ),
        ),
        _gate(
            "evidence-locators",
            "deterministic",
            source_locator,
            deterministic_findings,
            "locator",
            detail=(
                f"Locators: {len(locator_index.locators)}\n"
                f"Invalid locators: {locator_index.invalid_count}"
            ),
        ),
        claim_support_gate,
    )
    report = IngestConfidenceReport(
        run_id=run_id,
        source_locator=source_locator,
        artifact_decisions=decisions,
        gates=gates,
        findings=findings,
    )
    _write_artifacts(store, source_locator, page_plan, registry, locator_index, fingerprint, report)
    _file_report_page(store, today, report)
    return PostIngestConfidenceArtifacts(report, registry, locator_index)


def skipped_claim_support_gate(
    source_locator: str, reason: str
) -> tuple[IngestConfidenceGate, tuple[ValidationFinding, ...]]:
    finding = validation_finding(
        severity="info",
        category="claim-support",
        source_locator=source_locator,
        message=reason,
    )
    return (
        IngestConfidenceGate(
            gate_id="claim-support",
            gate_kind="model-assisted",
            scope=f"raw/{source_locator}",
            status="skipped",
            finding_ids=(finding.finding_id,),
            detail=reason,
        ),
        (finding,),
    )


def claim_support_gate_from_audit(
    source_locator: str, audit: ClaimSupportAuditReport
) -> tuple[IngestConfidenceGate, tuple[ValidationFinding, ...]]:
    findings = _claim_support_findings(source_locator, audit)
    gate = IngestConfidenceGate(
        gate_id="claim-support",
        gate_kind="model-assisted",
        scope=f"raw/{source_locator}",
        status=gate_status(findings),
        finding_ids=tuple(finding.finding_id for finding in findings),
        detail=_claim_support_detail(audit),
    )
    return gate, findings


def _stored_fingerprint(store: WikiStore, source_locator: str) -> ArtifactFingerprint | None:
    text = store.read_artifact_fingerprint(source_locator)
    if text is None:
        return None
    try:
        return ArtifactFingerprint.from_json_text(text)
    except (KeyError, TypeError, ValueError):
        return None


def _raw_source_hash(store: WikiStore, source_locator: str) -> str:
    return hashlib.sha256(store.raw_source_path(source_locator).read_bytes()).hexdigest()


def _planned_page_texts(store: WikiStore, page_plan: PagePlan) -> dict[str, str]:
    result: dict[str, str] = {}
    for write in page_plan.planned_writes:
        page_id = write.page_metadata.page_id
        if page_id in store.list_pages():
            result[page_id] = store.read_page(page_id)
    return result


def _page_plan_findings(source_locator: str, page_plan: PagePlan) -> tuple[ValidationFinding, ...]:
    if page_plan.planned_writes:
        return ()
    return (
        validation_finding(
            severity="blocker",
            category="planning",
            source_locator=source_locator,
            message="PagePlan has no PlannedPageWrite records.",
        ),
    )


def _source_summary_findings(
    source_locator: str, page_plan: PagePlan, scoped_pages: dict[str, str]
) -> tuple[ValidationFinding, ...]:
    report = source_summary_quality_report(page_plan, scoped_pages)
    checks = (
        ("selected_ineligible_claims", "Selected source-summary claims include ineligible claims."),
        (
            "false_source_uncertainty_claims",
            "Source-summary claims mark uncertainty without source-uncertainty evidence.",
        ),
        ("source_framing_bullets", "Source-summary bullets use source-framing prose."),
        ("missing_unit_coverage", "Source-summary plans omit covered source units."),
    )
    findings: list[ValidationFinding] = []
    for attr, message in checks:
        count = int(getattr(report, attr))
        if count:
            findings.append(
                validation_finding(
                    severity="warning",
                    category="source-summary",
                    source_locator=source_locator,
                    message=f"{message} Count: {count}.",
                )
            )
    return tuple(findings)


def _registry_findings(
    source_locator: str, registry: EvidenceRegistry
) -> tuple[ValidationFinding, ...]:
    findings: list[ValidationFinding] = []
    if not registry.source_texts:
        findings.append(
            validation_finding(
                severity="blocker",
                category="evidence",
                source_locator=source_locator,
                message="EvidenceRegistry has no SourceText.",
            )
        )
    if not registry.evidence_records:
        findings.append(
            validation_finding(
                severity="warning",
                category="evidence",
                source_locator=source_locator,
                message="EvidenceRegistry has no EvidenceRecord entries.",
            )
        )
    return tuple(findings)


def _locator_findings(
    source_locator: str, locator_index: EvidenceLocatorIndex
) -> tuple[ValidationFinding, ...]:
    return tuple(
        validation_finding(
            severity=finding.severity,
            category="locator",
            source_locator=source_locator,
            message=f"{finding.category}: {finding.message}",
            fingerprint=finding.finding_id,
        )
        for finding in locator_index.findings
    )


def _claim_support_findings(
    source_locator: str, audit: ClaimSupportAuditReport
) -> tuple[ValidationFinding, ...]:
    findings: list[ValidationFinding] = []
    if audit.missing_verdict_candidate_ids:
        missing = ", ".join(audit.missing_verdict_candidate_ids[:5])
        omitted = len(audit.missing_verdict_candidate_ids) - 5
        if omitted > 0:
            missing = f"{missing} ({omitted} more)"
        findings.append(
            validation_finding(
                severity="blocker",
                category="claim-support",
                source_locator=source_locator,
                message=(
                    f"Missing model verdicts for selected claim-support candidates: {missing}."
                ),
                fingerprint="missing-claim-support-verdicts",
            )
        )
    for finding in audit.selection.deterministic_findings:
        findings.append(
            validation_finding(
                severity=finding.severity,
                category="claim-support",
                source_locator=source_locator,
                page_id=finding.page_id,
                message=f"{finding.category}: {finding.message}",
                fingerprint=finding.finding_id,
            )
        )
    for verdict in audit.verdicts:
        candidate = _candidate_page(audit, verdict.candidate_id)
        findings.append(
            validation_finding(
                severity=verdict.severity,
                category="claim-support",
                source_locator=source_locator,
                page_id=candidate,
                message=f"{verdict.verdict}: {verdict.rationale}",
                fingerprint=verdict.candidate_id,
            )
        )
    return tuple(findings)


def _claim_support_detail(audit: ClaimSupportAuditReport) -> str:
    coverage = audit.selection.sample_coverage
    coverage_detail = coverage.render() if coverage is not None else "No sample coverage report."
    return (
        f"Claim candidates discovered: {audit.selection.candidate_count}\n"
        f"Selected for model judgment: {audit.selection.selected_count}\n"
        f"Skipped by deterministic findings: {audit.selection.deterministic_skipped_count}\n"
        f"Skipped by cap: {audit.selection.skipped_count}\n"
        f"Verdicts recorded: {len(audit.verdicts)}\n"
        f"{coverage_detail}"
    )


def _candidate_page(audit: ClaimSupportAuditReport, candidate_id: str) -> str:
    candidates = (*audit.selection.candidates, *audit.selection.blocked_candidates)
    for candidate in candidates:
        if candidate.candidate_id == candidate_id:
            return candidate.page_id
    return ""


def _gate(
    gate_id: str,
    gate_kind: str,
    source_locator: str,
    all_findings: tuple[ValidationFinding, ...],
    category: str,
    detail: str = "",
) -> IngestConfidenceGate:
    findings = tuple(finding for finding in all_findings if finding.category == category)
    return IngestConfidenceGate(
        gate_id=gate_id,
        gate_kind=gate_kind,  # type: ignore[arg-type]
        scope=f"raw/{source_locator}",
        status=gate_status(findings),
        finding_ids=tuple(finding.finding_id for finding in findings),
        detail=detail,
    )


def _write_artifacts(
    store: WikiStore,
    source_locator: str,
    page_plan: PagePlan,
    registry: EvidenceRegistry,
    locator_index: EvidenceLocatorIndex,
    fingerprint: ArtifactFingerprint,
    report: IngestConfidenceReport,
) -> None:
    store.write_page_plan_artifacts(
        source_locator,
        page_plan_to_json(page_plan),
        observation_report(page_plan),
    )
    store.write_evidence_registry_artifact(source_locator, registry_to_json(registry))
    store.write_evidence_locator_index_artifact(
        source_locator, evidence_locator_index_to_json(locator_index)
    )
    store.write_artifact_fingerprint(source_locator, fingerprint.to_json_text())
    store.write_ingest_confidence_report_artifact(source_locator, report.render())


def _file_report_page(store: WikiStore, today: str, report: IngestConfidenceReport) -> None:
    store.write_page(
        WikiPage.from_metadata(
            PageMetadata(
                page_id=INGEST_CONFIDENCE_PAGE,
                page_kind="synthesis",
                summary="Latest bounded post-ingest confidence report.",
                sources=(),
                updated=today,
            ),
            report.render(),
        )
    )
