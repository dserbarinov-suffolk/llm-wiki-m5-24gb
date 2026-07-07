---
page_id: javascriptallonge-identity
page_kind: concept
summary: Identity: 2 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-identity@f5c390fff57238daf5569e4cb92c7aa4
---

# Identity

What [[javascriptallonge]] covers about identity:

## Statements

### functions and identities

- You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. _(javascriptallonge.pdf (source-range-c98ab3e6-00170))_


## Technical atoms

### Technical frame 1: functions and identities

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00173))_

> Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. 'Function' is a reference type.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00172))_

<a id="atom-technical-atom-1bdec14274efa197"></a>
```
(() => 0) === (() => 0)
//=> false
```


## Related pages

### Shared claims

- [[javascriptallonge-type]] - shared statements: Type shares source evidence from functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
