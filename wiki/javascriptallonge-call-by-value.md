---
page_id: javascriptallonge-call-by-value
page_kind: concept
summary: call by value: 3 accepted assertion(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_7375dfee87c685d5@17fcd96dd9a4ba5a49fe8bfdb5973c48
---

# call by value

Source: [[javascriptallonge]]

## Statements

- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). (javascriptallonge.pdf p.40)
- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . (javascriptallonge.pdf p.41)
- Then our circumference function was applied to 2 . (javascriptallonge.pdf p.41)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
((diameter) => diameter * 3.14159265)(1 + 1)
//=> 6.2831853
```
