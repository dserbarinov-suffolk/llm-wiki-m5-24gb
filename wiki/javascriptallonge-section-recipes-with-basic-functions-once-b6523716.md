---
page_id: javascriptallonge-section-recipes-with-basic-functions-once-b6523716
page_kind: source
summary: Recipes with Basic Functions / Once: 8 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-once-b6523716@d3ac753beb1fb8266b6a150e289492f7
---

# Recipes with Basic Functions / Once

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-basic-functions-maybe-c5a7d5d9]] - previous source section: Recipes with Basic Functions / Maybe
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-903c33c6]] - next source section: Recipes with Basic Functions / Left-Variadic Functions

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-8e785fac]] - broader source section: Recipes with Basic Functions

## Statements

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-c98ab3e6-00705))_
- Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let's try it: _(javascriptallonge.pdf (source-range-c98ab3e6-00707))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. We'll look at that again in stateful method decorators.) _(javascriptallonge.pdf (source-range-c98ab3e6-00710))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-c98ab3e6-00705))_
- That function will call your function once, and thereafter will return undefined whenever it is called. _(javascriptallonge.pdf (source-range-c98ab3e6-00707))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00707))_

> Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00706))_

<a id="atom-technical-atom-a7a053c1d4c6b810"></a>
```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

### Technical frame 2: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00710))_

> (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. We'll look at that again in stateful method decorators.)

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00708))_

<a id="atom-technical-atom-945418d0db616740"></a>
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
