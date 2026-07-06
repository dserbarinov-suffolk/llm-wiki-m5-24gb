---
page_id: javascriptallonge-recipe-higher-order-functions
page_kind: recipe
summary: higher-order functions: reusable source-backed pattern with 3 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: higher-order-functions
projection_coverage: recipe-javascriptallonge-recipe-higher-order-functions@0053f3bd0fe636e2c732fd1dde86aae7
---

# higher-order functions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-b21997ec]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-c98ab3e6-00552))_
- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-c98ab3e6-00552))_
- But before we go on, we'll talk about some specific types of higher-order functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00555))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00554)_

```
const repeat = (num, fn) =>
(num > 0)
? (repeat(num - 1, fn), fn(num))
: undefined
repeat(3, function (n) {
console.log(`Hello ${n}`)
})
//=>
'Hello 1'
'Hello 2'
'Hello 3'
undefined
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-b21997ec]]
