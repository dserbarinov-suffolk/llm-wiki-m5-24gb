# Local LLM-Wiki Object Boundaries - TDD (2026-06-18)

## Context & Problem

The current local LLM-Wiki already has immutable source files in `raw/`, generated markdown files in `wiki/`, deterministic `index.md` and `log.md`, PDF chunking, and forge workflows.
The implementation still uses page name, category, source path, and chunk run where this TDD needs `PageMetadata`, `PageKind`, `RawSource`, and `IngestRun`.
Architecture-wiki shows the useful boundary shape: `RawSource`, `SourcePlan`, `PageMetadata`, `WikiStructure`, `WikiPage`, `Index`, `Log`, and run records are separate responsibilities.
This TDD adopts those object boundaries for the local LLM-Wiki without adopting architecture-wiki's folder taxonomy.

## Goals

- Preserve the current flat `wiki/*.md` layout.
- Introduce the domain object boundaries needed by the local implementation.
- Make `WikiStructure` render `PagePath` from `PageMetadata`.
- Configure the local default `WikiStructure` as `{PageId}.md`.
- Treat current frontmatter as the rendered form of `PageMetadata`.
- Treat one-file ingest as a one-member `SourceBundle`.
- Treat PDF chunking and integration as one `IngestRun` with multiple `SourcePlan` entries.
- Keep `SCHEMA.md` as the local `Schema`.

## Non-Goals & Forbidden Approaches

Non-goals:

- Do not redesign the current wiki folder layout.
- Do not migrate existing pages into nested folders.
- Do not implement architecture-wiki's architecture, interiors, finish, door, lighting, ceiling, casework, source, prompt, or project taxonomy.
- Do not add human-in-the-loop ingest.
- Do not add parallel ingest topology.
- Do not replace forge workflows.
- Do not replace markdown as the persisted wiki page format.

Forbidden approaches:

- Do not infer application meaning from `PagePath`.
- Do not make `PagePath` the stable identity of a page.
- Do not encode `PageKind` as a folder name in this implementation.
- Do not add architecture-specific constants to local LLM-Wiki code.
- Do not add required frontmatter fields that break existing pages.
- Do not let the model write raw frontmatter text directly.
- Do not create a second wiki root beside `wiki/`.

## Requirements

- `PageMetadata.PageId` must be the stable identity of a `WikiPage`.
- `PagePath` must be derived from `PageMetadata` by `WikiStructure`.
- The local default `WikiStructure` must render `javascriptallonge-chapter-5.md` from `PageMetadata.PageId = javascriptallonge-chapter-5`.
- Existing pages must parse into `WikiPage` objects without file moves.
- Existing page categories `source`, `entity`, `concept`, and `synthesis` must become local `PageKind` values.
- Existing frontmatter fields `category`, `summary`, `sources`, and `updated` must map to `PageMetadata`.
- Existing citations such as `(raw/javascriptallonge.pdf p.28-41)` must map to `Evidence`.
- Existing wikilinks such as `[[closure]]` must map to `CrossReference`.
- Existing `wiki/index.md` must remain the persisted `Index`.
- Existing `wiki/log.md` must remain the persisted `Log`.
- Existing PDF map and integrate workflows must record one logical `IngestRun` for the source PDF.
- `ExtractionPrompt` must be built from `Schema` workflow text and run-specific ingest instructions.

## Invariants

- `raw/` remains immutable.
- `wiki/` remains the only generated knowledge base.
- `index.md` remains deterministic bookkeeping.
- `log.md` remains append-only.
- `Wiki.CurrentStructure` remains the single effective `WikiStructure`.
- `IngestRun` remains unattended.
- `IngestTopology` remains `serial` for local ingest.
- `Wavefront` remains a future topology and is not introduced by this TDD.
- Query answers must still cite `WikiPage` and `Evidence`.
- Lint must still report broken links, orphan pages, index drift, contradictions, missing cross-references, and provenance gaps where implemented.

## Proposed Architecture

The implementation gains a domain-object layer between workflows and the store.
The forge workflows continue to decide when to read, search, write, and finish.
The domain-object layer converts workflow inputs and outputs into `RawSource`, `SourceBundle`, `IngestRun`, `SourcePlan`, `WikiPage`, `PageMetadata`, `Evidence`, and `CrossReference`.
The store persists rendered markdown, `index.md`, `log.md`, and run transcripts exactly where they live today.
The local `WikiStructure` is flat and contains one `PathTemplate`.

```
+----------+      +----------------+      +---------------------+
| CLI      |----->| forge workflow |----->| domain-object layer |
+----------+      +----------------+      +----------+----------+
                                                     |
                                                     v
+----------+      +----------------+      +---------------------+
| SCHEMA.md|----->| Schema         |----->| WikiStructure       |
+----------+      +----------------+      | {PageId}.md         |
                                          +----------+----------+
                                                     |
                                                     v
+----------+      +----------------+      +---------------------+
| raw/     |----->| SourceBundle   |----->| WikiStore           |
+----------+      +----------------+      | wiki/*.md           |
                                          | index.md + log.md   |
                                          +---------------------+
```

