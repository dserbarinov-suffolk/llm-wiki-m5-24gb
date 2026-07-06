---
page_id: javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-b21997ec
page_kind: source
summary: And also: / Combinators and Function Decorators / higher-order functions: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-combinators-and-function-decorators-higher-order-functions-b21997ec@edcb792f5b923172d15f57925583b2df
---

# And also: / Combinators and Function Decorators / higher-order functions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-combinators-21ded55c]] - next source section: And also: / Combinators and Function Decorators / combinators

### Source structure

- [[javascriptallonge-section-and-also-combinators-and-function-decorators-f08ca983]] - broader source section: And also: / Combinators and Function Decorators

## Statements

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-c98ab3e6-00552))_
- But before we go on, we'll talk about some specific types of higher-order functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00555))_

## Technical atoms

### Technical frame 1: And also: / Combinators and Function Decorators / higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00552))_

> As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00554))_

<a id="atom-technical-atom-efae692b221fbed3"></a>
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
