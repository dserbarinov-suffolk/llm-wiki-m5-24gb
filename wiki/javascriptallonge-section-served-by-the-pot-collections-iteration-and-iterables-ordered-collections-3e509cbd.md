---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-ordered-collections-3e509cbd
page_kind: source
summary: Served by the Pot: Collections / Iteration and Iterables / ordered collections: 12 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-ordered-collections-3e509cbd@b07a3621a7781ec31729a35c1c2d39cc
---

# Served by the Pot: Collections / Iteration and Iterables / ordered collections

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-6006fd95]] - broader source section: Served by the Pot: Collections / Iteration and Iterables
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterables-out-to-infinity-376606ac]] - previous source section: Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-operations-on-ordered-collections-097315e6]] - next source section: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

## Statements

- The iterables we're discussing represent ordered collections . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example: _(javascriptallonge.pdf (source-range-0e12e052-01574))_
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward. _(javascriptallonge.pdf (source-range-0e12e052-01576))_
- Iterables needn't represent ordered collections. We could make an infinite iterable representing random numbers: _(javascriptallonge.pdf (source-range-0e12e052-01577))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-0e12e052-01579))_
- Right now, we're just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-0e12e052-01580))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-0e12e052-01579))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01576))_

> This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01575))_

```
const abc = ["a", "b", "c"];
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
```

### Technical frame 2: Served by the Pot: Collections / Iteration and Iterables / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01579))_

> Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01578))_

```
const RandomNumbers = {
[Symbol.iterator]: () =>
({
next () {
return {value: Math.random()};
}
})
}
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.494052127469331
0.835459444206208
0.1408337657339871
...
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.7845381607767195
0.4956772483419627
0.20259276474826038
...
```
