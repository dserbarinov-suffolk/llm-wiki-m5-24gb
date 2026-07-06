---
page_id: javascriptallonge-section-once-70058fab
page_kind: source
summary: Once: 8 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-once-70058fab@2518a7fa75aa9b3a55a45dac075e5ea5
---

# Once

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-maybe-21b793e6]] - previous source section: Maybe
- [[javascriptallonge-section-left-variadic-functions-979e597b]] - next source section: Left-Variadic Functions

## Statements

- once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe: _(javascriptallonge.pdf (source-range-c98ab3e6-00693))_
- Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let's try it: _(javascriptallonge.pdf (source-range-c98ab3e6-00695))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. We'll look at that again in stateful method decorators.) _(javascriptallonge.pdf (source-range-c98ab3e6-00698))_
- It ensures that a function can only be called, well, once . _(javascriptallonge.pdf (source-range-c98ab3e6-00693))_
- That function will call your function once, and thereafter will return undefined whenever it is called. _(javascriptallonge.pdf (source-range-c98ab3e6-00695))_

## Technical atoms

### Technical frame 1: Once

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00695))_

> Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00694))_

<a id="atom-technical-atom-0f3208d550e42a8b"></a>
```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

### Technical frame 2: Once

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00698))_

> (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. We'll look at that again in stateful method decorators.)

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00696))_

<a id="atom-technical-atom-684b04e22940fa75"></a>
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
