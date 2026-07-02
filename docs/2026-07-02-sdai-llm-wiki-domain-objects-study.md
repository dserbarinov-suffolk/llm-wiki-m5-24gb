# SDAI LLM-Wiki Domain Objects Branch Study

## Scope

This note studies `/Users/DSerbarinov/gits/SDAI-LLM-Wiki` after checkout of
branch `domain-objects-and-projection-mechanism`.

The purpose is to build a lookup artifact for the local `llm-wiki` project.
The study treats the external repository as source material. It does not copy
code. It identifies reusable systems, risks, and follow-up study areas.

This note is not a TDD or DDD. It is a research log and reference map.

## Branch State

External repository:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki`

Branch:

`domain-objects-and-projection-mechanism`

Recent branch themes:

- Atomic target selection by specificity, with tags and aliases union.
- Topic heading fixes for project-location-like headings.
- Removal of older Gen1 pipeline code.
- New page retraction mechanic.
- Tier 1 category and domain-topic synthesis.
- Tier 2 LLM selection groundwork.
- OCR and large-PDF scaling experiments.
- Walkability improvements.

## High-Level Map

The repository is a monorepo with these main areas:

- `packages/wiki_core`: pure Python domain and parsing helpers.
- `packages/wiki_io`: local and artifact I/O helpers, evidence validation, state.
- `packages/wiki_llm`: model backends, prompts, and LLM response parsing.
- `packages/wiki_cli`: local command-line phase orchestration.
- `packages/client-py`: generated Python contracts from the shared OpenAPI schema.
- `packages/client-ts`: generated TypeScript contracts from the shared OpenAPI schema.
- `packages/api`: HTTP API handlers over persisted wiki artifacts.
- `packages/chat-agent`: tool-driven chat agent over the wiki API.
- `infra/processing-service`: AWS Step Functions, Lambda, ECS, S3, Bedrock, and worker code.
- `docs/processing-service`: production-service designs and operational notes.
- `tools`: thin wrappers and local scripts.

The important architectural move in this branch is that the processing pipeline
is no longer only "extract text and write pages." It now has explicit middle
artifacts:

- `SourcePlan`
- `DocumentStructure`
- `ClaimLedger`
- `TopicIndex`
- `SectionPlan`
- `ExtractionResult`
- `StagedWikiPage`
- `MaintenanceArtifactSet`
- `LintRun`
- `PublishRun`

Those objects make ingestion inspectable before Markdown is written.

## Runtime Flow

The processing-service path is approximately:

1. The wiki profile and raw sources resolve into a configured ingest run.
2. `source-plans.ts` builds source plans from raw source metadata, classifier
   rules, target plan rules, category contracts, page contracts, and structured
   fact types.
3. `source_plan_extraction_worker.py` loads the extraction work artifact and
   runs each source-plan item.
4. Each source plan is converted into source-topic artifacts:
   `DocumentStructure`, `ClaimLedger`, `TopicIndex`, and `SectionPlan`.
5. The worker calls an LLM in target batches, but the prompt is bound to the
   planned targets and shared contracts.
6. `source_plan_bound_extraction.py` validates the LLM result against the
   planned source targets, page contracts, structured fact types, and evidence.
7. `wiki_page_projection.py` converts accepted extraction results and section
   plans into `StagedWikiPage` artifacts.
8. `wiki_projection_lint.py` checks staged pages, paths, evidence, facts,
   related links, graph consistency, and missing required content.
9. `wiki_projection_publish.py` writes accepted pages and updates graph and
   index artifacts.
10. `wiki_aggregate_projection.py` creates deterministic category and
    domain-topic pages from the current graph, with fingerprint-based no-op
    detection and retraction.
11. `wiki_maintenance_artifacts.py` creates maintenance artifacts used by
    index, graph, attribution, and diagnostics.

The most important pattern is that extraction is not trusted to decide final
wiki pages or paths. Extraction must fit inside a plan. Projection and publish
are separate decisions.

## First-Class Domain Objects

The generated Python contract file in `packages/client-py` is the best quick
index of the branch's domain model.

Important source and profile objects:

- `WikiCreationRequest`
- `WikiIdentity`
- `SourceBundle`
- `RawSource`
- `WikiProfile`
- `WikiSchema`
- `PageContract`
- `CategoryContract`
- `StructuredFactType`
- `FactField`
- `ExtractionPrompt`
- `ResolvedIngestRunConfig`

Important planning objects:

- `SourcePlan`
- `SourcePlanTarget`
- `SourceClassification`
- `SourcePlanGap`
- `PlannedPageMetadata`
- `ProjectionPolicy`
- `PageFamily`
- `ProjectionEligibility`

Important source-derived middle artifacts:

- `DocumentStructure`
- `DocumentStructureNode`
- `SourceStatement`
- `LedgerEntry`
- `ClaimLedger`
- `TopicSignal`
- `Topic`
- `TopicIndex`
- `TopicDecision`
- `SectionPlan`
- `SectionPlanTarget`
- `SectionCoverageMapEntry`

Important extraction objects:

- `SourcePlanBoundExtractionResult`
- `ExtractionResult`
- `ExtractedEvidence`
- `ExtractedClaim`
- `StructuredFact`
- `ExtractionGap`

Important projection objects:

- `StagedWikiPage`
- `PageMetadata`
- `PagePath`
- `ProjectionEvidenceBlock`
- `TechnicalAtomFrame`
- `RelatedPageLink`
- `WalkabilityFinding`

Important publish and maintenance objects:

- `MaintenanceArtifactSet`
- `LintRun`
- `PublishDecision`
- `PublishRun`
- `WikiHealth`
- `WikiIndex`
- `WikiPage`

## Pass 1: Modules

### Generated Contracts

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/client-py/src/sdai_llm_wiki_client/types.py`

