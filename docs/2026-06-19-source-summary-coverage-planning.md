# Source Summary Coverage Planning - TDD (2026-06-19)

## Context & Problem

`SourceClaim` is one atomic statement extracted from one `ExtractedUnit`.
`ClaimRoleTag` is one `Schema` label that describes how a `SourceClaim` functions.
`SourceClaimGroup` is one semantic group of related `SourceClaim` objects.
`SourceSummaryPlan` is the selected `SourceClaim` coverage for one source `PlannedPageWrite`.
`SourceSummaryDraft` is the model proposal that the write boundary validates before it renders `PageBody`.
`CoveragePolicy` is the `PageBodyContract` field that selects claim coverage rules.
`PageBodyValidator` is the component that rejects invalid draft content before a `WikiPage` write.
`TopicCluster` is the existing page-planning group that creates or enriches `WikiPage` targets.
`PageMetadata` is the existing metadata object that `WikiStructure` uses to render `PagePath`.
`CandidateClaim` is the existing incomplete claim object in `planning.py`.
Current source-summary writes use `PageBodyContract` shape checks and prompt text.
The model currently satisfies shape checks while it copies a local source phrase or omits important claim types.
The current `CandidateClaim` implementation also keeps only the first source statement, so it cannot plan source-summary coverage.

## Goals

- Add `SourceClaim` as the source-owned claim inventory for each `IngestRun`.
- Add `ClaimRoleTag` classification from `Schema` plus a local default role vocabulary.
- Add `SourceClaimGroup` so source-summary coverage and page planning share claim groups.
- Add `SourceSummaryPlan` so one source `PlannedPageWrite` receives selected `SourceClaim` coverage.
- Keep `TopicCluster` responsible for page targets.
- Keep `PageMetadata` responsible for folder projection input.
- Keep `WikiStructure` as the only `PagePath` renderer.
- Add local copy checks that catch one copied bullet without rejecting useful technical terms.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not create a universal ontology for every wiki.

Forbidden approaches:

- Do not tune `ClaimRoleTag` values for one source.
- Do not require every `SourceClaim` to have one `ClaimRoleTag`.
- Do not infer `PageMetadata` from `PagePath`.
- Do not use `SourceSummaryPlan` as a folder classifier.
- Do not make `TopicCluster` depend on rendered folders.
- Do not let a source-summary write read the whole existing wiki.
- Do not let a generated `PageBody` contain internal `SourceClaimId` values.

## Requirements

- `IngestRun` must create `SourceClaim` records before source `PlannedPageWrite` records execute.
- Each `SourceClaim` must retain `Evidence`.
- Each `SourceClaim` must retain one source span locator inside one `ExtractedUnit`.
- Each `SourceClaim` must retain `ClaimRoleTags`, `ClaimSalience`, and `ClaimCertainty`.
- `Schema` must provide default `ClaimRoleTag` values.
- `Schema` must allow a wiki to add or replace `ClaimRoleTag` values.
- The default `ClaimRoleTag` values must include broad roles, not domain examples.
- The pipeline must allow an unlabeled `SourceClaim`.
- The pipeline must allow multiple `ClaimRoleTag` values on one `SourceClaim`.
- `SourceClaimGroup` must group `SourceClaim` records before `TopicCluster` selects wiki page targets.
- `SourceSummaryPlan` must select `SourceClaim` records from `SourceClaimGroup` records.
- `SourceSummaryPlan` must select high-salience uncertainty, limitation, contradiction, and negative-evidence claims when they exist.
- `SourceSummaryPlan` must select claims from multiple high-salience `SourceClaimGroup` records when the source has multiple groups.
- `PlannedPageWrite` for a source page must carry `SourceSummaryPlan`.
- The source-summary write interface must require one draft bullet to cite one or more selected `SourceClaim` records.
- The write boundary must render source-summary `PageBody` from accepted draft bullets.
- The validator must reject draft bullets that copy a long source span.
- The validator must reject draft bullets that omit selected claim coverage.
- `TopicCluster` must accept `SourceClaimGroup` records as input.
- `PageMetadata` must accept `SourceClaimGroup` labels and `ClaimRoleTag` values as candidate metadata.
- `WikiStructure` must render `PagePath` from `PageMetadata`.

