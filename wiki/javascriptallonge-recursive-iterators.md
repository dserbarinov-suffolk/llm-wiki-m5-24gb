---
page_id: javascriptallonge-recursive-iterators
page_kind: concept
summary: recursive iterators: 6 accepted assertion(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_4ff24cdf2cba6740@c5a956c112b5127e371e2622bd0f50cc
---

# recursive iterators

Source: [[javascriptallonge]]

## Statements

- Iterators maintain state, that's what they do . (javascriptallonge.pdf p.226)
- Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. (javascriptallonge.pdf p.226)
- elements that are not, themselves, iterable. (javascriptallonge.pdf p.226)
- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. (javascriptallonge.pdf p.227)
- In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit . (javascriptallonge.pdf p.227)
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. (javascriptallonge.pdf p.228)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
One of those cases is when we have to recursively enumerate something.
```

<a id="atom-2"></a>
**Atom:** code block

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

<a id="atom-3"></a>
**Atom:** code block

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
