# Source Claim Quality - TDD (2026-06-19)

## Context & Problem

`ExtractedUnit` is one source section or source chunk that feeds `PagePlan`.
`SourceClaim` is one atomic statement from one `ExtractedUnit`.
`ClaimEligibility` is the planning decision that permits a `SourceClaim` to appear in a default `SourceSummaryPlan`.
`ClaimRoleTag` is one `Schema` label that describes the function of a `SourceClaim`.
`ClaimCentrality` is the planning score that ranks a `SourceClaim` against its `ExtractedUnit.heading_path`.
`ClaimSalience` is the planning score that ranks a `SourceClaim` inside an `IngestRun`.
`SourceClaimClassifier` is the component that assigns `ClaimEligibility`, `ClaimRoleTag`, `ClaimCentrality`, and `ClaimSalience`.
`SourceSummaryPlan` is the selected `SourceClaim` coverage for one source `PlannedPageWrite`.
`SourceSummaryDraft` is the model proposal that the write boundary validates before it renders `PageBody`.
`SourceSummaryDraftValidator` is the component that validates `SourceSummaryDraft`.
`SourceClaimQualityFixture` is a test fixture with labeled `SourceClaim` examples.
`SourceSummaryQualityReport` is the deterministic report for selected claims and generated wiki pages.
The current planner treats analogies, rhetorical examples, code fragments, and source-framing statements as high-salience claims.
The current planner also treats ordinary modal language as source uncertainty.
The current source-summary prompt asks the model to invent a limitation bullet when no source uncertainty exists.

## Goals

- Add `ClaimEligibility` before `SourceSummaryPlan` selects claims.
- Add default `ClaimRoleTag` values for discourse roles.
- Split source uncertainty from ordinary modal language.
- Select one eligible central claim per grouped `ExtractedUnit` when the group fits the source-summary claim limit.
- Reject source-summary drafts that use source-framing language in claim bullets.
- Add deterministic quality experiments that run without a model call.
- Keep Docling extraction unchanged.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not change `DocumentModel`, `SourceSection`, or `SourceChunk`.
- This TDD does not add a new model call before `SourceSummaryPlan`.
- This TDD does not create a universal claim ontology.
- This TDD does not require perfect JavaScript Allonge summaries.

Forbidden approaches:

- Do not tune rules only for JavaScript Allonge.
- Do not remove per-unit coverage from grouped source pages.
- Do not select an ineligible `SourceClaim` when an eligible `SourceClaim` exists in the same `ExtractedUnit`.
- Do not require a source-summary draft to invent uncertainty.
- Do not allow `PageBody` to contain internal `SourceClaim` ids.
- Do not make `WikiStructure` depend on `ClaimEligibility`.

## Requirements

- `SourceClaimClassifier` must assign `ClaimEligibility` to every `SourceClaim`.
- `SourceClaimClassifier` must assign `ClaimRoleTag` values before `ClaimSalience`.
- `ClaimEligibility` must have the values `eligible`, `analogy`, `rhetorical-example`, `narrative-frame`, `source-furniture`, `code-fragment`, and `source-framing`.
- `SourceSummaryPlan` must select `eligible` claims before any other `ClaimEligibility`.
- `SourceSummaryPlan` must select zero ineligible claims when an `ExtractedUnit` has one eligible claim.
- `SourceSummaryPlan` must select one eligible claim per `ExtractedUnit` when the source page has five or fewer `ExtractedUnit` records.
- `ClaimRoleTag` defaults must include `source-uncertainty` and `ordinary-modality`.
- `SourceSummaryPlan` must treat `source-uncertainty` as source-summary coverage input.
- `SourceSummaryPlan` must not treat `ordinary-modality` as source-summary uncertainty input.
- `ClaimSalience` must include `ClaimCentrality`.
- `ClaimCentrality` must compare `SourceClaim.statement` with `ExtractedUnit.heading_path`.
- `ClaimSalience` must penalize `analogy`, `rhetorical-example`, `narrative-frame`, `source-furniture`, `code-fragment`, and `source-framing`.
- `SourceSummaryDraftValidator` must reject claim bullets that start with source-framing phrases.
- `SourceSummaryDraftValidator` must reject a source-summary draft that omits selected eligible claim coverage.
- `SourceSummaryQualityReport` must run against cached `PagePlan` and generated wiki pages.
- `SourceSummaryQualityReport` must not call the model.

## Invariants

- `RawSource` remains immutable.
- `Evidence` remains required for generated claims.
- `IngestRun` remains unattended.
- `IngestTopology` remains `serial`.
- `ExtractedUnit` remains the `PagePlan` source input.
- `PageMetadata.PageId` remains page identity.
- `WikiStructure` remains the only `PagePath` renderer.
- `PageBody` does not contain internal planning identifiers.

## Proposed Architecture

The planner adds claim quality classification between `SourceClaim` creation and `SourceSummaryPlan` selection.
`SourceClaimClassifier` assigns `ClaimEligibility`, `ClaimRoleTag`, `ClaimCentrality`, and `ClaimSalience`.
`SourceSummaryPlan` selects eligible central claims for source pages.
`SourceSummaryDraftValidator` validates source-summary wording and selected-claim coverage.
`SourceSummaryQualityReport` reads cached artifacts and reports quality metrics.

