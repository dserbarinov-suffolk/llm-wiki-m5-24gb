---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Latest bounded post-ingest confidence report.
updated: 2026-07-06
---

# Ingest Confidence Report

## Summary

Run id: 2026-07-06-113449
Source: raw/Sword World RPG - Complete Edition.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
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
- Status: pass
- Findings: none
SelectedIneligibleClaims: 0
FalseSourceUncertaintyClaims: 0
SourceFramingBullets: 0
MissingUnitCoverage: 0

### evidence-registry
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 1159
Evidence records: 12262

### evidence-locators
- Kind: deterministic
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: pass
- Findings: none
Locators: 11990
Invalid locators: 0

### claim-support
- Kind: model-assisted
- Scope: raw/Sword World RPG - Complete Edition.pdf
- Status: skipped
- Findings: validation-finding-cd5ef7ea607195c1
ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Findings

- INFO claim-support: ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
