---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Latest bounded post-ingest confidence report.
updated: 2026-06-26
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-26-154722
Source: raw/rpg_dnd_srd_excerpt.pdf
Confidence status: passed
Blockers: 0
Warnings: 0
Gates: 5

## Artifact Reuse

- page-plan: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/rpg-dnd-srd-excerpt-f7c05ef0468a/page-plan.json` (fingerprint matches; fingerprint 3fb5ee3841274f09)
- evidence-registry: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/rpg-dnd-srd-excerpt-f7c05ef0468a/evidence-registry.json` (fingerprint matches; fingerprint 3fb5ee3841274f09)
- evidence-locators: reuse `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/rpg-dnd-srd-excerpt-f7c05ef0468a/evidence-locators.json` (fingerprint matches; fingerprint 3fb5ee3841274f09)

## Gates

### page-plan
- Kind: deterministic
- Scope: raw/rpg_dnd_srd_excerpt.pdf
- Status: pass
- Findings: none

### source-summary-quality
- Kind: deterministic
- Scope: raw/rpg_dnd_srd_excerpt.pdf
- Status: pass
- Findings: none
SelectedIneligibleClaims: 0
FalseSourceUncertaintyClaims: 0
SourceFramingBullets: 0
MissingUnitCoverage: 0

### evidence-registry
- Kind: deterministic
- Scope: raw/rpg_dnd_srd_excerpt.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 137
Evidence records: 958

### evidence-locators
- Kind: deterministic
- Scope: raw/rpg_dnd_srd_excerpt.pdf
- Status: pass
- Findings: none
Locators: 951
Invalid locators: 0

### claim-support
- Kind: model-assisted
- Scope: raw/rpg_dnd_srd_excerpt.pdf
- Status: skipped
- Findings: validation-finding-33f18d23b9783b15
ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Findings

- INFO claim-support: ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
