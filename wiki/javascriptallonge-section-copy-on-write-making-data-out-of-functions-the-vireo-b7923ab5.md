---
page_id: javascriptallonge-section-copy-on-write-making-data-out-of-functions-the-vireo-b7923ab5
page_kind: source
summary: Copy on Write / Making Data Out Of Functions / the vireo: 13 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-making-data-out-of-functions-the-vireo-b7923ab5@34232a9d07aec4587d161b95836169c0
---

# Copy on Write / Making Data Out Of Functions / the vireo

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-12daea71]] - broader source section: Copy on Write / Making Data Out Of Functions
- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-backwardness-24f99a95]] - previous source section: Copy on Write / Making Data Out Of Functions / backwardness
- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-lists-with-functions-as-data-52fd04fd]] - next source section: Copy on Write / Making Data Out Of Functions / lists with functions as data

## Statements

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. For arrays, we'd write cons = (first, second) => [first, second] . For objects we'd write: cons = (first, second) => {first, second} . In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-0e12e052-01359))_
- For 'data' we access with K and K(I) , our 'structure' is the function (selector) => selector("primus")("secundus") . Let's extract those into parameters: _(javascriptallonge.pdf (source-range-0e12e052-01360))_
- For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function: _(javascriptallonge.pdf (source-range-0e12e052-01362))_
- As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap . _(javascriptallonge.pdf (source-range-0e12e052-01369))_

## Technical atoms

### Technical frame 1: Copy on Write / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01369))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01368))_

```
const first = K,
second = K(I),
pair = V;
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```
