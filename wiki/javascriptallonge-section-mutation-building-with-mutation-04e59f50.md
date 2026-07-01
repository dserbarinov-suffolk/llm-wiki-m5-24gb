---
page_id: javascriptallonge-section-mutation-building-with-mutation-04e59f50
page_kind: source
summary: Mutation / building with mutation: 9 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mutation-building-with-mutation-04e59f50@64f70439fb813483067dc3f61c535f6b
---

# Mutation / building with mutation

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-mutation-93ded492]] - broader source section: Mutation
- [[javascriptallonge-section-mutation-mutation-and-data-structures-a8d1f947]] - previous source section: Mutation / mutation and data structures

## Statements

- As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-0e12e052-01148))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-0e12e052-01150))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-0e12e052-01152))_

## Technical atoms

### Technical frame 1: Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01150))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01149))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const copy = (node) => reverse(reverse(node));
```
