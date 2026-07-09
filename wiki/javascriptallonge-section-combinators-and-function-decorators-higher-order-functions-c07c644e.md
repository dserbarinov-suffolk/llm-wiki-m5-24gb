---
page_id: javascriptallonge-section-combinators-and-function-decorators-higher-order-functions-c07c644e
page_kind: source
summary: Combinators and Function Decorators / higher-order functions: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-combinators-and-function-decorators-higher-order-functions-c07c644e@43a9d28f33653864de9677084207afcb
---

# Combinators and Function Decorators / higher-order functions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-combinators-and-function-decorators-combinators-96e491bc]] - next source section: Combinators and Function Decorators / combinators

### Source structure

- [[javascriptallonge-section-combinators-and-function-decorators-901f172c]] - broader source section: Combinators and Function Decorators

### Recipes

- [[javascriptallonge-recipe-higher-order-functions]] - recipe pattern: higher-order functions

## Statements

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-c98ab3e6-00542))_
- But before we go on, we'll talk about some specific types of higher-order functions. _(javascriptallonge.pdf (source-range-c98ab3e6-00545))_

## Technical atoms

### Technical frame 1: Combinators and Function Decorators / higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00542))_

> As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00544))_

<a id="atom-technical-atom-4fc3e2e77a3ff1bc"></a>
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
