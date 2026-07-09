---
page_id: javascriptallonge-recipe-a-look-back-at-functional-iterators
page_kind: recipe
summary: a look back at functional iterators: reusable source-backed pattern with 4 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: a-look-back-at-functional-iterators
projection_coverage: recipe-javascriptallonge-recipe-a-look-back-at-functional-iterators@8fd4f8e384cc4db48d666ecd5eb20e03
---

# a look back at functional iterators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-57a76f01]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- We can do the same thing for objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01502))_
- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-c98ab3e6-01511))_
- If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01513))_
- Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-c98ab3e6-01513))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01503)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01504)_

```
const iter = stack.iterator();
iter().value
//=> "you!"
iter().value
//=> "to"
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01508)_

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

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01510)_

```
const stack = Stack1();
stack.push(1);
stack.push(2);
stack.push(3);
iteratorSum(stack.iterator())
//=> 6
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01512)_

```
const collectionSum = (collection) => {
const iterator = collection.iterator();
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 6
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-57a76f01]]
