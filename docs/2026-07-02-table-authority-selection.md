# Table Authority Selection - TDD (2026-07-02)

## Context & Problem

`TableCandidate` is one possible table found in a source.
`TableReconstruction` is one structured representation of a `TableCandidate`.
`TableVariant` is one competing reconstruction for the same source table.
`CellGrid` is the ordered rows, columns, and cells for one reconstruction.
`TableAuthorityDecision` is the accepted table representation for page projection.
Current table output includes malformed wide tables beside better raw table text.
The wiki must publish one authoritative table representation or mark the table for review.

## Goals

- Preserve high-recall table detection.
- Keep competing table reconstructions for audit.
- Select one authoritative table representation for rendering.
- Preserve source-equivalent raw table text.
- Mark unresolved table conflicts as review work.
- Keep table logic source-agnostic and portable.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not select a specific OCR library.
- This TDD does not require visual PDF rendering for every source.
- This TDD does not change non-table atom schemas.

Forbidden approaches:

- Do not render all table variants as equally authoritative.
- Do not choose a table variant by source title.
- Do not choose a table variant by quoted source phrases.
- Do not discard raw table text after reconstruction.
- Do not silently merge cells when confidence is low.

## Requirements

- The extraction pipeline must create `TableCandidate` records before table rendering.
- Each `TableCandidate` must retain source range and raw text evidence.
- The pipeline must allow multiple `TableVariant` records for one `TableCandidate`.
- Each `TableVariant` must include one `CellGrid` or one raw-equivalent representation.
- Each `TableVariant` must include detector provenance.
- Each `TableVariant` must include confidence signals.
- Confidence signals must use reusable categories.
- Reusable categories include row alignment, column alignment, header stability, cell continuity, caption proximity, note proximity, and source-order coverage.
- `TableAuthoritySelector` must create one `TableAuthorityDecision` for each `TableCandidate`.
- `TableAuthorityDecision` must choose `accepted`, `needs-review`, or `rejected`.
- An accepted decision must name one canonical `TableVariant`.
- A needs-review decision must retain all variants and visible diagnostics.
- Renderers must use only accepted canonical variants as authoritative tables.
- Renderers must show raw-equivalent text for needs-review tables.
- `ProjectionLintRun` must reject pages that render two authoritative variants for one table candidate.

## Invariants

- `RawSource` remains immutable.
- Raw table text remains available for audit.
- Table cell order remains source-derived.
- Table authority decisions use reusable layout and evidence categories.
- Table authority decisions do not use source titles.
- Technical atom addresses remain stable after table selection.

## Proposed Architecture

The table pipeline separates detection, reconstruction, authority selection, and rendering.
`TableDetector` creates table candidates.
`TableReconstructionAdapter` creates variants from text, layout, or OCR-like cells.
`TableAuthoritySelector` chooses the canonical variant or marks review work.
`TableRenderer` renders only the authority decision.

```
+-------------+     +---------------+     +---------------------+
| Source Unit |---->| TableDetector |---->| TableCandidate      |
+-------------+     +-------+-------+     +----------+----------+
                            |                        |
                            v                        v
                   +--------------------+     +-------------------+
                   | Reconstruction     |---->| TableVariant      |
                   | Adapters           |     +---------+---------+
                   +--------------------+               |
                                                        v
                                             +---------------------+
                                             | AuthoritySelector   |
                                             +----------+----------+
                                                        |
                                                        v
                                             +---------------------+
                                             | TableRenderer       |
                                             +---------------------+
```

`TableDetector` finds table candidates.
`TableReconstructionAdapter` creates variants.
`TableAuthoritySelector` decides the table state.
`TableRenderer` renders the selected table state.

## Key Interactions

High-recall detection:

```
ExtractedUnit -> TableDetector -> TableCandidate
TableCandidate -> ReconstructionAdapter -> TableVariant
```

Authority selection:

```
TableVariant -> TableAuthoritySelector -> TableAuthorityDecision
TableAuthorityDecision -> TechnicalAtomAddressPlanner -> addressed table atom
```

Page rendering:

```
TableAuthorityDecision -> TableRenderer -> PageBody
PageBody -> ProjectionLintRun -> table diagnostics
```

## Data Model

| Object | Contract |
|---|---|
| `TableCandidate` | Source range, raw text, caption evidence, note evidence, and variant ids. |
| `TableVariant` | Variant id, detector provenance, cell grid, raw-equivalent text, and confidence signals. |
| `CellGrid` | Ordered rows, ordered columns, cell spans, cell text, and cell confidence. |
| `TableAuthorityDecision` | Candidate id, status, canonical variant id, diagnostics, and support ids. |

`TableAuthorityDecision.status` values are `accepted`, `needs-review`, and `rejected`.

## APIs / Interfaces

- `TableDetector`: accepts extracted units and returns table candidates.
- `TableReconstructionAdapter`: accepts candidates and returns variants.
- `TableAuthoritySelector`: accepts candidates and variants and returns authority decisions.
- `TableRenderer`: accepts authority decisions and renders technical atom blocks.
- `ProjectionLintRun`: validates table authority constraints.

## Behavior & Domain Rules

Rule: The renderer shows one authoritative table variant.

Example: A table has one layout variant and one text variant.
Expected outcome: The renderer shows the accepted canonical variant only.

Rule: The selector marks unresolved conflicts for review.

Example: Two variants disagree on row count and both have low confidence.
Expected outcome: The decision is `needs-review` and the page shows diagnostics plus raw-equivalent text.

Rule: The selector preserves raw evidence.

Example: A cell grid loses parenthetical text.
Expected outcome: The raw table text remains attached to the table candidate.

## Acceptance Criteria

- A synthetic table with clean grid structure renders one accepted table.
- A synthetic table with conflicting variants renders no authoritative duplicate.
- A synthetic table with low-confidence cells becomes needs-review.
- A reingested rulebook source no longer renders malformed and clean versions of the same table as parallel authority.
- Every accepted table has one technical atom address.
- Every needs-review table retains raw-equivalent text.
- Table diagnostics appear in ingest confidence output.
- A synthetic source with renamed nouns preserves the same table decisions.

## Cross-Cutting Concerns

Observability: The ingest report records table candidates, variants, accepted tables, needs-review tables, and rejected tables.

Error handling: The page renderer blocks authoritative table rendering when `TableAuthorityDecision` is missing.

## Reference Implementations

- Technical atom ledger objects: `harness/src/llmwiki/domain/ledger`
- Table parsing tests: `harness/tests`
- Staged projection lint: `harness/src/llmwiki/domain/ledger/staged_flow.py`

## Alternatives Considered

- Render every detected variant; rejected because users cannot know which table is authoritative.
- Pick the longest table text; rejected because length does not prove table structure.
- Depend on one OCR engine; rejected because the domain accepts variants from adapters.

## Halt Conditions

- If implementation discards raw table text, stop and preserve it in `TableCandidate`.
- If implementation needs source-specific table names, stop and add reusable confidence signals.
- If a page would render duplicate authoritative variants, stop and reject the page in lint.
