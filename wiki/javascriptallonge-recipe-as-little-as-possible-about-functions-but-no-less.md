---
page_id: javascriptallonge-recipe-as-little-as-possible-about-functions-but-no-less
page_kind: recipe
summary: As Little As Possible About Functions, But No Less: reusable source-backed pattern with 8 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: as-little-as-possible-about-functions-but-no-less
projection_coverage: recipe-javascriptallonge-recipe-as-little-as-possible-about-functions-but-no-less@4a5ed6c1e3dff9f8b4b9dc3c72d311e3
---

# As Little As Possible About Functions, But No Less

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-091e464e]].
- Evidence roles: decision, constraint, example, structured-state.

## Applicability And Rationale

- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-c98ab3e6-00162))_
- Like numbers, strings, and arrays, they have a representation. _(javascriptallonge.pdf (source-range-c98ab3e6-00162))_
- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. _(javascriptallonge.pdf (source-range-c98ab3e6-00162))_
- This is a function that is applied to no values and returns 0 . _(javascriptallonge.pdf (source-range-c98ab3e6-00164))_
- The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. _(javascriptallonge.pdf (source-range-c98ab3e6-00166))_
- This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. _(javascriptallonge.pdf (source-range-c98ab3e6-00166))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00163)_

```
() => 0
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00165)_

```
(() => 0)
//=> [Function]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-091e464e]]
