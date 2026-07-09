# Assertion Graph Topic State - Domain Design Document (DDD) (2026-07-09)

## Context & Problem

`RawSource` is an immutable user-supplied source file.
`SourceUnit` is one source-derived block, section, table, code block, formula, image note, or list item.
`EvidenceSpan` is one exact source span with location, source text, and surrounding context.
`Assertion` is one atomic source-backed statement.
`TechnicalAtom` is one exact structured source item such as a table, code block, formula, rule, procedure, or example.
`Relationship` is one accepted typed edge between domain records.
`ArgumentEdge` is one accepted typed edge between assertions.
`TopicState` is the durable accumulated state for one wiki topic.
`PageProjection` is one markdown view generated from `TopicState`.
`ProposedChange` is one model-generated or deterministic change that awaits validation before accepted state changes.
`ProvenanceActivity` is one recorded action that created or changed domain records.
`Archive` is the local file store for raw sources and source-derived artifacts.
`Ledger` is the canonical local store for accepted domain records and proposed changes.
`Wiki` is the generated markdown layer that users browse and query.
`Universal Standard` is the rule that production logic uses reusable source categories and never source particulars.

The current ingest pipeline creates too many thin pages.
Many pages group claims by weak topic labels instead of durable source-backed state.
Major pages such as character creation and combat do not become complete references.
The system needs a new canonical flow that enriches topic state before it writes pages.

## Goals

- Replace the current page-first pipeline with `SourceUnit -> EvidenceSpan -> Assertion -> Relationship / ArgumentEdge -> TopicState -> PageProjection`.
- Make `TopicState` the canonical input to every generated wiki page.
- Make `EvidenceSpan`, `Assertion`, `Relationship`, `ArgumentEdge`, and `TopicState` portable across LLM-Wiki implementations.
- Lower page count by publishing only coherent `TopicState` records as pages.
- Enrich existing `TopicState` records when new source evidence arrives.
- Preserve tables, code blocks, formulas, procedures, rules, and examples as complete `TechnicalAtom` records.
- Make every factual sentence in a page trace to accepted assertions or technical atoms.
- Keep raw sources immutable.
- Keep wiki markdown generated and disposable.
- Delete replaced claim-ledger, topic-index, section-plan, and projection code in the implementation slice that supersedes it.
- Adopt KoteKomi-style agent guidance for task routing, authority order, boundary validation, and architecture role.

## Proposed Architecture

### Alignment With LLM-Wiki

The new flow keeps the three LLM-Wiki layers.
`RawSource` remains immutable source truth.
`Ledger` becomes the maintained knowledge compiler between raw sources and wiki markdown.
`Wiki` remains the generated reader layer.

The new flow strengthens the LLM-Wiki pattern.
The model does not rediscover source knowledge at query time.
The system stores accepted assertions and topic state once.
The system projects pages from accumulated topic state.

### Agent Guidance Contract

The repository root `AGENTS.md` must gain explicit task routing.
Each task type must name the documents an agent reads before work starts.
The task routing table must cover design documents, Domain Core, Application Layer, Adapters, Pipelines, model behavior, tests, and generated wiki output.

The repository root `AGENTS.md` must gain an authority order.
The authority order must place accepted design documents before code.
The authority order must place Domain Core before Application Layer.
The authority order must place Application Layer before Adapters and Pipelines.
The authority order must place generated wiki data last.

The repository root `AGENTS.md` must state the architecture role.
Dependencies point inward.

```text
Pipelines -> Application Layer -> Domain Core
Adapters  -> Application Layer -> Domain Core
Domain Core -> no external package
```

The repository root `AGENTS.md` must state the boundary validation rule.
Domain Core records and Application Layer DTOs define boundary shape.
Every deterministic boundary must parse inbound values through declared records or DTOs.
Every deterministic boundary must serialize outbound values from declared records or DTOs.
Deterministic invalid values fail fast.
Only model output can enter recovery.
Recovery produces rejection, quarantine, validation error, or `ProposedChange`.
Invalid model output never becomes accepted state.

### Components

```text
RawSource
  |
  v
SourceUnitExtractor
  |
  v
EvidenceSpanBuilder
  |
  v
AssertionProposer
  |
  v
ProposedChangeReview
  |
  v
Accepted Ledger
  |
  +--> RelationshipMiner
  |
  +--> ArgumentEdgeMiner
  |
  v
TopicStateBuilder
  |
  v
PageProjectionBuilder
  |
  v
WikiPublisher
```

`SourceUnitExtractor` maps a raw source into ordered source units.
`EvidenceSpanBuilder` maps source units into exact source spans.
`AssertionProposer` proposes assertions and technical atoms from evidence spans.
`ProposedChangeReview` validates proposed records and accepts or rejects them.
`Accepted Ledger` stores accepted records and provenance.
`RelationshipMiner` derives typed relationships from accepted assertions.
`ArgumentEdgeMiner` derives typed edges between assertions.
`TopicStateBuilder` groups accepted records into durable topic state.
`PageProjectionBuilder` renders page plans from topic state.
`WikiPublisher` writes generated markdown, index, log, graph, and health pages.

