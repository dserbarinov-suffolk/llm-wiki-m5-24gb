# PageBodyContract Guide

`PageBodyContract` defines the required shape of a generated `PageBody`.
`Schema` owns `PageBodyContract` values for one `Wiki`.
`SourcePlanContractSelection` selects or overrides `PageBodyContract` for one `RawSource` during one `IngestRun`.
`PlannedPageWrite` carries one `ResolvedPageBodyContract` to the write tool.
`RawSource` does not carry `PageBodyContract` because `RawSource` is immutable evidence.

## Local Defaults

The local `Schema` includes these default `PageBodyContract` values.

| ContractId | MatchPageKinds | Purpose |
| --- | --- | --- |
| `source-summary` | `source` | A compact source evidence page with required sections and claim bullets. |
| `entity-page` | `entity` | A grounded entity page that cites sources and links planned related pages. |
| `concept-page` | `concept` | A grounded concept page that cites sources and links planned related pages. |
| `synthesis-page` | `synthesis` | A grounded synthesis page with a larger word limit. |

`source-summary` requires `Source record` and `Key supported claims` sections.
`source-summary` requires at least three markdown bullet claims.
`source-summary` uses coverage policy `main-supported-claims-and-explicit-limits`.
That policy means the bullets should cover the source's central supported claims plus explicit uncertainty, gaps, or non-confirmations when present.
`source-summary` limits source-copying so the page becomes a compact source record, not a transcript.
The planner resolves required links, required citations, and required uncertainty terms into `ResolvedPageBodyContract`.
The write tool rejects a `PageBody` that violates `ResolvedPageBodyContract`.

## User-Defined Contracts

A user defines domain-specific `PageBodyContract` values on `Schema`.
The reusable ingest pipeline should not need code changes when the user adds a domain contract.

Example for an architecture wiki:

```yaml
PageBodyContract:
  ContractId: product-page
  MatchPageKinds: [entity]
  RequiredSections:
    - Applications
    - Performance
    - Compatibility
    - Limitations
  RequiredMarkdownShape: prose
  MinClaimBullets: 0
  CoveragePolicy: product-claims-and-limitations
  MaxWords: 420
  MaxCopiedNgramRatio: 0.60
  RequiredLinkPolicy: planned-related-pages
  RequiredCitationPolicy: all-raw-sources
  RequiredUncertaintyPolicy: preserve-source-uncertainty
```

Example for a physics textbook wiki:

```yaml
PageBodyContract:
  ContractId: derivation-page
  MatchPageKinds: [concept]
  RequiredSections:
    - Definition
    - Assumptions
    - Derivation
    - Limits
  RequiredMarkdownShape: prose
  MinClaimBullets: 0
  CoveragePolicy: definitions-assumptions-and-limits
  MaxWords: 520
  MaxCopiedNgramRatio: 0.70
```

## Per-Source Selection

`SourcePlanContractSelection` selects a `PageBodyContract` for one `RawSource` during one `IngestRun`.
Use it when one source needs a stricter or different contract than the `Schema` default.

Example:

```yaml
SourcePlanContractSelection:
  ContractId: product-page
  PageIds:
    - lcn-4040xp
  MaxWordsOverride: 300
```

`SourcePlanContractSelection` belongs to `SourcePlan`.
It does not belong to `RawSource`.
The same PDF can be ingested into two different wikis with two different `Schema` objects and two different contract selections.

## Runtime Flow

`Schema` supplies `PageBodyContract`.
`SourcePlan` may select or override `PageBodyContract`.
`PagePlan` creates `PlannedPageWrite`.
`PlannedPageWrite` carries `ResolvedPageBodyContract`.
The model supplies `PageBody`.
The write tool validates `PageBody` against `ResolvedPageBodyContract`.
The write tool writes the page only after validation succeeds.
