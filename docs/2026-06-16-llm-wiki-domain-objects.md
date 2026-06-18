# LLM-Wiki Domain Objects - TDD (2026-06-16)

This TDD describes the domain objects for LLM-Wiki.
The application must support real-time wiki creation from user-supplied sources and configuration.

## Application Boundary

The projection pipeline is shared by all wikis.
It must not contain hardcoded rules for architecture, physics, tabletop RPGs, plumbing codes, or any other wiki type.

The reusable pipeline shape is:

```
SourceBundle
-> IngestRun
-> SourcePlans
-> Evidence and Claim extraction
-> WikiPage projection
-> CrossReference, Index, and Log updates
-> LintRun
```

Wiki-specific behavior enters through three user-facing configuration objects:

- `Schema` declares `PageKind`, `PageMetadataFields`, `PageContracts`, `Defaults`, `LintRunRules`, and workflow rules.
- `WikiStructure` declares `PathTemplate` rules that render `PagePath` values from `PageMetadata`.
- `ExtractionPrompt` declares what the user wants extracted, preserved, ignored, routed, verified, and deferred for this run.

`IngestRun` must create `PageMetadata` and `PagePath` from the same resolved page description.
`PagePath` is a rendered location, not a source of application meaning.

Architecture-wiki is a specific wiki configuration, not the definition of the pipeline.
Its domains, product layers, manufacturer conventions, source summaries, `_schema.yaml` contracts, and routing rules belong in `WikiStructure`, `Schema`, and `ExtractionPrompt`.
They must not be hardcoded in projection pipeline code.

The flat local LLM-Wiki is the minimal configuration.
A physics textbook wiki, a tabletop RPG wiki, and a plumbing code wiki require different configuration objects, not different projection code.

## First-Class Objects

`RawSource`
One immutable input item: book, article, PDF, image set, data file, transcript, or similar.

`SourceBundle`
A collection of one or more `RawSource` objects selected as a unit for unattended ingestion.
Single-source ingest is represented as a one-member `SourceBundle`.

`Wiki`
The persistent generated knowledge base for a purpose, project, or area of inquiry.
It has exactly one `CurrentStructure` at any point in time.

`Schema`
The operating contract for the projection pipeline.
It defines `Defaults`, `PageKind`, `PageMetadataFields`, `PageContracts`, workflow rules, and `LintRunRules`.

`WikiStructure`
The path-template set used by a `Wiki`.
It renders `PagePath` from `PageMetadata`.

`Topic`
A subject discovered, maintained, linked, or gap-flagged inside the generated wiki.

`ExtractionPrompt`
The preconfigured ingestion prompt for a source bundle.
It records what to extract, ignore, route, preserve, verify, and defer.

`IngestRun`
A recorded unattended application of one `ExtractionPrompt` to one `SourceBundle`.
It resolves the effective `Schema`, `WikiStructure`, and `ExtractionPrompt`, then applies the projection pipeline.

`WikiPage`
One generated markdown page in the wiki.
Its `PageMetadata` carries its stable identity, page kind, schema binding, and queryable fields.
Its `PagePath` is rendered from `PageMetadata` by `WikiStructure`.

`PageKind`
The role of a wiki page.
Examples include `source-summary`, `entity`, `concept`, `comparison`, `overview`, `synthesis`, and query-derived analysis.

`Claim`
A maintained knowledge statement inside the wiki.
Claims can be supported, contradicted, stale, uncertain, or gap-flagged.

`Evidence`
The citation or provenance link from a claim or page back to source material.

`CrossReference`
A maintained relationship among pages, topics, entities, claims, and sources.

`Index`
Content-oriented navigation over wiki pages.

`Log`
Chronological audit trail of ingests, queries, lint passes, failures, and notable decisions.

`QueryRun`
A question asked against the wiki that may produce an answer or a new wiki page.

`LintRun`
A maintenance pass over the wiki that produces findings and follow-up work.

`LintFinding`
One maintenance issue found during lint.
Examples include contradiction, stale claim, orphan page, missing page, missing cross-reference, and data gap.

## Second-Class Objects

Second-class objects are structured supporting objects.
They may be persisted or rendered, but they should not be lifecycle roots.
Their identity is subordinate to a first-class object.

Diagrams mark shared supporting objects with `[shared]`.
Relationship properties should use the target object name, pluralized when the property is a collection.
Use a role qualifier only when the role matters, such as `CurrentStructure -> WikiStructure` or `DefaultStructure -> WikiStructure`.

### RawSource

```
RawSource
|-- SourceLocator
|-- SourceFormat
|-- SourceContent
|-- SourceAsset [shared]
`-- ImmutabilityRule [shared]
```

`ImmutabilityRule` prevents generated wiki updates from mutating source material.

### SourceBundle

```
SourceBundle
`-- RawSources -> RawSource [shared]
```

Member count is derived from the collection length.
Prompt choice, topology, planning, execution, and completion reporting belong to `IngestRun`, not `SourceBundle`.

