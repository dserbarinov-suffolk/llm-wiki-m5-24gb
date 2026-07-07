---
page_id: javascriptallonge-recipe-picking-the-bean-choice-and-truthiness
page_kind: recipe
summary: Picking the Bean: Choice and Truthiness: reusable source-backed pattern with 4 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: picking-the-bean-choice-and-truthiness
projection_coverage: recipe-javascriptallonge-recipe-picking-the-bean-choice-and-truthiness@e14c82b1ccf327d0293cadf53829985f
---

# Picking the Bean: Choice and Truthiness

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d2a76f30]].
- Evidence roles: decision, example.

## Applicability And Rationale

- In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. _(javascriptallonge.pdf (source-range-c98ab3e6-00735))_
- true and false are value types. _(javascriptallonge.pdf (source-range-c98ab3e6-00741))_
- All values of true are === all other values of true. _(javascriptallonge.pdf (source-range-c98ab3e6-00741))_
- Now, note well: We have said what happens if you pass boolean values to ! _(javascriptallonge.pdf (source-range-c98ab3e6-00745))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00742)_

```
!true
//=> false
!false
//=> true
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00744)_

```
false && false //=> false
false && true
//=> false
true
&& false //=> false
true
&& true
//=> true
false || false //=> false
false || true
//=> true
true
|| false //=> true
true
|| true
//=> true
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d2a76f30]]