## Invariants

- `RawSource` remains immutable.
- `Evidence` remains required for generated claims.
- `IngestRun` remains unattended.
- `IngestTopology` remains `serial`.
- `PageMetadata.PageId` remains page identity.
- `PagePath` remains a rendered location.
- `WikiStructure` remains declarative.
- `PageBody` does not contain internal planning identifiers.

## Proposed Architecture

The pipeline adds a claim inventory phase between `ExtractedUnit` creation and `PagePlan` creation.
The claim inventory phase creates `SourceClaim` records, assigns `ClaimRoleTag` values, assigns salience, and groups related claims.
`SourceSummaryPlan` uses those records to select coverage for source pages.
`TopicCluster` uses those records to choose non-source page targets.
`PageMetadata` uses those records as candidate metadata only after `PagePlan` chooses a page target.
`SourceClaimExtractor` creates `SourceClaim` records.
`ClaimRoleClassifier` assigns `ClaimRoleTag` values.
`ClaimSalienceRanker` assigns `ClaimSalience`.
`SourceClaimGrouper` creates `SourceClaimGroup` records.

```
+---------------+     +-------------+     +------------------+
| ExtractedUnit |---->| SourceClaim |---->| SourceClaimGroup |
+---------------+     +------+------+     +--------+---------+
                              |                     |
                              v                     v
                     +------------------+   +----------------+
                     | SourceSummaryPlan|   | TopicCluster   |
                     +--------+---------+   +--------+-------+
                              |                      |
                              v                      v
                     +------------------+   +----------------+
                     | source WikiPage  |   | PageMetadata   |
                     +------------------+   +--------+-------+
                                                       |
                                                       v
                                               +---------------+
                                               | WikiStructure |
                                               +---------------+
```

`SourceClaim` stores one source-supported statement with evidence and role tags.
`SourceClaimGroup` stores related source claims for coverage and page planning.
`SourceSummaryPlan` selects source claims for one source page.
`TopicCluster` selects claim groups for wiki page targets.
`PageMetadata` stores queryable page metadata.

## Key Interactions

Claim inventory:

```
ExtractedUnit -> SourceClaimExtractor -> SourceClaim
SourceClaim -> ClaimRoleClassifier -> ClaimRoleTag
SourceClaim -> ClaimSalienceRanker -> ClaimSalience
SourceClaim -> SourceClaimGrouper -> SourceClaimGroup
```

Precondition: `IngestRun` has `ExtractedUnit` records.
Function: the pipeline creates claim records that fit bounded contexts.
Postcondition: `PagePlan` uses `SourceClaim` records without reading the whole source again.

Source-summary coverage:

```
SourceClaimGroup -> SourceSummaryPlan -> PlannedPageWrite
PlannedPageWrite -> source-summary draft -> PageBodyValidator -> WikiPage
```

Precondition: one source `PlannedPageWrite` targets `PageKind = source`.
Function: `SourceSummaryPlan` selects source claims for the source page.
Postcondition: the source page covers selected claims and cites the selected evidence.

Page and folder planning:

```
SourceClaimGroup -> TopicCluster -> PageMetadata -> WikiStructure -> PagePath
```

Precondition: `PagePlan` needs non-source page targets.
Function: `TopicCluster` uses claim groups to choose page targets and metadata.
Postcondition: `WikiStructure` renders `PagePath` from `PageMetadata`.

## Data Model

