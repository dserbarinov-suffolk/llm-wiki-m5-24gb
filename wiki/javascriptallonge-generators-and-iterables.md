---
page_id: javascriptallonge-generators-and-iterables
page_kind: concept
summary: topic-concept: 12 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_76b434583f5f8876@a86973a6941d1511e1a4ef8194b83d01
---

# generators and iterables

Source: [[javascriptallonge]]

## Procedure

- We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. (javascriptallonge.pdf p.234)
- Our generator function oneTwoThree is not an iterator. (javascriptallonge.pdf p.234)
- Recalling the way we wrote ordered collections, we could make a collection that uses a generator function:. (javascriptallonge.pdf p.234)
- As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . (javascriptallonge.pdf p.234)
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:. (javascriptallonge.pdf p.235-236)
- Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. (javascriptallonge.pdf p.236)
- This object declares a [Symbol.iterator] function that makes it iterable. (javascriptallonge.pdf p.236)

## Required tables and formulas

<a id="atom-1"></a>
**Atom:** table

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


## Rules and exceptions

- We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. (javascriptallonge.pdf p.234)
- Recalling the way we wrote ordered collections, we could make a collection that uses a generator function:. (javascriptallonge.pdf p.234)

## Related pages

- [[javascriptallonge-generators-are-coroutines]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-more-generators]] - contextualizes: source-supported topic dependency
