# Global Ingest Planning - TDD (2026-06-18)

## Context & Problem

PDF ingest currently writes wiki pages one pending chunk at a time, then runs a final integration pass.
That makes page choice local to one chunk and lets early chunks create pages before the pipeline can see whole-source commonalities, repeated topics, conflicts, and relationships.
The new domain-object boundary gives us `RawSource`, `SourceBundle`, `Schema`, `WikiStructure`, `ExtractionPrompt`, `IngestRun`, `SourcePlan`, `WikiPage`, `PageMetadata`, and `Evidence`.
This TDD adds a global planning phase that categorizes extracted source material before any wiki page write, then uses the same categorization to produce `PageMetadata` and `PagePath`.

## Goals

- Extract a whole `SourceBundle` into planning records before writing generated wiki pages.
- Categorize `ExtractedUnit` records with a conventional retrieval and clustering pipeline.
- Match planned content against existing `WikiPage` records before creating new pages.
- Detect likely enrichments, new pages, contradictions, and low-confidence gaps before page writes.
- Produce `PageMetadata` and `PagePath` from the same `PagePlan`.
- Keep `WikiStructure` as the only mechanism that renders `PagePath`.
- Preserve serial writes after planning is complete.
- Verify the implementation with a live `javascriptallonge.pdf` ingest and a human-readable observation report.

## Non-Goals & Forbidden Approaches

Non-goals:

- Do not build a web UI.
- Do not add human-in-the-loop live review during ingest.
- Do not add parallel ingest topology.
- Do not replace markdown wiki pages.
- Do not replace the existing PDF extractor in this TDD.
- Do not solve scanned whole-document OCR in this TDD.
- Do not design architecture-wiki folder taxonomy.

Forbidden approaches:

- Do not write `WikiPage` records during per-chunk extraction.
- Do not ask one model context to hold a whole PDF or whole wiki.
- Do not infer `PageMetadata` from `PagePath`.
- Do not create a separate folder classifier.
- Do not let folder placement diverge from `PageMetadata`.
- Do not skip existing-wiki matching before planned page writes.
- Do not create pages from clusters without `Evidence`.

## Requirements

- `IngestRun` must create `ExtractedUnits` before any `WikiPage` write.
- Each `ExtractedUnit` must retain `RawSource`, page range or locator, heading path, extracted text, and extraction status.
- Each candidate claim must retain `Evidence`.
- Candidate categorization must use bounded text features plus nearest-neighbor search plus hierarchical clustering.
- Existing wiki matching must use retrieval over existing page text before any model read of full pages.
- Claim comparisons must record at least overlap against retrieved existing page excerpts.
- `PagePlan` must decide whether each `PlannedPageWrite` is `enrich-existing`, `create-new`, or `defer`.
- Source-page planned writes replace the target from supplied `Evidence`; non-source planned writes must read an existing target before rewriting it.
- `PagePlan` must produce `PageMetadata`.
- `WikiStructure` must render every planned `PagePath` from `PageMetadata`.
- The same planned `PageMetadata` fields used for page categorization must be available to `WikiStructure`.
- The local default `WikiStructure` must still render `{PageId}.md`.
- A user-defined `WikiStructure` must be able to render nested paths from planned metadata without changing categorization code.
- The implementation must preserve `index.md`, `log.md`, and transcript observability.

## Invariants

- `raw/` remains immutable.
- `wiki/` remains the generated knowledge base.
- `Wiki.CurrentStructure` remains the single effective `WikiStructure`.
- `PageMetadata.PageId` remains page identity.
- `PagePath` remains a rendered location.
- `IngestRun` remains unattended.
- `IngestTopology` remains `serial`.
- Existing `wiki/*.md` pages remain valid.
- Existing markdown ingest remains supported.
- `Evidence` remains required for generated claims.

## Proposed Architecture

The ingest pipeline becomes extract, plan, then write.
Extraction and categorization produce small structured records that fit in bounded model contexts and deterministic indexes.
Planning reads the existing wiki through retrieval, resolves page targets, and emits `PagePlan`.
Writing applies `PagePlan` serially through the existing `write_page` boundary.

```
+--------------+     +----------------+     +----------------+
| SourceBundle |---->| ExtractedUnits |---->| CandidateFacts |
+--------------+     +----------------+     +-------+--------+
                                                     |
                                                     v
+--------------+     +----------------+     +----------------+
| Wiki Index   |---->| Wiki Matching  |---->| TopicClusters  |
+--------------+     +----------------+     +-------+--------+
                                                     |
                                                     v
+--------------+     +----------------+     +----------------+
| Schema       |---->| PagePlan       |---->| WikiPage Writes|
| WikiStructure|     | PageMetadata   |     | Index + Log    |
+--------------+     +----------------+     +----------------+
```

