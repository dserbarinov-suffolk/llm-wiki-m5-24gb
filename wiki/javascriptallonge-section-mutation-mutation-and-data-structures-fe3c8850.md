---
page_id: javascriptallonge-section-mutation-mutation-and-data-structures-fe3c8850
page_kind: source
summary: Mutation / mutation and data structures: 11 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mutation-mutation-and-data-structures-fe3c8850@f216b1d21ca52270b9f3766cdb715bb3
---

# Mutation / mutation and data structures

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-mutation-building-with-mutation-e30d36e8]] - next source section: Mutation / building with mutation

### Source structure

- [[javascriptallonge-section-mutation-ae8039d8]] - broader source section: Mutation

## Statements

- Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell 70 don't permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-c98ab3e6-01118))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let's recall linked lists from Plain Old JavaScript Objects. While we're executing the mapWith function, we're constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-01119))_
- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' _(javascriptallonge.pdf (source-range-c98ab3e6-01126))_
- So back to avoiding mutation. In general, it's easier to reason about data that doesn't change. We don't have to remember to use copying operations when we pass it as a value to a function, or extract some data from it. We just use the data, and the less we mutate it, the fewer the times we have to think about whether making changes will be 'safe.' _(javascriptallonge.pdf (source-range-c98ab3e6-01127))_

## Technical atoms

### Technical frame 1: Mutation / mutation and data structures

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01126))_

> The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. '

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01120))_

<a id="atom-technical-atom-02e050cf9b1a8a6c"></a>
> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:
