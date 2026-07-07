---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Latest bounded post-ingest confidence report.
updated: 2026-07-07
---

# Ingest Confidence Report

## Summary

Run id: 2026-07-07-104627
Source: raw/javascriptallonge.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 5

## Artifact Reuse

- page-plan: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/javascriptallonge-5873116c6496/page-plan.json` (fingerprint matches; fingerprint ec686518dd5aa1f9)
- evidence-registry: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/javascriptallonge-5873116c6496/evidence-registry.json` (fingerprint matches; fingerprint ec686518dd5aa1f9)
- evidence-locators: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/javascriptallonge-5873116c6496/evidence-locators.json` (fingerprint matches; fingerprint ec686518dd5aa1f9)

## Gates

### page-plan
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none

### source-summary-quality
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none
SelectedIneligibleClaims: 0
FalseSourceUncertaintyClaims: 0
SourceFramingBullets: 0
MissingUnitCoverage: 0

### evidence-registry
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 170
Evidence records: 3059

### evidence-locators
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none
Locators: 3031
Invalid locators: 0

### claim-support
- Kind: model-assisted
- Scope: raw/javascriptallonge.pdf
- Status: skipped
- Findings: validation-finding-cf596b10e496becb
ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Findings

- INFO claim-support: ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