`CLI` creates `IngestRun`, `QueryRun`, and `LintRun` requests.
`forge workflow` preserves the existing guarded operation flow.
`domain-object layer` owns object construction, validation, and projection boundaries.
`Schema` is loaded from `SCHEMA.md`.
`WikiStructure` renders local `PagePath` values from `PageMetadata`.
`SourceBundle` groups one or more `RawSource` objects for one `IngestRun`.
`WikiStore` remains the only component that touches `raw/`, `wiki/`, `index.md`, and `log.md`.

## Key Interactions

Markdown ingest:

```
User -> CLI -> SourceBundle -> IngestRun -> RawSource -> Workflow
Workflow -> WikiPage -> PageMetadata -> WikiStructure -> PagePath
PagePath -> WikiStore -> wiki/*.md + index.md + log.md
```

Precondition: `RawSource` exists in `raw/`.
Function: `IngestRun` applies `ExtractionPrompt` to a one-member `SourceBundle`.
Postcondition: `WikiPage`, `Index`, `Log`, `Evidence`, and `CrossReference` reflect the source.

PDF ingest:

```
User -> CLI -> RawSource -> PDF pipeline -> SourcePlans
SourcePlans -> map workflows -> WikiPages
SourcePlans -> integrate workflow -> source hub -> IngestRun
IngestRun -> Index + Log
```

Precondition: `RawSource.SourceFormat` is `pdf`.
Function: The PDF pipeline creates chunk `SourcePlan` entries for one `IngestRun`.
Postcondition: The wiki contains source pages, affected pages, `Evidence`, `CrossReference`, `Index`, and `Log`.

Query and lint:

```
QueryRun -> Index -> WikiPages -> Evidence -> optional WikiPage
LintRun -> WikiPages -> CrossReferences -> LintFindings -> optional WikiPage
QueryRun/LintRun -> Log
```

Precondition: `Wiki` has `WikiPages`, `Index`, and `Log`.
Function: `QueryRun` reads the wiki, and `LintRun` validates wiki health.
Postcondition: Answers cite `WikiPage` and `Evidence`, and lint records `LintFinding`.

## Data Model

| Object | Local representation | Contract |
|---|---|---|
| `RawSource` | file under `raw/` | immutable source input |
| `SourceBundle` | one or more `RawSource` values | source selection for one `IngestRun` |
| `Wiki` | `wiki/`, `index.md`, `log.md`, run traces | generated knowledge base |
| `Schema` | `SCHEMA.md` | `PageKind`, `PageMetadata`, workflow, and lint contract |
| `WikiStructure` | local-flat `PathTemplate` | renders `PagePath` from `PageMetadata` |
| `PathTemplate` | `{PageId}.md` | local default page placement |
| `ExtractionPrompt` | resolved `SCHEMA.md` ingest workflow plus run instruction | extraction and uncertainty instruction |
| `IngestRun` | markdown ingest or PDF map-plus-integrate ingest | unattended source projection |
| `SourcePlan` | per-source or per-PDF-chunk plan | run-owned target planning |
| `WikiPage` | rendered markdown page | `PageMetadata`, `PagePath`, and `PageBody` |
| `PageMetadata` | rendered frontmatter | `PageId`, `PageKind`, `Summary`, `Sources`, and `Updated` |
| `PageKind` | current category | `source`, `entity`, `concept`, or `synthesis` |
| `Claim` | supported statement in page body | claim text with status and evidence |
| `Evidence` | citation or `sources` value | raw path plus optional locator |
| `CrossReference` | `[[page-id]]` link | page relationship |
| `Index` | `wiki/index.md` | deterministic navigation |
| `Log` | `wiki/log.md` | append-only operation record |
| `QueryRun` | query transcript and optional page write | question against the wiki |
| `LintRun` | lint transcript and `wiki-health` write | maintenance pass |
| `LintFinding` | deterministic or model-reported issue | actionable wiki health issue |

Concrete local example:

```
RawSource: raw/javascriptallonge.pdf
SourceBundle: [raw/javascriptallonge.pdf]
Schema: local-llm-wiki
WikiStructure: local-flat, {PageId}.md
PageMetadata: PageId=javascriptallonge-chapter-5
PageMetadata: PageKind=source
PageMetadata: Sources=[raw/javascriptallonge.pdf p.28-41]
PagePath: javascriptallonge-chapter-5.md
```

Architecture-wiki boundary mapping:

- Architecture-wiki source PDFs map to `RawSource`.
- Architecture-wiki source-summary pages map to `WikiPage` with `PageKind = source`.
- Architecture-wiki sidecars map to `SourcePlan`.
- Architecture-wiki prompts map to `ExtractionPrompt`.
- Architecture-wiki `_schema.yaml` files map to `Schema.PageContracts`.
- Architecture-wiki folder paths map to `WikiStructure`.
- Architecture-wiki folder taxonomy does not map into the local default `WikiStructure`.

## APIs / Interfaces