### Wiki

```
Wiki
|-- WikiPages -> WikiPage [shared]
|-- CurrentStructure -> WikiStructure [shared]
|-- CrossReferences -> CrossReference [shared]
|-- Index -> Index [shared]
|-- Log -> Log [shared]
|-- LintFindings -> LintFinding [shared]
`-- VersionHistory
```

`CurrentStructure` is the single effective `WikiStructure` for `PagePath` rendering, navigation, and lint.
The structure may be revised over time, but only one structure governs the wiki at once.

### Schema

```
Schema
|-- DefaultStructure -> WikiStructure [shared]
|-- DefaultExtractionPrompt -> ExtractionPrompt [shared]
|-- PageKinds -> PageKind [shared]
|-- PageMetadataFields
|-- PageContracts
|-- Defaults
|-- IngestRunRules -> IngestRun [shared]
|-- QueryRunRules -> QueryRun [shared]
|-- LintRunRules -> LintRun [shared]
`-- CrossReferenceRules -> CrossReference [shared]
```

The minimal default is flat markdown files in a wiki folder.

### WikiStructure

```
WikiStructure
|-- DefaultPathTemplate -> PathTemplate
`-- PathTemplates -> PathTemplate
```

`WikiStructure` is declarative.
It is a set of `PathTemplate` rules.
It is not a separate ontology.
It is not a placement algorithm.
`IngestRun` creates `PageMetadata` first, then `WikiStructure` renders `PagePath`.

Architecture-wiki's `_schema.yaml` files are an example of `LocalSchema`.

### PathTemplate

```
PathTemplate
|-- TemplateText
|-- MatchPageKinds -> PageKind [shared]
|-- MatchPageMetadata
|-- RequiredPageMetadataFields
`-- LocalSchema -> Schema [shared]
```

`PathTemplate` renders one `PagePath` from one `PageMetadata` object.
`TemplateText` uses named fields from `PageMetadata`.
`MatchPageKinds` and `MatchPageMetadata` decide whether the template applies.
`RequiredPageMetadataFields` lists the fields needed to render the template.

### Topic

```
Topic
|-- TopicSummary -> WikiPage [shared]
|-- Claims -> Claim [shared]
|-- CrossReferences -> CrossReference [shared]
|-- Evidence -> Evidence [shared]
`-- LintFindings -> LintFinding [shared]
```

`Topic` is generated, linked, or gap-flagged by ingest, query, and lint.
It is not required setup input.

### ExtractionPrompt

```
ExtractionPrompt
|-- InstructionText
|-- WikiStructureGuidance -> WikiStructure [shared]
|-- PageKindGuidance -> PageKind [shared]
|-- RawSourceGuidance -> RawSource [shared]
|-- UncertaintyPolicy
|-- VariantPolicy
|-- OutputPageKinds -> PageKind [shared]
`-- DeferredQueryRuns -> QueryRun [shared]
```

`InstructionText` is the natural-language ingestion prompt.
Routing, page-role, source-use, uncertainty, and variant guidance may be derived from it as structured facets.
The instruction text remains the source of truth.

In the architecture-wiki migration case, this is where instructions such as "use only uploaded source content," "route only into locked folders," "preserve `[verify]` flags," and "do not explode variants unless the source presents separately selectable families" belong.

### IngestRun

```
IngestRun
|-- SourceBundle -> SourceBundle [shared]
|-- Wiki -> Wiki [shared]
|-- Schema -> Schema [shared]
|-- WikiStructure -> WikiStructure [shared]
|-- ExtractionPrompt -> ExtractionPrompt [shared]
|-- IngestTopology
|-- SourcePlans -> SourcePlan
|   |-- RawSource -> RawSource [shared]
|   |-- SourceClassification
|   |-- IngestDisposition
|   |-- TargetPageMetadata -> PageMetadata [shared]
|   |-- TargetPagePaths
|   |-- ExpectedWikiPages -> WikiPage [shared]
|   `-- HandlingNotes
|-- Placement -> WikiStructure [shared]
|-- WikiPages -> WikiPage [shared]
|-- Index -> Index [shared]
|-- Log -> Log [shared]
`-- CrossReferences -> CrossReference [shared]
```

`Wiki`, `Schema`, `WikiStructure`, and `ExtractionPrompt` record the resolved configuration for reproducibility.
`SourcePlans` are run-owned per-source projection plans.
`SourcePlan` is the TDD name for the planning data that architecture-wiki stored as sidecars.
`SourcePlan` records classification, disposition, `TargetPageMetadata`, `TargetPagePaths`, expected pages, and handling notes before page projection begins.
`IngestRun` produces `SourcePlans` from `SourceBundle`, `Schema`, `WikiStructure`, and `ExtractionPrompt`.

`IngestTopology` has exactly two values:

