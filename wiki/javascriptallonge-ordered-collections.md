---
page_id: javascriptallonge-ordered-collections
page_kind: concept
summary: topic-concept: 13 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_8f95ff08c0afa97c@af8f5a13ae0d6652dc4c2815c1f49e2b
---

# ordered collections

Source: [[javascriptallonge]]

## Statements

- The iterables we're discussing represent ordered collections . (javascriptallonge.pdf p.216)
- One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. (javascriptallonge.pdf p.216)
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward. (javascriptallonge.pdf p.216)
- Iterables needn't represent ordered collections. (javascriptallonge.pdf p.216)
- Therefore, RandomNumbers is not an ordered collection. (javascriptallonge.pdf p.217)
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. (javascriptallonge.pdf p.217)
- Right now, we're just looking at ordered collections. (javascriptallonge.pdf p.217)
- To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. (javascriptallonge.pdf p.217)
- Every time we get an iterator from an ordered collection, we start iterating from the beginning. (javascriptallonge.pdf p.217)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

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


## Related pages

- [[javascriptallonge-iterables-out-to-infinity]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-operations-on-ordered-collections]] - contextualizes: source-supported topic dependency
