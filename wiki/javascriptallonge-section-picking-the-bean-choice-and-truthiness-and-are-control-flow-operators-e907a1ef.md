---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-e907a1ef
page_kind: source
summary: Picking the Bean: Choice and Truthiness / || and && are control-flow operators: 4 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-e907a1ef@57a8c70760bc746b285c8175ddd16dce
---

# Picking the Bean: Choice and Truthiness / || and && are control-flow operators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-851a6e13]] - broader source section: Picking the Bean: Choice and Truthiness
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-e7aa9191]] - previous source section: Picking the Bean: Choice and Truthiness / truthiness and operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-fbbf2d6a]] - next source section: Picking the Bean: Choice and Truthiness / function parameters are eager

## Statements

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-0e12e052-00787))_
- This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-0e12e052-00793))_
