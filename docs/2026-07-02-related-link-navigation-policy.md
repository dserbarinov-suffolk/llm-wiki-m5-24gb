# Related Link Navigation Policy - TDD (2026-07-02)

## Context & Problem

`RelatedLinkCandidate` is one possible link from one wiki page to another wiki page.
`RelatedLink` is one accepted link with a source-neutral reason.
`RelationKind` is the category that explains why a target page helps the reader.
`RelatedLinkGroup` is an ordered group of accepted links with the same navigation purpose.
`LinkBudget` is the visible link limit for one page or group.
Current pages show many flat related links.
Flat link lists make collection pages and broad topic pages hard to scan.

## Goals

- Make related links explain why the target helps the reader.
- Group related links by source-neutral relation kind.
- Limit visible related links on large pages.
- Keep source-order navigation visible.
- Keep links deterministic and graph-checkable.
- Preserve zero unresolved wiki graph edges.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not change page target selection.
- This TDD does not create semantic search.
- This TDD does not remove graph export.

Forbidden approaches:

- Do not emit bare related links without a reason.
- Do not rank links from rendered markdown text.
- Do not use source-specific phrases to choose relation kind.
- Do not hide source-order links behind overflow.
- Do not create links that graph export cannot resolve.

## Requirements

- `RelatedLinkPlanner` must create `RelatedLinkCandidate` records from domain artifacts.
- Each `RelatedLinkCandidate` must include one `RelationKind`.
- Each `RelatedLinkCandidate` must include source support ids or structure support ids.
- `RelatedLinkPolicy` must accept or reject candidates before rendering.
- `RelatedLinkPolicy` must group accepted links into `RelatedLinkGroup` records.
- The page renderer must render related links by group.
- The page renderer must show link reason text for each visible link.
- The visible page link budget must be 24 links.
- The visible group link budget must be 8 links.
- Source-order links must use the `source-order` group.
- Broader and narrower structure links must use the `source-structure` group.
- Collection membership links must use the `collection` group.
- Shared technical atom links must use the `shared-technical-atom` group.
- Overflow links must move to a generated index page or collection page.
- `ProjectionLintRun` must reject a visible related link that lacks `RelationKind`.

## Invariants

- Wiki graph export remains complete.
- Every rendered related link resolves to an existing page.
- Every rendered related link has one reason.
- Relation kinds use reusable source categories.
- Relation kinds do not depend on source titles.
- Source-order navigation remains available when source order exists.

## Proposed Architecture

`RelatedLinkPlanner` produces candidates from page plans, structure edges, collection plans, topic links, and technical atom support.
`RelatedLinkPolicy` groups and budgets candidates.
`RelatedLinkRenderer` renders grouped links.
`GraphExporter` checks the resulting wiki links after publish.

```
+--------------+     +--------------------+     +-------------------+
| Page Plans   |---->| RelatedLinkPlanner |---->| RelatedLinkPolicy |
+--------------+     +----------+---------+     +---------+---------+
                              ^                         |
                              |                         v
        +---------------------+--------------+   +-------------------+
        | Structure, Topic, Atom, Collection |   | RelatedLinkGroups |
        +------------------------------------+   +---------+---------+
                                                            |
                                                            v
                                                    +---------------+
                                                    | Page Renderer |
                                                    +---------------+
```

`RelatedLinkPlanner` creates candidates.
`RelatedLinkPolicy` applies relation rules and budgets.
`RelatedLinkRenderer` renders grouped links.

## Key Interactions

Candidate planning:

```
SectionPlan -> RelatedLinkPlanner -> RelatedLinkCandidate
TopicIndex -> RelatedLinkPlanner -> RelatedLinkCandidate
CollectionPlan -> RelatedLinkPlanner -> RelatedLinkCandidate
TechnicalAtomIndex -> RelatedLinkPlanner -> RelatedLinkCandidate
```

Budgeted rendering:

```
RelatedLinkCandidate -> RelatedLinkPolicy -> RelatedLinkGroup
RelatedLinkGroup -> RelatedLinkRenderer -> PageBody
PageBody -> GraphExporter -> graph check
```

Lint rejection:

```
StagedWikiPage -> ProjectionLintRun -> RelatedLink diagnostics
ProjectionLintRun -> PublishRun -> accepted or rejected page
```

## Data Model

| Object | Contract |
|---|---|
| `RelatedLinkCandidate` | Source page id, target page id, relation kind, support ids, and score. |
| `RelatedLink` | Accepted target page id, relation kind, reason text, support ids, and order. |
| `RelatedLinkGroup` | Group kind, visible links, overflow count, and overflow target page id. |
| `LinkBudget` | Page visible limit and group visible limit. |

Allowed `RelationKind` values include `source-order`, `source-structure`, `collection`, `procedure-step`, `shared-technical-atom`, `shared-claim`, `contradiction`, and `qualification`.

## APIs / Interfaces

- `RelatedLinkPlanner`: accepts page plans and support artifacts and returns link candidates.
- `RelatedLinkPolicy`: accepts candidates and returns ordered groups.
- `RelatedLinkRenderer`: accepts groups and returns markdown sections.
- `ProjectionLintRun`: validates visible link reasons and graph resolvability.

## Behavior & Domain Rules

Rule: The renderer explains every visible related link.

Example: A page links to the next source section.
Expected outcome: The rendered link reason says that the target is the next source section.

Rule: The policy preserves source-order navigation.

Example: A page has previous, next, and 30 shared-atom candidates.
Expected outcome: Previous and next links remain visible.

Rule: The policy moves overflow links into a structured target.

Example: A collection page has 40 member links.
Expected outcome: The page shows visible grouped links and links to the member index for the rest.

## Acceptance Criteria

- A reingested large source has no unresolved graph edges.
- No page renders a bare related link.
- No page renders more than 24 visible related links.
- No related link group renders more than 8 visible links.
- Previous and next links remain visible on section pages.
- Broad topic pages group related links by relation kind.
- Collection pages use overflow targets for large member sets.
- A synthetic fixture with renamed nouns preserves relation kinds and budgets.

## Cross-Cutting Concerns

Observability: The ingest report records link candidate counts, accepted counts, overflow counts, and rejected counts.

Error handling: The renderer omits rejected candidates and emits lint diagnostics.

## Reference Implementations

- Graph export: `harness/src/llmwiki/runtime/graph_export.py`
- Related page projection: `harness/src/llmwiki/domain/related_link_planning.py`
- Staged lint: `harness/src/llmwiki/domain/ledger/staged_flow.py`

## Alternatives Considered

- Keep flat related link lists; rejected because large source pages become unscannable.
- Rank only by lexical similarity; rejected because lexical overlap creates inscrutable links.
- Run a model after page write to prune links; rejected because prevention belongs before rendering.

## Halt Conditions

- If implementation ranks links from rendered markdown, stop and use domain artifacts.
- If implementation cannot provide a relation kind, stop and reject the candidate.
- If graph export cannot resolve overflow targets, stop and fix target planning first.
