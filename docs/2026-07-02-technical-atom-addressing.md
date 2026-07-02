# Technical Atom Addressing - TDD (2026-07-02)

## Context & Problem

`TechnicalAtom` is one preserved source item such as a table, code block, formula, rule block, or worked example.
`TechnicalAtomAddress` is the stable wiki address for one `TechnicalAtom`.
`TechnicalAtomAnchor` is the markdown anchor for one rendered atom.
`TechnicalAtomContext` is the source-derived explanation for why the atom matters.
`TechnicalAtomReference` is a link from a wiki page to one addressed atom.
Current pages mention tables, formulas, and code blocks without direct links to the exact rendered atom.
This makes procedures and concept pages harder to verify.

## Goals

- Give every rendered technical atom a stable address.
- Preserve one source code block as one technical atom.
- Preserve one source table as one technical atom.
- Preserve one source formula as one technical atom.
- Attach source-derived context to each technical atom.
- Let procedure and concept pages link directly to the exact atom they use.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not improve table cell reconstruction.
- This TDD does not define every technical atom schema.
- This TDD does not require one standalone page per atom.

Forbidden approaches:

- Do not split one source code block into line-level atoms.
- Do not include a technical atom on a concept page without `TechnicalAtomContext`.
- Do not link to a table by plain text label only.
- Do not create atom ids from rendered markdown order.
- Do not use source-specific wording to decide atom context.

## Requirements

- Each accepted `TechnicalAtom` must have one `TechnicalAtomAddress`.
- `TechnicalAtomAddress` must include source id, atom id, atom kind, and source range id.
- Each rendered atom must have one `TechnicalAtomAnchor`.
- The anchor id must remain stable when unrelated pages change.
- Each `TechnicalAtomReference` must target one `TechnicalAtomAddress`.
- Each `TechnicalAtomReference` must include one relation kind.
- Relation kinds must include `demonstrates`, `defines`, `calculates`, `constrains`, `enumerates`, and `supports-step`.
- Each atom rendered on a concept page must have `TechnicalAtomContext`.
- `TechnicalAtomContext` must cite source support.
- Procedure pages must link table, formula, rule, and example references to atom anchors.
- Concept pages must render atom context before the atom body.
- Code atoms must preserve source line order and whitespace.
- Formula atoms must preserve source expression text.
- Table atoms must preserve row and column order from the table authority decision.
- `ProjectionLintRun` must reject a rendered atom without an anchor.

## Invariants

- `RawSource` remains immutable.
- Technical atoms preserve source-equivalent structure.
- Technical atom ids use source-derived identity.
- Technical atom addressing does not depend on page title.
- Technical atom addressing does not depend on rendered markdown order.
- Technical atom references remain graph-checkable.

## Proposed Architecture

The ledger pipeline already creates technical atoms.
`TechnicalAtomAddressPlanner` creates stable atom addresses before page projection.
`TechnicalAtomReferencePlanner` connects page plans to addressed atoms.
`TechnicalAtomRenderer` renders anchors and source-derived context.
`ProjectionLintRun` verifies atom addresses and references before publish.

```
+-------------+     +-----------------------+     +------------------+
| ClaimLedger |---->| AtomAddressPlanner    |---->| AtomIndex        |
+-------------+     +-----------+-----------+     +--------+---------+
                                |                          |
                                v                          v
                    +-----------------------+     +------------------+
                    | AtomReferencePlanner  |---->| Page Renderer    |
                    +-----------------------+     +------------------+
```

`AtomAddressPlanner` creates stable atom addresses.
`AtomReferencePlanner` attaches atom references to pages.
`TechnicalAtomRenderer` renders anchors, context, and atom bodies.

## Key Interactions

Atom addressing:

```
TechnicalAtom -> AtomAddressPlanner -> TechnicalAtomAddress
TechnicalAtomAddress -> AtomIndex -> address lookup
```

Page projection:

```
PagePlan -> AtomReferencePlanner -> TechnicalAtomReference
TechnicalAtomReference -> TechnicalAtomRenderer -> PageBody
PageBody -> ProjectionLintRun -> atom diagnostics
```

Procedure reference:

```
ProcedureStep -> AtomReferencePlanner -> TechnicalAtomReference
TechnicalAtomReference -> ProcedurePageRenderer -> linked table or formula
```

## Data Model

| Object | Contract |
|---|---|
| `TechnicalAtomAddress` | Source id, atom id, atom kind, source range id, and canonical anchor id. |
| `TechnicalAtomContext` | Relation kind, support ids, context text, and confidence. |
| `TechnicalAtomReference` | Source page id, target atom address, relation kind, and support ids. |
| `AtomIndex` | Source-scoped lookup from atom id and anchor id to address and target page. |

`TechnicalAtomContext.context_text` is source-derived.
It summarizes nearby source explanation or source statement support.

## APIs / Interfaces

- `TechnicalAtomAddressPlanner`: accepts technical atoms and returns `AtomIndex`.
- `TechnicalAtomReferencePlanner`: accepts page plans and `AtomIndex` and returns atom references.
- `TechnicalAtomRenderer`: accepts atom references and renders anchors plus atom bodies.
- `ProjectionLintRun`: validates anchors, references, and context.

## Behavior & Domain Rules

Rule: One source code block remains one atom.

Example: A code block has four lines.
Expected outcome: The ledger stores one code atom with four ordered lines.

Rule: A concept page uses only contextual atoms.

Example: A page topic is arrays and a code atom merely contains an array literal in unrelated example code.
Expected outcome: The page excludes the atom unless source context says the atom demonstrates arrays.

Rule: A procedure page links exact required atoms.

Example: A step requires a lookup table.
Expected outcome: The step links to the table atom anchor.

## Acceptance Criteria

- Every rendered technical atom has one stable anchor.
- Every procedure table reference links to a technical atom anchor.
- Every procedure formula reference links to a technical atom anchor.
- Every concept-page atom includes context text and source support.
- No code block atom splits into line-level atoms.
- No concept page renders an atom without context.
- Graph export resolves all atom target page links.
- A synthetic source with renamed nouns preserves the same atom addressing decisions.

## Cross-Cutting Concerns

Observability: The ingest report records atom counts by kind, addressed count, referenced count, and rejected uncontextualized count.

Error handling: The renderer excludes an atom from a topic page when context support is absent.

## Reference Implementations

- Technical atom domain objects: `harness/src/llmwiki/domain/ledger`
- Page body contracts: `docs/page-body-contracts.md`
- Staged page validation: `harness/src/llmwiki/domain/ledger/staged_flow.py`

## Alternatives Considered

- Link atoms by display label; rejected because duplicate labels exist.
- Create one atom page for every atom; rejected because anchors preserve locality.
- Add post-write anchor repair; rejected because addressing must exist before rendering.

## Halt Conditions

- If implementation needs rendered markdown order to make atom ids, stop and use ledger identity.
- If a topic page needs an atom without context support, stop and reject that atom reference.
- If a procedure step references a missing atom, stop and emit a blocked write diagnostic.
