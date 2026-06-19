# Domain Language Consistency - TDD (2026-06-19)
## Context & Problem
Glossary:
- `DomainTerm`: exact name of one concept.
- `CodeName`: snake_case Python form of one `DomainTerm`.
- `DomainFrontmatter`: generated page metadata block.
- `GeneratedWikiState`: generated `wiki/`, generated `index.md`, generated `log.md`, and generated ingest cache.

This TDD defines a refactor for one domain language.
The code mixes page identity, page kind, source identity, and write planning terms.
That mix makes one concept have many names and lets one fact live in more than one place.
After the refactor, the implementer clears `GeneratedWikiState` and re-ingests sources.
## Goals
- Define one authoritative `DomainTerm` and one `CodeName` for each first-order concept used by local LLM-Wiki.
- Make internal code use `CodeName` for each concept.
- Make generated markdown use `DomainFrontmatter` field names.
- Make `Schema` the authoritative source for allowed `PageKind` values and `PageMetadataField` values.
- Make `PageMetadata` the authoritative object for `PageId`, `PageKind`, `Summary`, `Sources`, and queryable page fields.
- Make `WikiStructure` the only object that renders `PagePath` from `PageMetadata`.
- Make `PagePlan` and `PlannedPageWrite` the authoritative owners of page write targets.
- Make `SourcePlan` the authoritative owner of `RawSource` classification and run-level handling notes.
- Make tests enforce the domain language rule.
- Clear `GeneratedWikiState` after the refactor and re-ingest Antikythera Mechanism first.
- Re-ingest JavaScript Allonge only after Antikythera Mechanism succeeds.
## Non-Goals & Forbidden Approaches
Non-goals:
- This TDD does not preserve pre-refactor `WikiPage` content.
- This TDD does not add architecture-wiki folder taxonomy.
- This TDD does not add human-in-the-loop ingest.
- This TDD does not add parallel ingest topology.
- This TDD does not replace forge workflows.
- This TDD does not change CLI command names.

Forbidden approaches:
- Do not use `name` as an internal page identity term.
- Do not use `category` as an internal page kind term.
- Do not use `path` as a synonym for `SourceLocator`.
- Do not add adapters for pre-refactor `WikiPage` content.
- Do not parse pre-refactor frontmatter after the rebuild.
- Do not infer `PageMetadata` from `PagePath`.
- Do not duplicate allowed `PageKind` values outside `Schema`.
- Do not duplicate `PageMetadataField` values outside `Schema`.
- Do not copy target `PageMetadata` or `PagePath` from `PlannedPageWrite` into `SourcePlan`.
- Do not introduce a new persisted database for this refactor.
## Requirements
- Each domain concept must have one `DomainTerm`.
- Each `DomainTerm` must have one `CodeName`.
- Internal modules must use `CodeName`.
- Documentation and prompts must use `DomainTerm`.
- `DomainFrontmatter` must use `CodeName`.
- `PageMetadata` must contain `page_id`, `page_kind`, `summary`, `sources`, `updated`, and zero or more `Schema.PageMetadataFields`.
- `WikiPage` must contain `PageMetadata` and `PageBody`.
- `IndexEntry` must consume `PageMetadata`.
- `LintRun` must report `LintFindings -> LintFinding`.
- `compute_findings` must return `LintRun` or `LintFinding` records.
- `SalienceReport` must consume `WikiPage` or `PageMetadata`.
- Model-facing `read_page` must use `page_id`.
- Model-facing `write_page` must use `page_id`, `page_kind`, `summary`, `sources`, and `page_body`.
- Model-facing `read_source` must use `source_locator`.
- `RawSource.SourceLocator` must be the source identity inside code.
- `SourceBundle.RawSources` must be the source collection for `IngestRun`.
- `IngestRun.IngestTopology` must remain `serial`.
- `PagePlan` must own `PlannedPageWrites`.
- `PlannedPageWrite` must own target `PageMetadata`, target `PagePath`, write action, evidence, matches, comparisons, and `ExistingPageId`.
- `SourcePlan` must own `RawSource`, source classification, ingest disposition, `PlannedPageWrite` references, and handling notes.
- `Claim` must mean a maintained wiki statement, and `CandidateClaim` must mean a source-derived statement before page write.
- `ClaimComparison` must compare one `CandidateClaim` with one existing `Claim` or one existing page excerpt.
- The migration run must clear `GeneratedWikiState` before the first re-ingest.
- The migration run must preserve `raw/`, `SCHEMA.md`, docs, source code, tests, and transcripts outside `GeneratedWikiState`.
## Invariants
- `raw/` remains immutable.
- `wiki/` remains the generated knowledge base.
- `GeneratedWikiState` is disposable during this migration.
- Rebuilt markdown pages use `DomainFrontmatter` field names only.
- Rebuilt index entries use `IndexEntry`.
- Rebuilt wikilinks are `CrossReference` candidates.
- `PageMetadata.PageId` remains page identity.
- `PagePath` remains a rendered location.
- `Wiki.CurrentStructure` remains the single effective `WikiStructure`.
- `IngestRun` remains unattended.
## Proposed Architecture
The refactor removes adapters for pre-refactor `WikiPage` content.
Domain modules accept and return domain objects.
Workflow tools expose domain terms to the model.
Store code persists domain objects as generated markdown with `DomainFrontmatter`.

