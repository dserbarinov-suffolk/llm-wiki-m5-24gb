# Source Manifest Navigation - TDD (2026-07-02)

## Context & Problem

`SourceManifestPage` is the wiki page that represents one `RawSource`.
`SourceNavigationPlan` is the source-scoped navigation plan for one `SourceManifestPage`.
`SourceEntryPoint` is one link from a `SourceManifestPage` to a useful wiki page.
`PageFamilySummary` is the count and purpose summary for one generated page family.
`SourceSectionIndex` is the ordered section map derived from `DocumentStructure`.
Current source pages become large content dumps.
Large source pages hide procedures, sections, collections, and concepts behind extracted content.
The source page must act as a navigation page before it acts as an evidence page.

## Goals

- Make every `SourceManifestPage` a compact entry point for one source.
- Show generated page counts by page family.
- Show procedure, collection, concept, and top-level section entry points.
- Keep source content available through section pages and technical atom links.
- Preserve the LLM-Wiki pattern: raw sources stay immutable and wiki pages stay generated.
- Keep `index.md` and `log.md` current through the existing ingest workflow.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not redesign source extraction.
- This TDD does not create cross-source overview pages.
- This TDD does not change chat retrieval.

Forbidden approaches:

- Do not render a whole source transcript into `SourceManifestPage`.
- Do not select entry points from source-specific phrases.
- Do not select entry points from source title rules.
- Do not make source pages depend on existing wiki page text.
- Do not hide section pages from graph export.

## Requirements

- The pipeline must create one `SourceNavigationPlan` for each `RawSource`.
- `SourceNavigationPlan` must use `SourcePlan`, `DocumentStructure`, `SectionPlan`, `TopicIndex`, and `ClaimLedger`.
- `SourceNavigationPlan` must not read rendered markdown.
- `SourceManifestPage` must place navigation sections before evidence sections.
- `SourceManifestPage` must show one `PageFamilySummary` for each generated page family.
- `SourceManifestPage` must show the top-level `SourceSectionIndex`.
- `SourceManifestPage` must show all procedure entry points.
- `SourceManifestPage` must show all collection entry points.
- `SourceManifestPage` must show the highest-salience concept entry points.
- `SourceManifestPage` must link to the source artifact path.
- `SourceManifestPage` must link to graph and ingest confidence artifacts when they exist.
- `SourceManifestPage` must omit raw extracted content unless the content is a short source abstract.
- The source abstract must cite source evidence.
- The source abstract must fit within 12 bullets.
- The renderer must write a stable section order.

## Invariants

- `RawSource` remains immutable.
- `SourceManifestPage` remains generated wiki content.
- `SourceManifestPage` uses source-derived structure.
- `SourceManifestPage` uses portable artifact ids for provenance.
- `SourceManifestPage` does not become evidence storage.
- Section pages retain source evidence.
- Technical atom pages or anchors retain technical atom evidence.

## Proposed Architecture

The ingest pipeline adds `SourceNavigationPlanner` before page rendering.
`SourceNavigationPlanner` reads existing source-scoped artifacts.
`SourceNavigationPlanner` creates `SourceNavigationPlan`.
`SourceManifestRenderer` renders only the source entry page.
Other renderers keep ownership of section, concept, procedure, and collection pages.

```
+------------+     +-------------------+     +----------------------+
| SourcePlan |---->| SourceNavigation  |---->| SourceManifestPage   |
+------------+     | Planner           |     | Renderer             |
                   +---------+---------+     +----------+-----------+
                             ^                          |
                             |                          v
       +---------------------+----------------+   +------------+
       | DocumentStructure, SectionPlan,      |   | WikiPage   |
       | TopicIndex, ClaimLedger              |   +------------+
       +--------------------------------------+
```

`SourceNavigationPlanner` selects source entry points.
`SourceManifestRenderer` renders the navigation page.
`SectionPageRenderer` renders source sections.
`TechnicalAtomRenderer` renders technical atom targets.

## Key Interactions

Source page render:

```
SourcePlan -> SourceNavigationPlanner -> SourceNavigationPlan
SourceNavigationPlan -> SourceManifestRenderer -> SourceManifestPage
SourceManifestPage -> GraphExporter -> wiki graph
```

Query entry:

```
ChatSearch -> SourceManifestPage -> SourceEntryPoint
SourceEntryPoint -> target WikiPage -> source evidence
```

## Data Model

| Object | Contract |
|---|---|
| `SourceNavigationPlan` | One ordered plan for one source entry page. |
| `PageFamilySummary` | Page family, count, purpose text, and representative page ids. |
| `SourceEntryPoint` | Target page id, relation kind, source support ids, and display label. |
| `SourceSectionIndex` | Ordered top-level structure nodes with target section page ids. |

`SourceEntryPoint.relation_kind` uses source-neutral values.
Allowed values include `procedure`, `collection`, `concept`, `top-level-section`, `source-artifact`, and `quality-artifact`.

## APIs / Interfaces

- `SourceNavigationPlanner`: accepts source-scoped artifacts and returns `SourceNavigationPlan`.
- `SourceManifestRenderer`: accepts `SourceNavigationPlan` and returns one `StagedWikiPage`.
- `ProjectionLintRun`: validates manifest structure before publish.

## Behavior & Domain Rules

Rule: The renderer places navigation before source evidence.

Example: A source has one character creation procedure and one equipment section.
Expected outcome: The source page links to the procedure and equipment section before any abstract bullets.

Rule: The planner selects entry points from artifact categories.

Example: A source has a collection page because one section contains repeated table rows.
Expected outcome: The source page links to the collection page with relation kind `collection`.

Rule: The renderer does not copy long source content onto the manifest page.

Example: A source abstract candidate contains 30 bullets.
Expected outcome: The renderer keeps 12 cited bullets and leaves full evidence on section pages.

## Acceptance Criteria

- A reingested large rulebook source has one compact source page.
- The source page shows page family counts.
- The source page links to every procedure page for that source.
- The source page links to every collection page for that source.
- The source page links to top-level section pages in source order.
- The source page contains no raw table body.
- The source page contains no raw code block.
- The source page contains no source transcript section.
- `uv run llmwiki graph --check` reports zero unresolved edges.
- A synthetic source with renamed nouns produces the same manifest structure.

## Cross-Cutting Concerns

Observability: The ingest report records source entry point counts by relation kind.

Error handling: The renderer blocks the source page when `SourceNavigationPlan` has no source artifact link.

## Reference Implementations

- Staged flow: `harness/src/llmwiki/domain/ledger/staged_flow.py`
- Source plan artifact: `harness/src/llmwiki/domain/ledger/staged_contracts.py`
- Page rendering adapters: `harness/src/llmwiki/runtime/ledger_linked_pages.py`

## Alternatives Considered

- Keep source pages as full source summaries; rejected because large sources hide navigation.
- Put all navigation in `index.md`; rejected because source-local navigation belongs on the source page.
- Generate navigation from markdown after publish; rejected because domain artifacts already contain the required structure.

## Halt Conditions

- If implementation requires source-title rules, stop and redesign the selector.
- If implementation requires reading rendered markdown to plan the source page, stop and define a missing artifact field.
- If the source page must contain full technical atom bodies, stop and use technical atom targets instead.
