---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-like-this-7bace9b8
page_kind: source
summary: Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:: 4 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-like-this-7bace9b8@80be774e3589bf4e9f22954cbccfeeff
---

# Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-157fa74f]] - broader source section: Served by the Pot: Collections / Iteration and Iterables / iterator objects

## Statements

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-c98ab3e6-01547))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01547))_

> Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01545))_

<a id="atom-technical-atom-4c8abfc1b8a16688"></a>
```
const Stack2 = () =>
({
array: [],
index: -1,
push (value) {
return this.array[this.index += 1] = value;
},
pop () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty () {
return this.index < 0
},
iterator () {
let iterationIndex = this.index;
return {
next () {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
}
});
```

### Technical frame 2: Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01547))_

> Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01546))_

<a id="atom-technical-atom-83128f97a0b04767"></a>
```
const stack = Stack2();
stack.push(2000);
stack.push(10);
stack.push(5)
const collectionSum = (collection) => {
const iterator = collection.iterator();
let eachIteration,
sum = 0;
while ((eachIteration = iterator.next(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 2015
```
