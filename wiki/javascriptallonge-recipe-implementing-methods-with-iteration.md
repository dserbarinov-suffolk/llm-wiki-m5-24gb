---
page_id: javascriptallonge-recipe-implementing-methods-with-iteration
page_kind: recipe
summary: implementing methods with iteration: reusable source-backed pattern with 6 statement(s) and 8 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: implementing-methods-with-iteration
projection_coverage: recipe-javascriptallonge-recipe-implementing-methods-with-iteration@b6d61161604765d7b62cab69907b4045
---

# implementing methods with iteration

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e2493942]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-0e12e052-01765))_
- And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-0e12e052-01765))_
- And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-0e12e052-01766))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. _(javascriptallonge.pdf (source-range-0e12e052-01766))_
- For simplicity, we'll show how to mix it into Numbers and Pair . _(javascriptallonge.pdf (source-range-0e12e052-01772))_
- To use LazyCollection , we mix it into an any iterable object. _(javascriptallonge.pdf (source-range-0e12e052-01772))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01768)_

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

_Source: javascriptallonge.pdf (source-range-0e12e052-01769)_

```
},
filter(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
do {
const {
done, value
} = iterator.next();
} while (!done && !fn(value));
return {
done, value
};
}
}
}
}, LazyCollection)
},
find(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
let {
done, value
} = iterator.next();
done = done || fn(value);
return ({
done, value: done ? undefined : value
});
}
}
}
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01770)_

```
}, LazyCollection)
},
until(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
let {
done, value
} = iterator.next();
done = done || fn(value);
return ({
done, value: done ? undefined : value
});
}
}
}
}, LazyCollection)
},
first() {
return this[Symbol.iterator]().next().value;
},
rest() {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
iterator.next();
return iterator;
}
}, LazyCollection);
},
take(numberToTake) {
return Object.assign({
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01771)_

```
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
let remainingElements = numberToTake;
return {
next: () => {
let {
done, value
} = iterator.next();
done = done || remainingElements-- <= 0;
return ({
done, value: done ? undefined : value
});
}
}
}
}, LazyCollection);
}
}
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01773)_

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

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01774)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e2493942]]
