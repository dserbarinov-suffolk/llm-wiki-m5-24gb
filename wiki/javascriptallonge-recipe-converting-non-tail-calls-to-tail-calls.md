---
page_id: javascriptallonge-recipe-converting-non-tail-calls-to-tail-calls
page_kind: recipe
summary: converting non-tail-calls to tail-calls: reusable source-backed pattern with 5 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: converting-non-tail-calls-to-tail-calls
projection_coverage: recipe-javascriptallonge-recipe-converting-non-tail-calls-to-tail-calls@99fdf68db018e1bba5034463d103eae0
---

# converting non-tail-calls to tail-calls

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-22a8069d]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- The obvious solution is push the 1 + work into the call to length . _(javascriptallonge.pdf (source-range-c98ab3e6-00958))_
- Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. _(javascriptallonge.pdf (source-range-c98ab3e6-00960))_
- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. _(javascriptallonge.pdf (source-range-c98ab3e6-00963))_
- We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. _(javascriptallonge.pdf (source-range-c98ab3e6-00967))_
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-c98ab3e6-00967))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00959)_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? 0 + numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
lengthDelaysWork(["foo", "bar", "baz"], 0)
//=> 3
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00961)_

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
const length = (n) =>
lengthDelaysWork(n, 0);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-22a8069d]]
