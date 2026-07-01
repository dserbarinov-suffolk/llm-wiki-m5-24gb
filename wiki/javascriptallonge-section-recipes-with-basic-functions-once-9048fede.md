---
page_id: javascriptallonge-section-recipes-with-basic-functions-once-9048fede
page_kind: source
summary: Recipes with Basic Functions / Once: 8 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-once-9048fede@f88b36ecedc90b8d5e3d56db7ef2596b
---

# Recipes with Basic Functions / Once

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-58df4c63]] - broader source section: Recipes with Basic Functions
- [[javascriptallonge-section-recipes-with-basic-functions-maybe-d9752e09]] - previous source section: Recipes with Basic Functions / Maybe
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-c0cc9e6b]] - next source section: Recipes with Basic Functions / Left-Variadic Functions

## Statements

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-0e12e052-00705))_
- Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let's try it: _(javascriptallonge.pdf (source-range-0e12e052-00707))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. We'll look at that again in stateful method decorators.) _(javascriptallonge.pdf (source-range-0e12e052-00710))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-0e12e052-00705))_
- That function will call your function once, and thereafter will return undefined whenever it is called. _(javascriptallonge.pdf (source-range-0e12e052-00707))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00707))_

> Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00706))_

```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

### Technical frame 2: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00710))_

> (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. We'll look at that again in stateful method decorators.)

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00708))_

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