Learning:

- The shared OpenAPI schema is the source of truth for Python and TypeScript
  boundary shapes.
- Worker code parses unknown JSON into generated Pydantic models before using it.
- This gives both repos a plausible route to portable domain artifacts.

Portable value:

- High. A shared contract package would make porting safer than copying local
  dataclasses or ad hoc dictionaries.

Local caution:

- The schema includes product-catalog roles and categories. The mechanism is
  portable; those concrete labels are not universal.

### Worker Contract Parsing

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/worker_contracts.py`

Learning:

- The worker boundary has small helpers for contract parsing and serialization.
- Validation errors are reported by path and message, without dumping payloads.
- Boundary parsing is centralized instead of repeated throughout workers.

Portable value:

- High. Our local wiki should use the same pattern at CLI, cache, and page-plan
  boundaries.

### Source Planning

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/node/src/wiki-api/source-plans.ts`

Learning:

- Source plans are built before extraction.
- The plan is driven by profile rules, target templates, page contracts, and
  category contracts.
- The extraction work artifact includes only planned source targets.
- Final path authority stays with deterministic projection code.

Portable value:

- High. This is the cleanest preventative answer to invented pages and weak
  page candidates.

Local caution:

- Some classifier hints are production-domain words such as project, standard,
  report, analytics, and reference. The source-plan mechanism is reusable, but
  source-type labels should be configurable or source-derived.

### Page Path Projection

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/node/src/wiki-api/page-path-projection.ts`

Learning:

- Page paths are rendered from `PathTemplate` and target metadata.
- Metadata cannot contain path traversal, absolute paths, or file extensions.
- Ambiguous templates block projection.
- The final path must end in `{pageId}.md`.

Portable value:

- High. Page paths should be deterministic products of typed metadata, never LLM
  output.

### Source-Plan-Bound Extraction

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/source_plan_bound_extraction.py`

Learning:

- Extraction output is validated against a `SourcePlan`.
- Claims and facts can target only planned page ids.
- Supported claims and facts require evidence.
- Claim types must be expected by the target page contract.
- Fact types must be expected by the target page contract.
- Fact fields must be declared, have required fields, and satisfy type and
  allowed-value checks.
