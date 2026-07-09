---
page_id: javascriptallonge-recipe-left-variadic-functions
page_kind: recipe
summary: Left-Variadic Functions: reusable source-backed pattern with 5 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: left-variadic-functions
projection_coverage: recipe-javascriptallonge-recipe-left-variadic-functions@42254ac9cbee1149ea7d8165ed95fb9c
---

# Left-Variadic Functions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-574b019e]].
- Evidence roles: decision, constraint, explanation, example.

## Applicability And Rationale

- A variadic function is a function that is designed to accept a variable number of arguments. _(javascriptallonge.pdf (source-range-c98ab3e6-00700))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-c98ab3e6-00702))_
- This can be useful when writing certain kinds of destructuring algorithms. _(javascriptallonge.pdf (source-range-c98ab3e6-00702))_
- 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. _(javascriptallonge.pdf (source-range-c98ab3e6-00704))_
- ECMAScript 2015 only permits gathering parameters from the end of the parameter list. _(javascriptallonge.pdf (source-range-c98ab3e6-00706))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00701)_

```
const abccc = (a, b, ...c) => {
console.log(a);
console.log(b);
console.log(c);
};
abccc(1, 2, 3, 4, 5)
1
2
[3,4,5]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00705)_

```
function team2(...players, captain, coach) {
console.log(`${captain} (captain)`);
for (let player of players) {
console.log(player);
}
console.log(`squad coached by ${coach}`);
}
//=> Unexpected token
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-574b019e]]
