---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Latest bounded post-ingest confidence report.
updated: 2026-06-29
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-29-114130
Source: raw/rpg_cairn_2e_core.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 5

## Artifact Reuse

- page-plan: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/rpg-cairn-2e-core-fa06f8c4cd9f/page-plan.json` (fingerprint matches; fingerprint 396e49d6012d7aaf)
- evidence-registry: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/rpg-cairn-2e-core-fa06f8c4cd9f/evidence-registry.json` (fingerprint matches; fingerprint 396e49d6012d7aaf)
- evidence-locators: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/rpg-cairn-2e-core-fa06f8c4cd9f/evidence-locators.json` (fingerprint matches; fingerprint 396e49d6012d7aaf)

## Gates

### page-plan
- Kind: deterministic
- Scope: raw/rpg_cairn_2e_core.pdf
- Status: pass
- Findings: none

### source-summary-quality
- Kind: deterministic
- Scope: raw/rpg_cairn_2e_core.pdf
- Status: pass
- Findings: none
SelectedIneligibleClaims: 0
FalseSourceUncertaintyClaims: 0
SourceFramingBullets: 0
MissingUnitCoverage: 0

### evidence-registry
- Kind: deterministic
- Scope: raw/rpg_cairn_2e_core.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 65
Evidence records: 1595

### evidence-locators
- Kind: deterministic
- Scope: raw/rpg_cairn_2e_core.pdf
- Status: pass
- Findings: none
Locators: 1453
Invalid locators: 0

### claim-support
- Kind: model-assisted
- Scope: raw/rpg_cairn_2e_core.pdf
- Status: skipped
- Findings: validation-finding-75225c0631fce33b
ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Findings

- INFO claim-support: ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
