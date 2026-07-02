---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-from-b90bf31a
page_kind: source
summary: Served by the Pot: Collections / Iteration and Iterables / from: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-from-b90bf31a@f9730fdf5af0632fe058b0faba694ece
---

# Served by the Pot: Collections / Iteration and Iterables / from

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-operations-on-ordered-collections-097315e6]] - previous source section: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-summary-02851e42]] - next source section: Served by the Pot: Collections / Iteration and Iterables / summary

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-6006fd95]] - broader source section: Served by the Pot: Collections / Iteration and Iterables

## Statements

- Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-0e12e052-01606))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript's built-in Array class already has one: _(javascriptallonge.pdf (source-range-0e12e052-01607))_
- We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-0e12e052-01609))_
- Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-0e12e052-01612))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / from

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01609))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01608))_

<a id="atom-technical-atom-796cd4abc1f1f1a2"></a>
```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Technical frame 2: Served by the Pot: Collections / Iteration and Iterables / from

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01612))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01611))_

<a id="atom-technical-atom-7fc8699bd710f113"></a>
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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01612))_

> Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01613))_

<a id="atom-technical-atom-ada69411918922ed"></a>
```
const numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
Pair1.from(Squares)
//=> {"first":0,
"rest":{"first":1,
"rest":{"first":4,
"rest":{ ...
```
