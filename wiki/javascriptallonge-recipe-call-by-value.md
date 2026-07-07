---
page_id: javascriptallonge-recipe-call-by-value
page_kind: recipe
summary: call by value: reusable source-backed pattern with 3 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: call-by-value
projection_coverage: recipe-javascriptallonge-recipe-call-by-value@1fb80683618a32f257873512900ed1a1
---

# call by value

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-value-9e24e866]].
- Evidence roles: decision, definition, explanation, example.

## Applicability And Rationale

- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-c98ab3e6-00277))_
- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . _(javascriptallonge.pdf (source-range-c98ab3e6-00281))_
- Then our circumference function was applied to 2 . _(javascriptallonge.pdf (source-range-c98ab3e6-00281))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00280)_

```
((diameter) => diameter * 3.14159265)(1 + 1)
//=> 6.2831853
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-value-9e24e866]]
