# PageBodyContract Defaults and User Configuration - TDD (2026-06-19)

## Context & Problem

Glossary:
- `PageBodyContract`: the `Schema` object that defines the required structure of `PageBody`.
- `ResolvedPageBodyContract`: the run-owned contract that binds one `PageBodyContract` to one `PlannedPageWrite`.
- `PageBodyFinding`: one failed contract check for a model-supplied `PageBody`.
- `PageBodyValidator`: the domain service that checks `PageBody` before `WikiStore` writes `WikiPage`.
- `SourcePlanContractSelection`: the `SourcePlan` fields that select or override `PageBodyContract` for one `RawSource`.

`PlannedPageWrite` now owns target `PageMetadata`, `PagePath`, evidence, links, citations, and uncertainty checks.
It does not own the required structure of `PageBody`.
The Antikythera verification run produced a `WikiPage` with `PageKind = source` that copied almost the whole `RawSource`.
This TDD adds `PageBodyContract`, local defaults, user-defined `PageBodyContract` values, and user documentation.

## Goals

- Add default `PageBodyContract` values to the local `Schema`.
- Make `Schema` own all `PageBodyContract` values for one `Wiki`.
- Make `SourcePlan` select `PageBodyContract` values for one `RawSource`.
- Make `PlannedPageWrite` reference one `ResolvedPageBodyContract`.
- Make `PageBodyValidator` reject invalid `PageBody` before `WikiStore` writes `WikiPage`.
- Make `source-summary` produce compact, claim-oriented, grounded `PageBody` text by default.
- Make user-defined `PageBodyContract` values support domain-specific `PageBody` rules without pipeline code changes.
- Document local default `PageBodyContract` values, user-defined `PageBodyContract` values, and `SourcePlanContractSelection`.

## Non-Goals & Forbidden Approaches

Non-goals:
- This TDD does not add a web UI.
- This TDD does not design architecture-wiki `PageBodyContract` values in full.
- This TDD does not change `WikiStructure`.
- This TDD does not change `PageMetadata`.
- This TDD does not add human-in-the-loop ingest.
- This TDD does not replace model-written `PageBody` text with deterministic rendering.

Forbidden approaches:
- Do not put `PageBodyContract` definitions on `RawSource`.
- Do not rely on prompt text alone for `PageBodyContract` enforcement.
- Do not infer `PageBodyContract` from `PagePath`.
- Do not hardcode domain-specific `PageBodyContract` values in the reusable pipeline.
- Do not let `PlannedPageWrite` duplicate `PageBodyContract` definitions.
- Do not write a `WikiPage` after `PageBodyValidator` returns a `PageBodyFinding`.

## Requirements

- `Schema` must define `PageBodyContract` values for one `Wiki`.
- `Schema` must define default `PageBodyContract` selection by `PageKind`.
- The local default `Schema` must include `source-summary`, `entity-page`, `concept-page`, and `synthesis-page`.
- `SourcePlan` must select a `PageBodyContract` for each planned output page.
- `SourcePlan` must allow per-source `PageBodyContract` parameter overrides.
- `RawSource` must remain immutable source evidence.
- `PagePlan` must resolve one `ResolvedPageBodyContract` for each `PlannedPageWrite`.
- `ResolvedPageBodyContract` must include concrete required links, citations, uncertainty terms, and limits.
- `PageBodyValidator` must run before `WikiStore.write_page`.
- `PageBodyValidator` must return `PageBodyFinding` records for contract failures.
- The planned `write_page` tool must return `PageBodyFinding` records through the forge tool-error path.
- `docs/page-body-contracts.md` must explain local defaults, user-defined `PageBodyContract` values, and `SourcePlanContractSelection`.

## Invariants

- `raw/` remains immutable.
- `wiki/` remains the generated knowledge base.
- `Schema` remains the wiki-level configuration object.
- `SourcePlan` remains run-owned per-source planning data.
- `PlannedPageWrite` remains the only object that authorizes a planned page write.
- `WikiStore` remains the only component that writes markdown pages.
- `WikiStructure` remains the only object that renders `PagePath`.
- `IngestRun` remains unattended.

