---
page_id: javascriptallonge-recipe-call-by-sharing
page_kind: recipe
summary: call by sharing: reusable source-backed pattern with 11 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: call-by-sharing
projection_coverage: recipe-javascriptallonge-recipe-call-by-sharing@9f9dc86686e69d91579da226d3c89bac
---

# call by sharing

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-call-by-sharing-d6249c17]].
- Evidence roles: decision, constraint, definition, explanation, procedure, structured-state, example.

## Applicability And Rationale

- Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-c98ab3e6-00306))_
- At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. _(javascriptallonge.pdf (source-range-c98ab3e6-00306))_
- Earlier, we distinguished JavaScript's value types from its reference types . _(javascriptallonge.pdf (source-range-c98ab3e6-00306))_
- There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original. _(javascriptallonge.pdf (source-range-c98ab3e6-00307))_
- As you recall, value types like strings and numbers are identical to each other if they have the same content. _(javascriptallonge.pdf (source-range-c98ab3e6-00308))_
- Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00308))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00313)_

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-call-by-sharing-d6249c17]]
