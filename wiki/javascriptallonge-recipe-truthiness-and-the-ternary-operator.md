---
page_id: javascriptallonge-recipe-truthiness-and-the-ternary-operator
page_kind: recipe
summary: truthiness and the ternary operator: reusable source-backed pattern with 13 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: truthiness-and-the-ternary-operator
projection_coverage: recipe-javascriptallonge-recipe-truthiness-and-the-ternary-operator@27224fba8c0e8dbf6d40862656b4683c
---

# truthiness and the ternary operator

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-b715a907]].
- Evidence roles: decision, explanation, constraint, example, structured-state.

## Applicability And Rationale

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. _(javascriptallonge.pdf (source-range-c98ab3e6-00747))_
- So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. _(javascriptallonge.pdf (source-range-c98ab3e6-00747))_
- 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-c98ab3e6-00747))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-c98ab3e6-00748))_
- (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-c98ab3e6-00748))_
- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. _(javascriptallonge.pdf (source-range-c98ab3e6-00749))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00754)_

```
true ? 'Hello' : 'Good bye'
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-b715a907]]