- `serial` -- process each member through classify, extract, write, log, and lint before starting the next member.
- `wavefront` -- classify and plan the bundle first, then process members in dependency-aware waves with a lint or reconciliation gate after each wave.

There is no third topology in the core model.
A scaled implementation still presents staged member results as wavefront ingestion.
Member results are reduced through ordered write and lint gates.

`Placement`, `WikiPages`, `Index`, `Log`, and `CrossReferences` record the run's outputs.

### WikiPage

```
WikiPage
|-- PageMetadata -> PageMetadata [shared]
|-- PagePath
|-- PageTitle
|-- PageBody
|-- Index -> Index [shared]
|-- CrossReferences -> CrossReference [shared]
|-- Claims -> Claim [shared]
`-- Evidence -> Evidence [shared]
```

`PagePath` is the page's rendered relative location inside the wiki.
It may be a flat slug such as `javascriptallonge.md`.
It may be a hierarchical path such as `finishes/floor-finishes/rubber-sheet/nora-rubber-sheet-bod.md`.
Changing `WikiStructure` should not change `PageId`.

### PageMetadata

```
PageMetadata
|-- PageId
|-- PageKind -> PageKind [shared]
|-- SchemaId
|-- Domain
|-- CategoryPath
|-- ProjectId
|-- SourceId
|-- Tags
`-- Aliases
```

`PageMetadata` stores the queryable fields for a `WikiPage`.
`Schema` defines which `PageMetadataFields` are allowed or required for each `PageKind`.
`WikiStructure` reads `PageMetadata` to render `PagePath`.
`Index` reads `PageMetadata` so queries do not infer meaning from `PagePath`.

### PageKind

```
PageKind
|-- KindName
|-- Schema -> Schema [shared]
|-- QueryRuns -> QueryRun [shared]
|-- WikiStructure -> WikiStructure [shared]
|-- Index -> Index [shared]
`-- LintRuns -> LintRun [shared]
```

`Schema` defines the contract for pages of that kind.
`Schema` uses `PageKind` to select required `PageMetadataFields` and `PageContracts`.
`WikiStructure` constrains how a `PageKind` renders to `PagePath`.

### Claim

```
Claim
|-- Statement
|-- ClaimStatus
|-- Evidence -> Evidence [shared]
|-- LintFindings -> LintFinding [shared]
|-- WikiPage -> WikiPage [shared]
`-- CrossReferences -> CrossReference [shared]
```

`ClaimStatus` records support, uncertainty, contradiction, staleness, or gap state.

### Evidence

```
Evidence
|-- RawSource -> RawSource [shared]
|-- WikiPage -> WikiPage [shared]
|-- SourceAsset -> SourceAsset [shared]
|-- QueryRun -> QueryRun [shared]
`-- Claim -> Claim [shared]
```

`Evidence` links wiki knowledge back to source material for a claim, page, or query answer.

### CrossReference

```
CrossReference
|-- FromPage -> WikiPage [shared]
|-- ToPage -> WikiPage [shared]
|-- ToTopic -> Topic [shared]
|-- ToClaim -> Claim [shared]
|-- LinkText
|-- InboundLinkState
`-- LintFindings -> LintFinding [shared]
```

`InboundLinkState` supports orphan detection.

### Index

```
Index
|-- IndexEntry
|   |-- WikiPage -> WikiPage [shared]
|   |-- OneLineSummary
|   |-- PageMetadata
|   `-- EntryMetadata
|-- PageKinds -> PageKind [shared]
`-- QueryRuns -> QueryRun [shared]
```

`Index` queries use `PageMetadata` instead of `PagePath`.
`EntryMetadata` can include dates, source counts, status, or display hints.

### Log

```
Log
|-- LogEntry
|   |-- Timestamp
|   |-- IngestRun -> IngestRun [shared]
|   |-- QueryRun -> QueryRun [shared]
|   |-- LintRun -> LintRun [shared]
|   |-- SubjectLabel
|   `-- ParseablePrefix
`-- RecentActivityWindow
```

`ParseablePrefix` gives entries a stable shape for tooling.
`RecentActivityWindow` helps runs account for recent changes.

### QueryRun

```
QueryRun
|-- UserQuestion
|-- RelevantWikiPages -> WikiPage [shared]
|-- AnswerWikiPage -> WikiPage [shared]
|-- PageKind -> PageKind [shared]
|-- Evidence -> Evidence [shared]
`-- CrossReferences -> CrossReference [shared]
```

`QueryRun` reads the wiki and may write an answer back as a page with its own `PageKind`, evidence, and cross-references.

### LintRun

```
LintRun
|-- Wiki -> Wiki [shared]
|-- LintChecklist
|-- LintFindings -> LintFinding [shared]
|-- SuggestedQueryRuns -> QueryRun [shared]
|-- SuggestedRawSources -> RawSource [shared]
`-- WikiPages -> WikiPage [shared]
```

`LintRun` checks consistency, coverage, provenance, and graph health.
It can suggest follow-up queries or missing sources.