### Domain Objects

#### Source Objects

`SourceUnit` has stable identity, source locator, source hash, source order, unit kind, parent id, child ids, source text, page span, and layout data.
`SourceUnit` kinds include heading, paragraph, list, table, code, formula, figure, caption, footnote, index entry, glossary entry, and unknown.

`EvidenceSpan` has stable identity, source locator, source hash, source unit ids, exact text, prefix text, suffix text, page span, selector type, layout boxes, and text fingerprint.
`EvidenceSpan` points to source text.
`EvidenceSpan` never points to wiki text.

`TechnicalAtom` has stable identity, atom kind, source span ids, exact payload, normalized payload, parse status, context span ids, and source order.
`TechnicalAtom` kinds include table, code block, formula, rule, procedure, example, diagram, and structured record.
One source table creates one table atom.
One source code block creates one code atom.
One source formula creates one formula atom.

#### Knowledge Objects

`Assertion` has stable identity, assertion kind, subject, predicate, object entity id or object value, qualifiers, status, confidence values, source ids, evidence span ids, technical atom ids, and provenance activity ids.
`Assertion` kinds include source claim, definition, rule statement, procedure step, example statement, event statement, entity fact, technical fact, analytic inference, corroboration, contradiction, and status update.

`Relationship` has stable identity, subject id, predicate, object id, assertion ids, confidence, and provenance activity ids.
`Relationship` connects domain records.
`Relationship` never uses a page id as its subject or object.

`ArgumentEdge` has stable identity, from assertion id, to assertion id, relation, rationale, evidence span ids, confidence, and provenance activity id.
`ArgumentEdge` relations include supports, contradicts, weakens, contextualizes, narrows, elaborates, depends-on, example-of, exception-to, and infers.

`TopicState` has stable identity, topic key, label, topic kind, accepted assertion ids, accepted technical atom ids, relationship ids, argument edge ids, source unit ids, required dependency ids, unresolved gap ids, and projection policy.
`TopicState` kinds include concept, entity, procedure, rule set, collection, source manifest, comparison, and synthesis.

`TopicDependency` links one topic state to another topic state.
`TopicDependency` records relation, required status, rationale assertion ids, and source order.

`TopicGap` records missing source support, missing dependency, unresolved contradiction, ambiguous source structure, or weak topic identity.

#### Lifecycle Objects

`ProposedChange` stores proposed records before acceptance.
`ProposedChange` has review status, proposed JSON, accepted JSON, source id, source unit ids, model name, prompt id, and provenance activity id.

`ProvenanceActivity` records source ingest, source unit extraction, assertion proposal, proposed change review, relationship mining, topic state build, page projection, lint, and query filing.

`PageProjection` has stable identity, topic state id, page id, page kind, page family, page body, coverage records, source ids, rendered related links, and projection findings.
`PageProjection` is derived state.
`PageProjection` can be rebuilt from accepted ledger records.

### Flow

#### Source Unit Flow

`SourceUnitExtractor` reads one raw source.
It writes a source-unit artifact to the Archive.
It preserves parent, child, sibling, and source-order structure.
It preserves tables, code blocks, and formulas as source units.
It records extraction provenance.

#### Evidence Flow

`EvidenceSpanBuilder` creates evidence spans from source units.
It preserves exact text and bounded context.
It creates layout selectors when the source provides layout data.
It links evidence spans to source units.

#### Assertion Flow

`AssertionProposer` receives evidence spans and technical atoms.
It returns proposed assertions, technical atoms, and support records.
It never writes accepted state.
It emits `ProposedChange` records.

`ProposedChangeReview` validates proposed records.
It checks domain record shape.
It checks cross-record references.
It checks evidence span existence.
It checks technical atom existence.
It accepts valid records.
It rejects invalid records with visible findings.

#### Relationship Flow

`RelationshipMiner` reads accepted assertions and technical atoms.
It proposes relationships when accepted assertions support an edge.
It stores relationship proposals as `ProposedChange` records.

`ArgumentEdgeMiner` reads accepted assertions.
It proposes argument edges for support, contradiction, dependency, example, exception, context, and inference.
It stores argument-edge proposals as `ProposedChange` records.

#### Topic State Flow

`TopicStateBuilder` reads accepted assertions, technical atoms, relationships, argument edges, and source structure.
It updates existing topic states when new records belong to them.
It creates a new topic state only when the records form a coherent topic.
It records topic gaps instead of publishing incoherent pages.

`TopicStateBuilder` treats repeated local section labels as local evidence.
It promotes repeated labels to topic state only when assertions share a subject and compatible structural context.

`TopicStateBuilder` builds major pages from dependency closure.
A procedure topic includes steps, rules, tables, formulas, examples, inputs, outputs, exceptions, and unresolved gaps.
A concept topic includes definitions, rules, examples, contrasts, technical atoms, and related topics.
A collection topic includes records, shared schema fields, variants, tables, and selection axes.

#### Page Projection Flow

