---
page_id: javascriptallonge-recipe-combinators
page_kind: recipe
summary: combinators: reusable source-backed pattern with 3 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: combinators
projection_coverage: recipe-javascriptallonge-recipe-combinators@45ba9ad4b40c63c4ebf7bee17bc4e97b
---

# combinators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-combinators-and-function-decorators-combinators-21ded55c]].
- Evidence roles: decision, procedure, explanation, structured-state, example.

## Applicability And Rationale

- We won't be strict about using only previously defined combinators in their construction. _(javascriptallonge.pdf (source-range-c98ab3e6-00558))_
- While some programmers believe 'There Should Only Be One Way To Do It,' having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously. _(javascriptallonge.pdf (source-range-c98ab3e6-00561))_
- This is, of course, just one example of many. _(javascriptallonge.pdf (source-range-c98ab3e6-00561))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00560)_

```
const compose = (a, b) =>
(c) => a(b(c))
Let’s say we have:
const addOne = (number) => number + 1;
const doubleOf = (number) => number * 2;
With compose, anywhere you would write
const doubleOfAddOne = (number) => doubleOf(addOne(number));
You could also write:
const doubleOfAddOne = compose(doubleOf, addOne);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-combinators-and-function-decorators-combinators-21ded55c]]