### LintFinding

```
LintFinding
|-- FindingType
|-- WikiPage -> WikiPage [shared]
|-- Claim -> Claim [shared]
|-- CrossReference -> CrossReference [shared]
|-- Topic -> Topic [shared]
`-- ResolutionRuns -> IngestRun [shared] / QueryRun [shared] / LintRun [shared]
```

`ResolutionRuns` records the operation that addressed it.

## Structure Examples

`WikiStructure` makes both simple and opinionated wikis valid under the same domain model.

### Local LLM-Wiki Default

The minimal structure is flat:

```
wiki/
|-- <page-slug>.md
|-- index.md
`-- log.md
```

The default has one root `StructureNode`.
`PageKind` is stored in `PageMetadata`, not encoded in `PagePath`.
`WikiStructure` renders `PagePath` from `PageMetadata`.

Example:

```
page_kind=concept
page_id=javascript-allonge
schema_id=concept

-> javascript-allonge.md
```

### Architecture-Wiki

The legacy architecture-wiki demonstrates a richer structure:

```
wiki/
|-- overview/
|-- selection-guides/
|-- finishes/
|-- lighting/
|-- doors/
|   |-- hardware.md
|   `-- hardware/
|       |-- auto-operators.md
|       |-- auto-operators/
|       |   |-- _schema.yaml
|       |   `-- <product>.md
|       `-- <other-category>/
|-- ceilings/
|-- casework/
|-- interiors/
|-- concepts/
|-- sources/
|-- projects/
|-- prompts/
`-- raw/
```

Some structure is explicit.
`Schema` names `PageKind`, `PageMetadataFields`, `PageContracts`, and local schema contracts.
`WikiStructure` names top-level domains, source-summary folders, project folders, and `PathTemplate` rules.

Some structure is emergent.
`IngestRun` can produce `SourcePlan.TargetPageMetadata` for a product category that is not already represented by `Index`.
`WikiStructure` renders the new category `PagePath`.
`Index` and `Log` make the new category durable.

`IngestRun` writes `PageMetadata` and `PagePath` from the same resolved page description.
`PageMetadata` carries application meaning.
`PagePath` is the rendered location.

Product example:

```
page_kind=product
domain=doors
category_path=hardware/closers
page_id=lcn-4040xp
schema_id=door_hardware_product

-> doors/hardware/closers/lcn-4040xp.md
```

Project example:

```
page_kind=project
project_id=bradley-hospital-irl
page_id=bradley-hospital-irl
schema_id=architecture_project

-> projects/bradley-hospital-irl.md
```

Manufacturer is `PageMetadata`, not `PagePath`.
In architecture-wiki, `PagePath` reflects product function rather than corporate ownership.
The same `RawSource` ingested into the flat default wiki and architecture-wiki produces different `PagePath` values while preserving `PageMetadata`, `Claim`, `Evidence`, and `CrossReference`.

## Concrete Architecture-Wiki Migration Example

This example configures LLM-Wiki for functional parity with architecture-wiki.
Architecture-wiki `PagePath` rules become `WikiStructure`.
Architecture-wiki sidecars become `SourcePlans`.
Architecture-wiki prompts become `ExtractionPrompt`.
Architecture-wiki `_schema.yaml` `PageContracts` become `Schema`.
Architecture-wiki `index.md` becomes `Index`.
Architecture-wiki `log.md` becomes `Log`.
Architecture-wiki `/sources/*.md` pages become generated `WikiPage` objects with `PageKind: source-summary`.
Architecture-wiki `/sources/*.md` frontmatter becomes `PageMetadata`, `Evidence`, and `Log` output from `IngestRun`.

### Concrete First-Class Objects

`RawSource`

```yaml
RawSource:
  RawSourceId: rawsource-hes-2026-catalog-pdf
  SourceLocator: s3://sdai-raw-catalog/HES_2026_Catalog.pdf
  SourceFormat: pdf
  SourceContent: binary-pdf
  SourceAsset:
    SourceLocator: s3://sdai-raw-catalog/HES_2026_Catalog.pdf
    PageRange: 1-110
  ImmutabilityRule: immutable-after-IngestRun-start
```

`SourceBundle`

```yaml
SourceBundle:
  SourceBundleId: architecture-wiki-door-hardware-source-bundle-001
  RawSources:
    - s3://sdai-raw-catalog/HES_2026_Catalog.pdf
    - s3://sdai-raw-catalog/Von_Duprin_Electrical_Security_Products_Catalog_109981.pdf
    - s3://sdai-raw-catalog/Schlage_L_Series_Catalog.pdf
```

`Wiki`

```yaml
Wiki:
  WikiId: architecture-wiki-migration
  CurrentStructure: architecture-wiki-structure-v1
  WikiPages:
    - sources/hes-2026-catalog.md
    - doors/hardware/electric-strikes.md
    - doors/hardware/electric-strikes/hes-1006-series.md
  CrossReferences: architecture-wiki-crossreferences
  Index: architecture-wiki-index
  Log: architecture-wiki-log
  LintFindings: architecture-wiki-lintfindings
  VersionHistory:
    - architecture-wiki-import-v1
```