```
+------------------+      +-------------------+      +----------------+
| CLI and tools    |----->| Domain objects    |----->| PageMetadata   |
+------------------+      +-------------------+      | WikiStructure  |
                                                     +-------+--------+
                                                             |
                                                             v
+------------------+      +-------------------+      +----------------+
| raw/             |<---->| WikiStore         |<---->| WikiPage       |
| wiki/            |      | Index + Log       |      | PagePath       |
+------------------+      +-------------------+      +----------------+
```
`CLI and tools` receive user input and model tool calls.
`Domain objects` carry `CodeName` fields across workflows and store calls.
`Schema` owns allowed `PageKind` values and `PageMetadataField` values.
`PageMetadata` owns page identity and queryable page fields.
`WikiStructure` renders `PagePath`.
`WikiPage` owns `PageMetadata` and `PageBody`.
`WikiStore` remains the only component that touches `raw/`, `wiki/`, `index.md`, and `log.md`.
## Key Interactions
Read generated markdown page:
```
WikiStore -> DomainFrontmatter -> PageMetadata -> WikiPage
WikiStore -> WikiStructure -> PagePath
```
Precondition: a generated markdown page exists under `wiki/`.
Function: `DomainFrontmatter` parses `DomainFrontmatter` fields into `PageMetadata`.
Postcondition: callers receive `WikiPage` with `PageMetadata` and `PageBody`.

Write page through model tool:
```
write_page tool -> PageMetadata -> WikiPage -> WikiStructure -> WikiStore
WikiStore -> DomainFrontmatter + Index + Log
```
Precondition: the model supplies `page_id`, `page_kind`, `summary`, `sources`, and `page_body`.
Function: `write_page` creates `PageMetadata`, and `WikiStructure` renders `PagePath`.
Postcondition: `WikiStore` writes one markdown page and one `IndexEntry`.

Plan PDF ingest:
```
IngestRun -> SourceBundle -> ExtractedUnits -> PagePlan
PagePlan -> PlannedPageWrites -> WikiPage writes
SourcePlan -> PlannedPageWrite references
```
Precondition: `RawSource.SourceFormat` is `pdf`.
Function: `PagePlan` creates write targets, and `SourcePlan` records source handling.
Postcondition: write targets live in `PlannedPageWrite`, and source handling lives in `SourcePlan`.

Migration rebuild:
```
Refactor complete -> clear GeneratedWikiState -> ingest Antikythera Mechanism
Antikythera success -> ingest JavaScript Allonge
```
Precondition: tests pass after the domain language refactor.
Function: the implementation deletes `GeneratedWikiState` and rebuilds it from `RawSource`.
Postcondition: rebuilt pages contain no pre-refactor generated page field names.
## Data Model
Authoritative vocabulary:
| DomainTerm | CodeName |
|---|---|
| `PageId` | `page_id` |
| `PageKind` | `page_kind` |
| `PagePath` | `page_path` |
| `PageBody` | `page_body` |
| `PageMetadata` | `page_metadata` |
| `PageMetadataField` | `page_metadata_field` |
| `DomainFrontmatter` | `domain_frontmatter` |
| `GeneratedWikiState` | `generated_wiki_state` |
| `SourceLocator` | `source_locator` |
| `RawSource` | `raw_source` |
| `SourceBundle` | `source_bundle` |
| `Schema` | `schema` |
| `WikiStructure` | `wiki_structure` |
| `PathTemplate` | `path_template` |
| `IngestRun` | `ingest_run` |
| `PagePlan` | `page_plan` |
| `SourcePlan` | `source_plan` |
| `PlannedPageWrite` | `planned_page_write` |
| `Claim` | `claim` |
| `CandidateClaim` | `candidate_claim` |
| `Evidence` | `evidence` |
| `CrossReference` | `cross_reference` |
| `IndexEntry` | `index_entry` |
| `LogEntry` | `log_entry` |
| `QueryRun` | `query_run` |
| `LintRun` | `lint_run` |
| `LintFinding` | `lint_finding` |
| `SalienceReport` | `salience_report` |

