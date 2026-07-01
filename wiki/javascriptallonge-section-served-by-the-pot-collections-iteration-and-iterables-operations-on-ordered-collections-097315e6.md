---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-operations-on-ordered-collections-097315e6
page_kind: source
summary: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: 30 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-operations-on-ordered-collections-097315e6@226f83b900bd7a84c8c3cca5a78aeae8
---

# Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-6006fd95]] - broader source section: Served by the Pot: Collections / Iteration and Iterables
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-ordered-collections-3e509cbd]] - previous source section: Served by the Pot: Collections / Iteration and Iterables / ordered collections
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-from-b90bf31a]] - next source section: Served by the Pot: Collections / Iteration and Iterables / from

## Statements

- Let's define some operations on ordered collections. Here's mapWith , it takes an ordered collection, and returns another ordered collection representing a mapping over the original: 89 _(javascriptallonge.pdf (source-range-0e12e052-01582))_
- 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It's the same idea, after all. _(javascriptallonge.pdf (source-range-0e12e052-01583))_
- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-0e12e052-01585))_
- Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith : _(javascriptallonge.pdf (source-range-0e12e052-01586))_
- Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this: _(javascriptallonge.pdf (source-range-0e12e052-01588))_
- Every time we write for (const i of Evens) , JavaScript calls Evens[Symbol.iterator]() . That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers . _(javascriptallonge.pdf (source-range-0e12e052-01590))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation . _(javascriptallonge.pdf (source-range-0e12e052-01591))_
- Like mapWith , they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-0e12e052-01598))_
- Andhere's a computation performed using operations on ordered collections: We'll create an ordered collection of square numbers that end in one and are less than 1,000: _(javascriptallonge.pdf (source-range-0e12e052-01599))_
- As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning. _(javascriptallonge.pdf (source-range-0e12e052-01601))_
- For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] : _(javascriptallonge.pdf (source-range-0e12e052-01602))_
- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-0e12e052-01604))_
- It's the same idea, after all. _(javascriptallonge.pdf (source-range-0e12e052-01583))_
- That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers . _(javascriptallonge.pdf (source-range-0e12e052-01590))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-0e12e052-01591))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-0e12e052-01591))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01585))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01584))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01588))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01587))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01590))_

> Every time we write for (const i of Evens) , JavaScript calls Evens[Symbol.iterator]() . That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01589))_

```
const Evens =
{
[Symbol.iterator] () {
const iterator = Numbers[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : 2 *value});
}
}
}
};
```

### Technical frame 4: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01598))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01597))_

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

### Technical frame 5: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01601))_

> As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01600))_

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
