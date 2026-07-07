---
page_id: javascriptallonge-recipe-gathering
page_kind: recipe
summary: gathering: reusable source-backed pattern with 5 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: gathering
projection_coverage: recipe-javascriptallonge-recipe-gathering@88f1dde7514550b317bf771ab4b83793
---

# gathering

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-1b2d594b]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-c98ab3e6-00833))_
- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-c98ab3e6-00833))_
- car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. _(javascriptallonge.pdf (source-range-c98ab3e6-00835))_
- notation does not provide a universal patten-matching capability. _(javascriptallonge.pdf (source-range-c98ab3e6-00836))_
- to place the elements of an array inside another array. _(javascriptallonge.pdf (source-range-c98ab3e6-00840))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-00834)_

```
const [car, ...cdr] = [1, 2, 3, 4, 5];
car
//=> 1
cdr
//=> [2, 3, 4, 5]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-1b2d594b]]
