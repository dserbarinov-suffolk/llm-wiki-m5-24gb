---
page_id: javascriptallonge-recipe-recursive-iterators
page_kind: recipe
summary: recursive iterators: reusable source-backed pattern with 7 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: recursive-iterators
projection_coverage: recipe-javascriptallonge-recipe-recursive-iterators@fc9fcd81fb15187929190f9afb8c35e5
---

# recursive iterators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-recursive-iterators-6db8d95d]].
- Evidence roles: decision, constraint, explanation, procedure, structured-state, example.

## Applicability And Rationale

- Iterators maintain state, that's what they do. _(javascriptallonge.pdf (source-range-c98ab3e6-01606))_
- Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. _(javascriptallonge.pdf (source-range-c98ab3e6-01606))_
- elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-c98ab3e6-01607))_
- For example, iterating over a tree. _(javascriptallonge.pdf (source-range-c98ab3e6-01607))_
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. _(javascriptallonge.pdf (source-range-c98ab3e6-01613))_
- In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit . _(javascriptallonge.pdf (source-range-c98ab3e6-01613))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01608)_

```
// Generation
const isIterable = (something) =>
!!something[Symbol.iterator];
const generate = (iterable) => {
for (let element of iterable) {
if (isIterable(element)) {
generate(element)
}
else {
console.log(element)
}
}
}
generate([1, [2, [3, 4], 5]])
//=>
1
2
3
4
5
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01612)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-recursive-iterators-6db8d95d]]
