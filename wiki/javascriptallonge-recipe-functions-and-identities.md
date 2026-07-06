---
page_id: javascriptallonge-recipe-functions-and-identities
page_kind: recipe
summary: functions and identities: reusable source-backed pattern with 4 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: functions-and-identities
projection_coverage: recipe-javascriptallonge-recipe-functions-and-identities@3549b352a2c5a09e9595f1e399008f2b
---

# functions and identities

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-functions-and-identities-6c73c07b]].
- Evidence roles: decision, example.

## Applicability And Rationale

- You recall that we have two types of values with respect to identity: Value types and reference types. _(javascriptallonge.pdf (source-range-c98ab3e6-00170))_
- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-c98ab3e6-00170))_
- Reference types do not. _(javascriptallonge.pdf (source-range-c98ab3e6-00170))_
- Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. _(javascriptallonge.pdf (source-range-c98ab3e6-00173))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00172)_

```
(() => 0) === (() => 0)
//=> false
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-functions-and-identities-6c73c07b]]
