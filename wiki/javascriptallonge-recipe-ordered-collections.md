---
page_id: javascriptallonge-recipe-ordered-collections
page_kind: recipe
summary: ordered collections: reusable source-backed pattern with 9 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: ordered-collections
projection_coverage: recipe-javascriptallonge-recipe-ordered-collections@02e1f3cfecc7efac334cb5b1a7ae1f99
---

# ordered collections

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-ordered-collections-3e509cbd]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- The iterables we're discussing represent ordered collections . _(javascriptallonge.pdf (source-range-0e12e052-01574))_
- One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. _(javascriptallonge.pdf (source-range-0e12e052-01574))_
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward. _(javascriptallonge.pdf (source-range-0e12e052-01576))_
- Iterables needn't represent ordered collections. _(javascriptallonge.pdf (source-range-0e12e052-01577))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-0e12e052-01579))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-0e12e052-01579))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01575)_

```
const abc = ["a", "b", "c"];
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01578)_

```
const RandomNumbers = {
[Symbol.iterator]: () =>
({
next () {
return {value: Math.random()};
}
})
}
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.494052127469331
0.835459444206208
0.1408337657339871
...
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.7845381607767195
0.4956772483419627
0.20259276474826038
...
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-ordered-collections-3e509cbd]]