Object ownership:
| Owner | Owns |
|---|---|
| `Schema` | `PageKinds`, `PageMetadataFields`, `PageContracts`, workflow rules, lint rules |
| `Wiki` | `CurrentStructure`, `WikiPages`, `Index`, `Log`, `CrossReferences` |
| `WikiStructure` | `PathTemplates` |
| `PathTemplate` | `TemplateText`, `MatchPageKinds`, `RequiredPageMetadataFields` |
| `WikiPage` | `PageMetadata`, `PageBody` |
| `DomainFrontmatter` | `PageMetadataFields` |
| `PagePlan` | `CandidateClaims`, `CandidateTopics`, `CandidateEntities`, `TopicClusters`, `WikiMatches`, `ClaimComparisons`, `PlannedPageWrites` |
| `SourcePlan` | `RawSource`, `SourceClassification`, `IngestDisposition`, `PlannedPageWriteIds`, `HandlingNotes` |
| `PlannedPageWrite` | `PageMetadata`, `PagePath`, `WriteAction`, `Evidence`, `WikiMatches`, `ClaimComparisons`, `ExistingPageId` |
| `LintRun` | `LintFindings`, `SuggestedQueryRuns`, `SuggestedRawSources` |
## APIs / Interfaces
- Model-facing `read_page` uses `page_id`.
- Model-facing `write_page` uses `page_id`, `page_kind`, `summary`, `sources`, and `page_body`.
- Model-facing `read_source` uses `source_locator`.
- Store-facing page reads return `WikiPage`.
- Store-facing page writes accept `WikiPage`.
- Index updates accept `PageMetadata`.
- Lint reads accept `WikiPage` records.
- Salience reads accept `WikiPage` records.
- CLI code maps the user source argument to `SourceLocator`.
- `DomainFrontmatter` uses `page_id`, `page_kind`, `summary`, `sources`, `updated`, and zero or more `Schema.PageMetadataFields`.
- `Index` parses persisted index lines.
## Behavior & Domain Rules
Rule: `PageMetadata` is the page metadata authority.
- Input: `PageMetadata.PageId = closure`.
  Expected outcome: internal code uses `page_id`.
- Input: `DomainFrontmatter.page_kind = concept`.
  Expected outcome: `DomainFrontmatter` derives `PageKind = concept`.

Rule: `Schema` is the page-kind authority.
- Input: local page kinds are `source`, `entity`, `concept`, and `synthesis`.
  Expected outcome: `Schema.PageKinds` contains those values.
- Input: a test searches for a second hardcoded page-kind tuple.
  Expected outcome: the test fails when another authoritative tuple exists.

Rule: `WikiStructure` is the page-path authority.
- Input: `PageMetadata.PageId = closure` and local-flat `WikiStructure`.
  Expected outcome: `PagePath = closure.md`.
- Input: generated page path `concepts/closure.md`.
  Expected outcome: code does not infer `PageKind = concept` from the folder.

Rule: `SourceLocator` is the source identity.
- Input: `uv run llmwiki ingest javascriptallonge.pdf`.
  Expected outcome: CLI maps the user source argument to `SourceLocator = javascriptallonge.pdf`.
- Input: citation `(raw/javascriptallonge.pdf p.44-48)`.
  Expected outcome: `Evidence.RawSource.SourceLocator = javascriptallonge.pdf` and `Evidence.Locator = p.44-48`.

Rule: `SourcePlan` and `PlannedPageWrite` do not duplicate facts.
- Input: one PDF produces ten planned page writes.
  Expected outcome: `PagePlan.PlannedPageWrites` owns the ten targets.
