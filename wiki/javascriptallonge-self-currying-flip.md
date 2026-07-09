---
page_id: javascriptallonge-self-currying-flip
page_kind: concept
summary: topic-concept: 4 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_fba1380f005e2aa0@1b0e5717f8f006158aa755080711a9ad
---

# self-currying flip

Source: [[javascriptallonge]]

## Statements

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). (javascriptallonge.pdf p.196)
- Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice. (javascriptallonge.pdf p.196)

## Rules

- Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice. (javascriptallonge.pdf p.196)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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
