---
page_id: javascriptallonge-section-that-constant-coffee-craving-inside-out-6df7936c
page_kind: source
summary: That Constant Coffee Craving / inside-out: 21 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-that-constant-coffee-craving-inside-out-6df7936c@ab1700560e18e4e0c36c7576b99558dd
---

# That Constant Coffee Craving / inside-out

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-that-constant-coffee-craving-const-37801120]] - next source section: That Constant Coffee Craving / const

### Source structure

- [[javascriptallonge-section-that-constant-coffee-craving-614e2fd3]] - broader source section: That Constant Coffee Craving

### Recipes

- [[javascriptallonge-recipe-inside-out]] - recipe pattern: inside-out

## Statements

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00383))_
- Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-c98ab3e6-00387))_
- The third one is easiest for most people to read. It separates concerns nicely: The 'outer' function describes its parameters: _(javascriptallonge.pdf (source-range-c98ab3e6-00388))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-c98ab3e6-00389))_
- Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation: _(javascriptallonge.pdf (source-range-c98ab3e6-00391))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing _(javascriptallonge.pdf (source-range-c98ab3e6-00395))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-c98ab3e6-00397))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. And JavaScript does. _(javascriptallonge.pdf (source-range-c98ab3e6-00398))_
- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00383))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00389))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-c98ab3e6-00397))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-c98ab3e6-00398))_

## Technical atoms

### Technical frame 1: That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00387))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00384))_

<a id="atom-technical-atom-777993b745dde7ca"></a>
```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```