- Input: `SourcePlan` needs to report affected writes.
  Expected outcome: `SourcePlan.PlannedPageWriteIds` references the writes.

Rule: `Claim` and `CandidateClaim` are different concepts.
- Input: `ExtractedUnit` contains a source-grounded statement.
  Expected outcome: planning creates `CandidateClaim`.
- Input: a `WikiPage` stores the statement as maintained knowledge.
  Expected outcome: wiki content represents `Claim`.

Rule: `GeneratedWikiState` migration is destructive.
- Input: domain language refactor tests pass.
  Expected outcome: implementation clears `GeneratedWikiState` before re-ingest.
- Input: Antikythera Mechanism ingest fails.
  Expected outcome: implementation stops before JavaScript Allonge ingest.
## Acceptance Criteria
- The test suite passes.
- `WikiPage` construction uses `PageMetadata` and `PageBody`.
- Static tests reject internal `name`, `category`, `path`, `rel_path`, and `source_path` uses for domain concepts.
- `read_page`, `write_page`, and `read_source` use the `CodeName` values in this TDD.
- `Index`, `LintRun`, and `SalienceReport` consume `WikiPage` or `PageMetadata`.
- `LintRun` owns `LintFindings -> LintFinding`.
- `Schema` is the only authoritative source for `PageKind` values and `PageMetadataField` values.
- `SourcePlan` does not contain target `PageMetadata` or target `PagePath`.
- `PlannedPageWrite` contains target `PageMetadata` and target `PagePath`.
- Prompt text for planned writes uses `PageId`, `PageKind`, `PageMetadata`, `PagePath`, `SourceLocator`, and `PageBody`.
- Static tests fail when documentation or prompts introduce an unapproved synonym for an authoritative `DomainTerm`.
- `DomainFrontmatter` uses `page_id`, `page_kind`, `summary`, `sources`, and `updated`.
- `DomainFrontmatter` does not use `name` or `category`.
- The implementation clears `GeneratedWikiState` before verification ingest.
- `uv run llmwiki ingest antikythera-mechanism.md` completes after `GeneratedWikiState` is cleared.
- `uv run llmwiki ingest javascriptallonge.pdf` runs only after Antikythera Mechanism succeeds.
- `uv run llmwiki ingest javascriptallonge.pdf` completes after Antikythera Mechanism succeeds.
- The JavaScript Allonge observation report still lists `ExtractedUnits`, `TopicClusters`, write counts, contradictions, deferrals, and final `PagePath` values.
## Cross-Cutting Concerns
Observability:
Run transcripts remain valid historical records.
New run artifacts use `DomainTerm` names.

Error handling:
Errors use `DomainTerm`.

Migration:
This TDD permits deleting `GeneratedWikiState`.
It does not permit deleting `RawSource`, source code, tests, docs, or user-owned files outside `GeneratedWikiState`.

Testing:
Unit tests enforce object behavior.
Static tests enforce vocabulary use.
## Reference Implementations
- Current domain objects: `harness/src/llmwiki/domain/objects.py`.
- Current page metadata and structure code: `harness/src/llmwiki/domain/pages.py`.
- Current store boundary: `harness/src/llmwiki/store/wiki_store.py`.
- Current tool boundary: `harness/src/llmwiki/workflows/tools.py`.
- Current global planning code: `harness/src/llmwiki/domain/planning.py`.
- Domain-object vocabulary source: `docs/2026-06-16-llm-wiki-domain-objects.md`.
- TDD style guide: `docs/writing-tdds.md`.
## Alternatives Considered
- Keep pre-refactor `WikiPage` content: rejected because the migration will clear and rebuild `GeneratedWikiState`.
- Keep pre-refactor `DomainFrontmatter` field names: rejected because generated pages must use the same domain language as code.
- Remove `SourcePlan`: rejected because architecture-wiki migration needs source-level handling records.
- Keep target metadata in both `SourcePlan` and `PlannedPageWrite`: rejected because one fact would live in two places.
- Enforce vocabulary only through reviewer discipline: rejected because tests must fail on drift.
## Halt Conditions
- If implementation requires changing CLI command names, stop and ask.
- If implementation requires deleting `SourcePlan`, stop and ask.
- If implementation requires a new database, stop and ask.
- If implementation requires deleting files outside `GeneratedWikiState`, stop and ask.
