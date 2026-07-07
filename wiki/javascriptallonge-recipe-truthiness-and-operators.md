---
page_id: javascriptallonge-recipe-truthiness-and-operators
page_kind: recipe
summary: truthiness and operators: reusable source-backed pattern with 8 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: truthiness-and-operators
projection_coverage: recipe-javascriptallonge-recipe-truthiness-and-operators@b4ebf728ab5cf409b43aa5e97a796e8e
---

# truthiness and operators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-44549e80]].
- Evidence roles: decision, explanation, definition, example, structured-state.

## Applicability And Rationale

- , && , and || are a little more subtle than our examples above implied. _(javascriptallonge.pdf (source-range-c98ab3e6-00758))_
- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-c98ab3e6-00758))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. _(javascriptallonge.pdf (source-range-c98ab3e6-00760))_
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-c98ab3e6-00760))_
- , && and || do not necessarily evaluate to true or false . _(javascriptallonge.pdf (source-range-c98ab3e6-00762))_
- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. _(javascriptallonge.pdf (source-range-c98ab3e6-00769))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00759)_

```
!5
//=> false
!undefined
//=> true
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00770)_

```
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-44549e80]]
