"""Claim-ledger ingest pipeline (adapter/orchestrator).

Wires deterministic extraction artifacts into the pure claim-ledger domain:
segment chunks, build the document structure and claim ledger, run the
ledger-build and page-projection quality reports, render the source page as a
projection of the ledger, assemble the portable artifacts and manifest, and
apply the write boundary. No model is called: a source page is a projection of
its ledger, not an independent summary.
"""

from __future__ import annotations

from dataclasses import dataclass

from llmwiki.domain.ledger.artifacts import (
    BlockedWriteDiagnosticArtifact,
    PortableArtifactMember,
    PortableArtifactSet,
    ProjectionCoverageArtifact,
    build_blocked_write_diagnostic_artifact,
    build_claim_ledger_artifact,
    build_document_structure_artifact,
    build_ledger_quality_report_artifact,
    build_portable_artifact_set,
    build_projection_coverage_artifact,
    build_quality_check_catalog_artifact,
)
from llmwiki.domain.ledger.builder import build_claim_ledger, default_schema_bundle
from llmwiki.domain.ledger.canonical import canonical_json, deterministic_id
from llmwiki.domain.ledger.ledger import ClaimLedger
from llmwiki.domain.ledger.pointers import (
    claim_ledger_pointer,
    document_structure_pointer,
    ledger_quality_report_pointer,
    quality_check_catalog_pointer,
)
from llmwiki.domain.ledger.projection import ProjectionSourceSupport, plan_source_page
from llmwiki.domain.ledger.quality import (
    LedgerQualityReport,
    build_ledger_quality_report,
    build_projection_quality_report,
    page_write_decision,
)
from llmwiki.domain.ledger.quality_catalog import (
    default_quality_check_catalog,
    default_reason_applicability_policy,
    default_severity_policy,
)
from llmwiki.domain.ledger.renderer import render_source_page
from llmwiki.domain.ledger.structure import DocumentStructure
from llmwiki.domain.objects import Schema
from llmwiki.domain.pages import PageMetadata, WikiPage, slugify
from llmwiki.runtime.ledger_segmentation import ChunkText, segment_chunks


@dataclass(frozen=True)
class SourceLedgerResult:
    page_id: str
    wiki_page: WikiPage | None
    page_write_decision: str
    ledger_report: LedgerQualityReport
    projection_report: LedgerQualityReport
    blocked_write_diagnostic: BlockedWriteDiagnosticArtifact | None
    artifact_files: dict[str, str]
    portable_artifact_set: PortableArtifactSet
    summary: str


