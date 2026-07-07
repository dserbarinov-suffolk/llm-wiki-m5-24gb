---
page_id: javascriptallonge-section-function-parameters-are-eager-a0f9ecc8
page_kind: source
summary: function parameters are eager: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-function-parameters-are-eager-a0f9ecc8@79cef983d61f711b89e696c9793a5ba5
---

# function parameters are eager

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-and-are-control-flow-operators-ca841bc9]] - previous source section: || and && are control-flow operators
- [[javascriptallonge-section-summary-96eff45c]] - next source section: summary

## Statements

- If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique: _(javascriptallonge.pdf (source-range-c98ab3e6-00785))_
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-c98ab3e6-00787))_
- This leads to the infinite recursion we fear. _(javascriptallonge.pdf (source-range-c98ab3e6-00784))_

## Technical atoms

### Technical frame 1: function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00785))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00783))_

<a id="atom-technical-atom-d46d0adcfad1d7bc"></a>
```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```
