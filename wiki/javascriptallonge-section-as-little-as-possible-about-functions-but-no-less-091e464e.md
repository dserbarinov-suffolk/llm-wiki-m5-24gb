---
page_id: javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-091e464e
page_kind: source
summary: As Little As Possible About Functions, But No Less: 12 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-091e464e@03d7fedd2697b0f9de25cd565615a14a
---

# As Little As Possible About Functions, But No Less

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-functions-and-identities-6c73c07b]] - next source section: functions and identities

## Statements

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00162))_
- This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others: _(javascriptallonge.pdf (source-range-c98ab3e6-00164))_
- What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else. _(javascriptallonge.pdf (source-range-c98ab3e6-00166))_
- I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-c98ab3e6-00168))_

## Technical atoms

### Technical frame 1: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00164))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00163))_

<a id="atom-technical-atom-55063c246fc08fa6"></a>
```
() => 0
```
