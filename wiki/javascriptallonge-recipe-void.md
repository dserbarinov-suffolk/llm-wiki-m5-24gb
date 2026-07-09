---
page_id: javascriptallonge-recipe-void
page_kind: recipe
summary: void: reusable source-backed pattern with 4 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: void
projection_coverage: recipe-javascriptallonge-recipe-void@73cb8685ea204e6dd589f2fa7a651307
---

# void

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-or-even-void-81631fb5]].
- Evidence roles: decision, example.

## Applicability And Rationale

- By writing undefined ourselves. _(javascriptallonge.pdf (source-range-c98ab3e6-00222))_
- void is an operator that takes any value and evaluates to undefined , always. _(javascriptallonge.pdf (source-range-c98ab3e6-00225))_
- The first form works but it's cumbersome. _(javascriptallonge.pdf (source-range-c98ab3e6-00226))_
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-c98ab3e6-00226))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00224)_

```
void 0
//=> undefined
void 1
//=> undefined
void (2 + 2)
//=> undefined
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-or-even-void-81631fb5]]
