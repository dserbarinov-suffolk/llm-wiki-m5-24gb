---
page_id: javascriptallonge-recipe-and-are-control-flow-operators
page_kind: recipe
summary: || and && are control-flow operators: reusable source-backed pattern with 3 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: and-are-control-flow-operators
projection_coverage: recipe-javascriptallonge-recipe-and-are-control-flow-operators@b428d945473d18c25db054e7ad6eaee8
---

# || and && are control-flow operators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-are-control-flow-operators-ca841bc9]].
- Evidence roles: decision, example.

## Applicability And Rationale

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. _(javascriptallonge.pdf (source-range-c98ab3e6-00774))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-c98ab3e6-00780))_
- This is more than just an optimization. _(javascriptallonge.pdf (source-range-c98ab3e6-00780))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00776)_

```
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-are-control-flow-operators-ca841bc9]]
