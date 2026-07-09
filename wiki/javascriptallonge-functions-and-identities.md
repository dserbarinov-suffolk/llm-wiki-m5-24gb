---
page_id: javascriptallonge-functions-and-identities
page_kind: concept
summary: functions and identities: 4 accepted assertion(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_f9d9007bfb3139ed@b2da23a82594d2d653f8df541f1583db
---

# functions and identities

Source: [[javascriptallonge]]

## Statements

- You recall that we have two types of values with respect to identity: Value types and reference types. (javascriptallonge.pdf p.31)
- Value types share the same identity if they have the same contents. (javascriptallonge.pdf p.31)
- Reference types do not. (javascriptallonge.pdf p.31)
- Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. (javascriptallonge.pdf p.31)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
(() => 0) === (() => 0)
//=> false
```
