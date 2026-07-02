---
page_id: javascriptallonge-recipe-once
page_kind: recipe
summary: Once: reusable source-backed pattern with 4 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: once
projection_coverage: recipe-javascriptallonge-recipe-once@3ddd2c48fc408192a8af5cbfd6eb44f8
---

# Once

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-once-9048fede]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- once is an extremely helpful combinator. _(javascriptallonge.pdf (source-range-0e12e052-00705))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-0e12e052-00705))_
- That function will call your function once, and thereafter will return undefined whenever it is called. _(javascriptallonge.pdf (source-range-0e12e052-00707))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. _(javascriptallonge.pdf (source-range-0e12e052-00710))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00706)_

```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00708)_

```
const askedOnBlindDate = once(
() => "sure, why not?"
);
askedOnBlindDate()
//=> 'sure, why not?'
askedOnBlindDate()
//=> undefined
askedOnBlindDate()
//=> undefined
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-once-9048fede]]
