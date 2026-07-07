---
page_id: javascriptallonge-recipe-lazy-collection-operations
page_kind: recipe
summary: lazy collection operations: reusable source-backed pattern with 11 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: lazy-collection-operations
projection_coverage: recipe-javascriptallonge-recipe-lazy-collection-operations@1245105fa91502924d4f4ec86afa547a
---

# lazy collection operations

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-0de83c02]].
- Evidence roles: decision, constraint, explanation, example, structured-state.

## Applicability And Rationale

- But it can be an excellent strategy for efficiency in algorithms. _(javascriptallonge.pdf (source-range-c98ab3e6-01753))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-c98ab3e6-01756))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-c98ab3e6-01757))_
- They produce small iterable objects that refer back to the original iteration. _(javascriptallonge.pdf (source-range-c98ab3e6-01758))_
- Whereas the .map and .filter methods on Pair work with iterators. _(javascriptallonge.pdf (source-range-c98ab3e6-01758))_
- This expression begins with a stack containing 30 elements. _(javascriptallonge.pdf (source-range-c98ab3e6-01761))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01755)_

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01769)_

```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
const firstCubeOver1234 =
Numbers
.map((x) => x * x * x)
.filter((x) => x > 1234)
.first()
//=> 1331
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-0de83c02]]