def build_source_ledger(
    *,
    source_locator: str,
    source_hash: str,
    evidence_registry_hash: str,
    chunks: tuple[ChunkText, ...],
    today: str,
    schema: Schema | None = None,
) -> SourceLedgerResult:
    resolved_schema = schema or Schema()
    bundle = default_schema_bundle()
    inputs, profiles = segment_chunks(
        chunks, source_locator=source_locator, source_hash=source_hash, schema=resolved_schema
    )
    built = build_claim_ledger(
        source_locator=source_locator,
        source_hash=source_hash,
        evidence_registry_hash=evidence_registry_hash,
        segments=inputs,
        profiles=profiles,
        schema=bundle,
    )
    ledger, structure = built.ledger, built.document_structure

    catalog = default_quality_check_catalog()
    applicability = default_reason_applicability_policy()
    severity = default_severity_policy()
    catalog_artifact = build_quality_check_catalog_artifact(catalog, applicability, severity)
    catalog_pointer = quality_check_catalog_pointer(
        catalog_artifact.quality_check_catalog_artifact_id,
        catalog_artifact.quality_check_catalog_fingerprint,
    )

    ledger_report = build_ledger_quality_report(
        ledger, structure, catalog=catalog, severity=severity, catalog_pointer=catalog_pointer
    )
    ledger_report_artifact = build_ledger_quality_report_artifact(ledger_report)
    ds_artifact = build_document_structure_artifact(structure, source_hash)
    ds_pointer = document_structure_pointer(
        ds_artifact.document_structure_artifact_id, ds_artifact.document_structure_fingerprint
    )
    ledger_artifact = build_claim_ledger_artifact(
        ledger,
        ds_pointer,
        ledger_quality_report_pointer(
            ledger_report_artifact.ledger_quality_report_artifact_id,
            ledger_report_artifact.ledger_quality_report_fingerprint,
        ),
    )

    page_id = slugify(source_locator.rsplit(".", 1)[0])
    title = _title(source_locator, structure)
    support = ProjectionSourceSupport(
        projection_source_support_id=deterministic_id(
            "projection-source-support", source_hash, ledger_artifact.claim_ledger_id
        ),
        source_hash=source_hash,
        source_locator=source_locator,
        claim_ledger_pointer=claim_ledger_pointer(
            ledger_artifact.claim_ledger_id, ledger_artifact.claim_ledger_fingerprint
        ),
        document_structure_pointer=ds_pointer,
    )
    plan = plan_source_page(
        ledger, structure, wiki_page_locator=page_id, title=title, source_support=support
    )
    rendered = render_source_page(plan, ledger)

    projection_report = build_projection_quality_report(
        plan,
        rendered.coverage,
        rendered.page_body,
        ledger,
        catalog=catalog,
        severity=severity,
        catalog_pointer=catalog_pointer,
    )
    projection_report_artifact = build_ledger_quality_report_artifact(projection_report)
    coverage_artifact = build_projection_coverage_artifact(
        wiki_page_locator=page_id,
        page_body_hash=rendered.page_body_hash,
        support_set=(support,),
        coverage=rendered.coverage,
        ledger_quality_report_pointer=ledger_quality_report_pointer(
            projection_report_artifact.ledger_quality_report_artifact_id,
            projection_report_artifact.ledger_quality_report_fingerprint,
        ),
    )

    decision = page_write_decision(ledger_report, projection_report)
    summary = _summary(ledger, decision)
    blocked = None
    wiki_page: WikiPage | None = None
    if decision == "block-authoritative-write":
        blocked = build_blocked_write_diagnostic_artifact(
            wiki_page_locator=page_id,
            claim_ledger_pointer=support.claim_ledger_pointer,
            ledger_quality_report_pointer=ledger_quality_report_pointer(
                projection_report_artifact.ledger_quality_report_artifact_id,
                projection_report_artifact.ledger_quality_report_fingerprint,
            ),
        )
    else:
        wiki_page = _wiki_page(
            page_id, source_locator, title, summary, today, rendered.page_body, coverage_artifact
        )

    members = [
        _member(
            "document-structure-artifact",
            ds_artifact.document_structure_artifact_id,
            ds_artifact.document_structure_fingerprint,
        ),
        _member(
            "claim-ledger-artifact",
            ledger_artifact.claim_ledger_id,
            ledger_artifact.claim_ledger_fingerprint,
        ),
        _member(
            "quality-check-catalog-artifact",
            catalog_artifact.quality_check_catalog_artifact_id,
            catalog_artifact.quality_check_catalog_fingerprint,
        ),
        _member(
            "ledger-quality-report-artifact",
            ledger_report_artifact.ledger_quality_report_artifact_id,
            ledger_report_artifact.ledger_quality_report_fingerprint,
        ),
        _member(
            "ledger-quality-report-artifact",
            projection_report_artifact.ledger_quality_report_artifact_id,
            projection_report_artifact.ledger_quality_report_fingerprint,
        ),
        _member(
            "projection-coverage-artifact",
            coverage_artifact.projection_coverage_artifact_id,
            coverage_artifact.projection_coverage_fingerprint,
        ),
    ]
    artifact_files = {
        "document-structure.json": canonical_json(ds_artifact, indent=2),
        "claim-ledger.json": canonical_json(ledger_artifact, indent=2),
        "quality-check-catalog.json": canonical_json(catalog_artifact, indent=2),
        "ledger-quality-report.json": canonical_json(ledger_report_artifact, indent=2),
        "projection-quality-report.json": canonical_json(projection_report_artifact, indent=2),
        "projection-coverage.json": canonical_json(coverage_artifact, indent=2),
    }
    if blocked is not None:
        members.append(
            _member(
                "blocked-write-diagnostic-artifact",
                blocked.blocked_write_diagnostic_artifact_id,
                blocked.blocked_write_diagnostic_fingerprint,
            )
        )
        artifact_files["blocked-write-diagnostic.json"] = canonical_json(blocked, indent=2)
    manifest = build_portable_artifact_set(tuple(members))
    artifact_files["portable-artifact-set.json"] = canonical_json(manifest, indent=2)

    return SourceLedgerResult(
        page_id=page_id,
        wiki_page=wiki_page,
        page_write_decision=decision,
        ledger_report=ledger_report,
        projection_report=projection_report,
        blocked_write_diagnostic=blocked,
        artifact_files=artifact_files,
        portable_artifact_set=manifest,
        summary=summary,
    )


def _wiki_page(
    page_id: str,
    source_locator: str,
    title: str,
    summary: str,
    today: str,
    page_body: str,
    coverage_artifact: ProjectionCoverageArtifact,
) -> WikiPage:
    pointer = (
        f"{coverage_artifact.projection_coverage_artifact_id}"
        f"@{coverage_artifact.projection_coverage_fingerprint}"
    )
    metadata = PageMetadata(
        page_id=page_id,
        page_kind="source",
        summary=summary,
        sources=(f"raw/{source_locator}",),
        updated=today,
        domain=page_id,
        category_path="sources",
        source_id=source_locator,
        projection_coverage_pointer=pointer,
    )
    return WikiPage.from_metadata(metadata, page_body)


def _member(kind: str, target_id: str, fingerprint: str) -> PortableArtifactMember:
    return PortableArtifactMember(kind, target_id, fingerprint)


def _title(source_locator: str, structure: DocumentStructure) -> str:
    for node in structure.structure_nodes:
        if node.structure_node_kind == "chapter" and node.heading_text.strip():
            return node.heading_text.strip()
    stem = source_locator.rsplit(".", 1)[0].replace("_", " ").replace("-", " ")
    return stem.title()


def _summary(ledger: ClaimLedger, decision: str) -> str:
    usable = len(ledger.usable_entries)
    atoms = len(ledger.technical_atoms)
    review = len(ledger.needs_review_entries)
    label = ledger.source_family_assignment.top_label
    return (
        f"Claim-ledger projection ({label}): {usable} usable entries, {atoms} technical atoms, "
        f"{review} needs-review; write decision {decision}."
    )