`SourceBundle` selects one or more `RawSource` objects.
`ExtractedUnits` hold source-derived material with provenance.
`CandidateFacts` hold candidate claims, topics, entities, and page hints.
`Wiki Matching` retrieves existing `WikiPage` records and claim evidence.
`TopicClusters` group related candidate facts across the full source bundle.
`PagePlan` chooses target pages and page metadata.
`WikiStructure` renders page paths from planned page metadata.
`WikiPage Writes` execute the plan through the existing store boundary.

## Key Interactions

Planned PDF ingest:

```
User -> CLI -> IngestRun -> SourceBundle -> ExtractedUnits
ExtractedUnits -> CandidateFacts -> TopicClusters -> WikiMatches
WikiMatches + TopicClusters -> PagePlan -> WikiPage Writes -> Index + Log
```

Precondition: `RawSource.SourceFormat` is `pdf`.
Function: `IngestRun` plans the whole extracted source before writing pages.
Postcondition: every written `WikiPage` has `PageMetadata`, `PagePath`, and `Evidence` from `PagePlan`.

Existing wiki matching:

```
CandidateFacts -> lexical candidates
CandidateFacts -> embedding candidates
merged candidates -> top WikiPages -> PagePlan
```

Precondition: `Wiki` may already contain related pages.
Function: retrieval narrows the wiki to pages that can fit into bounded planning contexts.
Postcondition: `PagePlan` marks each target as enrich, create, or defer.

Metadata and folder projection:

```
TopicCluster -> PageMetadata -> WikiStructure -> PagePath
```

Precondition: `Schema` declares the metadata fields available for the wiki.
Function: `PagePlan` assigns metadata once.
Postcondition: `WikiStructure` renders folders from the same metadata used for topic categorization.

## Data Model

| Object | Contract |
|---|---|
| `ExtractedUnit` | One source-derived unit with `RawSource`, locator, heading path, text, extraction status, and source hash. |
| `CandidateClaim` | One extracted claim with `Evidence`, confidence, and source locator. |
| `CandidateTopic` | One extracted topic label with supporting `CandidateClaim` records. |
| `CandidateEntity` | One extracted person, organization, product, concept instance, or named thing. |
| `TopicCluster` | A cluster of candidate claims, topics, and entities formed across the `SourceBundle`. |
| `WikiMatch` | A retrieved existing wiki target with match score, match reason, and page excerpt. |
| `ClaimComparison` | A support, contradiction, overlap, or unrelated comparison between candidate and existing claims. |
| `PagePlan` | The full run-owned plan for page creation, enrichment, contradiction recording, deferral, and projection. |
| `PlannedPageWrite` | One serial write operation from `PagePlan` to `WikiPage`. |
| `ProjectionMetadata` | The subset of `PageMetadata` fields that `WikiStructure` may use for `PagePath`. |

`SourcePlan` remains run-owned.
It records which `RawSource` and `ExtractedUnit` records contributed to each `PagePlan`.
`PagePlan` is new because page targets can combine facts from many chunks and many sources.

Example:

```
TopicCluster: closures and lexical scope
PagePlan: enrich-existing
Target WikiPage: closure
PageMetadata.PageId: closure
PageMetadata.PageKind: concept
PageMetadata.CategoryPath: javascript/functions
Evidence: raw/javascriptallonge.pdf p.44-48
WikiStructure local-flat: closure.md
WikiStructure nested-example: javascript/functions/closure.md
```

## APIs / Interfaces

- `llmwiki ingest <path-in-raw>` uses global planning for PDF sources.
- `llmwiki ingest <path-in-raw> --reextract` rebuilds `ExtractedUnits` and reruns global planning.
- `llmwiki ingest <path-in-raw> --reintegrate` is replaced by planned rewrite from existing `ExtractedUnits`.
- `PagePlan` is persisted under the source cache with the same source hash identity as the PDF manifest.
- `PlannedPageWrite` is the only object allowed to call `write_page`.
- `WikiStructure.render_path(PageMetadata)` remains the only path projection interface.

## Behavior & Domain Rules

Rule: extraction does not write pages.

- Input: `raw/javascriptallonge.pdf`.
  Expected outcome: `ExtractedUnits`, `CandidateClaims`, `TopicClusters`, and `PagePlan` exist before any `WikiPage` write.

Rule: categorization chooses metadata before path projection.

