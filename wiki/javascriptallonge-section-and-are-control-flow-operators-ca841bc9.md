---
page_id: javascriptallonge-section-and-are-control-flow-operators-ca841bc9
page_kind: source
summary: || and && are control-flow operators: 4 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-are-control-flow-operators-ca841bc9@50298f2a4b1efc77f9b8dec3072d65c2
---

# || and && are control-flow operators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-truthiness-and-operators-8e6eee14]] - previous source section: truthiness and operators
- [[javascriptallonge-section-function-parameters-are-eager-a0f9ecc8]] - next source section: function parameters are eager

## Statements

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-c98ab3e6-00774))_
- This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-c98ab3e6-00780))_
