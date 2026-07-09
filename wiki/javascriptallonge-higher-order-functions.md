---
page_id: javascriptallonge-higher-order-functions
page_kind: concept
summary: topic-concept: 5 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_f771ce17e35be6c8@149330cc1bb1e695a4f46bfadcc6a047
---

# higher-order functions

Source: [[javascriptallonge]]

## Statements

- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. (javascriptallonge.pdf p.68)
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. (javascriptallonge.pdf p.68)

## Rules

- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. (javascriptallonge.pdf p.68)

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


## Related pages

- [[javascriptallonge-combinator]] - contextualizes: source-supported topic dependency
