---
page_id: javascriptallonge-function-parameters-are-eager
page_kind: concept
summary: topic-concept: 8 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_6e769687d7d8e7e1@e9da32b0a41c9f27e9cb6765ee523d46
---

# function parameters are eager

Source: [[javascriptallonge]]

## Statements

- If we need to have functions with control-flow semantics, we can pass anonymous functions. (javascriptallonge.pdf p.98)
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. (javascriptallonge.pdf p.99)

## Rules

- If we need to have functions with control-flow semantics, we can pass anonymous functions. (javascriptallonge.pdf p.98)
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. (javascriptallonge.pdf p.99)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```

<a id="atom-2"></a>
**Atom:** code block

```
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
even(7)
//=> false
```


## Related pages

- [[javascriptallonge-truthiness-and-operators]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-summary]] - contextualizes: source-supported topic dependency