`Schema`

```yaml
Schema:
  SchemaId: architecture-wiki-schema-v1
  DefaultStructure: architecture-wiki-structure-v1
  DefaultExtractionPrompt: architecture-wiki-pdf-ingest
  PageKinds:
    - source-summary
    - domain-overview
    - category
    - product
    - concept
    - project
    - submittal-checklist
    - selection-guide
    - lesson-learned
  PageMetadataFields:
    - page_id
    - page_kind
    - schema_id
    - domain
    - category_path
    - source_id
    - project_id
    - manufacturer
    - tags
    - aliases
  PageContracts:
    product:
      RequiredPageMetadataFields:
        - page_id
        - page_kind
        - schema_id
        - domain
        - category_path
      RequiredClaimTypes:
        - product_identity
        - application
        - source_grounding
      RequiredEvidence: true
    source-summary:
      RequiredPageMetadataFields:
        - page_id
        - page_kind
        - source_id
      RequiredEvidence: true
  Defaults:
    PageKind: source-summary
    ClaimStatus: uncertain-until-supported
  IngestRunRules:
    IngestTopology: wavefront
    RequireSourcePlan: true
  QueryRunRules:
    RequireIndexFirst: true
  LintRunRules:
    RequireEvidenceForClaim: true
    RequireIndexEntryForWikiPage: true
```

`WikiStructure`

```yaml
WikiStructure:
  StructureId: architecture-wiki-structure-v1
  DefaultPathTemplate:
    MatchPageKinds:
      - concept
    TemplateText: "{page_id}.md"
  PathTemplates:
    - MatchPageKinds: [source-summary]
      RequiredPageMetadataFields: [source_id]
      TemplateText: "sources/{source_id}.md"
    - MatchPageKinds: [domain-overview]
      RequiredPageMetadataFields: [domain]
      TemplateText: "{domain}/index.md"
    - MatchPageKinds: [category]
      RequiredPageMetadataFields: [domain, category_path]
      TemplateText: "{domain}/{category_path}.md"
    - MatchPageKinds: [product]
      RequiredPageMetadataFields: [domain, category_path, page_id]
      TemplateText: "{domain}/{category_path}/{page_id}.md"
    - MatchPageKinds: [concept]
      RequiredPageMetadataFields: [page_id]
      TemplateText: "concepts/{page_id}.md"
    - MatchPageKinds: [project]
      RequiredPageMetadataFields: [project_id]
      TemplateText: "projects/{project_id}.md"
    - MatchPageKinds: [submittal-checklist]
      RequiredPageMetadataFields: [page_id]
      TemplateText: "checklists/submittals/{page_id}.md"
```

`Topic`

```yaml
Topic:
  TopicId: electric-strikes
  TopicSummary: doors/hardware/electric-strikes.md
  Claims:
    - claim-hes-1006-routes-to-electric-strikes
  CrossReferences:
    - xref-hes-1006-to-electric-strikes
  Evidence:
    - evidence-hes-2026-catalog-pdf
  LintFindings:
    - lintfinding-hes-1006-warranty-gap
```

`ExtractionPrompt`

```yaml
ExtractionPrompt:
  PromptId: architecture-wiki-pdf-ingest
  InstructionText: |
    Use RawSource content only.
    Use WikiStructure as locked routing.
    Use Schema PageContracts for WikiPage validation.
    Use PageMetadata.manufacturer for manufacturer.
    Do not place manufacturer in PagePath.
    Preserve verify flags as ClaimStatus.
    Preserve route gaps as LintFinding.
    Create one source-summary WikiPage for each RawSource.
    Create product WikiPages only from RawSource-supported product evidence.
  WikiStructureGuidance: architecture-wiki-structure-v1
  PageKindGuidance:
    product: manufacturer product, product family, series, or selectable system
    category: functional category page
    concept: standard, metric, code topic, method, compatibility rule, or selection principle
    source-summary: one WikiPage per RawSource
  RawSourceGuidance:
    pdf: extract document title, publisher, file name, page coverage, product families, open items, and provenance into source-summary WikiPage
  UncertaintyPolicy: preserve-verify-flags
  VariantPolicy: keep-variants-on-most-specific-product-WikiPage
  OutputPageKinds:
    - source-summary
    - category
    - product
    - concept
```

`IngestRun`

