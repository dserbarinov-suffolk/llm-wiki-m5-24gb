---
page_id: javascriptallonge-self-currying-flip
page_kind: concept
summary: self-currying flip: 2 accepted assertion(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_50d9fa60281e1ad0@541615ff14cdd85c6b63ece196acc73a
---

# self-currying flip

Source: [[javascriptallonge]]

## Statements

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). (javascriptallonge.pdf p.196)
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
