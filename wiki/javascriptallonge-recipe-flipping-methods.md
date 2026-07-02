---
page_id: javascriptallonge-recipe-flipping-methods
page_kind: recipe
summary: flipping methods: reusable source-backed pattern with 1 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: flipping-methods
projection_coverage: recipe-javascriptallonge-recipe-flipping-methods@f8c8d102d335b765d090d46b7ea38f33
---

# flipping methods

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-f076629f]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. _(javascriptallonge.pdf (source-range-0e12e052-01465))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01466)_

```
const flipAndCurry = (fn) =>
(first) =>
function (second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
return fn.call(this, second, first);
}
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn.call(this, second, first);
}
else {
return function (second) {
return fn.call(this, second, first);
};
};
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-f076629f]]
