---
page_id: javascriptallonge-section-mutation-building-with-mutation-e30d36e8
page_kind: source
summary: Mutation / building with mutation: 9 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mutation-building-with-mutation-e30d36e8@763fb5d0e167c3c862bca4382df8be4e
---

# Mutation / building with mutation

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-mutation-mutation-and-data-structures-fe3c8850]] - previous source section: Mutation / mutation and data structures

### Source structure

- [[javascriptallonge-section-mutation-ae8039d8]] - broader source section: Mutation

### Recipes

- [[javascriptallonge-recipe-building-with-mutation]] - recipe pattern: building with mutation

## Statements

- As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-c98ab3e6-01129))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-c98ab3e6-01131))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-c98ab3e6-01133))_

## Technical atoms

### Technical frame 1: Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01131))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01130))_

<a id="atom-technical-atom-4afa51806ee60093"></a>
```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const copy = (node) => reverse(reverse(node));
```
