---
page_id: javascriptallonge-recipe-generating-iterables
page_kind: recipe
summary: Generating Iterables: reusable source-backed pattern with 11 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: generating-iterables
projection_coverage: recipe-javascriptallonge-recipe-generating-iterables@f3ea911d7d2d14becc7aebda87752497
---

# Generating Iterables

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-generating-iterables-5c843adb]].
- Evidence roles: decision, explanation, structured-state, example.

## Applicability And Rationale

- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. _(javascriptallonge.pdf (source-range-c98ab3e6-01594))_
- Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-c98ab3e6-01595))_
- This seems blindingly obvious and simple. _(javascriptallonge.pdf (source-range-c98ab3e6-01596))_
- The Numbers iterable returns an object that updates a mutable variable, n , to deliver number after number. _(javascriptallonge.pdf (source-range-c98ab3e6-01598))_
- There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. _(javascriptallonge.pdf (source-range-c98ab3e6-01599))_
- Then it waits for the next request. _(javascriptallonge.pdf (source-range-c98ab3e6-01599))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01597)_

```
const Numbers = {
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
};
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01601)_

```
let n = 0;
while (true) {
console.log(n++)
}
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01603)_

```
// Iteration
let n = 0;
() =>
({done: false, value: n++})
// Generation
let n = 0;
while (true) {
console.log(n++)
}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-generating-iterables-5c843adb]]
