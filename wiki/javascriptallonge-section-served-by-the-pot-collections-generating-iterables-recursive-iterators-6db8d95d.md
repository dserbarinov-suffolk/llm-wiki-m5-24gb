---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-recursive-iterators-6db8d95d
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables / recursive iterators: 11 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-recursive-iterators-6db8d95d@4901390fe41eae5c20dda62cbc333d90
---

# Served by the Pot: Collections / Generating Iterables / recursive iterators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-b395ef25]] - next source section: Served by the Pot: Collections / Generating Iterables / state machines

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-f68c47a5]] - broader source section: Served by the Pot: Collections / Generating Iterables

## Statements

- Iterators maintain state, that's what they do. Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. One of those cases is when we have to recursively enumerate something. _(javascriptallonge.pdf (source-range-c98ab3e6-01606))_
- For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-c98ab3e6-01607))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit . _(javascriptallonge.pdf (source-range-c98ab3e6-01613))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-c98ab3e6-01614))_
- For example, iterating over a tree. _(javascriptallonge.pdf (source-range-c98ab3e6-01607))_
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. _(javascriptallonge.pdf (source-range-c98ab3e6-01614))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01613))_

> If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01612))_

<a id="atom-technical-atom-b81e33caa69d1ec6"></a>
```
const isIterable = (something) =>
!!something[Symbol.iterator];
const treeIterator = (iterable) => {
const iterators = [ iterable[Symbol.iterator]() ];
return () => {
while (!!iterators[0]) {
const iterationResult = iterators[0].next();
if (iterationResult.done) {
iterators.shift();
}
else if (isIterable(iterationResult.value)) {
iterators.unshift(iterationResult.value[Symbol.iterator]());
}
else {
return iterationResult.value;
}
}
return;
}
}
const i = treeIterator([1, [2, [3, 4], 5]]);
let n;
while (n = i()) {
console.log(n)
}
//=>
1
2
3
4
5
```
