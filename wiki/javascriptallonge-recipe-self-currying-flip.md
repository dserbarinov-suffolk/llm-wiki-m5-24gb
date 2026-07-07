---
page_id: javascriptallonge-recipe-self-currying-flip
page_kind: recipe
summary: self-currying flip: reusable source-backed pattern with 2 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: self-currying-flip
projection_coverage: recipe-javascriptallonge-recipe-self-currying-flip@fbeec110f2444d4b7a9b01d4d8b52032
---

# self-currying flip

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-self-currying-flip-afc1011e]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-c98ab3e6-01439))_
- Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice. _(javascriptallonge.pdf (source-range-c98ab3e6-01441))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01440)_

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
- Source section: [[javascriptallonge-section-self-currying-flip-afc1011e]]
