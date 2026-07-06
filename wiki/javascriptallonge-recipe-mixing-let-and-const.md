---
page_id: javascriptallonge-recipe-mixing-let-and-const
page_kind: recipe
summary: mixing let and const: reusable source-backed pattern with 3 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: mixing-let-and-const
projection_coverage: recipe-javascriptallonge-recipe-mixing-let-and-const@b6908afd051b0cd0e69814aa6690f4f2
---

# mixing let and const

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-mixing-let-and-const-485aff44]].
- Evidence roles: decision, structured-state, example.

## Applicability And Rationale

- The suggestion is that shadowing a variable is confusing code. _(javascriptallonge.pdf (source-range-c98ab3e6-01156))_
- Shadowing a let with a const does not change our ability to rebind the variable in its original scope. _(javascriptallonge.pdf (source-range-c98ab3e6-01159))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-c98ab3e6-01161))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01158)_

```
(() => {
let age = 49;
if (true) {
const age = 50;
}
age = 51;
return age;
})()
//=> 51
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01160)_

```
(() => {
const age = 49;
if (true) {
let age = 50;
}
age = 52;
return age;
})()
//=> ERROR: age is read-only
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-mixing-let-and-const-485aff44]]
