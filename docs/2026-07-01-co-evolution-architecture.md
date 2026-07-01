# Co-Evolution Architecture

## Context & Problem

An LLM-Wiki implementation is one repository that ingests raw sources, writes wiki pages, and answers questions from those pages.

A sister implementation is another LLM-Wiki repository that evolves the same product ideas with different local code.

A portable feature is a domain behavior that both repositories can run with the same inputs and expected outputs.

A local adapter is code that connects a portable feature to a repository-specific store, CLI, model client, or workflow runner.

The two repositories now learn from each other, but ports still depend on manual file comparison. This slows useful changes and lets hidden adapter differences leak into domain behavior.

## Goals

- Make each portable feature easy to identify, copy, and verify.
- Keep portable behavior in pure domain modules.
- Keep local adapters small and explicit.
- Let both repositories run the same portability tests.
- Preserve the LLM-Wiki pattern: raw sources stay immutable, wiki pages stay generated, and query behavior reads the wiki layer.
- Enforce the Universal Standard: the system ingests all sources equally and uses categories found in sources, never source-specific particulars.

## Proposed Architecture

### Domain Boundary

The portable kernel owns domain objects and domain logic.

The portable kernel has no file I/O.

The portable kernel has no network I/O.

The portable kernel has no model calls.

The portable kernel has no process-global configuration.

The portable kernel receives typed domain objects and plain DTOs.

The portable kernel returns typed domain objects, decisions, diagnostics, and projection plans.

### Ports And Adapters

Each repository owns its local adapters.

A `WikiPageRepository` adapter reads and writes rendered wiki pages.

A `RawSourceRepository` adapter reads immutable source files.

A `ModelClient` adapter calls the local or remote model backend.

A `SearchIndex` adapter returns ranked page hits.

An `ExtractionBackend` adapter turns raw files into source-derived document objects.

Portable domain logic uses adapter output only after the adapter maps it into shared domain objects.

### Portable Feature Shape

Each portable feature uses this layout:

- One public domain module with the same import path in both repositories.
- Helper modules only for local file-size and readability constraints.
- One portability test file under `tests/portability`.
- Synthetic fixtures that rename domain nouns and still prove the invariant.
- Optional real-source regression fixtures that prove observed failures do not return.

### Shared Test Contract

The portability suite tests behavior, not markdown byte equality.

The portability suite can assert these invariants:

- A table remains one structured artifact.
- A code block remains one structured artifact.
- A procedure page yields every required step.
- A procedure execution cites evidence for source-derived outputs.
- A procedure execution marks missing details unresolved.
- A derived output explains its derivation.
- A related link explains why the target helps the reader.

### First Portable Slice

The first portable slice covers task evidence and procedure execution.

`TaskEvidencePack` selects a bounded evidence surface for a task-shaped chat turn.

`StructuredEvidenceArtifact` preserves table, formula, code, and worked-example evidence from already-projected pages.

`ProcedureExecution` records a typed execution trace for a procedure.

`validate_procedure_execution` checks that the trace covers every required step and cites only evidence pages in scope.

The chat workflow remains a local adapter.

### Universal Standard Invariants

The portable kernel can use reusable source categories.

Reusable source categories include heading, section, table, code block, formula, example, decision point, procedure step, and citation.

The portable kernel must not depend on a quoted source phrase.

The portable kernel must not depend on a specific source title.

The portable kernel must not depend on a specific page id.

The portability suite must include synthetic fixtures that replace source nouns while preserving source categories.

### Verification Targets

Both repositories run `tests/portability` for every portable feature port.

Both repositories run local adapter tests after a portable feature reaches a workflow.

Both repositories compare ingestion quality with the same source set when a feature changes page output.

Both repositories keep generated wiki pages out of the portability contract.

### Alignment With The LLM-Wiki Pattern

The portable kernel strengthens the generated wiki layer.

The raw source layer remains immutable.

The local adapters keep `index.md` and `log.md` repository-specific.

The query operation can use portable task evidence without expanding the model prompt to the whole wiki.

The lint operation can use portability diagnostics to find drift between repositories.
