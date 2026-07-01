---
page_id: javascriptallonge-lazy
page_kind: concept
summary: Lazy: 1 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-lazy@f2d323f6f3d9a7663c4289fb313e4978
---

# Lazy

What [[javascriptallonge]] covers about lazy:

## Statements

### Lazy and Eager Collections / lazy collection operations

- Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-0e12e052-01796))_


## Technical atoms

### Technical frame 1: Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01796))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01795))_

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

- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from Lazy and Eager Collections / lazy collection operations: const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false, value: n++}) } } }, LazyCollection); const firstCubeOver123 ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