```yaml
IngestRun:
  IngestRunId: architecture-wiki-door-hardware-wave-001
  SourceBundle: architecture-wiki-door-hardware-source-bundle-001
  Wiki: architecture-wiki-migration
  Schema: architecture-wiki-schema-v1
  WikiStructure: architecture-wiki-structure-v1
  ExtractionPrompt: architecture-wiki-pdf-ingest
  IngestTopology: wavefront
  SourcePlans:
    - sourceplan-hes-2026-catalog
  Placement: architecture-wiki-structure-v1
  WikiPages:
    - sources/hes-2026-catalog.md
    - doors/hardware/electric-strikes/hes-1006-series.md
  Index: architecture-wiki-index
  Log: architecture-wiki-log
  CrossReferences:
    - xref-hes-1006-to-electric-strikes
```

`SourcePlan`

```yaml
SourcePlan:
  SourcePlanId: sourceplan-hes-2026-catalog
  RawSource: rawsource-hes-2026-catalog-pdf
  SourceClassification:
    SourceFormat: pdf
    SourceKind: manufacturer-catalog-pdf
    Domains:
      - doors
    CandidatePageKinds:
      - source-summary
      - category
      - product
  IngestDisposition: project-to-WikiPage
  TargetPageMetadata:
    - PageId: hes-2026-catalog
      PageKind: source-summary
      SchemaId: architecture-wiki-schema-v1
      SourceId: hes-2026-catalog
    - PageId: hes-1006-series
      PageKind: product
      SchemaId: architecture-wiki-schema-v1
      Domain: doors
      CategoryPath: hardware/electric-strikes
      SourceId: hes-2026-catalog
  TargetPagePaths:
    - sources/hes-2026-catalog.md
    - doors/hardware/electric-strikes/hes-1006-series.md
  ExpectedWikiPages:
    - sources/hes-2026-catalog.md
    - doors/hardware/electric-strikes/hes-1006-series.md
  HandlingNotes:
    - Create source-summary WikiPage from RawSource.
    - Use extracted product names as CrossReference candidates.
    - Preserve verify flags as ClaimStatus.
    - Preserve missing warranty as LintFinding.
```

`WikiPage`

```yaml
WikiPage:
  PageMetadata:
    PageId: hes-2026-catalog
    PageKind: source-summary
    SchemaId: architecture-wiki-schema-v1
    SourceId: hes-2026-catalog
    Domain: doors
    Tags:
      - electric-strike
      - hes
      - assa-abloy
      - folger-adam
      - source
      - catalog
  PagePath: sources/hes-2026-catalog.md
  PageTitle: HES 2026 Electric Strikes and Cabinet Locks Catalog
  PageBody: generated source-summary WikiPage
  Claims:
    - claim-hes-catalog-pages-1-110-ingested
  Evidence:
    - evidence-hes-2026-catalog-pdf
  CrossReferences:
    - xref-hes-source-to-hes-1006
```

`WikiPage`

```yaml
WikiPage:
  PageMetadata:
    PageId: hes-1006-series
    PageKind: product
    SchemaId: architecture-wiki-schema-v1
    Domain: doors
    CategoryPath: hardware/electric-strikes
    SourceId: hes-2026-catalog
    Tags:
      - door-hardware
      - electric-strikes
    Aliases:
      - HES 1006 Series
  PagePath: doors/hardware/electric-strikes/hes-1006-series.md
  PageTitle: HES 1006 Series
  PageBody: source-grounded product WikiPage
  Claims:
    - claim-hes-1006-routes-to-electric-strikes
  Evidence:
    - evidence-hes-2026-catalog-pdf
  CrossReferences:
    - xref-hes-1006-to-electric-strikes
```

`PageKind`

```yaml
PageKind:
  KindName: product
  Schema: architecture-wiki-schema-v1
  WikiStructure: architecture-wiki-structure-v1
  Index: architecture-wiki-index
  LintRuns:
    - lintrun-architecture-wiki-door-hardware-wave-001
```

`Claim`

```yaml
Claim:
  ClaimId: claim-hes-1006-routes-to-electric-strikes
  Statement: HES 1006 Series is represented by product WikiPage doors/hardware/electric-strikes/hes-1006-series.md.
  ClaimStatus: supported
  Evidence: evidence-hes-2026-catalog-pdf
  WikiPage: doors/hardware/electric-strikes/hes-1006-series.md
  CrossReferences:
    - xref-hes-1006-to-electric-strikes
```

`Evidence`

```yaml
Evidence:
  EvidenceId: evidence-hes-2026-catalog-pdf
  RawSource: rawsource-hes-2026-catalog-pdf
  WikiPage: sources/hes-2026-catalog.md
  SourceAsset: s3://sdai-raw-catalog/HES_2026_Catalog.pdf
  Claim: claim-hes-catalog-pages-1-110-ingested
```

`CrossReference`

```yaml
CrossReference:
  CrossReferenceId: xref-hes-1006-to-electric-strikes
  FromPage: doors/hardware/electric-strikes/hes-1006-series.md
  ToPage: doors/hardware/electric-strikes.md
  ToTopic: electric-strikes
  ToClaim: claim-hes-1006-routes-to-electric-strikes
  LinkText: "[[doors/hardware/electric-strikes]]"
  InboundLinkState: linked
```

