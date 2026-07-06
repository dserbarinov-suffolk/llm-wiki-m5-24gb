---
page_id: javascriptallonge-recipe-bonus
page_kind: recipe
summary: bonus: reusable source-backed pattern with 6 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: bonus
projection_coverage: recipe-javascriptallonge-recipe-bonus@f0a129930b9eefc2d93d19622672a972
---

# bonus

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-copy-on-write-functional-iterators-bonus-9d9a69d5]].
- Evidence roles: decision, constraint, explanation, procedure, example.

## Applicability And Rationale

- In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-c98ab3e6-01311))_
- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-c98ab3e6-01311))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-c98ab3e6-01314))_
- If array was very large, and fn very slow, this would consume a lot of unnecessary time. _(javascriptallonge.pdf (source-range-c98ab3e6-01316))_
- And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-c98ab3e6-01316))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-c98ab3e6-01316))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01313)_

```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01315)_

```
const firstInArray = (fn, array) =>
array.filter(fn)[0];
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-copy-on-write-functional-iterators-bonus-9d9a69d5]]
