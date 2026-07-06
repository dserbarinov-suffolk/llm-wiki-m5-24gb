---
page_id: javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-1aea92c2
page_kind: source
summary: And also: / That Constant Coffee Craving / inside-out: 21 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-1aea92c2@d31dae6043e87018958e47dcf21911e8
---

# And also: / That Constant Coffee Craving / inside-out

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-const-c47e2fa1]] - next source section: And also: / That Constant Coffee Craving / const

### Source structure

- [[javascriptallonge-section-and-also-that-constant-coffee-craving-149774f4]] - broader source section: And also: / That Constant Coffee Craving

## Statements

- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00393))_
- Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-c98ab3e6-00397))_
- The third one is easiest for most people to read. It separates concerns nicely: The 'outer' function describes its parameters: _(javascriptallonge.pdf (source-range-c98ab3e6-00398))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. Explaining the pattern, Ben Alman coined the term [Immediately Invoked Function Expression][iife] for it, often abbreviated 'IIFE.' _(javascriptallonge.pdf (source-range-c98ab3e6-00399))_
- Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation: _(javascriptallonge.pdf (source-range-c98ab3e6-00401))_
- Well, the wrinkle with this is that typically, invoking functions is considerably more expensive than evaluating expressions. Every time we invoke the outer function, we'll invoke the inner function. We could get around this by writing _(javascriptallonge.pdf (source-range-c98ab3e6-00405))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-c98ab3e6-00407))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. And JavaScript does. _(javascriptallonge.pdf (source-range-c98ab3e6-00408))_
- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00393))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00399))_
- But then we've obfuscated our code, and we don't want to do that unless we absolutely have to. _(javascriptallonge.pdf (source-range-c98ab3e6-00407))_
- What would be very nice is if the language gave us a way to bind names inside of blocks without incurring the cost of a function invocation. _(javascriptallonge.pdf (source-range-c98ab3e6-00408))_

## Technical atoms

### Technical frame 1: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00397))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00394))_

<a id="atom-technical-atom-4395b77b43edc5c5"></a>
```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```
