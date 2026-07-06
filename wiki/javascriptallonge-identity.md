---
page_id: javascriptallonge-identity
page_kind: concept
summary: Identity: 2 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-identity@03bdb599ade09e91441e5ecd5c915428
---

# Identity

What [[javascriptallonge]] covers about identity:

## Statements

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. _(javascriptallonge.pdf (source-range-c98ab3e6-00178))_


## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00181))_

> Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. 'Function' is a reference type.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00180))_

<a id="atom-technical-atom-f6e13870f2a36c24"></a>
```
(() => 0) === (() => 0)
//=> false
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: (() => 0) === (() => 0) //=> false (1 shared atom(s))

### Shared claims

- [[javascriptallonge-type]] - shared statements: Type shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