| Object | Contract |
|---|---|
| `SourceClaim` | One atomic source-supported statement with `Evidence`, source span locator, role tags, salience, certainty, and subject terms. |
| `ClaimRoleTag` | One `Schema` label such as `identity`, `function`, `method`, `limitation`, `uncertainty`, or `negative-evidence`. |
| `ClaimSalience` | One numeric or ordinal score that ranks a `SourceClaim` inside an `IngestRun`. |
| `ClaimCertainty` | One value that records source certainty, source uncertainty, contradiction, or unknown status. |
| `SourceClaimGroup` | A group of related `SourceClaim` records with label, salience, and role coverage. |
| `SourceSummaryPlan` | The selected `SourceClaim` coverage for one source `PlannedPageWrite`. |
| `SourceSummaryDraft` | The model-proposed source-summary bullets before `PageBody` rendering. |

Default `ClaimRoleTag` values cover identity, definition, attribute, function, mechanism, method, evidence, and provenance.
Default `ClaimRoleTag` values also cover temporal, quantitative, relationship, comparison, requirement, procedure, limitation, uncertainty, negative-evidence, and open-question.

`SourceSummaryPlan` fields:

| Field | Contract |
|---|---|
| `SourceSummaryPlanId` | Stable id inside one `PagePlan`. |
| `PageId` | Target source page id. |
| `SelectedSourceClaims` | Ordered selected `SourceClaim` ids. |
| `RequiredClaimRoleTags` | Claim role tags that the draft must cover when selected claims contain them. |
| `RequiredSourceClaimGroups` | Claim group ids that the draft must cover. |
| `CoveragePolicy` | The `PageBodyContract.CoveragePolicy` value used to select claims. |

`SourceSummaryDraft` fields:

| Field | Contract |
|---|---|
| `SourceRecordText` | One source-record sentence without internal ids. |
| `ClaimBullets` | Three to five draft bullets. |
| `CoveredSourceClaims` | Source claim ids covered by each draft bullet. |

The renderer writes `SourceRecordText` and `ClaimBullets` into `PageBody`.
The renderer does not write `CoveredSourceClaims` into `PageBody`.

## APIs / Interfaces

- `PagePlan` must expose `SourceClaims`.
- `PagePlan` must expose `SourceClaimGroups`.
- `PlannedPageWrite` must carry `SourceSummaryPlan` when `PageKind = source`.
- The planned source-summary write tool must accept `SourceSummaryDraft` instead of raw `PageBody`.
- The planned non-source write tool continues to accept raw `PageBody`.
- `WikiStructure.render_path(PageMetadata)` remains the only path projection interface.

## Behavior & Domain Rules

Rule: `SourceClaim` is the shared claim inventory.

- Input: one source paragraph with five factual statements.
  Expected outcome: `IngestRun` creates separate `SourceClaim` records for the factual statements.
- Input: one source sentence that says one product has two limitations.
  Expected outcome: `IngestRun` creates two `SourceClaim` records with `ClaimRoleTag = limitation`.

Rule: `ClaimRoleTag` supports coverage but does not define an ontology.

- Input: one claim about a date.
  Expected outcome: the classifier assigns `temporal`.
- Input: one claim about a rule exception.
  Expected outcome: the classifier assigns `requirement` and `limitation`.
- Input: one claim that fits no default tag.
  Expected outcome: the classifier leaves `ClaimRoleTags` empty.

Rule: `SourceSummaryPlan` selects coverage before writing.

- Input: a source with three high-salience claim groups.
  Expected outcome: `SourceSummaryPlan` selects at least one claim from each high-salience group.
- Input: a source with one uncertainty claim and one negative-evidence claim.
  Expected outcome: `SourceSummaryPlan` selects both claims when they meet salience thresholds.
- Input: a source with twenty low-salience attribute claims.
  Expected outcome: `SourceSummaryPlan` selects only representative claims.

Rule: `SourceClaimGroup` is reusable but not universal.

- Input: source claims about one concept and one existing concept page.
  Expected outcome: `TopicCluster` uses the matching `SourceClaimGroup`.