- Evidence must preserve raw source identity and locator fields.

Portable value:

- Very high. This is a root-cause fix for model-created scope drift.

### Extraction Worker

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/source_plan_extraction_worker.py`

Learning:

- The worker is a large orchestrator.
- It builds topic artifacts before model extraction.
- It prompts the model with source plan targets and contracts.
- It removes path authority fields from model-facing context.
- It batches targets to control model context.
- It records parser and validation gaps instead of silently accepting weak output.
- It can run projection-only from already persisted source artifacts.
- It publishes incrementally as each file completes by rereading cumulative
  artifacts.

Portable value:

- Medium as code, high as architecture.

Local caution:

- The file mixes orchestration, prompt construction, artifact reads and writes,
  normalization, validation, and projection calls. We should not mirror that
  shape. The local repo should split these concerns into pure domain services
  and adapters.

### Claim Ledger And Topic Index

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/claim_ledger_topic_index.py`

Learning:

- This is the core source-topic system.
- It builds document structure from normalized Markdown.
- It builds source statements and ledger entries.
- It creates technical atoms from tables and source nodes.
- It creates topic signals from headings, ledger concepts, and table/entity
  candidates.
- It expands source plans from topic decisions.
- It builds section coverage and technical atom bindings.

Portable value:

- High for object flow. Medium for direct code.

Local caution:

- The file has many product-catalog assumptions: manufacturer, model, series,
  product-name, part-number, category path, product pages, project-location
  banners, and US state abbreviation checks.
- Those assumptions may be useful in the production architecture wiki, but they
  violate the local Universal Standard if copied as production logic.
- The table atom implementation is row-oriented in this file. Our local
  invariant is stricter: one source table should remain one technical atom,
  with row-level facts as optional child facts or indexes.

### Page Projection

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_page_projection.py`

Learning:

- Projection groups accepted claims and structured facts by planned target page.
- It uses section context to produce evidence blocks.
- It renders technical atom frames with section labels.
- It computes related page links from structured relations, shared context,
  source summary, same section, and same category source.
- It audits related links so unsupported links do not survive.
- It rejects extraction results that try to supply path authority.
- It resolves multi-source target collisions by choosing the most specific
  target atomically, then unions tags and aliases.

Portable value:

- Very high as a projection architecture.

Local caution:

- Product-page content filtering is hard-coded in several places.
- The local wiki should express this as a profile-driven target support policy,
  not as product-specific code.

### Aggregate Projection

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_aggregate_projection.py`

Learning:

- Category and domain-topic pages are generated deterministically from the
  graph.
- Member fingerprints avoid unnecessary rewrites.
- Empty existing aggregate pages are retracted by deleting the page and
  updating graph and index artifacts.
- Category pages are projected before domain pages so domain pages can see the
  new category nodes.
- Per-group failures are captured as gaps instead of aborting the whole run.

Portable value:

- High if generalized to domain-neutral collection pages.

Local caution:

- The renderer is product-catalog flavored. It uses words like products,
  category, domain-topic, governing standards, and uncategorized products.

### Maintenance Artifacts

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_maintenance_artifacts.py`

Learning:

- Maintenance artifacts are built after staging.
- They include index entries, fact references, cross references, log entries,
  unresolved references, graph check data, and counts.
- Graph checks compare rendered Markdown links and related-page links against
  known staged pages.

Portable value:

- High. The local wiki should treat graph/index/log output as artifacts derived
  from staged pages, not as incidental side effects.

### Projection Publish

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_projection_publish.py`

Learning:

- Publish writes only accepted staged pages.
- It merges graph nodes into the existing graph.
- It removes old outgoing edges for rewritten nodes, then adds the new supported
  related-link edges.
- It writes a public index from the merged graph.
- Rendered pages include frontmatter and deterministic page text.

Portable value:

- High.

Local caution:

