---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-c8371217
page_kind: source
summary: Picking the Bean: Choice and Truthiness / || and && are control-flow operators: 4 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-c8371217@9615281d2df6dab79cfd28967125acb8
---

# Picking the Bean: Choice and Truthiness / || and && are control-flow operators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-44549e80]] - previous source section: Picking the Bean: Choice and Truthiness / truthiness and operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-699c4c1b]] - next source section: Picking the Bean: Choice and Truthiness / function parameters are eager

### Source structure

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d2a76f30]] - broader source section: Picking the Bean: Choice and Truthiness

## Statements

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-c98ab3e6-00774))_
- This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-c98ab3e6-00780))_
