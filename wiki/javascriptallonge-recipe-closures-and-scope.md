---
page_id: javascriptallonge-recipe-closures-and-scope
page_kind: recipe
summary: Closures and Scope: reusable source-backed pattern with 4 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: closures-and-scope
projection_coverage: recipe-javascriptallonge-recipe-closures-and-scope@c566fb72fefda83090a553c791b17795
---

# Closures and Scope

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-closures-and-scope-77af1b0f]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- It makes sense that the result value is a function, because the expression for (x) => ... _(javascriptallonge.pdf (source-range-c98ab3e6-00320))_
- So now we have a value representing that function. _(javascriptallonge.pdf (source-range-c98ab3e6-00322))_
- There is no x in its environment, it must come from somewhere else. _(javascriptallonge.pdf (source-range-c98ab3e6-00324))_
- This, by the way, is one of the great defining characteristics of JavaScript and languages in the same family: Whether they allow things like functions to nest inside each other, and if so, how they handle variables from 'outside' of a function that are referenced inside a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00325))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00317)_

```
((x) => (y) => x)(1)(2)
//=> 1
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00319)_

```
((x) => (y) => x)(1)
//=> [Function]
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00321)_

```
(y) => x
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00323)_

```
((y) => x)(2)
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00326)_

```
lambda { |x|
lambda { |y| x }
}[1][2]
#=> 1
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-closures-and-scope-77af1b0f]]