- The frontmatter appears thinner than the full page metadata. If the local wiki
  wants strong offline query and graph behavior, full metadata should remain
  available in a machine-readable artifact.

### Projection Lint

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_projection_lint.py`

Learning:

- Lint validates staged pages against contracts, paths, consumer metadata,
  category contracts, facts, projection gaps, maintenance artifacts, evidence,
  related links, and graph unresolved edges.
- It can distinguish blocking findings from warnings.
- It is a publish gate, not only a report.

Portable value:

- High. The local wiki should make lint a required gate before page writes or
  after staging, depending on the local workflow.

### Chat Agent

Files:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/chat-agent/src/agentic-loop.ts`

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/chat-agent/src/agentic-loop-streaming.ts`

Learning:

- The chat agent is tool-based.
- The prompt forces index-first behavior, then page reads, then graph following.
- It requires citations from read pages only.
- It limits tool calls.
- The streaming path filters trailing source sections because read pages are
  surfaced separately.

Portable value:

- Medium. The policy is useful, but the local wiki already needs context-limited
  deterministic retrieval over local artifacts. The search tool is basic keyword
  search and is not the strongest part of this branch.

### API Handlers

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/api/src/wiki-handlers.ts`

Learning:

- The API serves summary, index, pages, individual page, graph, and attribution.
- It reads persisted wiki artifacts rather than recomputing the pipeline.

Portable value:

- Medium for local server mode.

Local caution:

- Some handlers appear to reflect older artifact assumptions, such as route
  summary and attribution parsing. This needs deeper drift review before porting.

## Pass 2: Lower-Level Parsing And Evidence

### Structural Chunking

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/wiki_core/src/wiki_core/parsing/chunking.py`

Learning:

- The pure chunker recognizes headings, paragraphs, code, tables, equations,
  figures, captions, lists, footnotes, page headers, page footers, TOC entries,
  bibliography blocks, blockquotes, HTML, and unknown blocks.
- Blocks carry source file, page span, section path, line span, reading order,
  token count, language, assets, checksum, quality score, and quality issues.
- Atomic units preserve complete code blocks, tables, equations, and figures.
- Heading groups preserve heading plus nearby explanatory prose.
- Oversized units can be split, with continuation metadata.

Portable value:

- Very high. This is closer to the local wiki's technical atom invariant than
  the row-oriented table atoms in the processing worker.

Local caution:

- Table splitting for oversized tables is acceptable for chunking, but the
  source table should still have one stable technical atom identity. Splits
  should be views or continuations, not independent tables.

### Markdown Table Parsing

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/wiki_core/src/wiki_core/parsing/tables.py`

Learning:

- Table row parsing handles escaped pipes and code spans.
- Separator rows are recognized.
- Markdown link and code-cell targets can be extracted.

Portable value:

- Medium to high. It is a useful pure helper for Markdown-derived sources.

Local caution:

- PDF table reconstruction needs layout-aware extraction before this parser can
  help. This module parses Markdown tables; it does not reconstruct PDF cells.

### Evidence Validation

File:

`/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/wiki_io/src/wiki_io/evidence/validator.py`

Learning:

- Evidence validation distinguishes hard failures from soft locator precision
  issues.
- It canonicalizes only for matching, not for user-facing text.
- It handles page break artifacts, page numbers, Unicode repair, dash variants,
  Markdown table escapes, quotes, trailing ellipses, PDF hyphenation, wrapped
  prose lines, whitespace, and bullet variants.
- It checks exact local match, canonicalized local match, prefix local match,
  nearby window match, and global source match.
- It can suggest a locator when evidence is found elsewhere.

Portable value:

- Very high. This is a strong source-agnostic provenance tool.

Local caution:

- Header/footer removal uses lexical patterns. It is acceptable as a
  validator-normalization aid, but it should not become user-facing source text
  rewriting.

## Pass 3: Systems And Layers

### Contract Boundary System

The contract boundary system has three parts:

