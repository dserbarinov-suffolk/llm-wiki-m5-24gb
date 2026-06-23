---
page_id: wiki-ingest-confidence
page_kind: synthesis
summary: Latest bounded post-ingest confidence report.
updated: 2026-06-23
---

# Ingest Confidence Report

## Summary

Run id: 2026-06-23-094159
Source: raw/javascriptallonge.pdf
Confidence status: passed with warnings
Blockers: 0
Warnings: 1
Gates: 5

## Artifact Reuse

- page-plan: missing `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/javascriptallonge-5873116c6496/page-plan.json` (artifact is missing; fingerprint 6cb7ee7b8fe55b95)
- evidence-registry: missing `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/javascriptallonge-5873116c6496/evidence-registry.json` (artifact is missing; fingerprint 6cb7ee7b8fe55b95)
- evidence-locators: missing `/Users/DSerbarinov/llm-wiki/harness/.cache/page-plans/javascriptallonge-5873116c6496/evidence-locators.json` (artifact is missing; fingerprint 6cb7ee7b8fe55b95)

## Gates

### page-plan
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none

### source-summary-quality
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: fail
- Findings: validation-finding-803bcc6b4d2a91a4
SelectedIneligibleClaims: 0
FalseSourceUncertaintyClaims: 0
SourceFramingBullets: 1
MissingUnitCoverage: 0
SourceFramingExamples:
- javascriptallonge-programming-from-functions-to-classes-in-ecmascript-2015-through-a-pull-of-the: - The source discusses the evolution of JavaScript from functional programming to class-based programming. (raw/javascriptallonge.pdf p.2-2)

### evidence-registry
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none
Source texts: 1
Source ranges: 167
Evidence records: 2908

### evidence-locators
- Kind: deterministic
- Scope: raw/javascriptallonge.pdf
- Status: pass
- Findings: none
Locators: 2894
Invalid locators: 0

### claim-support
- Kind: model-assisted
- Scope: raw/javascriptallonge.pdf
- Status: skipped
- Findings: validation-finding-cf596b10e496becb
ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Findings

- WARNING source-summary: Source-summary bullets use source-framing prose. Count: 1.
- INFO claim-support: ClaimSupportAuditReport is model-assisted and is not run by ordinary ingest.

## Caveat

This is a bounded post-ingest confidence report, not proof that every wiki claim is correct.
