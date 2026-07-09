---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Latest bounded post-ingest confidence report.
updated: 2026-07-09
---

# Ingest Confidence Report

## Summary

Run id: 2026-07-09-105809
Source: raw/Sword World RPG - Complete Edition.pdf
Confidence status: passed with warnings
Blockers: 0
Warnings: 1
Gates: 5

## Artifact Reuse

- page-plan: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/page-plan.json` (fingerprint matches; fingerprint 490351c8bcdb3913)
- evidence-registry: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/evidence-registry.json` (fingerprint matches; fingerprint 490351c8bcdb3913)
- evidence-locators: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/sword-world-rpg-complete-edition-8e67d04d99d8/evidence-locators.json` (fingerprint matches; fingerprint 490351c8bcdb3913)

## Gates

### page-plan
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none

### source-summary-quality
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: fail
- Findings: validation-finding-f32f9db9f342bab7
SelectedIneligibleClaims: 0
FalseSourceUncertaintyClaims: 0
SourceFramingBullets: 0
MissingUnitCoverage: 1
MissingUnitCoverageExamples:
- sword-world-rpg-complete-edition-2-5-difficulty-checks-through-2-5-1-2-5-3-analogy-of-success: unit-0064

### evidence-registry
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 276
Evidence records: 12346

### evidence-locators
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none
Locators: 11891
Invalid locators: 0

### claim-support
- Kind: model-assisted
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: skipped
- Findings: validation-finding-cd5ef7ea607195c1
ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Findings

- WARNING source-summary: Source-summary plans omit covered source units. Count: 1.
- INFO claim-support: ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
