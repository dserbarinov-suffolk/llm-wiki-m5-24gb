---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Latest bounded post-ingest confidence report.
updated: 2026-07-08
---

# Ingest Confidence Report

## Summary

Run id: 2026-07-08-065958
Source: raw/antikythera-mechanism.md
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 5

## Artifact Reuse

- page-plan: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/antikythera-mechanism-6b8d9991ac96/page-plan.json` (fingerprint matches; fingerprint ec3a52a50c773dc2)
- evidence-registry: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/antikythera-mechanism-6b8d9991ac96/evidence-registry.json` (fingerprint matches; fingerprint ec3a52a50c773dc2)
- evidence-locators: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/antikythera-mechanism-6b8d9991ac96/evidence-locators.json` (fingerprint matches; fingerprint ec3a52a50c773dc2)

## Gates

### page-plan
- Kind: deterministic
- Scope: raw/antikythera-mechanism.md
- Status: pass
- Findings: none

### source-summary-quality
- Kind: deterministic
- Scope: raw/antikythera-mechanism.md
- Status: pass
- Findings: none
SelectedIneligibleClaims: 0
FalseSourceUncertaintyClaims: 0
SourceFramingBullets: 0
MissingUnitCoverage: 0

### evidence-registry
- Kind: deterministic
- Scope: raw/antikythera-mechanism.md
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 2
Evidence records: 10

### evidence-locators
- Kind: deterministic
- Scope: raw/antikythera-mechanism.md
- Status: pass
- Findings: none
Locators: 10
Invalid locators: 0

### claim-support
- Kind: model-assisted
- Scope: raw/antikythera-mechanism.md
- Status: skipped
- Findings: validation-finding-469583d66a49e774
ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Findings

- INFO claim-support: ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
