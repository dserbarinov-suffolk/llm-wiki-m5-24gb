---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Latest bounded post-ingest confidence report.
updated: 2026-06-24
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-24-150033
Source: raw/nennius_giles.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 5

## Artifact Reuse

- page-plan: missing `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/nennius-giles-85c1a0dfadb7/page-plan.json` (artifact is missing; fingerprint f0b9877822d57d0b)
- evidence-registry: missing `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/nennius-giles-85c1a0dfadb7/evidence-registry.json` (artifact is missing; fingerprint f0b9877822d57d0b)
- evidence-locators: missing `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/nennius-giles-85c1a0dfadb7/evidence-locators.json` (artifact is missing; fingerprint f0b9877822d57d0b)

## Gates

### page-plan
- Kind: deterministic
- Scope: raw/nennius_giles.pdf
- Status: pass
- Findings: none

### source-summary-quality
- Kind: deterministic
- Scope: raw/nennius_giles.pdf
- Status: pass
- Findings: none
SelectedIneligibleClaims: 0
FalseSourceUncertaintyClaims: 0
SourceFramingBullets: 0
MissingUnitCoverage: 0

### evidence-registry
- Kind: deterministic
- Scope: raw/nennius_giles.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 13
Evidence records: 575

### evidence-locators
- Kind: deterministic
- Scope: raw/nennius_giles.pdf
- Status: pass
- Findings: none
Locators: 575
Invalid locators: 0

### claim-support
- Kind: model-assisted
- Scope: raw/nennius_giles.pdf
- Status: skipped
- Findings: validation-finding-36def439905ccc18
ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Findings

- INFO claim-support: ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
