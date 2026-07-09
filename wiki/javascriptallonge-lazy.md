---
page_id: javascriptallonge-lazy
page_kind: concept
summary: Lazy: 1 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-lazy@687e8b9a0b36c266ac65607d7cc1787d
---

# Lazy

What [[javascriptallonge]] covers about lazy:

## Statements

### Lazy and Eager Collections / lazy collection operations

- Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-c98ab3e6-01770))_


## Technical atoms

### Technical frame 1: Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01770))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01769))_

<a id="atom-technical-atom-e580d74457bcad4b"></a>
```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
const firstCubeOver1234 =
Numbers
.map((x) => x * x * x)
.filter((x) => x > 1234)
.first()
//=> 1331
```


## Related pages

### Source structure

- [[javascriptallonge-section-lazy-and-eager-collections-7308cac5]] - source section: Lazy and Eager Collections
- [[javascriptallonge-section-lazy-and-eager-collections-eager-collections-527b72b9]] - source section: Lazy and Eager Collections / eager collections
- [[javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e67a1913]] - source section: Lazy and Eager Collections / implementing methods with iteration
- [[javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-0de83c02]] - source section: Lazy and Eager Collections / lazy collection operations

### Shared technical atoms

- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from Lazy and Eager Collections / lazy collection operations: const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false, value: n++}) } } }, LazyCollection); const firstCubeOver123 ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
