---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-from-c3929b11
page_kind: source
summary: Served by the Pot: Collections / Iteration and Iterables / from: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-from-c3929b11@fff0ef3cec65dbe318e8e37d9cfc60d0
---

# Served by the Pot: Collections / Iteration and Iterables / from

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-operations-on-ordered-collections-da2b4aad]] - previous source section: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-summary-9b459d83]] - next source section: Served by the Pot: Collections / Iteration and Iterables / summary

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-07b8f3fd]] - broader source section: Served by the Pot: Collections / Iteration and Iterables

## Statements

- Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-c98ab3e6-01606))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript's built-in Array class already has one: _(javascriptallonge.pdf (source-range-c98ab3e6-01607))_
- We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-c98ab3e6-01609))_
- Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-c98ab3e6-01612))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / from

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01609))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01608))_

<a id="atom-technical-atom-801a82a9217c279c"></a>
```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Technical frame 2: Served by the Pot: Collections / Iteration and Iterables / from

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01612))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01611))_

<a id="atom-technical-atom-33b8604e941fb067"></a>
```
Stack3.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
Pair1.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair1(value, iterationToList(iteration));
})(iterable[Symbol.iterator]())
```

### Technical frame 3: Served by the Pot: Collections / Iteration and Iterables / from

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01612))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01613))_

<a id="atom-technical-atom-fd7c26986833f7ea"></a>
```
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
Pair1.from(Squares)
//=> {"first":0,
"rest":{"first":1,
"rest":{"first":4,
"rest":{ ...
```
