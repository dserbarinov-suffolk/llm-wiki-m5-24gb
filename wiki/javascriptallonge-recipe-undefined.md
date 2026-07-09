---
page_id: javascriptallonge-recipe-undefined
page_kind: recipe
summary: undefined: reusable source-backed pattern with 8 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: undefined
projection_coverage: recipe-javascriptallonge-recipe-undefined@604c326529af6fe71934be63b5cfc0aa
---

# undefined

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-or-even-the-simplest-possible-block-undefined-d76b1338]].
- Evidence roles: decision, definition, explanation, constraint, example.

## Applicability And Rationale

- In JavaScript, the absence of a value is written undefined , and it means there is no value. _(javascriptallonge.pdf (source-range-c98ab3e6-00211))_
- It will crop up again. _(javascriptallonge.pdf (source-range-c98ab3e6-00211))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined . _(javascriptallonge.pdf (source-range-c98ab3e6-00214))_
- No matter how you evaluate undefined , you get an identical value back. _(javascriptallonge.pdf (source-range-c98ab3e6-00216))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-c98ab3e6-00217))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. _(javascriptallonge.pdf (source-range-c98ab3e6-00218))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00212)_

```
undefined
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00213)_

```
//=> undefined
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00215)_

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
- Source section: [[javascriptallonge-section-or-even-the-simplest-possible-block-undefined-d76b1338]]
