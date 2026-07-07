---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-a65d460b
page_kind: source
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: 11 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-a65d460b@a0bf4d63c3ff10ec5a1a4a0a36161b33
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-applying-functio-858c485d]] - previous source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions
- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-53801ea8]] - next source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

### Source structure

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-a62974a6]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

## Statements

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-c98ab3e6-00182))_
- In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow? _(javascriptallonge.pdf (source-range-c98ab3e6-00185))_
- Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ? _(javascriptallonge.pdf (source-range-c98ab3e6-00187))_
- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-c98ab3e6-00190))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00187))_

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
