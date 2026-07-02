---
page_id: javascriptallonge-recipe-function-parameters-are-eager
page_kind: recipe
summary: function parameters are eager: reusable source-backed pattern with 3 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: function-parameters-are-eager
projection_coverage: recipe-javascriptallonge-recipe-function-parameters-are-eager@e0f446494f9b38dcf01adca4b529b69e
---

# function parameters are eager

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-fbbf2d6a]].
- Evidence roles: explanation, decision, constraint, example.

## Applicability And Rationale

- This leads to the infinite recursion we fear. _(javascriptallonge.pdf (source-range-0e12e052-00797))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. _(javascriptallonge.pdf (source-range-0e12e052-00798))_
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-0e12e052-00800))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00796)_

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00799)_

```
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
even(7)
//=> false
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-fbbf2d6a]]
