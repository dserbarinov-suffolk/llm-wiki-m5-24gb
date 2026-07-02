---
page_id: javascriptallonge-recipe-and-are-control-flow-operators
page_kind: recipe
summary: || and && are control-flow operators: reusable source-backed pattern with 3 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: and-are-control-flow-operators
projection_coverage: recipe-javascriptallonge-recipe-and-are-control-flow-operators@e2f938b56ca8bdcb6b0413f79c8990f6
---

# || and && are control-flow operators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-e907a1ef]].
- Evidence roles: decision, example.

## Applicability And Rationale

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. _(javascriptallonge.pdf (source-range-0e12e052-00787))_
- This is more than just an optimization. _(javascriptallonge.pdf (source-range-0e12e052-00793))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-0e12e052-00793))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-00789)_

```
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-e907a1ef]]
