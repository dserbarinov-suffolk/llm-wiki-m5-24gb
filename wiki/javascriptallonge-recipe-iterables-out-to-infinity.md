---
page_id: javascriptallonge-recipe-iterables-out-to-infinity
page_kind: recipe
summary: iterables out to infinity: reusable source-backed pattern with 2 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: iterables-out-to-infinity
projection_coverage: recipe-javascriptallonge-recipe-iterables-out-to-infinity@ef2551fdbd87b65ea451828738898e9d
---

# iterables out to infinity

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterables-out-to-infinity-7b9b9df6]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- There are useful things we can do with iterables representing an infinitely large collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01570))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-c98ab3e6-01572))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01569)_

```
const Numbers = {
[Symbol.iterator] () {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01571)_

```
['all the numbers', ...Numbers]
//=> infinite loop!
firstAndSecondElement(...Numbers)
//=> infinite loop!
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterables-out-to-infinity-7b9b9df6]]
