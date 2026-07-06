---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-5e2fa23b
page_kind: source
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: 12 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-5e2fa23b@6ce66e231e62ef79f4eab1ec0e2de562
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-applying-functio-5e7d9915]] - previous source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions
- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-b207d7ab]] - next source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

### Source structure

- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-adfe6790]] - broader source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

## Statements

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-c98ab3e6-00190))_
- In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow? _(javascriptallonge.pdf (source-range-c98ab3e6-00193))_
- Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ? _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_
- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-c98ab3e6-00198))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00195))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00194))_

<a id="atom-technical-atom-05b18e9495339725"></a>
```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00198))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00199))_

<a id="atom-technical-atom-313acb45627b4528"></a>
> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.