## Proposed Architecture

`Schema` owns reusable `PageBodyContract` definitions.
`SourcePlan` selects `PageBodyContract` values for one `RawSource`.
`PagePlan` resolves those selections into `ResolvedPageBodyContract` values.
`PlannedPageWrite` carries `ResolvedPageBodyContract` to the tool boundary.
`PageBodyValidator` checks the model-supplied `PageBody`.
`WikiStore` writes the `WikiPage` only after `PageBodyValidator` returns no `PageBodyFinding`.

```
+------------------+       +-------------------+
| Schema           |------>| PageBodyContract  |
+--------+---------+       +---------+---------+
         |                           |
         v                           v
+------------------+       +-------------------+
| SourcePlan       |------>| PagePlan          |
+--------+---------+       | PlannedPageWrite  |
         |                 +---------+---------+
         v                           |
+------------------+                 v
| PageBodyValidator|------>| WikiStore         |
| PageBodyFinding  |       | WikiPage write    |
+------------------+       +-------------------+
```

`Schema` stores default and user-defined `PageBodyContract` values.
`PageBodyContract` defines reusable rules for one `PageBody` structure.
`SourcePlan` selects `PageBodyContract` values and override values for one `RawSource`.
`PagePlan` creates `ResolvedPageBodyContract` values for planned writes.
`PlannedPageWrite` carries target `PageMetadata`, target `PagePath`, and `ResolvedPageBodyContract`.
`PageBodyValidator` checks model-supplied `PageBody` against `ResolvedPageBodyContract`.

## Key Interactions

Default markdown source ingest:

```
IngestRun -> Schema -> PageBodyContract source-summary
SourcePlan -> PagePlan -> ResolvedPageBodyContract
PlannedPageWrite -> PageBodyValidator -> WikiStore
```

Precondition: the user starts markdown ingest without `SourcePlanContractSelection`.
Function: `Schema` supplies the default `source-summary` `PageBodyContract` for `PageKind = source`.
Postcondition: the `WikiPage` is compact, claim-oriented, grounded, linked, and uncertainty-preserving.

Contract failure and retry:

```
Model -> write_page -> PageBodyValidator
PageBodyValidator -> PageBodyFinding -> tool error
Model -> write_page retry -> PageBodyValidator -> WikiStore
```

Precondition: the model supplies a `PageBody` that violates `ResolvedPageBodyContract`.
Function: `PageBodyValidator` returns `PageBodyFinding` records.
Postcondition: `WikiStore` writes no page until a retry satisfies `ResolvedPageBodyContract`.

## Data Model

| Object | Responsibility |
|---|---|
| `PageBodyContract` | Reusable `PageBody` rules owned by `Schema`. |
| `ResolvedPageBodyContract` | One `PageBodyContract` with concrete planned links, citations, uncertainty terms, and limits. |
| `PageBodyFinding` | One failed check against `ResolvedPageBodyContract`. |
| `SourcePlanContractSelection` | Contract selection and override values for one `RawSource`. |

`PageBodyContract` fields:

| Field | Meaning |
|---|---|
| `ContractId` | Stable id such as `source-summary` or `product-page`. |
| `MatchPageKinds` | `PageKind` values that can use the contract. |
| `RequiredSections` | Required section labels or headings. |
| `RequiredMarkdownShape` | Shape value such as `claim-bullets`, `structured-sections`, or `prose`. |
| `MinClaimBullets` | Minimum markdown bullet claims when `RequiredMarkdownShape` is `claim-bullets`. |
| `CoveragePolicy` | Named semantic coverage policy for the model-written `PageBody`. |
| `MaxWords` | Absolute maximum word count for `PageBody`. |
| `MaxSourceWordRatio` | Maximum `PageBody` words divided by source words. |
| `MaxCopiedNGramRatio` | Maximum copied source n-gram ratio. |
| `RequiredLinkPolicy` | Policy that resolves planned `PageId` values into required wikilinks. |
| `RequiredCitationPolicy` | Policy that resolves `Evidence` into required citations. |
| `RequiredUncertaintyPolicy` | Policy that resolves source uncertainty into required terms. |

