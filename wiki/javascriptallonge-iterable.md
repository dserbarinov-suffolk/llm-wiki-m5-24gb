---
page_id: javascriptallonge-iterable
page_kind: concept
summary: Iterable: 14 statement(s) and 12 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterable@7f79223033a102ba2a242deca0fcd593
---

# Iterable

What [[javascriptallonge]] covers about iterable:

## Statements

### Served by the Pot: Collections / Iteration and Iterables / iterables

- The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable: _(javascriptallonge.pdf (source-range-c98ab3e6-01532))_

- Nowis the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal: _(javascriptallonge.pdf (source-range-c98ab3e6-01535))_

### Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity

- There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them: _(javascriptallonge.pdf (source-range-c98ab3e6-01545))_

- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-c98ab3e6-01547))_

### Served by the Pot: Collections / Iteration and Iterables / ordered collections

- The iterables we're discussing represent ordered collections . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example: _(javascriptallonge.pdf (source-range-c98ab3e6-01549))_

- Iterables needn't represent ordered collections. We could make an infinite iterable representing random numbers: _(javascriptallonge.pdf (source-range-c98ab3e6-01552))_

- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01554))_

### Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-c98ab3e6-01560))_

- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a collection operation . _(javascriptallonge.pdf (source-range-c98ab3e6-01566))_

- For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] : _(javascriptallonge.pdf (source-range-c98ab3e6-01577))_

### Served by the Pot: Collections / Iteration and Iterables / from

- One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript's built-in Array class already has one: _(javascriptallonge.pdf (source-range-c98ab3e6-01582))_

### Served by the Pot: Collections / Iteration and Iterables / summary

- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. Iterable ordered collections can be iterated over or gathered into another collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01590))_

### Served by the Pot: Collections / Generating Iterables / generators and iterables

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_


## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01534))_

> As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator ( ... ) can spread the elements of an array in an array literal or as parameters in a function invocation.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01533))_

<a id="atom-technical-atom-20470d41caf14e2c"></a>
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

### Technical frame 2: Served by the Pot: Collections / Iteration and Iterables / iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01540))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01536))_

<a id="atom-technical-atom-8f303d1919cf6aed"></a>
```
['some squares', ...someSquares]
//=> ["some squares", 1, 4, 9, 16, 25]
```

### Technical frame 3: Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01545))_

> There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01544))_

<a id="atom-technical-atom-63b2edaa330a89bb"></a>
```
const Numbers = {
[Symbol.iterator] () {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}
```

### Technical frame 4: Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01547))_

> Attempting to spread an infinite iterable into an array is always going to fail.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01546))_

<a id="atom-technical-atom-9e9e48d8f80d98b2"></a>
```
['all the numbers', ...Numbers]
//=> infinite loop!
firstAndSecondElement(...Numbers)
//=> infinite loop!
```

### Technical frame 5: Served by the Pot: Collections / Iteration and Iterables / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01551))_

> This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01550))_

<a id="atom-technical-atom-93d825a6af6fbea5"></a>
```
const abc = ["a", "b", "c"];
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
```

### Technical frame 6: Served by the Pot: Collections / Iteration and Iterables / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01554))_

> Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01553))_

<a id="atom-technical-atom-0aa94e55c461e8cf"></a>
```
const RandomNumbers = {
[Symbol.iterator]: () =>
({
next () {
return {value: Math.random()};
}
})
}
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.494052127469331
0.835459444206208
0.1408337657339871
...
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.7845381607767195
0.4956772483419627
0.20259276474826038
...
```

### Technical frame 7: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01573))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01568))_

<a id="atom-technical-atom-cd4c754accfe288e"></a>
```
const ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
5
1
9
...
for (const i of ZeroesToNines) {
console.log(i)
}
//=>
3
```

### Technical frame 8: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01573))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01569))_

<a id="atom-technical-atom-8c4a9a44d5638e88"></a>
```
6
1
...
```

### Technical frame 9: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01573))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01570))_

<a id="atom-technical-atom-be83b0baac640d01"></a>
> mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines , but if RandomNumbers doesn't behave like an ordered collection, that's not mapWith 's fault.

### Technical frame 10: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01579))_

> like our other operations, rest preserves the ordered collection semantics of its argument.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01578))_

<a id="atom-technical-atom-4b232b3666097328"></a>
```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
const rest = (iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
iterator.next();
return iterator;
}
});
```

### Technical frame 11: Served by the Pot: Collections / Iteration and Iterables / from

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01584))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01583))_

<a id="atom-technical-atom-492f235f0cd82891"></a>
```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Technical frame 12: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01683))_

<a id="atom-technical-atom-54530c82c657b597"></a>
```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```


## Related pages

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterables-94f83dae]] - source section: Served by the Pot: Collections / Iteration and Iterables / iterables shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts ... [truncated]; Served by the Pot: Collections / Iteration and Iterables / iterables shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (16 shared statement(s), 5 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-iteration]] - shared technical atoms: Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (11 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity: const Numbers = { [Symbol.iterator] () { let n = 0; return { next: () => ({done: false, value: n++}) } } } (8 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Served by the Pot: Collections / Iteration and Iterables / ordered collections: Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers ... [truncated]; Iterator shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that itera ... [truncated]; Element shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: ['some squares', ...someSquares] //=> ["some squares", 1, 4, 9, 16, 25] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterato ... [truncated]; Object shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Served by the Pot: Collections / Iteration and Iterables / from: Array.from(UpTo1000) //=> [1,81,121,361,441,841,961] (2 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (2 shared atom(s))
- [[javascriptallonge-pattern]] - shared statements and technical atoms: Pattern shares source evidence from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an ... [truncated]; Pattern shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared statement(s), 1 shared atom(s))

## Source

- [[javascriptallonge]]
