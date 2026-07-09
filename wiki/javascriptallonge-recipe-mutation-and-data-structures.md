---
page_id: javascriptallonge-recipe-mutation-and-data-structures
page_kind: recipe
summary: mutation and data structures: reusable source-backed pattern with 8 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: mutation-and-data-structures
projection_coverage: recipe-javascriptallonge-recipe-mutation-and-data-structures@703057ecc6489450a83e67393937832e
---

# mutation and data structures

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-mutation-mutation-and-data-structures-fe3c8850]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-c98ab3e6-01118))_
- Mutation is a surprisingly complex subject. _(javascriptallonge.pdf (source-range-c98ab3e6-01118))_
- It is possible to compute anything without ever mutating an existing entity. _(javascriptallonge.pdf (source-range-c98ab3e6-01118))_
- By this pattern, we would be happy to use mutation to construct the list while running mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-01119))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-c98ab3e6-01119))_
- While we're executing the mapWith function, we're constructing a new linked list. _(javascriptallonge.pdf (source-range-c98ab3e6-01119))_

## Technical Atoms

### Atom 1: `worked-example`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01120)_

```
But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01124)_

```
const OneToFive = [1, 2, 3, 4, 5];
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] = OneToFive;
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01125)_

```
OneToFive
//=> [1,2,3,4,5]
const [a, b, ...ThreeToFive] =
ThreeToFive
//=> [3, 4, 5]
ThreeToFive[0] = "three";
ThreeToFive[1] = "four";
ThreeToFive[2] = "five";
ThreeToFive
//=> ["three","four","five"]
OneToFive
//=> [1,2,3,4,5]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-mutation-mutation-and-data-structures-fe3c8850]]