`PageProjectionBuilder` reads one topic state.
It renders markdown from accepted topic state.
It renders each factual sentence from accepted assertions.
It renders each table, code block, and formula from accepted technical atoms.
It renders related links from topic dependencies, relationships, and argument edges.
It renders gaps as review work when the topic state is incomplete.

`WikiPublisher` writes accepted page projections.
It updates index, log, graph, and health pages.
It does not create pages from source-unit headings directly.

### Refactor Plan

#### Milestone 1: Agent Guidance And Domain Core

Update `AGENTS.md` with task routing, authority order, architecture role, and boundary validation.
Create pure Domain Core modules for source units, evidence spans, assertions, relationships, argument edges, topic state, proposed changes, provenance activities, and page projections.
Generate or validate schemas from Domain Core records.
Add tests for domain invariants.

#### Milestone 2: Source Unit And Evidence Span Canonicalization

Replace markdown-cache-derived source input with source-unit artifacts.
Create evidence spans from source units.
Preserve table, code, and formula source units as complete technical atoms.
Remove code that treats markdown cache as canonical ingest input.

#### Milestone 3: Proposed Change Review

Make model output enter the system only through `ProposedChange`.
Validate proposed records before acceptance.
Record provenance for every accepted state change.
Delete direct model-output-to-page projection paths.

#### Milestone 4: Assertion Graph

Build accepted assertions and technical atoms before relationships.
Mine relationships and argument edges from accepted assertions.
Store derived relationship and argument-edge proposals as proposed changes.
Add graph projection from accepted ledger records.

#### Milestone 5: Topic State

Build topic state from accepted assertions, technical atoms, relationships, argument edges, and source structure.
Use topic state as the only input to page projection.
Delete topic pages that derive directly from lexical topic candidates.
Delete section-repeat page synthesis.

#### Milestone 6: Page Projection

Render pages from topic state.
Render major procedure pages from complete dependency closure.
Render gaps when topic state lacks required support.
Write fewer pages with richer bodies.
Delete superseded page renderers.

#### Milestone 7: Cleanup

Delete replaced claim-ledger projection modules.
Delete replaced topic-index projection modules.
Delete replaced section-plan projection modules.
Delete obsolete artifact formats.
Delete tests that assert old page counts or old page shapes.
Regenerate the disposable wiki.

### Invariants

Raw sources remain immutable.
Generated wiki pages remain disposable.
The Ledger is canonical accepted state.
The Archive is canonical source-derived artifact state.
Domain Core imports no adapters, model clients, filesystem code, database code, graph libraries, or markdown renderers.
Application Layer defines ports.
Adapters implement ports.
Pipelines compose Application Layer use cases.
Every accepted source-backed assertion references at least one evidence span.
Every accepted source-backed assertion references provenance.
Every technical atom references evidence spans.
Every page projection references topic state.
Every factual page sentence references an accepted assertion or technical atom.
Every related link derives from a relationship, argument edge, or topic dependency.
Every model output enters as a proposed change.
Every invalid deterministic boundary value fails fast.
Every invalid model output becomes rejection, quarantine, validation error, or proposed change finding.
Production logic follows the Universal Standard.

### Verification Targets

Unit tests validate every Domain Core record.
Unit tests validate accepted assertion evidence requirements.
Unit tests validate proposed change review.
Unit tests validate relationship and argument-edge reference checks.
Unit tests validate topic state admission.
Unit tests validate page projection coverage.
Synthetic tests rename every domain noun and still pass the same invariants.
SwordWorld ingest produces a character creation topic state with steps, dependencies, tables, examples, and gaps.
SwordWorld ingest produces combat topic states that separate player combat, monster combat, and shared combat rules.
JavaScript Allonge ingest produces recipe and concept topic states with code atoms and explanatory assertions.
The generated wiki has fewer pages than the current page-first output for the same sources.
The generated wiki has richer major pages than the current page-first output for the same sources.
Graph check passes after publish.
Lint reads page projections and topic state instead of repairing raw markdown directly.

### Source-Neutral Rules

The system can use source categories.
Source categories include heading, section, paragraph, list, table, code block, formula, example, rule, procedure, glossary entry, index entry, figure, caption, and footnote.

The system can use assertion categories.
Assertion categories include definition, rule statement, procedure step, example statement, entity fact, event statement, technical fact, source claim, analytic inference, corroboration, contradiction, and status update.

The system can use relationship categories.
Relationship categories include depends-on, part-of, instance-of, option-for, example-of, exception-to, contrasts-with, narrows, elaborates, supports, contradicts, and infers.

The system must not use source titles as production branches.
The system must not use quoted source phrases as production branches.
The system must not use source-specific malformed words as production branches.
The system must not publish a page from a repeated label alone.

### Acceptance Gate

Implementation must stop if it adds compatibility code for the old projection flow.
Implementation must stop if old and new projection flows run side by side for production ingest.
Implementation must stop if a page can be projected without topic state.
Implementation must stop if model output can write accepted state directly.
Implementation must stop if markdown cache becomes canonical ingest input.
Implementation must stop if a source-specific phrase enters production logic.
