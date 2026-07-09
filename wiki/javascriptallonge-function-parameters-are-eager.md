---
page_id: javascriptallonge-function-parameters-are-eager
page_kind: concept
summary: function parameters are eager: 2 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_749255bc03762f99@742f1646128857cefb085295871b37f0
---

# function parameters are eager

Source: [[javascriptallonge]]

## Statements

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
