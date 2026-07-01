---
page_id: javascriptallonge-generator
page_kind: concept
summary: Generator: 4 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-generator@eb56d5eb97435307c2c0e5450cc21c98
---

# Generator

What [[javascriptallonge]] covers about generator:

## Statements

### Served by the Pot: Collections / Generating Iterables / generators and iterables

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-0e12e052-01704))_

- If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-0e12e052-01705))_

- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-0e12e052-01708))_

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-0e12e052-01710))_


## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01708))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01705))_

> If we call our generator function more than once, we get new iterators.

### Technical frame 2: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01708))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01706))_

```
const ThreeNumbers = {
[Symbol.iterator]: function * () {
yield 1;
yield 2;
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
```

### Technical frame 3: Served by the Pot: Collections / Generating Iterables / generators and iterables

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

### Technical frame 4: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01710))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01709))_

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

- [[javascriptallonge-pattern]] - shared statements and technical atoms: Pattern shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:; Pattern shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (4 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (2 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (2 shared atom(s))
- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: yield 3 } } for (const i of ThreeNumbers) { console.log(i); } //=> 1 2 3 [...ThreeNumbers] //=> [1,2,3] const iterator = ThreeNumbers[Symbol.iterator](); iterator.ne ... [truncated] (1 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms: Iterable shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared atom(s))
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-more-generators-17bb605f]] - source section: Served by the Pot: Collections / Generating Iterables / more generators shares source evidence from Served by the Pot: Collections / Generating Iterables / more generators: Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:; Served by the Pot: Collections / Generating Iterables / more generators shares technical record from Served by the Pot: Collections / Generating Iterables / more generators: const Numbers = { *[Symbol.iterator] () { let i = 0; while (true) { yield i++; } } }; for (const i of Numbers) { console.log(i); } //=> 0 1 2 3 4 5 6 7 (3 shared statement(s), 6 shared atom(s))

## Source

- [[javascriptallonge]]
