---
page_id: javascriptallonge-iterable
page_kind: concept
summary: iterables: 15 accepted assertion(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_566afaf28f4830b8@0e35945938caf079abcb239e9a7f114d
---

# iterables

Source: [[javascriptallonge]]

## Statements

- Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. (javascriptallonge.pdf p.211)
- People have been writing iterators since JavaScript was first released in the late 1990s. (javascriptallonge.pdf p.211)
- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. (javascriptallonge.pdf p.211)
- Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. (javascriptallonge.pdf p.211)
- Symbols are unique constants that are guaranteed not to conflict with existing strings. (javascriptallonge.pdf p.211)
- Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols. (javascriptallonge.pdf p.211)
- To ensure that the method would not conflict with any existing code, JavaScript provides a symbol . (javascriptallonge.pdf p.211)
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (javascriptallonge.pdf p.211)
- 88 You can read more about JavaScript symbols in Axel Rauschmayer's Symbols in ECMAScript 2015. (javascriptallonge.pdf p.211)
- Our stack does , so instead of binding the existing iterator method to the name iterator , we bind it to the Symbol.iterator . (javascriptallonge.pdf p.212)
- The for..of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. (javascriptallonge.pdf p.213)
- Nowis the time to note that we can spread any iterable. (javascriptallonge.pdf p.215)
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. (javascriptallonge.pdf p.215)
- That might be very wasteful for extremely large collections. (javascriptallonge.pdf p.215)
- And if we have an infinite collection, spreading is going to fail outright as we're about to see. (javascriptallonge.pdf p.215)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const Stack3 = () =>
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
[Symbol.iterator] () {
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
const stack = Stack3();
```

<a id="atom-2"></a>
**Atom:** code block

```
stack.push(2000);
stack.push(10);
stack.push(5)
const collectionSum = (collection) => {
const iterator = collection[Symbol.iterator]();
let eachIteration,
sum = 0;
while ((eachIteration = iterator.next(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 2015
Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing.
Do we get anything in return?
Indeed we do. Behold the for...of loop:
const iterableSum = (iterable) => {
let sum = 0;
for (const num of iterable) {
sum += num;
}
return sum
}
iterableSum(stack)
//=> 2015
```

<a id="atom-3"></a>
**Atom:** code block

```
const EMPTY = {
isEmpty: () => true
};
const isEmpty = (node) => node === EMPTY;
const Pair1 = (first, rest = EMPTY) =>
({
first,
rest,
isEmpty () { return false },
[Symbol.iterator] () {
let currentPair = this;
return {
next () {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.first;
currentPair = currentPair.rest;
return {done: false, value}
}
}
}
}
});
const list = (...elements) => {
const [first, ...rest] = elements;
return elements.length === 0
? EMPTY
: Pair1(first, list(...rest))
}
const someSquares = list(1, 4, 9, 16, 25);
iterableSum(someSquares)
//=> 55
```

<a id="atom-4"></a>
**Atom:** code block

```
['some squares', ...someSquares]
//=> ["some squares", 1, 4, 9, 16, 25]
```

<a id="atom-5"></a>
**Atom:** code block

```
const firstAndSecondElement = (first, second) =>
({first, second})
firstAndSecondElement(...stack)
//=> {"first":5,"second":10}
```
