---
page_id: javascriptallonge-recipe-tap
page_kind: recipe
summary: Tap: reusable source-backed pattern with 4 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: tap
projection_coverage: recipe-javascriptallonge-recipe-tap@9fb7c7b754767113032aa5a8b0f2af3e
---

# Tap

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-tap-51486e75]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- One is when you want to do something with a value for sideeffects, but keep the value around. _(javascriptallonge.pdf (source-range-c98ab3e6-00668))_
- It has some surprising applications. _(javascriptallonge.pdf (source-range-c98ab3e6-00668))_
- tap is a traditional name borrowed from various Unix shell commands. _(javascriptallonge.pdf (source-range-c98ab3e6-00670))_
- tap can do more than just act as a debugging aid. _(javascriptallonge.pdf (source-range-c98ab3e6-00676))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00667)_

```
const K = (x) => (y) => x;
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00669)_

```
const tap = (value) =>
(fn) => (
typeof(fn) === 'function' && fn(value),
value
)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-tap-51486e75]]
