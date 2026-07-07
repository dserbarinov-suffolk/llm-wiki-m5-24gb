---
page_id: javascriptallonge-generator
page_kind: concept
summary: Generator: 4 statement(s) and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-generator@8103d02eab8a4f66044780044c89deb9
---

# Generator

What [[javascriptallonge]] covers about generator:

## Statements

### Served by the Pot: Collections / Generating Iterables / generators and iterables

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-c98ab3e6-01678))_

- If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-c98ab3e6-01679))_

- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-c98ab3e6-01682))_

- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_


## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01682))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01679))_

<a id="atom-technical-atom-7ca2d5da0f09f056"></a>
> If we call our generator function more than once, we get new iterators.

### Technical frame 2: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01682))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01680))_

<a id="atom-technical-atom-36671def13809600"></a>
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

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-more-generators-30279cb0]] - source section: Served by the Pot: Collections / Generating Iterables / more generators shares source evidence from Served by the Pot: Collections / Generating Iterables / more generators: Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:; Served by the Pot: Collections / Generating Iterables / more generators shares technical record from Served by the Pot: Collections / Generating Iterables / more generators: const Numbers = { *[Symbol.iterator] () { let i = 0; while (true) { yield i++; } } }; for (const i of Numbers) { console.log(i); } //=> 0 1 2 3 4 5 6 7 (3 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-section-interactive-generators-c6339bc5]] - source section: Interactive Generators
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateful-function-94951f68]] - source section: Interactive Generators / representing naughts and crosses as a stateful function
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-e2c2d97f]] - source section: Interactive Generators / representing naughts and crosses as a stateless function
- [[javascriptallonge-section-interactive-generators-representing-naughts-and-crosses-as-a-stateless-function-will-be-represen-66494cc9]] - source section: Interactive Generators / representing naughts and crosses as a stateless function / Will be represented as:
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-ca8bdeb5]] - source section: Interactive Generators / this seems familiar
- [[javascriptallonge-section-interactive-generators-this-seems-familiar-interactive-generators-0e36e551]] - source section: Interactive Generators / this seems familiar / interactive generators
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-and-iterables-adba5c82]] - source section: Served by the Pot: Collections / Generating Iterables / generators and iterables

### Shared technical atoms

- [[javascriptallonge-iterator]] - shared technical atoms: Iterator shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (3 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (2 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (2 shared atom(s))
- [[javascriptallonge-pattern]] - shared statements and technical atoms: Pattern shares source evidence from Served by the Pot: Collections / Generating Iterables / generators and iterables: This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:; Pattern shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms: Iterable shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: const ThreeNumbers = { *[Symbol.iterator] () { yield 1; yield 2; yield 3 } } (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from Served by the Pot: Collections / Generating Iterables / generators and iterables: If we call our generator function more than once, we get new iterators. (1 shared atom(s))

## Source

- [[javascriptallonge]]
