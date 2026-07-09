---
page_id: javascriptallonge-maybe
page_kind: concept
summary: topic-concept: 11 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_3907b1f5ff00d1c3@106d52da858b1ee4aee5c769d0485632
---

# Maybe

Source: [[javascriptallonge]]

## Procedure

- A common problem in programming is checking for null or undefined (hereafter called 'nothing,' while all other values including 0 , [] and false will be called 'something'). (javascriptallonge.pdf p.86)
- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. (javascriptallonge.pdf p.86)
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:. (javascriptallonge.pdf p.86)
- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:. (javascriptallonge.pdf p.86)
- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. (javascriptallonge.pdf p.87)

## Required tables and formulas

<a id="atom-1"></a>
**Atom:** table

```text
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```


## Rules and exceptions

- Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing. (javascriptallonge.pdf p.86)
- Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:. (javascriptallonge.pdf p.86)
- Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:. (javascriptallonge.pdf p.86)

## Related pages

- [[javascriptallonge-tap]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-once]] - contextualizes: source-supported topic dependency
