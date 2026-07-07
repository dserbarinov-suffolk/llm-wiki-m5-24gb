---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-57a76f01
page_kind: source
summary: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-57a76f01@bb3dd8b28f849bceb9b76d6ee2347479
---

# Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-cbbb8baa]] - next source section: Served by the Pot: Collections / Iteration and Iterables / iterator objects

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-98745d63]] - broader source section: Served by the Pot: Collections / Iteration and Iterables

### Topics

- [[javascriptallonge-functional-iterator]] - topic hub: opens the topic page for Functional Iterator

## Statements

- When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here's a stack that has its own functional iterator method: _(javascriptallonge.pdf (source-range-c98ab3e6-01502))_
- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_
- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01513))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01503))_

<a id="atom-technical-atom-8042d9524ba796e4"></a>
```
const Stack1 = () =>
({
array:[],
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
return () => {
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
});
const stack = Stack1();
stack.push("Greetings");
stack.push("to");
stack.push("you!")
```

### Technical frame 2: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01504))_

<a id="atom-technical-atom-e056a601168332ef"></a>
```
const iter = stack.iterator();
iter().value
//=> "you!"
iter().value
//=> "to"
```

### Technical frame 3: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01508))_

<a id="atom-technical-atom-ef9b2ba6e355fbac"></a>
```
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
```