- Input: source claims that only matter for a source page.
  Expected outcome: `SourceSummaryPlan` uses the group without creating a non-source page.
- Input: a wiki with nested folders.
  Expected outcome: `PageMetadata` uses group labels as candidate metadata, then `WikiStructure` renders `PagePath`.

Rule: the validator blocks local copying.

- Input: one draft bullet with an eight-word source phrase copied verbatim.
  Expected outcome: `PageBodyValidator` rejects the bullet even when the page-level copied ratio passes.
- Input: one draft bullet with necessary technical terms and no long copied phrase.
  Expected outcome: `PageBodyValidator` accepts the bullet.

## Acceptance Criteria

- Unit tests cover `SourceClaim`, `ClaimRoleTag`, `SourceClaimGroup`, `SourceSummaryPlan`, and `SourceSummaryDraft`.
- Unit tests prove one `SourceClaim` accepts zero, one, or many `ClaimRoleTag` values.
- Unit tests prove `Schema` adds or replaces `ClaimRoleTag` values.
- Unit tests prove `SourceSummaryPlan` selects high-salience uncertainty and negative-evidence claims.
- Unit tests prove `SourceSummaryPlan` selects representative claims across high-salience `SourceClaimGroup` records.
- Unit tests prove a source-summary write rejects a copied phrase inside one draft bullet.
- Unit tests prove source-summary `PageBody` does not contain `SourceClaimId` values.
- Unit tests prove `TopicCluster` consumes `SourceClaimGroup` records without depending on `SourceSummaryPlan`.
- Unit tests prove `WikiStructure` still renders `PagePath` only from `PageMetadata`.
- A markdown ingest test proves source-summary coverage improves without source-specific prompt text.
- A fake PDF ingest test proves `SourceClaim` records exist before source `PlannedPageWrite` records execute.
- `uv run pytest` passes.
- `uv run llmwiki ingest antikythera-mechanism.md` produces a source summary with selected coverage and no copied long phrase.
- A second small fixture from a non-history domain produces selected coverage without changing default code.

## Cross-Cutting Concerns

Observability:
The cache or run artifact must retain `SourceClaims`, `SourceClaimGroups`, `SourceSummaryPlan`, and the accepted `SourceSummaryDraft`.

Error handling:
The pipeline stops before writes when `SourceClaim` creation fails.
The planned source-summary write retries when `SourceSummaryDraft` fails validation.

Performance:
The classifier and grouper must operate on bounded `ExtractedUnit` and `SourceClaim` windows.
The implementation must not place a whole large source or whole wiki in one model context.

## Reference Implementations

- Current planning pipeline: `harness/src/llmwiki/domain/planning.py`.
- Current page-body validator: `harness/src/llmwiki/domain/page_body_contracts.py`.
- Current domain objects: `harness/src/llmwiki/domain/objects.py`.
- Current planned write tool boundary: `harness/src/llmwiki/workflows/tools.py`.

## Alternatives Considered

- Keep prompt-only coverage.
  Rejected because the model omits source claim types while satisfying shape.
- Lower the copied-ngram threshold globally.
  Rejected because technical summaries need shared terms.
- Use one universal cluster object for every grouping task.
  Rejected because source-summary coverage and page-target planning have different outputs.
- Keep `CandidateClaim` as the authoritative claim inventory.
  Rejected because the current object stores too little source coverage.
- Require every `SourceClaim` to fit a default `ClaimRoleTag`.
  Rejected because user wikis contain claims outside the default vocabulary.

## Halt Conditions

- If implementation needs an external vector service, stop and ask.
- If implementation requires supervised training data, stop and ask.
- If implementation writes internal `SourceClaimId` values into `PageBody`, stop and ask.
- If implementation makes `SourceSummaryPlan` choose `PagePath`, stop and ask.
- If implementation makes `WikiStructure` depend on `SourceClaimGroup`, stop and ask.
