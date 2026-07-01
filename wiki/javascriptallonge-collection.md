---
page_id: javascriptallonge-collection
page_kind: concept
summary: Collection: 8 statement(s) and 26 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-collection@9feb6d50c20eff959130c7aa9302be1f
---

# Collection

What [[javascriptallonge]] covers about collection:

## Statements

### Served by the Pot: Collections / Iteration and Iterables

- All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-0e12e052-01525))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators. _(javascriptallonge.pdf (source-range-0e12e052-01541))_

- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-0e12e052-01542))_

### Served by the Pot: Collections / Iteration and Iterables / iterables

- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-0e12e052-01565))_

### Lazy and Eager Collections

- Over time, this informal 'interface' for collections grows by accretion. Some methods are only added to a few collections, some are added to all. But our objects grow fatter and fatter. We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-0e12e052-01761))_

- This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail. That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-0e12e052-01763))_

### Lazy and Eager Collections / lazy collection operations

- Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-0e12e052-01796))_

### Interactive Generators / this seems familiar / interactive generators

- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-0e12e052-01938))_


## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01570))_

> There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01569))_

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

### Technical frame 2: Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01572))_

> Attempting to spread an infinite iterable into an array is always going to fail.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01571))_

```
['all the numbers', ...Numbers]
//=> infinite loop!
firstAndSecondElement(...Numbers)
//=> infinite loop!
```

### Technical frame 3: Served by the Pot: Collections / Iteration and Iterables / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01576))_

> This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01575))_

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

### Technical frame 4: Served by the Pot: Collections / Iteration and Iterables / ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01579))_

> Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01578))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01585))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01584))_

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

### Technical frame 6: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01588))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01587))_

```
const Evens = mapWith((x) => 2 * x, Numbers);
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
```

### Technical frame 7: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01590))_

> Every time we write for (const i of Evens) , JavaScript calls Evens[Symbol.iterator]() . That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens) , and that means that iterator starts at the beginning of Numbers .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01589))_

```
const Evens =
{
[Symbol.iterator] () {
const iterator = Numbers[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : 2 *value});
}
}
}
};
```

### Technical frame 8: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01598))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01593))_

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

### Technical frame 9: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01598))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01594))_

```
6
1
...
```

### Technical frame 10: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01598))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01595))_

> mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines , but if RandomNumbers doesn't behave like an ordered collection, that's not mapWith 's fault.

### Technical frame 11: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01598))_

> Like mapWith , they preserve the ordered collection semantics of whatever you give them.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01597))_

```
const filterWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
do {
const {done, value} = iterator.next();
} while (!done && !fn(value));
return {done, value};
}
}
}
});
const untilWith = (fn, iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
return {
next () {
let {done, value} = iterator.next();
done = done || fn(value);
return ({done, value: done ? undefined : value});
}
}
}
});
```

### Technical frame 12: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01601))_

> As we expect from an ordered collection, each time we iterate over UpTo1000 , we begin at the beginning.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01600))_

```
const Squares = mapWith((x) => x * x, Numbers);
const EndWithOne = filterWith((x) => x % 10 === 1, Squares);
const UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
[...UpTo1000]
//=>
[1,81,121,361,441,841,961]
```

### Technical frame 13: Served by the Pot: Collections / Iteration and Iterables / from

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01609))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01608))_

