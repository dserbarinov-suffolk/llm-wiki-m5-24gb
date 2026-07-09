---
page_id: javascriptallonge-as-little-as-possible-about-functions-but-no-less
page_kind: concept
summary: topic-concept: 13 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_9f0c94166cd04f3a@a856afe68857700b378a22a7f73bab14
---

# As Little As Possible About Functions, But No Less

Source: [[javascriptallonge]]

## Statements

- Functions represent computations to be performed. (javascriptallonge.pdf p.30)
- Like numbers, strings, and arrays, they have a representation. (javascriptallonge.pdf p.30)
- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. (javascriptallonge.pdf p.30)
- This is a function that is applied to no values and returns 0 . (javascriptallonge.pdf p.30)
- The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. (javascriptallonge.pdf p.30)
- This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. (javascriptallonge.pdf p.30)
- I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. (javascriptallonge.pdf p.31)
- But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function. (javascriptallonge.pdf p.31)

## Rules

- I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. (javascriptallonge.pdf p.31)
- But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function. (javascriptallonge.pdf p.31)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
() => 0
```

<a id="atom-2"></a>
**Atom:** code block

```
(() => 0)
//=> [Function]
```

<a id="atom-3"></a>
**Atom:** rule

```
If you try the same thing in a browser, you may see something else.
```
