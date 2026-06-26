---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Latest bounded post-ingest confidence report.
updated: 2026-06-26
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-26-142028
Source: raw/history_short_history_of_england.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 5

## Artifact Reuse

- page-plan: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/history-short-history-of-england-204daea7b552/page-plan.json` (fingerprint matches; fingerprint fa5f1b46a0257bee)
- evidence-registry: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/history-short-history-of-england-204daea7b552/evidence-registry.json` (fingerprint matches; fingerprint fa5f1b46a0257bee)
- evidence-locators: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/history-short-history-of-england-204daea7b552/evidence-locators.json` (fingerprint matches; fingerprint fa5f1b46a0257bee)

## Gates

### page-plan
- Kind: deterministic
- Scope: raw/history_short_history_of_england.pdf
- Status: pass
- Findings: none

### source-summary-quality
- Kind: deterministic
- Scope: raw/history_short_history_of_england.pdf
- Status: pass
- Findings: none
SelectedIneligibleClaims: 0
FalseSourceUncertaintyClaims: 0
SourceFramingBullets: 0
MissingUnitCoverage: 0

### evidence-registry
- Kind: deterministic
- Scope: raw/history_short_history_of_england.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 43
Evidence records: 2476

### evidence-locators
- Kind: deterministic
- Scope: raw/history_short_history_of_england.pdf
- Status: pass
- Findings: none
Locators: 2476
Invalid locators: 0

### claim-support
- Kind: model-assisted
- Scope: raw/history_short_history_of_england.pdf
- Status: skipped
- Findings: validation-finding-af35a6d9a5be5899
ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Findings

- INFO claim-support: ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
