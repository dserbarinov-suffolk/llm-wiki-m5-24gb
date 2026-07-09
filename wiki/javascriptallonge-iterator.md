---
page_id: javascriptallonge-iterator
page_kind: concept
summary: Iterator: 27 statement(s) and 26 atom(s) from raw/javascriptallonge.pdf.
page_family: broad-topic
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterator@23c2b286cde761328007337f64765ab7
---

# Iterator

What [[javascriptallonge]] covers about iterator:

## Statements

### unfolding and laziness

- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_

### caveat

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-c98ab3e6-01299))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-c98ab3e6-01518))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-c98ab3e6-01522))_

### Served by the Pot: Collections / Iteration and Iterables / iterables

- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-c98ab3e6-01525))_

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-c98ab3e6-01527))_

### Served by the Pot: Collections / Iteration and Iterables / ordered collections

- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01554))_

- Right now, we're just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-c98ab3e6-01555))_

### Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

- This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-c98ab3e6-01560))_

### Served by the Pot: Collections / Iteration and Iterables / summary

- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. Iterable ordered collections can be iterated over or gathered into another collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01590))_

- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-c98ab3e6-01591))_

### Served by the Pot: Collections / Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-c98ab3e6-01595))_

### Served by the Pot: Collections / Generating Iterables / recursive iterators

- Iterators maintain state, that's what they do. Generators have to manage the exact same amount of state, but sometimes, it's much easier to manage that state in a generator. One of those cases is when we have to recursively enumerate something. _(javascriptallonge.pdf (source-range-c98ab3e6-01606))_

### Served by the Pot: Collections / Generating Iterables / state machines

- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-c98ab3e6-01623))_

### Served by the Pot: Collections / Generating Iterables / javascript's generators

- We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator . To write a generator, we write a function, but we make two changes: _(javascriptallonge.pdf (source-range-c98ab3e6-01632))_

- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-c98ab3e6-01641))_

### Served by the Pot: Collections / Generating Iterables / generators are coroutines

- The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-c98ab3e6-01651))_

- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-c98ab3e6-01657))_

- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-c98ab3e6-01662))_

### Served by the Pot: Collections / Generating Iterables / generators and iterables

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_

### Served by the Pot: Collections / Generating Iterables / more generators

- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-c98ab3e6-01695))_

### Served by the Pot: Collections / rewriting iterable operations

- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-c98ab3e6-01726))_

### Served by the Pot: Collections / Summary

- A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. And we don't need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-c98ab3e6-01729))_

### Interactive Generators / this seems familiar

- However, our solution inverts the control. We aren't calling our function with moves, it's calling us. With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow. _(javascriptallonge.pdf (source-range-c98ab3e6-01887))_


## Technical atoms

### Technical frame 1: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01285))_

<a id="atom-technical-atom-3cbb0179c9f157ad"></a>
```
const odds = () => {
```

### Technical frame 2: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01286))_

<a id="atom-technical-atom-c80140cd0040b3b4"></a>
```
let number = 1;
return () => {
const value = number;
number += 2;
return {done: false, value};
}
}
const squareOf = callLeft(mapIteratorWith, (x) => x * x)
toArray(take(squareOf(odds()), 5))
//=> [1, 9, 25, 49, 81]
```

### Technical frame 3: unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01289))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01288))_

<a id="atom-technical-atom-276e586089a73115"></a>
```
const filterIteratorWith = (fn, iterator) =>
() => {
do {
const {done, value} = iterator();
} while (!done && !fn(value));
return {done, value};
}
const oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);
toArray(take(squareOf(oddsOf(NumberIterator(1))), 5))
//=> [1, 9, 25, 49, 81]
```

### Technical frame 4: Served by the Pot: Collections / Iteration and Iterables / ordered collections

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

### Technical frame 5: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01560))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01559))_

<a id="atom-technical-atom-db03dd1e259d128a"></a>
```
const mapWith = (fn, collection) =>
({
[Symbol.iterator] () {
const iterator = collection[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Technical frame 6: Served by the Pot: Collections / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01623))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01621))_

<a id="atom-technical-atom-68a1c3d047c9c52e"></a>
```
// Generation
const fibonacci = () => {
let a, b;
console.log(a = 0);
console.log(b = 1);
while (true) {
[a, b] = [b, a + b];
console.log(b);
}
}
fibonacci()
//=>
0
1
1
2
3
5
8
13
21
34
```

### Technical frame 7: Served by the Pot: Collections / Generating Iterables / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01641))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01642))_

<a id="atom-technical-atom-271ecbd5db3880fa"></a>
```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

### Technical frame 8: Served by the Pot: Collections / Generating Iterables / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01641))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01644))_

<a id="atom-technical-atom-f53aec00fd0f6190"></a>
```
const sixteen = only("sixteen");
sixteen.next()
//=>
{"done":false, value: "sixteen"}
sixteen.next()
//=>
{"done":true}
```

### Technical frame 9: Served by the Pot: Collections / Generating Iterables / generators and iterables

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

### Technical frame 10: Served by the Pot: Collections / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01726))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01727))_

<a id="atom-technical-atom-aa611136013d179d"></a>
```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```


## Related pages

### Source structure

- [[javascriptallonge-section-copy-on-write-functional-iterators-74724e0a]] - source section: Copy on Write / Functional Iterators
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-recursive-iterators-6db8d95d]] - source section: Served by the Pot: Collections / Generating Iterables / recursive iterators
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-57a76f01]] - source section: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-cbbb8baa]] - source section: Served by the Pot: Collections / Iteration and Iterables / iterator objects

### Shared technical atoms

- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated]; Object shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (5 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects / Like this:: Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterato ... [truncated]; Method shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (3 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-iteration]] - shared technical atoms: Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array ... [truncated] (6 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from Served by the Pot: Collections / Generating Iterables / javascript's generators: Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:; Return shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from Served by the Pot: Collections / Iteration and Iterables / ordered collections: const RandomNumbers = { [Symbol.iterator]: () => ({ next () { return {value: Math.random()}; } }) } for (const i of RandomNumbers) { console.log(i) } //=> 0.49405212 ... [truncated] (5 shared atom(s))
- [[javascriptallonge-iterable]] - shared statements and technical atoms: Iterable shares source evidence from Served by the Pot: Collections / Iteration and Iterables / ordered collections: Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers ... [truncated]; Iterable shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from Served by the Pot: Collections / Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Functional shares technical record from Served by the Pot: Collections / Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Served by the Pot: Collections / Iteration and Iterables / summary: Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility ... [truncated]; Javascript shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const Evens = { [Symbol.iterator] () { const iterator = Numbers[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: d ... [truncated] (1 shared statement(s), 3 shared atom(s))

### Shared claims

- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))

## Source

- [[javascriptallonge]]