- Input: `TopicCluster = closures and lexical scope`.
  Expected outcome: `PageMetadata.PageId = closure`, then local `WikiStructure` renders `closure.md`.

Rule: existing pages are preferred over duplicates.

- Input: candidate claim about closures and existing page `closure`.
  Expected outcome: `PagePlan` uses `enrich-existing` unless contradiction or low confidence prevents it.

Rule: exact source-section identity beats semantic similarity.

- Input: extracted heading `Self-Similarity`, existing `javascriptallonge-self-similarity`, and semantically similar `javascriptallonge-copy-on-write`.
  Expected outcome: `PagePlan` routes the extracted unit to `javascriptallonge-self-similarity`.

Rule: folders are metadata projection.

- Input: planned metadata has `Domain = javascript` and `CategoryPath = functions`.
  Expected outcome: a nested `WikiStructure` can render `javascript/functions/closure.md` without changing categorization.

Rule: claim comparisons are planned before writes.

- Input: candidate claim conflicts with an existing cited claim.
  Expected outcome: `ClaimComparison` records the relation available from retrieved evidence, and `PagePlan` preserves provenance or defers if evidence is insufficient.

## Acceptance Criteria

- Existing markdown ingest tests still pass.
- Existing PDF extraction tests still pass.
- Unit tests cover `ExtractedUnit`, `PagePlan`, `PlannedPageWrite`, `PageMetadata`, and `WikiStructure`.
- A fake PDF ingest proves no `WikiPage` write occurs before `PagePlan` exists.
- A fake existing wiki proves related candidate claims enrich an existing page instead of creating a duplicate page.
- A source-section routing test proves exact section identity beats semantic source-page similarity.
- A nested `WikiStructure` test proves `CategoryPath` metadata renders nested `PagePath` without a separate folder classifier.
- A local-flat `WikiStructure` test proves the same `PageMetadata` still renders `{PageId}.md`.
- `uv run llmwiki ingest javascriptallonge.pdf` completes with the planned pipeline.
- The JavaScript Allonge observation report lists total `ExtractedUnits`, total `TopicClusters`, pages enriched, pages created, contradictions, deferrals, and final page paths.
- The JavaScript Allonge run must not create generic bucket pages when a specific existing page or topic cluster exists.
- The JavaScript Allonge run must record one `IngestRun`, one `PagePlan`, and serial `PlannedPageWrite` records.

## Cross-Cutting Concerns

Observability:
The cache must retain `ExtractedUnits`, clustering summaries, retrieval matches, `PagePlan`, and write transcripts.
The final `Log` entry must link to the observation report path.

Error handling:
Extraction failures stop before planning.
Planning failures stop before writes.
Write failures stop at the failed `PlannedPageWrite` and preserve the prior plan.

Performance:
Embedding and retrieval indexes may live under the existing source cache.
The implementation must not require all wiki pages or all extracted units in one model context.

Backward compatibility:
Existing wiki pages must parse without migration.
Existing cached manifests may be ignored or migrated only by source hash.

## Reference Implementations

- Current PDF extraction cache: `harness/src/llmwiki/pdf/pipeline.py`.
- Current manifest pattern: `harness/src/llmwiki/pdf/manifest.py`.
- Current run orchestration: `harness/src/llmwiki/runtime/session.py`.
- Current page metadata and projection: `harness/src/llmwiki/domain/pages.py`.
- Current object boundary: `harness/src/llmwiki/domain/objects.py`.
- Current store write boundary: `harness/src/llmwiki/store/wiki_store.py`.

## Alternatives Considered

- Keep chunk-immediate writes.
  Rejected because page choice is local to one chunk.
- Put the whole PDF and whole wiki in context.
  Rejected because source and wiki size exceed model context and make bookkeeping unstable.
- Use only model-generated topic labels.
  Rejected because clustering and retrieval need repeatable non-context-bound inputs.
- Build a folder classifier after page planning.
  Rejected because folders must project from the same `PageMetadata` that page planning produces.
- Require human review before writes.
  Rejected because unattended `SourceBundle` ingest remains the application boundary.

## Halt Conditions

- If implementation requires vector services outside local user space, stop and ask.
- If implementation requires moving existing `wiki/*.md` files during local-flat operation, stop and ask.
- If implementation needs a persistent database outside the cache and markdown wiki, stop and ask.
- If implementation changes `WikiStructure` so paths no longer render from `PageMetadata`, stop and ask.
- If JavaScript Allonge cannot complete under the local model and hardware limits, stop and report the failing stage before redesigning.