Local default `PageBodyContract` values:

| ContractId | Default use |
|---|---|
| `source-summary` | Compact source evidence page with claim bullets. |
| `entity-page` | Concise page for one named person, place, organization, system, or object. |
| `concept-page` | Concise page for one idea, rule, theme, or pattern. |
| `synthesis-page` | Cross-source answer or analysis page. |

Default `source-summary` `PageBodyContract`:

| Rule | Value |
|---|---|
| `RequiredSections` | `Source record`, `Key supported claims` |
| `RequiredMarkdownShape` | `claim-bullets` |
| `MinClaimBullets` | `3` |
| `CoveragePolicy` | `main-supported-claims-and-explicit-limits` |
| `MaxWords` | `160` |
| `MaxSourceWordRatio` | `0.65` |
| `MaxCopiedNGramRatio` | `0.50` |
| `RequiredLinkPolicy` | require planned related page links |
| `RequiredCitationPolicy` | require every `RawSource` citation |
| `RequiredUncertaintyPolicy` | preserve source uncertainty terms |

## APIs / Interfaces

- `Schema` exposes `PageBodyContracts`.
- `Schema` exposes default `PageBodyContract` selection by `PageKind`.
- `SourcePlan` exposes `SourcePlanContractSelection`.
- `PagePlan` emits `PlannedPageWrite` with `ResolvedPageBodyContract`.
- The planned `write_page` tool accepts `page_body`.
- The planned `write_page` tool rejects invalid `page_body` with `PageBodyFinding` text.
- `docs/page-body-contracts.md` must explain the local default `PageBodyContract` values.
- `docs/page-body-contracts.md` must show how a user defines a wiki-level `PageBodyContract`.
- `docs/page-body-contracts.md` must show how a user selects `PageBodyContract` for one `RawSource` through `SourcePlan`.
- `docs/page-body-contracts.md` must include one local default example, one architecture example, and one physics example.

## Behavior & Domain Rules

Rule: `Schema` owns `PageBodyContract` definitions.
- Input: a wiki uses the local default `Schema`.
  Expected outcome: `Schema.PageBodyContracts` contains `source-summary`, `entity-page`, `concept-page`, and `synthesis-page`.
- Input: a user configures `product-page`.
  Expected outcome: `Schema.PageBodyContracts` contains `product-page`.

Rule: `SourcePlan` owns per-source selection.
- Input: `RawSource = raw/antikythera-mechanism.md`.
  Expected outcome: `RawSource` contains no `PageBodyContract` values.
- Input: `SourcePlan` selects `source-summary` for a `WikiPage` with `PageKind = source`.
  Expected outcome: `PagePlan` resolves that selection into `ResolvedPageBodyContract`.

Rule: `PageBodyValidator` rejects copied `RawSource` text.
- Input: `RawSource` has 239 words and model-supplied `PageBody` has 264 words.
  Expected outcome: `PageBodyFinding` reports `MaxWords` or `MaxSourceWordRatio`.
- Input: model-supplied `PageBody` copies `RawSource` paragraphs with high n-gram overlap.
  Expected outcome: `PageBodyFinding` reports `MaxCopiedNGramRatio`.

Rule: `PageBodyValidator` rejects missing structure.
- Input: `source-summary` page has only prose paragraphs.
  Expected outcome: `PageBodyFinding` reports missing `RequiredMarkdownShape = claim-bullets`.
- Input: `source-summary` page omits `Key supported claims`.
  Expected outcome: `PageBodyFinding` reports missing `RequiredSections`.

Rule: `PageBodyValidator` keeps grounding checks.
- Input: `PageBody` omits a required wikilink.
  Expected outcome: `PageBodyFinding` reports missing `RequiredLinkPageIds`.
- Input: `PageBody` omits a required source citation.
  Expected outcome: `PageBodyFinding` reports missing `RequiredSourceCitations`.
