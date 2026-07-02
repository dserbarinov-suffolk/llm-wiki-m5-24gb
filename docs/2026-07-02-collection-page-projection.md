# Collection Page Projection - TDD (2026-07-02)

## Context & Problem

`CollectionCandidate` is a source-derived group of repeated peer items.
`CollectionPage` is a wiki page that represents one accepted `CollectionCandidate`.
`CollectionMember` is one item inside a collection.
`CollectionFacet` is one source-derived field that helps compare collection members.
`CollectionPlan` is the projection plan for one `CollectionPage`.
Current section pages use the same rendering shape for prose sections and list sections.
Large lists, catalogs, spell lists, equipment lists, and monster lists become long pages with many related links.
Those pages need a compact collection shape that preserves source evidence.

## Goals

- Detect collection-shaped source regions from source structure and repeated evidence shape.
- Render accepted collections as compact, navigable pages.
- Preserve full member evidence through claims and technical atoms.
- Group members by source-derived facets.
- Reduce related-link overload on list and catalog sections.
- Keep collection logic portable across LLM-Wiki implementations.

## Non-Goals & Forbidden Approaches

Non-goals:

- This TDD does not define a domain-specific catalog schema.
- This TDD does not replace ordinary section pages.
- This TDD does not change table reconstruction.

Forbidden approaches:

- Do not detect collections from source-specific headings.
- Do not maintain bespoke lists of catalog words.
- Do not create one page per table row by default.
- Do not collapse member evidence into uncited summaries.
- Do not require a model call to decide every collection member.

## Requirements

- `CollectionDetector` must evaluate `DocumentStructure`, `ClaimLedger`, and `TechnicalAtom` records.
- `CollectionDetector` must score repeated peer shape.
- Repeated peer shape must include at least two reusable signals.
- Reusable signals include sibling structure, repeated table rows, repeated definition entries, repeated stat blocks, repeated bullet shape, and repeated field labels.
- `CollectionDetector` must produce `CollectionCandidate` records.
- `CollectionPolicy` must accept or reject each `CollectionCandidate`.
- `CollectionPolicy` must require at least three `CollectionMember` records.
- `CollectionPolicy` must require one source-derived grouping basis or one source-order basis.
- `CollectionPlan` must retain source order for all members.
- `CollectionPlan` must retain source support ids for all members.
- `CollectionPage` must show a member index before long evidence sections.
- `CollectionPage` must group related pages by collection role.
- `CollectionPage` must link to broader section pages.
- `CollectionPage` must link to member pages when member pages exist.
- `CollectionPage` must not render more than 24 visible related links.
- Overflow related links must appear through grouped collection indexes.

## Invariants

- `RawSource` remains immutable.
- Every `CollectionMember` keeps source support.
- Collection detection uses reusable source categories.
- Collection detection does not use source titles.
- Collection detection does not use quoted source phrases as rules.
- A section page links to a collection page without duplicating the collection body.
- Generated wiki pages remain replaceable test data.

## Proposed Architecture

The pipeline adds collection planning after section planning and before page projection.
`CollectionDetector` finds repeated peer regions.
`CollectionPolicy` accepts candidates that have stable source-derived structure.
`CollectionPlanner` creates collection page targets and member indexes.
`CollectionPageRenderer` renders compact collection pages.

```
+-------------------+     +-------------------+     +----------------+
| DocumentStructure |---->| CollectionDetector|---->| CollectionPlan |
+-------------------+     +---------+---------+     +-------+--------+
                                  ^                       |
                                  |                       v
                   +--------------+------------+   +---------------+
                   | ClaimLedger, TechnicalAtom|   | CollectionPage|
                   +---------------------------+   +---------------+
```

`CollectionDetector` measures repeated peer shape.
`CollectionPolicy` decides whether a candidate becomes a page.
`CollectionPlanner` creates the page target and member order.
`CollectionPageRenderer` renders the member index and evidence links.

## Key Interactions

Collection detection:

```
DocumentStructure -> CollectionDetector -> CollectionCandidate
ClaimLedger -> CollectionDetector -> CollectionCandidate
TechnicalAtom -> CollectionDetector -> CollectionCandidate
CollectionCandidate -> CollectionPolicy -> CollectionPlan
```

Collection page projection:

```
CollectionPlan -> CollectionPageRenderer -> StagedWikiPage
StagedWikiPage -> ProjectionLintRun -> PublishRun
```

Section page link:

```
SectionPlan -> RelatedLinkPlanner -> collection RelatedLink
SectionPageRenderer -> link to CollectionPage
```

## Data Model

| Object | Contract |
|---|---|
| `CollectionCandidate` | Source range, peer signal set, candidate members, and score. |
| `CollectionMember` | Member id, source order, display label, support ids, and facet values. |
| `CollectionFacet` | Source-derived field name, value, support ids, and confidence. |
| `CollectionPlan` | Accepted candidate id, page id, member order, facets, and relation links. |

`CollectionCandidate.peer_signal_kind` uses controlled source-neutral values.
Allowed values include `sibling-structure`, `table-row`, `definition-entry`, `stat-block`, `bullet-shape`, and `field-label-set`.

## APIs / Interfaces

- `CollectionDetector`: accepts source-scoped artifacts and returns `CollectionCandidate` records.
- `CollectionPolicy`: accepts candidates and returns accepted `CollectionPlan` records.
- `CollectionPageRenderer`: accepts one `CollectionPlan` and returns one `StagedWikiPage`.
- `RelatedLinkPlanner`: accepts collection plans as link targets.

## Behavior & Domain Rules

Rule: A repeated peer region becomes a collection when evidence shape supports it.

Example: A section has 18 sibling entries with the same field labels.
Expected outcome: The pipeline creates one collection page with 18 members.

Rule: A normal prose section remains a section page.

Example: A section has 10 paragraphs and no repeated peer shape.
Expected outcome: The pipeline does not create a collection page.

Rule: A table row does not become a standalone page by default.

Example: A table has 12 equipment rows.
Expected outcome: The collection page lists all rows as members and links to the table atom.

## Acceptance Criteria

- A synthetic catalog source produces at least one `CollectionPage`.
- A synthetic prose source produces no `CollectionPage`.
- A reingested rulebook source groups spell, item, or monster lists into collection pages when repeated peer shape exists.
- Collection pages show member indexes before evidence.
- Collection pages preserve source order.
- Collection pages link to broader section pages.
- Section pages link to collection pages for accepted collections.
- No collection page renders more than 24 visible related links.
- A synthetic fixture that renames all domain nouns preserves the same collection decisions.

## Cross-Cutting Concerns

Observability: The ingest report records accepted and rejected collection counts with peer signal kinds.

Error handling: The pipeline keeps a candidate as a section page when collection acceptance fails.

## Reference Implementations

- Section planning: `harness/src/llmwiki/domain/section_planning.py`
- Topic index domain: `harness/src/llmwiki/domain/topic_index.py`
- Related link planning: `harness/src/llmwiki/domain/related_link_planning.py`

## Alternatives Considered

- Use heading word lists; rejected because that violates the Universal Standard.
- Ask the model to classify every collection; rejected because repeated shape is mostly deterministic.
- Render collections only as related links; rejected because users need a compact member index.

## Halt Conditions

- If implementation needs a source-specific heading phrase, stop and add a source-neutral signal instead.
- If implementation creates pages for every row by default, stop and revise `CollectionPolicy`.
- If a collection member lacks source support, stop and reject that candidate.
