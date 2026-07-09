---
page_id: javascriptallonge-void
page_kind: concept
summary: void: 4 accepted assertion(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_9819277a7f44860b@553a6c6de615c4741219e430f8de2a8b
---

# void

Source: [[javascriptallonge]]

## Statements

- By writing undefined ourselves. (javascriptallonge.pdf p.35)
- void is an operator that takes any value and evaluates to undefined , always. (javascriptallonge.pdf p.35)
- The first form works but it's cumbersome. (javascriptallonge.pdf p.35)
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. (javascriptallonge.pdf p.35)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
void 0
//=> undefined
void 1
//=> undefined
void (2 + 2)
//=> undefined
```
