---
page_id: javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-fed63222
page_kind: source
summary: Lazy and Eager Collections / lazy collection operations: 23 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-fed63222@4c1e21576ca1b43d5a7f819f9acae116
---

# Lazy and Eager Collections / lazy collection operations

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-7da1cc7d]] - previous source section: Lazy and Eager Collections / implementing methods with iteration
- [[javascriptallonge-section-lazy-and-eager-collections-eager-collections-0a3f9a39]] - next source section: Lazy and Eager Collections / eager collections

### Source structure

- [[javascriptallonge-section-lazy-and-eager-collections-8fb68091]] - broader source section: Lazy and Eager Collections

## Statements

- 'Laziness' is a very pejorative word when applied to people. But it can be an excellent strategy for efficiency in algorithms. Let's be precise: Laziness is the characteristic of not doing any work until you know you need the result of the work. _(javascriptallonge.pdf (source-range-c98ab3e6-01779))_
- Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-c98ab3e6-01782))_
- But it's still illustrative to dissect something important: Array's .map and .filter methods gather their results into new arrays. Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-c98ab3e6-01783))_
- Whereas the .map and .filter methods on Pair work with iterators. They produce small iterable objects that refer back to the original iteration. This reduces the memory footprint. When working with very large collections and many operations, this can be important. _(javascriptallonge.pdf (source-range-c98ab3e6-01784))_
- This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-c98ab3e6-01787))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-c98ab3e6-01788))_
- Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-c98ab3e6-01796))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-c98ab3e6-01782))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-c98ab3e6-01783))_
- Whereas the .map and .filter methods on Pair work with iterators. _(javascriptallonge.pdf (source-range-c98ab3e6-01784))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-c98ab3e6-01788))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-c98ab3e6-01796))_

## Technical atoms

### Technical frame 1: Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01796))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01795))_

<a id="atom-technical-atom-8961ba32fb300113"></a>
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