- OpenAPI schema as the source of truth.
- Generated Python and TypeScript clients.
- Worker helpers that parse unknown JSON into generated models.

What it solves:

- Shape drift between API, worker, client, and tests.
- Silent acceptance of malformed artifacts.
- Manual port friction between Python and TypeScript code.

Local implication:

- The local wiki should define portable artifact contracts once and parse them
  at boundaries. In-memory domain services can still use richer internal types,
  but artifact shapes should be shared.

### Source-Plan System

The source-plan system decides what pages may be produced before extraction.

What it solves:

- Model-invented pages.
- Model-invented paths.
- Cross-source pages that exist only because two words match.
- Page identity drift when multiple sources mention the same target.

Local implication:

- Our local wiki needs `SourcePlan` as a first-class durable artifact. The LLM
  can propose claims and facts for planned targets; it should not create final
  pages directly.

### Source-Derived Middle Artifact System

The middle artifact system turns source text into inspectable records before
page writing.

It includes:

- `DocumentStructure`
- `ClaimLedger`
- `TopicIndex`
- `SectionPlan`

What it solves:

- Rough summary pages with no audit trail.
- Technical atoms without section context.
- Weak related links that are not connected to source evidence.
- Loss of source structure before projection.

Local implication:

- This aligns with the local Claim-Ledger-First design. We should keep these as
  durable, portable, source-scoped artifacts.

### Projection System

The projection system converts accepted artifacts into staged pages, then lint,
then publish.

What it solves:

- Markdown as the first durable shape.
- Page text that cannot be mapped back to support.
- Related links with no explanation.
- Unvalidated graph edges.

Local implication:

- Our local wiki should preserve the difference between a proposed page, a
  staged page, an accepted page, and a published page.

### Aggregate Page System

The aggregate page system deterministically creates higher-level collection
pages from the current graph.

What it solves:

- Navigation across many entity pages.
- Stale aggregate pages after member changes.
- LLM rewriting of simple index-like pages.

Local implication:

- This is useful if generalized from product categories to source-derived
  collections, concepts, entities, procedures, recipe families, rule systems,
  event networks, and code idiom clusters.

## Portable Features Worth Lifting

### 1. Shared Artifact Contracts

Lift the pattern, not necessarily the exact schema.

The local wiki should have explicit artifact contracts for:

- `SourcePlan`
- `DocumentStructure`
- `ClaimLedger`
- `TopicIndex`
- `SectionPlan`
- `ExtractionResult`
- `StagedWikiPage`
- `ProjectionLint`
- `PublishRun`

Testable hypothesis:

- If every artifact boundary parses into a generated or centrally defined
  contract, then ports between repos become smaller and runtime shape drift
  becomes lint/test failures instead of page quality regressions.

### 2. Source-Plan-Bound Extraction

The local wiki should not let extraction create page identity or path authority.

Testable hypothesis:

- If extraction can target only planned page ids and accepted claim/fact types,
  then duplicate pages, strange pages, and weak cross-source pages decrease.

### 3. DocumentStructure Before Topic Planning

The local wiki should derive parent, child, sibling, section path, reading order,
and source spans before topic planning.

Testable hypothesis:

- If topic planning consumes source-derived structure, then repeated headings
  and same-heading sections can be distinguished without post-hoc duplicate-page
  filters.

### 4. SectionPlan As The Technical Atom Binding Layer

The local wiki should bind technical atoms to pages through section coverage and
explicit support.

Testable hypothesis:

- If technical atom frames require a section-plan binding and local explanatory
  context, then code and table examples appear on concept pages only when the
  source section supports that concept.

### 5. Staged Page Projection

The local wiki should produce a typed staged page before writing Markdown.

Testable hypothesis:

- If all pages pass through `StagedWikiPage` with evidence blocks, technical
  atom frames, related links, and projection metadata, then page lint can catch
  unsupported prose before publish.

### 6. Related Link Support Contract

Related links should carry relation, explanation, and support ids.

Testable hypothesis:

