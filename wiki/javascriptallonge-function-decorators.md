---
page_id: javascriptallonge-function-decorators
page_kind: concept
summary: topic-concept: 6 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_8ff172cee865ccd5@81a010ee422f9e708d81d9246d762d62
---

# function decorators

Source: [[javascriptallonge]]

## Procedure

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . (javascriptallonge.pdf p.70)
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. (javascriptallonge.pdf p.70)
- Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. (javascriptallonge.pdf p.70)

## Required tables and formulas

<a id="atom-1"></a>
**Atom:** table

```text
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```


## Rules and exceptions

- So instead of writing !someFunction(42) , we can write not(someFunction)(42) . (javascriptallonge.pdf p.70)

## Related pages

- [[javascriptallonge-balanced-statement-about-combinators]] - contextualizes: source-supported topic dependency
