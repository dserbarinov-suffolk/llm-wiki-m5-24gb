---
page_id: javascriptallonge-recipe-the-simplest-possible-block
page_kind: recipe
summary: the simplest possible block: reusable source-backed pattern with 2 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: the-simplest-possible-block
projection_coverage: recipe-javascriptallonge-recipe-the-simplest-possible-block@299b44c7bd63c729dc5ff1b65297f941
---

# the simplest possible block

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-simplest-possible-block-5da702d2]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- There's another thing we can put to the right of an arrow, a block . _(javascriptallonge.pdf (source-range-c98ab3e6-00204))_
- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-c98ab3e6-00207))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00206)_

```
() => {}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00208)_

```
(() => {})()
//=> undefined
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-simplest-possible-block-5da702d2]]
