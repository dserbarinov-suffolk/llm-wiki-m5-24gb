---
page_id: javascriptallonge-recipe-implementing-methods-with-iteration
page_kind: recipe
summary: implementing methods with iteration: reusable source-backed pattern with 6 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: implementing-methods-with-iteration
projection_coverage: recipe-javascriptallonge-recipe-implementing-methods-with-iteration@323618423aa8d61962bd0828dfa8324d
---

# implementing methods with iteration

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e67a1913]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-01739))_
- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-c98ab3e6-01739))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. _(javascriptallonge.pdf (source-range-c98ab3e6-01740))_
- And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-c98ab3e6-01740))_
- To use LazyCollection , we mix it into an any iterable object. _(javascriptallonge.pdf (source-range-c98ab3e6-01746))_
- For simplicity, we'll show how to mix it into Numbers and Pair . _(javascriptallonge.pdf (source-range-c98ab3e6-01746))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01742)_

```
const extend = function (consumer, ...providers) {
for (let i = 0; i < providers.length; ++i) {
const provider = providers[i];
for (let key in provider) {
if (provider.hasOwnProperty(key)) {
consumer[key] = provider[key]
}
}
}
return consumer
};
const LazyCollection = {
map(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
const {
done, value
} = iterator.next();
return ({
done, value: done ? undefined : fn(value)
});
}
}
}
}, LazyCollection);
},
reduce(fn, seed) {
const iterator = this[Symbol.iterator]();
let iterationResult,
accumulator = seed;
while ((iterationResult = iterator.next(), !iterationResult.done)) {
accumulator = fn(accumulator, iterationResult.value);
}
return accumulator;
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01747)_

```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
// Pair, a/k/a linked lists
const EMPTY = {
isEmpty: () => true
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01748)_

```
};
const isEmpty = (node) => node === EMPTY;
const Pair = (car, cdr = EMPTY) =>
Object.assign({
car,
cdr,
isEmpty: () => false,
[Symbol.iterator]: function () {
let currentPair = this;
return {
next: () => {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.car;
currentPair = currentPair.cdr;
return {done: false, value}
}
}
}
}
}, LazyCollection);
Pair.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair(value, iterationToList(iteration));
})(iterable[Symbol.iterator]());
// Stack
const Stack = () =>
Object.assign({
array: [],
index: -1,
push: function (value) {
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01749)_

```
return this.array[this.index += 1] = value;
},
pop: function () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty: function () {
return this.index < 0
},
[Symbol.iterator]: function () {
let iterationIndex = this.index;
return {
next: () => {
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
}, LazyCollection);
Stack.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-c98ab3e6-01750)_

```
// Pair and Stack in action
Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
//=> 100
Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e67a1913]]