- If related links require shared evidence, shared source structure, or an
  explicit structured relation, then inscrutable lexical cross-links decrease.

### 7. Aggregate Pages With Fingerprints And Retraction

Aggregate pages should be deterministic projections over the graph.

Testable hypothesis:

- If aggregate pages have member fingerprints and retraction, then navigation
  pages remain current without manual cleanup or LLM rewrites.

### 8. Evidence Validator

Evidence excerpts should be validated against the normalized source with
artifact-tolerant canonicalization.

Testable hypothesis:

- If every projected claim has evidence that validates locally or with a
  suggested locator, then fabricated and misplaced citations become measurable
  failures.

### 9. Structural Chunker

The local wiki should preserve block-level units before LLM calls.

Testable hypothesis:

- If code, tables, formulas, equations, and figures enter the pipeline as
  atomic blocks, then technical atom fragmentation decreases.

## Useful With Refactor

### Product Identity Logic

The branch has strong logic for product catalogs:

- manufacturer fields
- model fields
- series fields
- part-number fields
- category paths
- project-location-like heading rejection
- product detail section rejection

This should not be ported directly.

Refactor target:

- Replace hard-coded product identity with a profile-configured
  `EntityIdentityPolicy`.
- Express fields as roles such as identity axis, discriminator, collection axis,
  variant axis, compatibility axis, and detail facet.
- Keep domain-specific product labels in profile data or repository adapters,
  not portable domain logic.

### Projection Filtering

The branch filters product page content so claims about one identity do not leak
onto another identity page.

This is valuable, but the implementation is product-specific.

Refactor target:

- Generalize into `TargetSupportPolicy`.
- The policy should answer whether an evidence item, ledger entry, fact, or
  technical atom supports a target.
- The policy should be driven by target identity fields, section coverage,
  source structure, and category contracts.

### Aggregate Rendering

The aggregate projection system is useful, but the current copy is catalog
oriented.

Refactor target:

- Generalize the renderer to collection pages.
- Drive section names and member grouping from page family, category contracts,
  and profile-defined aggregate contracts.

### Chat Retrieval

The chat agent's index-first and citation-only behavior is useful.

Refactor target:

- Use the local wiki's deterministic search, graph, topic index, and staged page
  metadata rather than keyword-only page search.

## Do Not Port Directly

Do not port these as universal logic:

- Manufacturer/model/series/product-name hard-coded detection.
- Product page hard-coded support filtering.
- US state abbreviation checks for project-location-like headings.
- Door/hardware/product token filters.
- Architecture-catalog wording in aggregate pages.
- Row-granular table atoms as the only table atom representation.
- Old attribution parsing that expects older Markdown claim shapes.
- API route summary assumptions without checking current artifact writers.

These may be valid in that production wiki's domain profile. They are not valid
as local `llm-wiki` core behavior.

## Root Lessons For The Local Wiki

The strongest lesson is preventative architecture.

The external repo avoids many errors by deciding earlier:

- What source is being processed.
- What page targets are allowed.
- What page family each target belongs to.
- What claim and fact types each page accepts.
- What source structure supports each target.
- What evidence is required for each projected item.
- What related links are supported.
- What page path is allowed.

The local wiki should keep improving in the same direction. It should prevent
unsupported pages and links instead of detecting them after Markdown exists.

The second lesson is that middle artifacts are the real wiki authoring surface.
Markdown pages are projections. If the middle artifacts are weak, the pages will
be rough summaries. If the middle artifacts are strong, the pages can become
authoritative references.

The third lesson is that shared contracts make co-evolution practical. Without
shared contracts, both repos can use the same words but carry different artifact
shapes.

## Proposed Local Architecture Direction

The local wiki should keep pure domain modules for:

- source planning
- structure extraction
- technical atom preservation
- claim ledger construction
- topic signal construction
- section plan construction
- target support policy
- staged page projection
- projection lint
- graph/index maintenance

Adapters should own:

