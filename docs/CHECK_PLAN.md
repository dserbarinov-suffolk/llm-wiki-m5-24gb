# LLM-Wiki Check Plan

This file is the repeatable verification checklist for LLM-Wiki work.
Use it with `AGENTS.md`, `docs/llm-wiki.md`, and the KoteKomi TDD.

## 1. Deliverable 0 Checks

- Verify `AGENTS.md` names the KoteKomi TDD.
- Verify `AGENTS.md` names Deliverables 0 through 8.
- Verify `AGENTS.md` contains the canonical flow:
  `SourceUnit -> EvidenceSpan -> Assertion -> Relationship / ArgumentEdge -> TopicState -> PageProjection`.
- Verify `AGENTS.md` contains Task routing.
- Verify `AGENTS.md` contains Authority order.
- Verify `AGENTS.md` contains Architecture role.
- Verify `AGENTS.md` contains Boundary validation rule.
- Verify `docs/CHECK_PLAN.md` exists.
- Verify Deliverable 0 changes no ingest code, projection code, model code, or generated wiki output.

## 2. Domain Core Checks

- Run the Domain Core unit tests for changed domain records.
- Verify Domain Core imports no adapter package.
- Verify Domain Core imports no database package.
- Verify Domain Core imports no model runtime package.
- Verify Domain Core imports no graph library.
- Verify Domain Core imports no markdown renderer.
- Verify accepted source-backed assertions require `EvidenceSpan` records.
- Verify accepted source-backed assertions require `ProvenanceActivity` records.
- Verify accepted technical atoms require `EvidenceSpan` records.
- Verify invalid domain object shape fails fast.

## 3. Application Layer Checks

- Run Application Layer tests for changed use cases.
- Verify Application Layer owns status transitions.
- Verify Application Layer owns transaction intent.
- Verify Application Layer defines ports for adapters.
- Verify Application Layer validates cross-record references before accepted writes.
- Verify no model output writes accepted state directly.
- Verify invalid model output becomes rejection, quarantine, validation error, or `ProposedChange`.

## 4. Adapter Checks

- Run adapter tests for changed adapters.
- Verify adapters translate, validate, persist, load, or call tools.
- Verify adapters do not decide domain meaning.
- Verify adapters do not decide review outcomes.
- Verify adapters do not decide status transitions.
- Verify adapters do not repair invalid deterministic values silently.

## 5. Pipeline Checks

- Run pipeline or CLI tests for changed commands.
- Verify pipelines compose Application Layer use cases.
- Verify pipeline inputs parse through declared DTOs.
- Verify pipeline outputs serialize from declared DTOs or domain records.
- Verify command examples in changed docs run from the repo root with `uv run`.

## 6. Source Unit And Evidence Checks

- Verify raw sources remain immutable.
- Verify structured source artifacts live in the Archive.
- Verify `SourceUnit` records preserve source order.
- Verify `SourceUnit` records preserve parent, child, and sibling structure when the source provides it.
- Verify one source table produces one complete table atom.
- Verify one source code block produces one complete code atom.
- Verify one source formula produces one complete formula atom.
- Verify `EvidenceSpan` records point to source units and not wiki pages.
- Verify markdown cache is not canonical ingest input.

## 7. Assertion Graph Checks

- Verify accepted assertions cite evidence spans.
- Verify accepted assertions cite provenance.
- Verify relationships cite supporting assertions.
- Verify argument edges cite assertion endpoints and rationale.
- Verify graph projection rebuilds from accepted Ledger state.
- Verify graph mining writes proposed changes before accepted state changes.

## 8. TopicState Checks

- Verify `TopicState` is the only input to page projection.
- Verify repeated local section labels do not create topic state by themselves.
- Verify topic state admission requires coherent assertions or technical atoms.
- Verify major procedure topics include steps, rules, tables, formulas, examples, dependencies, and gaps.
- Verify concept topics include definitions, rules, examples, contrasts, technical atoms, and related topics.
- Verify incoherent candidates become `TopicGap` records instead of pages.

## 9. PageProjection Checks

- Verify every factual page sentence maps to an accepted assertion or technical atom.
- Verify every rendered table, code block, and formula maps to a technical atom.
- Verify every related link derives from a relationship, argument edge, or topic dependency.
- Verify gaps render as review work.
- Verify generated wiki pages remain disposable.
- Verify `index.md`, `log.md`, graph output, and health pages match published projections.

## 10. Ingest Quality Checks

- Before implementing any change that can affect ingest quality, collect the
  latest baseline traces for `javascriptallonge.pdf` and
  `Sword World RPG - Complete Edition.pdf`.
- Use `uv run llmwiki inspect-ingest javascriptallonge.pdf` for the JavaScript
  Allonge baseline.
- Use `uv run llmwiki inspect-ingest "Sword World RPG - Complete Edition.pdf"`
  for the Sword World baseline.
- Reingest the current test sources after each deliverable that changes ingest behavior.
- Treat `javascriptallonge.pdf` and `Sword World RPG - Complete Edition.pdf` as
  the canonical test-ingest sources for wiki-quality experiments.
- After the reingest, inspect both ingestion traces again.
- Inspect changed subsystems with `uv run llmwiki inspect-ingest <source> --stage <stage>`.
- Compare pre-change and post-change trace metrics, stage decisions, findings,
  counts, representative records, and generated page outcomes.
- Explain every meaningful movement in extraction, evidence span creation,
  assertion admission, relationship or argument-edge creation, topic state,
  page projection, lint, graph export, and publish results.
- If results improve coherence, comprehensiveness, walkability, or source
  support, continue iterating from the observed dynamics.
- If results regress important pages or produce incoherent output, do root cause
  analysis and either roll back the feature or revisit the design before moving on.
- Verify generated page count drops only because incoherent pages are not published.
- Verify major pages become richer than the current page-first output.
- Verify SwordWorld character creation has steps, dependencies, tables, examples, and gaps.
- Verify SwordWorld combat topics separate player combat, monster combat, and shared combat rules.
- Verify JavaScript Allonge recipes and concepts preserve code atoms with explanatory assertions.

## 11. Query, Chat, Graph, And Lint Checks

- Verify chat retrieves topic state and page projections instead of broad raw page blobs.
- Verify lint uses domain operations rather than ad hoc markdown repair.
- Verify graph check passes after publish.
- Verify query answers cite generated pages and source-backed support.
- Verify answers worth keeping can file back into the wiki layer.

## 12. Forbidden Patterns

- Source-specific production branches.
- Quoted source phrases as production branch conditions.
- Source-specific malformed words as production branch conditions.
- Model output written directly as accepted state.
- Page projection without `TopicState`.
- Markdown cache as canonical ingest input.
- Old and new production ingest flows running side by side.
- Compatibility branches for old generated wiki data.
- Dual-read or dual-write paths for replaced projection artifacts.
- Adapter imports inside Domain Core.
- Adapter code deciding domain meaning or status transitions.
- Generated wiki data constraining code.
