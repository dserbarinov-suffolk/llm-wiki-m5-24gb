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
projection_coverage: recipe-javascriptallonge-recipe-functions-and-identities@ecec357e78c56f9e2caf395a13304940
---

# functions and identities

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-and-id-6a23734c]].
- Evidence roles: decision, example.

## Applicability And Rationale

- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-c98ab3e6-00178))_
- You recall that we have two types of values with respect to identity: Value types and reference types. _(javascriptallonge.pdf (source-range-c98ab3e6-00178))_
- Reference types do not. _(javascriptallonge.pdf (source-range-c98ab3e6-00178))_
- Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. _(javascriptallonge.pdf (source-range-c98ab3e6-00181))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00180)_

```
(() => 0) === (() => 0)
//=> false
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-and-id-6a23734c]]
