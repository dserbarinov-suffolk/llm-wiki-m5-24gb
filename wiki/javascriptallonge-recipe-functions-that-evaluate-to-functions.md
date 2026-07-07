---
page_id: javascriptallonge-recipe-functions-that-evaluate-to-functions
page_kind: recipe
summary: functions that evaluate to functions: reusable source-backed pattern with 4 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: functions-that-evaluate-to-functions
projection_coverage: recipe-javascriptallonge-recipe-functions-that-evaluate-to-functions@246eeb3db84e6f842e532e9795238ab6
---

# functions that evaluate to functions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-functions-that-evaluate-to-functions-e337b1c9]].
- Evidence roles: decision, constraint, structured-state, example.

## Applicability And Rationale

- It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . _(javascriptallonge.pdf (source-range-c98ab3e6-00248))_
- So we have a function, that returns a function, that returns zero . _(javascriptallonge.pdf (source-range-c98ab3e6-00248))_
- Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. _(javascriptallonge.pdf (source-range-c98ab3e6-00255))_
- We've been very clever, but so far this all seems very abstract. _(javascriptallonge.pdf (source-range-c98ab3e6-00255))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00247)_

```
() => () => 0
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00249)_

```
() => () => true
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00251)_

```
(() => () => true)()()
//=> true
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00253)_

```
() => () => { return true; }
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-functions-that-evaluate-to-functions-e337b1c9]]
