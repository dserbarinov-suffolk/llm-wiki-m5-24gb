---
page_id: javascriptallonge-recursive-iterators
page_kind: concept
summary: topic-concept: 11 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_f987a3d90f85698a@63f1e83c02b6b933cd46a406549a487e
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

## Rules

- Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. (javascriptallonge.pdf p.226)

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


## Related pages

- [[javascriptallonge-state-machines]] - contextualizes: source-supported topic dependency
