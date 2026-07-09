---
page_id: javascriptallonge-operation
page_kind: concept
summary: Operation: 4 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-operation@e3fee078b79c9a5ac4aa7f02c37d4fa0
---

# Operation

What [[javascriptallonge]] covers about operation:

## Statements

### Recipes with Basic Functions / Maybe

- If some code ever tries to call model.setSomething with nothing, the operation will be skipped. _(javascriptallonge.pdf (source-range-c98ab3e6-00691))_

### Mutation / mutation and data structures

- The gathering operation [a, b, ...ThreeToFive] is slower, but 'safer. ' _(javascriptallonge.pdf (source-range-c98ab3e6-01126))_

### Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

- Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith : _(javascriptallonge.pdf (source-range-c98ab3e6-01561))_

- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-c98ab3e6-01579))_


## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01560))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01559))_

<a id="atom-technical-atom-db03dd1e259d128a"></a>
```
const mapWith = (fn, collection) =>
({
[Symbol.iterator] () {
const iterator = collection[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Technical frame 2: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01563))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01562))_

<a id="atom-technical-atom-c1f35f3a09f6c9fd"></a>
```
const Evens = mapWith((x) => 2 * x, Numbers);
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
```

### Technical frame 3: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01573))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01572))_

<a id="atom-technical-atom-1fc62d987d78a896"></a>
```
const filterWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
do {
const {done, value} = iterator.next();
} while (!done && !fn(value));
return {done, value};
}
}
}
});
const untilWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
let {done, value} = iterator.next();
done = done || fn(value);
return ({done, value: done ? undefined : value});
}
}
}
});
```

### Technical frame 4: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01576))_

> As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01575))_

<a id="atom-technical-atom-dbfe25dcdf43f6cb"></a>
```
const Squares = mapWith((x) => x * x, Numbers);
const EndWithOne = filterWith((x) => x % 10 === 1, Squares);
const UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
```


## Related pages

### Source structure

- [[javascriptallonge-section-a-rich-aroma-basic-numbers-operations-on-numbers-c7608822]] - source section: A Rich Aroma: Basic Numbers / operations on numbers
- [[javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-0de83c02]] - source section: Lazy and Eager Collections / lazy collection operations
- [[javascriptallonge-section-operations-that-compose-two-or-more-iterables-into-an-iterable-73854237]] - source section: operations that compose two or more iterables into an iterable
- [[javascriptallonge-section-operations-that-transform-an-iterable-into-a-value-f61dad02]] - source section: operations that transform an iterable into a value
- [[javascriptallonge-section-operations-that-transform-one-iterable-into-another-9f8c6529]] - source section: operations that transform one iterable into another
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-operations-on-ordered-collections-ee56851b]] - source section: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections
- [[javascriptallonge-section-served-by-the-pot-collections-rewriting-iterable-operations-f8a6e431]] - source section: Served by the Pot: Collections / rewriting iterable operations

### Shared technical atoms

- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (4 shared atom(s))
- [[javascriptallonge-iteration]] - shared technical atoms: Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (4 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))

## Source

- [[javascriptallonge]]
