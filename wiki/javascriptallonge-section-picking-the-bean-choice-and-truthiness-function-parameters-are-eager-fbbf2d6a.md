---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-fbbf2d6a
page_kind: source
summary: Picking the Bean: Choice and Truthiness / function parameters are eager: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-fbbf2d6a@247bffe51aa7647761cf841d9d441d1d
---

# Picking the Bean: Choice and Truthiness / function parameters are eager

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-851a6e13]] - broader source section: Picking the Bean: Choice and Truthiness
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-e907a1ef]] - previous source section: Picking the Bean: Choice and Truthiness / || and && are control-flow operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-summary-cb659264]] - next source section: Picking the Bean: Choice and Truthiness / summary

## Statements

- If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique: _(javascriptallonge.pdf (source-range-0e12e052-00798))_
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-0e12e052-00800))_
- This leads to the infinite recursion we fear. _(javascriptallonge.pdf (source-range-0e12e052-00797))_

## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00798))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00796))_

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```