```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Technical frame 14: Served by the Pot: Collections / Generating Iterables / state machines

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01649))_

> The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01648))_

```text
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
Served by the Pot: Collections
206
55
89
144
...
The thing to note here is that our fibonacci generator has three states: generating 0, generating
1, and generating everything after that. This isn’t a good fit for an iterator, because iterators have
one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps
using a state pattern90:
We’ll keep it simple:
// Iteration
let a, b, state = 0;
const fibonacci = () => {
switch (state) {
case 0:
state = 1;
return a = 0;
case 1:
state = 2;
return b = 1;
case 2:
[a, b] = [b, a + b];
return b
}
};
while (true) {
console.log(fibonacci());
}
//=>
0
1
1
2
3
5
8
13
90https://en.wikipedia.org/wiki/State_pattern
Served by the Pot: Collections
207
21
34
55
89
144
...
Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspun-
ning the natural linear state. In a generator, we write “do this, then this, then this.” In an iterator,
we have to wrap that up and explicitly keep track of what step we’re on.
So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear
control flow. Whereas the iteration version must make that state explicit.
javascript’s generators
It would be very nice if we could sometimes write iterators as a .next() method that gets called, and
sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript
makes this possible.
We can write an iterator, but use a generation style of programming. An iterator written in a
generation style is called a generator. To write a generator, we write a function, but we make two
changes:
1. We declare the function using the function * syntax. Not a fat arrow. Not a plain function.
2. We don’t return values or output them to console.log. We “yield” values using the yield
keyword.
When we invoke the function, we get an iterator object back. Let’s start with the degenerate example,
the empty iterator:91
function * empty () {};
empty().next()
//=>
{"done":true}
When we invoke empty, we get an iterator with no elements. This makes sense, because empty never
yields anything. We call its .next() method, but it’s done immediately.
Generator functions can take an argument. Let’s use that to illustrate yield:
91We wrote a generator declaration. We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword,
but we don’t need to do that here.
Served by the Pot: Collections
208
function * only (something) {
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 34 | Served by the Pot: Collections |
| 144 | The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern90: We’ll keep it simple: // Iteration let a, b, state = 0; const fibonacci = () => { switch (state) { case 0: state = 1; return a = 0; case 1: state = 2; return b = 1; case 2: [a, b] = [b, a + b]; return b while (true) { console.log(fibonacci()); |
| 13 | 90https://en.wikipedia.org/wiki/State_pattern |
| 207 | Served by the Pot: Collections |
| 144 | Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspun- ning the natural linear state. In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on. So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. Whereas the iteration version must make that state explicit. javascript’s generators It would be very nice if we could sometimes write iterators as a.next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible. We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator. To write a generator, we write a function, but we make two changes: |
| 1 | We declare the function using the function * syntax. Not a fat arrow. Not a plain function. |
| 2 | We don’t return values or output them to console.log. We “yield” values using the yield keyword. When we invoke the function, we get an iterator object back. Let’s start with the degenerate example, the empty iterator:91 function * empty () {}; empty().next() {"done":true} When we invoke empty, we get an iterator with no elements. This makes sense, because empty never yields anything. We call its.next() method, but it’s done immediately. 91We wrote a generator declaration. We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword, but we don’t need to do that here. |
| 208 | Generator functions can take an argument. Let’s use that to illustrate yield: Served by the Pot: Collections function * only (something) { |

</details>

### Technical frame 15: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01708))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01707))_

```text
yield 3
}
}
for (const i of ThreeNumbers) {
console.log(i);
}
//=>
1
2
3
[...ThreeNumbers]
//=>
[1,2,3]
const iterator = ThreeNumbers[Symbol.iterator]();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function
invocation, because we have written an iterable that uses a generator to return an iterator from its
[Symbol.iterator] method.
This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing
Served by the Pot: Collections
213
generator methods for objects:
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared
*[Symbol.iterator], it’s a generator instead of an iterator.
So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a generator
method for [Symbol.iterator].
more generators
Generators can produce infinite streams of values:
const Numbers = {
*[Symbol.iterator] () {
let i = 0;
while (true) {
yield i++;
}
}
};
for (const i of Numbers) {
console.log(i);
}
//=>
0
1
2
3
4
5
6
7
Served by the Pot: Collections
214
8
9
10
...
Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we
wrote Fibonacci using explicit state:
const Fibonacci = {
[Symbol.iterator]: () => {
let a = 0, b = 1, state = 0;
return {
next: () => {
switch (state) {
case 0:
state = 1;
return {value: a};
case 1:
state = 2;
return {value: b};
case 2:
[a, b] = [b, a + b];
return {value: b};
}
}
}
}
};
for (let n of Fibonacci) {
console.log(n)
}
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 3 | [...ThreeNumbers] [1,2,3] const iterator = ThreeNumbers[Symbol.iterator](); iterator.next() {"done":false, value: 1} iterator.next() {"done":false, value: 2} iterator.next() {"done":false, value: 3} iterator.next() {"done":true} Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method. This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing |
| 213 | Served by the Pot: Collections generator methods for objects: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator. So to summarize, ThreeNumbers is an object that we’ve made iterable, by way of writing a generator method for [Symbol.iterator]. more generators Generators can produce infinite streams of values: const Numbers = { *[Symbol.iterator] () { let i = 0; while (true) { yield i++; for (const i of Numbers) { console.log(i); |
| 7 | Served by the Pot: Collections |
| 10 | Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state: const Fibonacci = { [Symbol.iterator]: () => { let a = 0, b = 1, state = 0; return { next: () => { switch (state) { case 0: state = 1; return {value: a}; case 1: state = 2; return {value: b}; case 2: [a, b] = [b, a + b]; return {value: b}; for (let n of Fibonacci) { console.log(n) |

</details>

### Technical frame 16: Served by the Pot: Collections / Generating Iterables / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01736))_

> append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01742))_

```text
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
yield* is handy when writing generator functions that operate on or create iterables.
rewriting iterable operations
Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of:
Served by the Pot: Collections
221
const mapWith = (fn, iterable) =>
({
[Symbol.iterator]: () => {
const iterator = iterable[Symbol.iterator]();
return {
next: () => {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
We can write:
function * mapWith (fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return
an object with a .next() method. No need to fool around with {done} or {value}, just yield values
until we’re done.
We can do the same thing with our other operations like filterWith and untilWith. Here’re our
iterable methods rewritten as generators:
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
Served by the Pot: Collections
222
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 5 | yield* is handy when writing generator functions that operate on or create iterables. rewriting iterable operations Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of: |
| 221 | Served by the Pot: Collections const mapWith = (fn, iterable) => [Symbol.iterator]: () => { const iterator = iterable[Symbol.iterator](); return { next: () => { const {done, value} = iterator.next(); return ({done, value: done? undefined: fn(value)}); We can write: function * mapWith (fn, iterable) { for (const element of iterable) { yield fn(element); No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a.next() method. No need to fool around with {done} or {value}, just yield values until we’re done. We can do the same thing with our other operations like filterWith and untilWith. Here’re our iterable methods rewritten as generators: function * mapWith(fn, iterable) { for (const element of iterable) { yield fn(element); function * filterWith (fn, iterable) { for (const element of iterable) { if (!!fn(element)) yield element; |
| 222 | Served by the Pot: Collections function * untilWith (fn, iterable) { for (const element of iterable) { if (fn(element)) break; yield fn(element); first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: const first = (iterable) => iterable[Symbol.iterator]().next().value; function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next(); yield * iterator; |

</details>

### Technical frame 17: Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01772))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01768))_

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

### Technical frame 18: Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01772))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01769))_

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

### Technical frame 19: Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01772))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01770))_

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

### Technical frame 20: Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01796))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01795))_

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
const firstCubeOver1234 =
Numbers
.map((x) => x * x * x)
.filter((x) => x > 1234)
.first()
//=> 1331
```

### Technical frame 21: Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01799))_

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
```

### Technical frame 22: Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01800))_

```
const EagerCollection = (gatherable) =>
({
map(fn) {
const
original = this;
return gatherable.from(
(function* () {
for (let element of original) {
yield fn(element);
}
})()
);
},
reduce(fn, seed) {
let accumulator = seed;
for(let element of this) {
accumulator = fn(accumulator, element);
}
return accumulator;
},
filter(fn) {
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) yield element;
}
})()
);
},
find(fn) {
for (let element of this) {
if (fn(element)) return element;
}
},
until(fn) {
```

### Technical frame 23: Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01801))_

```
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) break;
yield element;
}
})()
);
},
first() {
return this[Symbol.iterator]().next().value;
},
rest() {
const iteration = this[Symbol.iterator]();
iteration.next();
return gatherable.from(
(function* () {
yield * iteration;
})()
);
return gatherable.from(iterable);
},
take(numberToTake) {
const original = this;
let numberRemaining = numberToTake;
return gatherable.from(
(function* () {
for (let element of original) {
if (numberRemaining-- <= 0) break;
yield element;
}
})()
);
}
});
```

### Technical frame 24: Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01803))_

```
const EMPTY = {
isEmpty: () => true
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
}, EagerCollection(Pair));
Pair.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair(value, iterationToList(iteration));
})(iterable[Symbol.iterator]());
Pair.from([1, 2, 3, 4, 5]).map(x => x * 2)
//=>
```

### Technical frame 25: Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01802))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01804))_

```
{"car": 2,
"cdr": {"car": 4,
"cdr": {"car": 6,
"cdr": {"car": 8,
"cdr": {"car": 10,
"cdr": {}
}
}
}
}
}
```

### Technical frame 26: Interactive Generators / this seems familiar / interactive generators

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01937))_

> Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1)

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01936))_

```
function* generatorNaughtsAndCrosses () {
const x1 = yield 0;
switch (x1) {
case 1:
const x2 = yield 6;
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
yield 3;
break;
case 3:
const x3 = yield 8;
switch (x3) {
case 2:
case 5:
case 7:
yield 4;
break;
case 4:
yield 7;
break;
```


## Related pages

- [[javascriptallonge-eager-collection]] - narrower topic: Eager Collection shares technical record from Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (3 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Served by the Pot: Collections / Iteration and Iterables: All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and ... [truncated]; Element shares technical record from Served by the Pot: Collections / Iteration and Iterables / ordered collections: const abc = ["a", "b", "c"]; for (const i of abc) { console.log(i) } //=> a b c for (const i of abc) { console.log(i) } //=> a b c (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional i ... [truncated]; Functional Iterators shares technical record from Served by the Pot: Collections / Generating Iterables / state machines: while (true) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 1 1 2 3 5 8 13 21 34 Served by the Pot: Collections 206 55 89 144 ... The thing to note he ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-interactive-generator]] - shared statements and technical atoms: Interactive Generators shares source evidence from Interactive Generators / this seems familiar / interactive generators: Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no mea ... [truncated]; Interactive Generators shares technical record from Interactive Generators / this seems familiar / interactive generators: function* generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3 ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iteration]] - shared technical atoms: Iteration shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity: const Numbers = { [Symbol.iterator] () { let n = 0; return { next: () => ({done: false, value: n++}) } } } (13 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms: Iterable shares technical record from Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity: const Numbers = { [Symbol.iterator] () { let n = 0; return { next: () => ({done: false, value: n++}) } } } (8 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Served by the Pot: Collections / Iteration and Iterables / ordered collections: const RandomNumbers = { [Symbol.iterator]: () => ({ next () { return {value: Math.random()}; } }) } for (const i of RandomNumbers) { console.log(i) } //=> 0.49405212 ... [truncated] (7 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from Lazy and Eager Collections / eager collections: const extend = function (consumer, ...providers) { for (let i = 0; i < providers.length; ++i) { const provider = providers[i]; for (let key in provider) { if (provid ... [truncated] (5 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (4 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const Evens = { [Symbol.iterator] () { const iterator = Numbers[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: d ... [truncated] (2 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical record from Served by the Pot: Collections / Generating Iterables / state machines: while (true) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() //=> 0 1 1 2 3 5 8 13 21 34 Served by the Pot: Collections 206 55 89 144 ... The thing to note he ... [truncated] (1 shared atom(s))
- [[javascriptallonge-generator]] - shared technical atoms: Generator shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: yield 3 } } for (const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumbers] //=> [1,2,3] const iterator = ThreeNumbers[Symbol.iterator](); iterator.ne ... [truncated] (1 shared atom(s))
- [[javascriptallonge-lazy]] - shared technical atoms: Lazy shares technical record from Lazy and Eager Collections / lazy collection operations: const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false, value: n++}) } } }, LazyCollection); const firstCubeOver123 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be ... [truncated] (2 shared statement(s))

## Source

- [[javascriptallonge]]
