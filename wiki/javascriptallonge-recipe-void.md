---
page_id: javascriptallonge-recipe-void
page_kind: recipe
summary: void: reusable source-backed pattern with 3 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: void
projection_coverage: recipe-javascriptallonge-recipe-void@286dc2af520fe014364f38eb45f506b5
---

# void

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-or-even-void-b48c3fc8]].
- Evidence roles: decision, example.

## Applicability And Rationale

- void is an operator that takes any value and evaluates to undefined , always. _(javascriptallonge.pdf (source-range-c98ab3e6-00233))_
- The first form works but it's cumbersome. _(javascriptallonge.pdf (source-range-c98ab3e6-00234))_
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-c98ab3e6-00234))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00232)_

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
- Source section: [[javascriptallonge-section-or-even-void-b48c3fc8]]