- file reads and writes
- PDF extraction
- model calls
- CLI orchestration
- cache paths
- local server and chat API

The portability suite should test pure domain modules with synthetic sources
that rename every domain noun while preserving source categories.

## Further Study

### API Contract Drift

Study whether `packages/api/src/wiki-handlers.ts` still matches the new
projection artifacts.

Questions:

- Is `_route-summary.json` still written by the current pipeline?
- Does attribution parsing still match the deterministic page format?
- Does the API graph endpoint use persisted graph edges or re-extract Markdown
  links?

### Lint Severity Policy

Study the complete lint severity policy in `wiki_projection_lint.py`.

Questions:

- Which findings block publish?
- Which findings only warn?
- How are run-level failures reconciled with incremental per-file publish?

### Large PDF And OCR Routing

Study large PDF preflight and adaptive chunking designs.

Questions:

- Which parts can help local-only ingestion without AWS Batch or Step Functions?
- Can local preflight choose extraction strategy before expensive OCR?
- Can layout density predict chunk sizes for large rulebooks and catalogs?

### Structural Chunker Integration

Study how `packages/wiki_core` chunking relates to the processing worker's
DocumentStructure builder.

Questions:

- Why does the processing worker rebuild structure from Markdown instead of
  using the richer pure chunker?
- Can the local wiki use the richer chunker as the first source-derived
  structure layer?
- Can table row facts become child facts under a full-table technical atom?

### Source Plan Rule Portability

Study how much of `source-plans.ts` is generic rule resolution versus
production-domain classification.

Questions:

- Can source classification be profile-provided or source-derived?
- Can the same planner handle history books, coding books, RPG manuals, product
  catalogs, standards, and news without hard-coded labels?

### Aggregate Contract Generalization

Study category/domain synthesis as a general collection-page system.

Questions:

- What does a generic collection member contract need?
- How should collection pages differ for events, people, code idioms, rules,
  tables, procedures, and products?
- Can retraction and fingerprinting stay identical across all collection types?

## Lookup Index

High-value files:

- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/client-py/src/sdai_llm_wiki_client/types.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/worker_contracts.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/node/src/wiki-api/source-plans.ts`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/node/src/wiki-api/page-path-projection.ts`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/source_plan_bound_extraction.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/source_plan_extraction_worker.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/claim_ledger_topic_index.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_page_projection.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_projection_lint.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_projection_publish.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_aggregate_projection.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/workers/wiki_maintenance_artifacts.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/wiki_core/src/wiki_core/parsing/chunking.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/wiki_core/src/wiki_core/parsing/tables.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/wiki_io/src/wiki_io/evidence/validator.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/chat-agent/src/agentic-loop.ts`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/chat-agent/src/agentic-loop-streaming.ts`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/packages/api/src/wiki-handlers.ts`

High-value tests:

- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/tests/test_source_plan_extraction_worker.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/tests/test_wiki_page_projection.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/tests/test_wiki_aggregate_projection.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/tests/test_claim_ledger_topic_index_identity.py`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/infra/processing-service/lambda/python/tests/test_claim_ledger_topic_index_labels.py`

High-value docs:

- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/docs/processing-service/README.md`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/docs/processing-service/designs/category-and-domain-synthesis.md`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/docs/processing-service/designs/content-addressed-layer-artifacts.md`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/docs/processing-service/designs/large-file-processing.md`
- `/Users/DSerbarinov/gits/SDAI-LLM-Wiki/docs/processing-service/designs/wiki-index-quality-improvements.md`

## Alignment With The Local LLM-Wiki Pattern

This study preserves raw sources as immutable reference material.

It improves the generated wiki layer by identifying source-derived middle
artifacts that can make pages more authoritative.

It supports query quality by pointing toward deterministic retrieval,
walkability, and evidence-backed related links.

It supports lint by identifying contract, projection, and graph checks that can
catch drift before bad pages become durable.

It keeps `index.md` and `log.md` out of scope because this is a docs research
artifact, not a source ingestion or wiki projection run.
