---
page_id: javascriptallonge-section-functions-that-return-values-and-evaluate-expressions-6ffa5875
page_kind: source
summary: functions that return values and evaluate expressions: 12 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-functions-that-return-values-and-evaluate-expressions-6ffa5875@829deacabdc0d385b453ffb7916ea92d
---

# functions that return values and evaluate expressions

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-applying-functions-09d5f96e]] - previous source section: applying functions
- [[javascriptallonge-section-commas-c347cbd5]] - next source section: commas

## Statements

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-c98ab3e6-00182))_
- In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow? _(javascriptallonge.pdf (source-range-c98ab3e6-00185))_
- Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ? _(javascriptallonge.pdf (source-range-c98ab3e6-00187))_
- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-c98ab3e6-00190))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-c98ab3e6-00187))_

## Technical atoms

### Technical frame 1: functions that return values and evaluate expressions

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

### Technical frame 2: functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00190))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00191))_

<a id="atom-technical-atom-5c40de3ec2a4cb7a"></a>
> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.
