---
page_id: javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-15759c94
page_kind: source
summary: And also: / Combinators and Function Decorators / higher-order functions: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-15759c94@270622fdaf4c6b35a8930190928856a5
---

# And also: / Combinators and Function Decorators / higher-order functions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-4a7771ac]] - broader source section: And also: / Combinators and Function Decorators
- [[javascriptallonge-section-and-also-combinators-and-function-decorators-combinators-d366528a]] - next source section: And also: / Combinators and Function Decorators / combinators

## Statements

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-0e12e052-00552))_
- But before we go on, we'll talk about some specific types of higher-order functions. _(javascriptallonge.pdf (source-range-0e12e052-00555))_

## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00552))_

> As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00554))_

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