- Input: `RawSource` contains `may`, `possibly`, or `suggest`, and `PageBody` removes uncertainty.
  Expected outcome: `PageBodyFinding` reports missing `RequiredUncertaintyTerms`.

Rule: user-defined `PageBodyContract` values do not change reusable pipeline code.
- Input: a user defines `product-page` with sections for manufacturer, application, performance data, standards, limitations, and open items.
  Expected outcome: `PageBodyValidator` checks those sections without architecture-specific code.
- Input: a user defines `theorem-page` with statement, assumptions, proof sketch, and applications.
  Expected outcome: `PageBodyValidator` checks those sections without physics-specific code.

## Acceptance Criteria

- Unit tests cover `PageBodyContract`, `ResolvedPageBodyContract`, `PageBodyFinding`, and `SourcePlanContractSelection`.
- Unit tests prove `Schema` owns local default `PageBodyContract` values.
- Unit tests prove `RawSource` stores no `PageBodyContract` selection.
- Unit tests prove `SourcePlan` selects `PageBodyContract` values and override values.
- Unit tests prove `PagePlan` creates one `ResolvedPageBodyContract` per `PlannedPageWrite`.
- Tool tests prove invalid `PageBody` stops before `WikiStore.write_page`.
- Tool tests prove a model retry can pass after a `PageBodyFinding`.
- Tests prove `source-summary` rejects a near-full copy of the Antikythera source.
- Tests prove `source-summary` accepts a compact claim-bullet source summary.
- Tests prove a user-defined `product-page` `PageBodyContract` is enforced without domain-specific code.
- `uv run llmwiki ingest antikythera-mechanism.md` produces a compact `source-summary` page.
- `uv run llmwiki ingest antikythera-mechanism.md` writes only successful pages to `log.md`.
- `docs/page-body-contracts.md` exists.
- `docs/page-body-contracts.md` explains local defaults, user-defined `PageBodyContract` values, and `SourcePlanContractSelection`.
- `docs/page-body-contracts.md` includes copyable examples for local default, architecture, and physics wikis.
- The feature appears in the top-level user-facing documentation that introduces wiki setup.

## Cross-Cutting Concerns

Observability:
Run transcripts must show `ResolvedPageBodyContract` values in planned write prompts.
Tool errors must show `PageBodyFinding` records in retry prompts.

Error handling:
`PageBodyValidator` failures must use `PageBodyFinding`.
The planned `write_page` tool must present findings as corrective instructions.

Documentation:
The user guide must explain what the system supplies by default.
The user guide must explain when the user defines a domain-specific `PageBodyContract`.
The user guide must state that `RawSource` is evidence and `SourcePlan` selects `PageBodyContract`.

## Reference Implementations

- Domain objects: `harness/src/llmwiki/domain/objects.py`.
- Planning boundary: `harness/src/llmwiki/domain/planning.py`.
- Planned write tool: `harness/src/llmwiki/workflows/tools.py`.
- Workflow prompts: `harness/src/llmwiki/workflows/prompts.py`.
- Store boundary: `harness/src/llmwiki/store/wiki_store.py`.
- Schema source: `SCHEMA.md`.
- TDD guidance: `docs/writing-tdds.md`.

## Alternatives Considered

- Put `PageBodyContract` definitions on `RawSource`.
  Rejected because `RawSource` must remain immutable evidence.
- Put all `PageBodyContract` rules directly on `PlannedPageWrite`.
  Rejected because `Schema` must own local defaults and user-defined `PageBodyContract` values.
- Use prompt text only.
  Rejected because the Antikythera run passed prompt text while copying the source.
- Use an LLM judge for contract validation.
  Rejected because deterministic failures must block writes before model judgment.

## Halt Conditions

- If implementation needs `PageBodyContract` configuration on `RawSource`, stop and ask.
- If implementation needs a new persisted database, stop and ask.
- If implementation needs domain-specific constants in pipeline code, stop and ask.
- If implementation changes `WikiStructure`, stop and ask.
- If implementation removes model-written `PageBody`, stop and ask.
