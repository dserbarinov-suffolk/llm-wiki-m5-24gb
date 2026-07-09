---
page_id: javascriptallonge-function-return-value
page_kind: concept
summary: Function Return Value: 1 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-return-value@3f51c500a2658c66e378f9645cdfe670
---

# Function Return Value

What [[javascriptallonge]] covers about function return value:

## Statements

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-c98ab3e6-00190))_


## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00187))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00186))_

<a id="atom-technical-atom-865137a5d59a0041"></a>
```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```


## Related pages

### Source structure

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-a65d460b]] - source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

### Topics

- [[javascriptallonge-return]] - broader topic: Return shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (1 shared atom(s))

## Source

- [[javascriptallonge]]
