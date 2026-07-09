---
page_id: javascriptallonge-bonu
page_kind: concept
summary: bonus: 6 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_44467298935360c7@74777e2ed7cd5830a2881e4f62cb4017
---

# bonus

Source: [[javascriptallonge]]

## Statements

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. (javascriptallonge.pdf p.175)
- In Smalltalk, for example, they are known as collect , select , and detect . (javascriptallonge.pdf p.175)
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. (javascriptallonge.pdf p.176)
- And if fn had some sort of side-effect, the program could be buggy. (javascriptallonge.pdf p.176)
- JavaScript would apply fn to every element. (javascriptallonge.pdf p.176)
- If array was very large, and fn very slow, this would consume a lot of unnecessary time. (javascriptallonge.pdf p.176)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const firstInIteration = (fn, iterator) =>
take(filterIteratorWith(fn, iterator), 1);
```

<a id="atom-2"></a>
**Atom:** code block

```
const firstInArray = (fn, array) =>
array.filter(fn)[0];
```
