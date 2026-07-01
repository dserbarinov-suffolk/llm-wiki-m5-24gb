---
page_id: javascriptallonge-recipe-undefined
page_kind: recipe
summary: undefined: reusable source-backed pattern with 8 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: undefined
projection_coverage: recipe-javascriptallonge-recipe-undefined@431d92a84b033aa151ca17c34492b340
---

# undefined

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-or-even-the-simplest-possible-block-undefined-7e43bbd5]].
- Evidence roles: decision, definition, explanation, constraint, example.

## Applicability And Rationale

- It will crop up again. _(javascriptallonge.pdf (source-range-0e12e052-00219))_
- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-0e12e052-00219))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-0e12e052-00222))_
- No matter how you evaluate undefined , you get an identical value back. _(javascriptallonge.pdf (source-range-0e12e052-00224))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-0e12e052-00225))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. _(javascriptallonge.pdf (source-range-0e12e052-00226))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00220)_

```
undefined
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00221)_

```
//=> undefined
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00223)_

```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-or-even-the-simplest-possible-block-undefined-7e43bbd5]]
