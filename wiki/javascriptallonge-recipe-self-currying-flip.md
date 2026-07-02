---
page_id: javascriptallonge-recipe-self-currying-flip
page_kind: recipe
summary: self-currying flip: reusable source-backed pattern with 1 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: self-currying-flip
projection_coverage: recipe-javascriptallonge-recipe-self-currying-flip@dde11eb9b5e768e2ed0e5c94702f5964
---

# self-currying flip

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-data-flip-self-currying-flip-419bc9f2]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-0e12e052-01461))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01462)_

```
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn(second, first);
}
else {
return function (second) {
return fn(second, first);
};
};
};
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-data-flip-self-currying-flip-419bc9f2]]