`Index`

```yaml
Index:
  IndexId: architecture-wiki-index
  IndexEntry:
    - WikiPage: sources/hes-2026-catalog.md
      OneLineSummary: HES 2026 Catalog generated source-summary WikiPage.
      PageMetadata:
        PageId: hes-2026-catalog
        PageKind: source-summary
        SourceId: hes-2026-catalog
    - WikiPage: doors/hardware/electric-strikes/hes-1006-series.md
      OneLineSummary: HES 1006 Series product WikiPage.
      PageMetadata:
        PageId: hes-1006-series
        PageKind: product
        Domain: doors
        CategoryPath: hardware/electric-strikes
  PageKinds:
    - source-summary
    - product
```

`Log`

```yaml
Log:
  LogId: architecture-wiki-log
  LogEntry:
    - Timestamp: 2026-06-18T00:00:00Z
      IngestRun: architecture-wiki-door-hardware-wave-001
      SubjectLabel: hes-2026-catalog
      ParseablePrefix: ingest
  RecentActivityWindow:
    IngestRuns:
      - architecture-wiki-door-hardware-wave-001
```

`QueryRun`

```yaml
QueryRun:
  QueryRunId: queryrun-electric-strike-options
  UserQuestion: What electric strike WikiPages exist in architecture-wiki?
  RelevantWikiPages:
    - doors/hardware/electric-strikes.md
    - doors/hardware/electric-strikes/hes-1006-series.md
  AnswerWikiPage: selection-guides/electric-strike-options.md
  PageKind: selection-guide
  Evidence:
    - evidence-hes-2026-catalog-pdf
  CrossReferences:
    - xref-hes-1006-to-electric-strikes
```

`LintRun`

```yaml
LintRun:
  LintRunId: lintrun-architecture-wiki-door-hardware-wave-001
  Wiki: architecture-wiki-migration
  LintChecklist:
    - every WikiPage has PageMetadata
    - every product WikiPage has Evidence
    - every WikiPage has IndexEntry
    - every PagePath matches WikiStructure
  LintFindings:
    - lintfinding-hes-1006-warranty-gap
  SuggestedQueryRuns:
    - queryrun-electric-strike-options
  SuggestedRawSources: []
  WikiPages:
    - doors/hardware/electric-strikes/hes-1006-series.md
```

`LintFinding`

```yaml
LintFinding:
  LintFindingId: lintfinding-hes-1006-warranty-gap
  FindingType: data-gap
  WikiPage: doors/hardware/electric-strikes/hes-1006-series.md
  Claim: null
  CrossReference: xref-hes-1006-to-electric-strikes
  Topic: electric-strikes
  ResolutionRuns:
    - lintrun-architecture-wiki-door-hardware-wave-001
```

### Concrete Reusable Pipeline

`SourceBundle`

Preconditions:

- `RawSource` exists.
- `SourceBundle.RawSources` contains one or more `RawSource`.
- `RawSource.ImmutabilityRule` is active.

Postconditions:

- `SourceBundle` is ready for `IngestRun`.
- `SourceBundle.RawSources` is the complete input set for `IngestRun`.

`IngestRun`

Preconditions:

- `SourceBundle` exists.
- `Wiki` exists.
- `Schema` exists.
- `WikiStructure` exists.
- `ExtractionPrompt` exists.

Postconditions:

- `IngestRun` records `SourceBundle`, `Wiki`, `Schema`, `WikiStructure`, and `ExtractionPrompt`.
- `IngestRun.IngestTopology` is `wavefront`.
- `Log` contains an `IngestRun` start `LogEntry`.

`SourcePlans`

Preconditions:

- `IngestRun` exists.
- `SourceBundle.RawSources` exists.
- `Schema.PageKinds` exists.
- `Schema.PageContracts` exists.
- `WikiStructure.PathTemplates` exists.
- `ExtractionPrompt.InstructionText` exists.

Postconditions:

- `SourcePlans` contains one `SourcePlan` per staged `RawSource`.
- `SourcePlan.TargetPageMetadata` exists.
- `SourcePlan.TargetPagePaths` exists.
- `SourcePlan.ExpectedWikiPages` exists.

`Evidence and Claim extraction`

Preconditions:

- `SourcePlans` exists.
- `SourcePlan.RawSource` exists.
- `SourcePlan.IngestDisposition` permits projection.
- `Schema.PageContracts` exists.

Postconditions:

- `Evidence` exists for supported `Claim`.
- `Claim` exists for source-grounded statements.
- `Claim.ClaimStatus` records supported, uncertain, contradicted, stale, or gap-flagged status.
- `LintFinding` exists for unresolved `Schema.PageContracts`.

`WikiPage projection`

Preconditions:

- `Claim` exists.
- `Evidence` exists.
- `SourcePlan.TargetPageMetadata` exists.
- `WikiStructure.PathTemplates` exists.
- `Schema.PageContracts` exists.

Postconditions:

