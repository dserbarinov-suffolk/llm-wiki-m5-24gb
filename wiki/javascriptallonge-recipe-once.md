---
page_id: javascriptallonge-recipe-once
page_kind: recipe
summary: Once: reusable source-backed pattern with 4 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: once
projection_coverage: recipe-javascriptallonge-recipe-once@2fb66fc61da7fed0d4abae350ca43e7f
---

# Once

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-d7445960]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- once is an extremely helpful combinator. _(javascriptallonge.pdf (source-range-c98ab3e6-00693))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-c98ab3e6-00693))_
- That function will call your function once, and thereafter will return undefined whenever it is called. _(javascriptallonge.pdf (source-range-c98ab3e6-00695))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. _(javascriptallonge.pdf (source-range-c98ab3e6-00698))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00694)_

```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00696)_

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
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-d7445960]]