```
+---------------+     +-----------------------+     +-------------+
| ExtractedUnit |---->| SourceClaimClassifier |---->| SourceClaim |
+---------------+     +-----------------------+     +------+------+
                                                           |
                                                           v
                                                  +-------------------+
                                                  | SourceSummaryPlan |
                                                  +---------+---------+
                                                            |
                                                            v
                                                  +-------------------+
                                                  | WikiPage          |
                                                  +-------------------+
```

`SourceClaimClassifier` owns claim eligibility, role tags, centrality, and salience.
`SourceSummaryPlan` owns source-summary claim selection.
`SourceSummaryDraftValidator` owns source-summary draft validation.
`SourceSummaryQualityReport` owns deterministic quality experiments.

## Key Interactions

Claim classification:

```
ExtractedUnit -> SourceClaim -> SourceClaimClassifier
SourceClaimClassifier -> ClaimEligibility
SourceClaimClassifier -> ClaimRoleTag
SourceClaimClassifier -> ClaimCentrality
SourceClaimClassifier -> ClaimSalience
```

Precondition: `IngestRun` has `ExtractedUnit` records.
Function: `SourceClaimClassifier` classifies every `SourceClaim`.
Postcondition: `SourceSummaryPlan` receives classified `SourceClaim` records.

Quality experiment:

```
PagePlan cache -> SourceSummaryQualityReport
wiki pages -> SourceSummaryQualityReport
SourceClaimQualityFixture -> SourceSummaryQualityReport
```

Precondition: cached artifacts exist for one completed ingest.
Function: `SourceSummaryQualityReport` computes quality metrics.
Postcondition: tests fail when metrics miss thresholds.

## Data Model

| Object | Contract |
|---|---|
| `ClaimEligibility` | One value that controls default source-summary eligibility. |
| `ClaimCentrality` | One score that ranks a claim against `ExtractedUnit.heading_path`. |
| `SourceClaimQualityFixture` | One labeled set of source-claim examples for deterministic tests. |
| `SourceSummaryQualityReport` | One deterministic report for selected claims and generated wiki pages. |

`ClaimEligibility` values:

| Value | Contract |
|---|---|
| `eligible` | `SourceSummaryPlan` selects the claim. |
| `analogy` | The claim is an analogy that supports a nearby claim. |
| `rhetorical-example` | The claim is a rhetorical or illustrative example. |
| `narrative-frame` | The claim is scene-setting prose. |
| `source-furniture` | The claim is source metadata, credits, or table text. |
| `code-fragment` | The claim is a code block fragment without prose claim shape. |
| `source-framing` | The claim describes what the source text does. |

Additional default `ClaimRoleTag` values:

| Value | Contract |
|---|---|
| `source-uncertainty` | The source states an unresolved, unknown, unconfirmed, or missing fact. |
| `ordinary-modality` | The sentence uses modal language without source uncertainty. |
| `analogy` | The sentence explains through comparison. |
| `worked-example` | The sentence belongs to a worked example. |
| `source-framing` | The sentence describes the source text instead of the source subject. |

`SourceClaimQualityFixture` stores `FixtureId`, `SourceLocator`, `HeadingPath`, `Statement`, `ExpectedClaimEligibility`, and `ExpectedClaimRoleTags`.
`SourceSummaryQualityReport` stores `SelectedIneligibleClaims`, `FalseSourceUncertaintyClaims`, `SourceFramingBullets`, and `MissingUnitCoverage`.

## APIs / Interfaces

- `PagePlan` must expose `SourceClaim.ClaimEligibility`.
- `PagePlan` must expose `SourceClaim.ClaimCentrality`.
- `SourceSummaryPlan.SelectedSourceClaims` must include only selected claim ids.
- The planned source-summary write tool must keep the existing `SourceSummaryDraft` interface.
- The planned source-summary write tool must reject source-framing bullets.
- The quality command or test helper must read `page_plan.json`, `source_sections.json`, and `wiki/*.md`.

## Behavior & Domain Rules

Rule: `ClaimEligibility` filters source-summary selection.

- Input: one `ExtractedUnit` has one analogy claim and one eligible JavaScript claim.
  Expected outcome: `SourceSummaryPlan` selects the eligible JavaScript claim.
- Input: one `ExtractedUnit` has one code fragment and one eligible prose claim.
  Expected outcome: `SourceSummaryPlan` selects the eligible prose claim.
- Input: one `ExtractedUnit` has no eligible claim.
  Expected outcome: `SourceSummaryPlan` selects one ineligible claim and records that fact in `SourceSummaryQualityReport`.

Rule: `source-uncertainty` differs from `ordinary-modality`.

- Input: the statement says "a caller possibly needs a function to return squares".
  Expected outcome: `ClaimRoleTag` includes `ordinary-modality`.
- Input: the statement says "the source does not specify the implementation".
  Expected outcome: `ClaimRoleTag` includes `source-uncertainty`.