- `WikiPage` exists for each projected `PageMetadata`.
- `WikiPage.PagePath` is rendered by `WikiStructure`.
- `WikiPage.PageMetadata` satisfies `Schema.PageContracts` or produces `LintFinding`.
- `WikiPage.Claims` references `Claim`.
- `WikiPage.Evidence` references `Evidence`.

`CrossReference, Index, and Log updates`

Preconditions:

- `WikiPage` exists.
- `WikiPage.PageMetadata` exists.
- `Claim` exists.
- `Evidence` exists.

Postconditions:

- `CrossReference` exists for wikilinks and `Topic` relationships.
- `Index.IndexEntry` exists for each `WikiPage`.
- `Log.LogEntry` records `IngestRun` output.
- `Wiki.CrossReferences`, `Wiki.Index`, and `Wiki.Log` reference the updates.

`LintRun`

Preconditions:

- `Wiki` exists.
- `Schema` exists.
- `WikiStructure` exists.
- `Wiki.WikiPages` exists.
- `Index` exists.
- `Log` exists.

Postconditions:

- `LintRun` exists.
- `LintFinding` exists for missing `Evidence`, invalid `PagePath`, missing `IndexEntry`, orphan `CrossReference`, unresolved `ClaimStatus`, or missing `Schema.PageContracts`.
- `Log` contains a `LintRun` `LogEntry`.
- `SuggestedQueryRuns` and `SuggestedRawSources` record follow-up work.

## Wiki Creation by Ingest

A user creates a wiki by triggering an unattended `IngestRun` with a `SourceBundle`.
The run must resolve three configuration objects before writing:

- `Schema` -- the schema version that provides defaults, constraints, and workflow rules.
- `WikiStructure` -- either a user-supplied structure or the schema's `DefaultStructure`.
- `ExtractionPrompt` -- either a user-supplied prompt or the schema's `DefaultExtractionPrompt`.

`IngestRun` derives `PageMetadata` under the selected `Schema`.
`WikiStructure` renders `PagePath` from `PageMetadata`.
The same `PageMetadata` drives `Index` queries, `LintRun`, schema validation, and `PagePath` rendering.
Application logic should query `PageMetadata` and `Index`, not parse `PagePath`.

The minimal `WikiStructure` default is flat markdown files in one wiki folder plus reserved navigation files.
The user's subject intent is part of `ExtractionPrompt`.
Concrete `Topic` objects are generated, linked, or gap-flagged as outputs of ingest and lint.

For different wiki types, only configuration changes:

- A physics textbook wiki changes `WikiStructure`, `PageKind`, equation or derivation `PageContracts`, and `ExtractionPrompt`.
- A tabletop RPG wiki changes `WikiStructure`, `PageKind`, rule or entity `PageContracts`, and `ExtractionPrompt`.
- A plumbing code wiki changes `WikiStructure`, `PageKind`, requirement or exception `PageContracts`, and `ExtractionPrompt`.

The projection code should not change for those cases.

## Key Boundary

`RawSource`, `SourceBundle`, `Topic`, `ExtractionPrompt`, and `WikiStructure` must not collapse into one object.
A source can contain many topics.
A bundle can mix unrelated topics.
An extraction prompt selects only the subset worth extracting for a particular wiki.
`WikiStructure` renders `PagePath` for extracted knowledge.

The practical rule is:

- `RawSource` answers: what material do we have?
- `SourceBundle` answers: what material are we processing together?
- `Schema` answers: what `PageMetadataFields`, `PageContracts`, `Defaults`, workflow rules, and `LintRunRules` are available?
- `Topic` answers: what subjects emerged or need wiki coverage?
- `ExtractionPrompt` answers: what should this unattended ingest extract, route, preserve, verify, or defer?
- `IngestRun` answers: what happened when this extraction prompt was applied?
- `Wiki` answers: what persistent synthesis exists after the run?
- `WikiStructure` answers: how does `PageMetadata` render to `PagePath`?

## Non-Goals

### Human-in-the-loop ingest

This TDD does not model live human review during ingest.
All ingest is modeled as unattended `SourceBundle` ingest.
Human intent enters before the run through `Schema`, `WikiStructure`, and `ExtractionPrompt`.
Questions, ambiguities, contradictions, and failed lint checks are recorded as output artifacts.

Do not add domain objects for approval gates, review checkpoints, confirmation prompts, supervision levels, interactive takeaway discussions, or mid-run human decisions.
If an ingest cannot proceed unattended, it should fail or emit follow-up work.

### Domain-specific projection forks

This TDD does not model a separate projection pipeline for each wiki domain.
The system must not require a programmer to add hardcoded routing rules for architecture, physics, tabletop RPGs, plumbing codes, or any other domain.
Domain behavior belongs in `WikiStructure`, `Schema`, and `ExtractionPrompt`.
The projection pipeline interprets those objects, derives `SourcePlans`, and emits wiki updates.
