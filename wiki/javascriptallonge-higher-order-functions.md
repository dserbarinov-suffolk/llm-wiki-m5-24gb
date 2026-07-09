---
page_id: javascriptallonge-higher-order-functions
page_kind: concept
summary: higher-order functions: 2 accepted assertion(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_e987f4f761557633@9520c2a27ba7d8d6c84a267622634847
---

# higher-order functions

Source: [[javascriptallonge]]

## Statements

- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. (javascriptallonge.pdf p.68)
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. (javascriptallonge.pdf p.68)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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