- `llmwiki ingest <path-in-raw>` continues to accept one user-provided path.
- The CLI wraps that path in a one-member `SourceBundle`.
- `llmwiki query "<question>"` continues to create one `QueryRun`.
- `llmwiki lint` continues to create one `LintRun`.
- `PageMetadata` must parse from existing frontmatter.
- `PageMetadata` must render back to existing frontmatter.
- `WikiStructure` must render `PagePath` from `PageMetadata`.
- `WikiStore.write_page` must persist a `WikiPage` at the `PagePath` rendered by `WikiStructure`.
- `WikiStore.read_page` must return a `WikiPage` with `PageMetadata`, `PagePath`, and `PageBody`.
- `Index` updates must consume `WikiPage.PageMetadata`.
- `Log` entries must reference `IngestRun`, `QueryRun`, or `LintRun` where available.

## Behavior & Domain Rules

Rule: `PageMetadata.PageId` is identity.

- Input: `PageMetadata.PageId = closure`.
  Expected outcome: `WikiStructure` renders `closure.md`.
- Input: a future `WikiStructure` renders `concepts/closure.md`.
  Expected outcome: `PageMetadata.PageId` remains `closure`.

Rule: The current local `WikiStructure` is flat.

- Input: `PageMetadata.PageId = javascriptallonge`.
  Expected outcome: `PagePath = javascriptallonge.md`.
- Input: `PageMetadata.PageKind = source`.
  Expected outcome: no `sources/` folder is created.
- Input: architecture-wiki page data with `domain = doors`.
  Expected outcome: local LLM-Wiki ignores `domain` unless a future `Schema` declares it.

Rule: `SourceBundle` owns source selection.

- Input: `llmwiki ingest antikythera-mechanism.md`.
  Expected outcome: one `SourceBundle` with one `RawSource`.
- Input: `llmwiki ingest javascriptallonge.pdf`.
  Expected outcome: one `SourceBundle` with one `RawSource` and one `IngestRun` with multiple `SourcePlan` entries.

Rule: `Evidence` is separate from `PagePath`.

- Input: citation `(raw/javascriptallonge.pdf p.28-41)`.
  Expected outcome: `Evidence.RawSource = raw/javascriptallonge.pdf` and `Evidence.Locator = p.28-41`.
- Input: page `javascriptallonge-chapter-5.md`.
  Expected outcome: source evidence is read from `PageMetadata.Sources` and body citations, not inferred from the file name.

## Acceptance Criteria

- Existing harness tests pass without moving any file under `wiki/`.
- Existing `wiki/*.md` pages parse into `WikiPage` and render back with the same frontmatter fields.
- `WikiStructure` has a tested local-flat configuration that renders `{PageId}.md` for all current `PageKind` values.
- `WikiStore.write_page` writes through `WikiStructure` and still rejects reserved names and paths outside `wiki/`.
- `llmwiki ingest antikythera-mechanism.md` still writes flat pages.
- `llmwiki ingest javascriptallonge.pdf` still runs the current PDF map and integrate flow.
- PDF chunk map runs record `SourcePlan` entries, and PDF integrate records one parent `IngestRun`.
- `index.md` updates use `WikiPage.PageMetadata`.
- `log.md` entries remain parseable by the existing prefix convention.
- Lint findings are representable as `LintFinding`.
- No new architecture-specific folder names appear in local LLM-Wiki code.
- No existing local page path changes unless the user explicitly changes `WikiStructure` in a future TDD.

## Cross-Cutting Concerns

Observability: run transcripts remain the source for model-turn audit.
The domain-object layer may add structured run summaries, but it must not remove transcripts.

Error handling: invalid `PageMetadata`, invalid `PageKind`, invalid `PagePath`, and invalid `Evidence` must raise errors that can be fed back through forge tool-error handling.

Backward compatibility: existing frontmatter stays valid.
Any new optional field must have a default when parsing existing pages.

Migration: this TDD is an in-place refactor.
It must not require a one-time file migration.

## Reference Implementations

- Domain modules: `harness/src/llmwiki/domain/`.
- Store boundary: `harness/src/llmwiki/store/wiki_store.py`.
- Workflow contracts: `harness/src/llmwiki/workflows/`.
- Live schema source: `SCHEMA.md`.
- Domain-object vocabulary: `docs/2026-06-16-llm-wiki-domain-objects.md`.

## Alternatives Considered

- Keep current page-name, category, source-path, and chunk-run objects.
  Rejected because the next wiki configuration would need one-off code paths.
- Adopt architecture-wiki folder taxonomy.
  Rejected because the local LLM-Wiki is not an architecture product-selection wiki.
- Make `PagePath` identity.
  Rejected because future `WikiStructure` changes would rename identity.
- Create a new persisted object store.
  Rejected because markdown plus run transcripts are sufficient for this TDD.

## Halt Conditions

- If implementation requires moving existing `wiki/*.md` files, stop and ask.
- If implementation needs architecture-specific folders or constants, stop and ask.
- If implementation needs a persisted database for domain objects, stop and ask.
- If implementation requires changing CLI command shapes, stop and ask.
- If implementation requires changing `SCHEMA.md` into a different file format, stop and ask.
