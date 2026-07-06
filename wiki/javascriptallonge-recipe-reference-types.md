---
page_id: javascriptallonge-recipe-reference-types
page_kind: recipe
summary: reference types: reusable source-backed pattern with 6 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: reference-types
projection_coverage: recipe-javascriptallonge-recipe-reference-types@12e0db449bf214b07caa002b911b7708
---

# reference types

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-reference-types-7c7ed5d8]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- This is an expression, and you can combine [] with other expressions. _(javascriptallonge.pdf (source-range-c98ab3e6-00129))_
- Notice that you are always generating arrays with the same contents. _(javascriptallonge.pdf (source-range-c98ab3e6-00131))_
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . _(javascriptallonge.pdf (source-range-c98ab3e6-00133))_
- Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. _(javascriptallonge.pdf (source-range-c98ab3e6-00134))_
- As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-c98ab3e6-00134))_
- They look the same, but if you examine them with === , you see that they are different. _(javascriptallonge.pdf (source-range-c98ab3e6-00134))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00130)_

```
[2-1, 2, 2+1]
[1, 1+1, 1+1+1]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00132)_

```
[2-1, 2, 2+1] === [1,2,3]
[1,2,3] === [1, 2, 3]
[1, 2, 3] === [1, 2, 3]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-reference-types-7c7ed5d8]]
