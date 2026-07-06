---
page_id: javascriptallonge-recipe-flipping-methods
page_kind: recipe
summary: flipping methods: reusable source-backed pattern with 1 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: flipping-methods
projection_coverage: recipe-javascriptallonge-recipe-flipping-methods@99eba8d9a4007c296d0720cc7dff4a2f
---

# flipping methods

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-94c63baf]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. _(javascriptallonge.pdf (source-range-c98ab3e6-01465))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01466)_

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
- Source section: [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-94c63baf]]
