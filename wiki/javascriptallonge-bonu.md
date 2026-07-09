---
page_id: javascriptallonge-bonu
page_kind: concept
summary: topic-concept: 12 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_712be17c6467e641@48cba0971b91fd5e4c972ea27df54cd8
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

## Rules

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. (javascriptallonge.pdf p.175)
- And if fn had some sort of side-effect, the program could be buggy. (javascriptallonge.pdf p.176)

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


## Related pages

- [[javascriptallonge-unfolding-and-laziness]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-caveat]] - contextualizes: source-supported topic dependency
