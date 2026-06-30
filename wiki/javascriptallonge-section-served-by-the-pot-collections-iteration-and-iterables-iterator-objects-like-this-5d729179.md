---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-like-this-5d729179
page_kind: source
summary: Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:: 4 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-like-this-5d729179@f20e5ed1505a11baf00e23822f4be2d9
---

# Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-7abb0097]] - broader source section: Served by the Pot: Collections / Iteration and Iterables / iterator objects

## Statements

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-0e12e052-01547))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01547))_

> Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01545))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01547))_

> Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01546))_

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
