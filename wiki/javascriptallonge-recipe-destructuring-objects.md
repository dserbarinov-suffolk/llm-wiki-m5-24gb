---
page_id: javascriptallonge-recipe-destructuring-objects
page_kind: recipe
summary: destructuring objects: reusable source-backed pattern with 2 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: destructuring-objects
projection_coverage: recipe-javascriptallonge-recipe-destructuring-objects@44c18bfdc3d4e876ce519793d7baa70e
---

# destructuring objects

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-plain-old-javascript-objects-destructuring-objects-6546a490]].
- Evidence roles: decision, example.

## Applicability And Rationale

- When the label is a valid variable name, it's often the most obvious variable name as well. _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_
- It is very common to write things like title: title when destructuring objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01079))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01077)_

```
} = us\
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01078)_

```
const description = ({name: { first: given }, occupation: { title: title } }) =>
`${given} is a ${title}`;
description(user)
//=> "Reginald is a Author"
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01081)_

```
const abbrev = ({name: { first, last }, occupation: { title } }) =>
return { first, last, title};
}
abbrev(user)
//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-plain-old-javascript-objects-destructuring-objects-6546a490]]