- Input: the statement says "there is more to generators".
  Expected outcome: `ClaimRoleTag` includes `ordinary-modality`.

Rule: `ClaimCentrality` affects `ClaimSalience`.

- Input: `ExtractedUnit.heading_path = Object.assign` and a claim mentions `Object.assign`.
  Expected outcome: the claim receives higher `ClaimCentrality` than a nearby string-literal claim.
- Input: `ExtractedUnit.heading_path = variables and bindings` and a claim only mentions `antidisestablishmentarianism`.
  Expected outcome: the claim receives low `ClaimCentrality`.
- Input: a claim matches `ExtractedUnit.heading_path` and has `ClaimEligibility = eligible`.
  Expected outcome: `SourceSummaryPlan` ranks it above a high-length analogy claim.

Rule: `SourceSummaryDraftValidator` blocks source-framing bullets.

- Input: a bullet starts with "The source discusses".
  Expected outcome: `SourceSummaryDraftValidator` rejects the draft.
- Input: a bullet starts with "The text mentions".
  Expected outcome: `SourceSummaryDraftValidator` rejects the draft.
- Input: a bullet states the source subject directly.
  Expected outcome: `SourceSummaryDraftValidator` accepts the wording.

Rule: quality experiments use cached artifacts.

- Input: JavaScript Allonge cached `PagePlan` and generated wiki pages.
  Expected outcome: `SourceSummaryQualityReport` reports all required metrics.
- Input: one fixture item has expected `ClaimEligibility = analogy`.
  Expected outcome: the fixture test fails when the classifier returns `eligible`.
- Input: one grouped source page has five `ExtractedUnit` records with eligible claims.
  Expected outcome: `MissingUnitCoverage = 0`.

## Acceptance Criteria

Milestone 1: deterministic claim fixtures.

- Add `SourceClaimQualityFixture` data for at least 80 JavaScript Allonge claims.
- Add `SourceClaimQualityFixture` data for at least 20 Antikythera claims.
- Fixture data must include analogies, rhetorical examples, source-framing statements, code fragments, ordinary modal statements, and source uncertainty statements.
- Unit tests must prove fixture classifier accuracy is at least 90 percent.
- Unit tests must prove selected ineligible claims stay under 5 percent when eligible claims exist.
- Unit tests must prove false source uncertainty stays under 10 percent.

Milestone 2: source-summary selection.

- Unit tests must prove grouped source pages keep per-unit eligible claim coverage.
- Unit tests must prove `SourceSummaryPlan` does not select an analogy when the unit has an eligible central claim.
- Unit tests must prove `SourceSummaryPlan` does not select a code fragment when the unit has an eligible prose claim.
- Unit tests must prove `SourceSummaryPlan` selects `source-uncertainty` only when it exists.

Milestone 3: draft validation.

- Unit tests must prove source-framing bullets are rejected.
- Unit tests must prove source-summary drafts do not leak `SourceClaim` ids.
- Unit tests must prove direct subject bullets are accepted.

Milestone 4: cached-quality experiments.

- A deterministic test must run `SourceSummaryQualityReport` against JavaScript Allonge cached artifacts.
- The report must return `MissingUnitCoverage = 0`.
- The report must return `SourceFramingBullets = 0` after the implementation regenerates pages.
- The report must show fewer selected analogy claims than the current cached baseline.
- The report must show fewer false source uncertainty claims than the current cached baseline.

Milestone 5: end-to-end ingest.

- Clear the wiki.
- Re-ingest JavaScript Allonge.
- Verify `Object.assign`, `Why?`, and `A Warm Cup` remain represented.
- Verify generated source-summary pages pass `SourceSummaryQualityReport`.
- Run `uv run ruff check src tests`.
- Run `uv run mypy src`.
- Run `uv run pytest`.

## Cross-Cutting Concerns

`SourceSummaryQualityReport` must print metric names, counts, and failing examples.
The planned source-summary write tool must return the same validation error shape that `PageBodyValidator` uses.
`SourceSummaryQualityReport` must run from cached JSON and wiki pages without Docling extraction.

## Reference Implementations

- `SourceClaim` and `SourceSummaryPlan`: [planning.py](/Users/DSerbarinov/llm-wiki/harness/src/llmwiki/domain/planning.py).
- `SourceSummaryDraftValidator`: [page_body_contracts.py](/Users/DSerbarinov/llm-wiki/harness/src/llmwiki/domain/page_body_contracts.py).
- Planned write tool: [tools.py](/Users/DSerbarinov/llm-wiki/harness/src/llmwiki/workflows/tools.py).

## Alternatives Considered

- Use prompt-only fixes: rejected because bad selected claims still reach the model.
- Add a model call for claim ranking: rejected because cached deterministic tests must run quickly.
- Remove grouped source pages: rejected because Docling creates too many sections for one model write per section.
- Keep uncertainty as one broad role: rejected because ordinary modal language caused false uncertainty bullets.

## Halt Conditions

- If implementation changes `DocumentModel`, stop and ask before proceeding.
- If implementation adds a model call before `SourceSummaryPlan`, stop and ask before proceeding.
- If fixture accuracy needs source-specific rules for one book, stop and ask before proceeding.
