---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-c4cec34a
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables / state machines: 17 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-c4cec34a@f68a751ee092439fa273a8982ae5908f
---

# Served by the Pot: Collections / Generating Iterables / state machines

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-8c929c4d]] - broader source section: Served by the Pot: Collections / Generating Iterables
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-state-machines-we-ll-keep-it-simple-b9ff91ab]] - narrower source section: Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-recursive-iterators-6bfe7273]] - previous source section: Served by the Pot: Collections / Generating Iterables / recursive iterators
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-javascript-s-generators-c3a5aa1e]] - next source section: Served by the Pot: Collections / Generating Iterables / javascript's generators

## Statements

- Some iterables can be modelled as state machines. Let's revisit the Fibonacci sequence. Again. One way to define it is: _(javascriptallonge.pdf (source-range-0e12e052-01642))_
- The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-0e12e052-01643))_
- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-0e12e052-01644))_
- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-0e12e052-01645))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-0e12e052-01649))_
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 : _(javascriptallonge.pdf (source-range-0e12e052-01649))_
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. _(javascriptallonge.pdf (source-range-0e12e052-01649))_

## Statements by subsection

### Served by the Pot: Collections / Generating Iterables / state machines / We'll keep it simple:

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-0e12e052-01654))_
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-0e12e052-01655))_
- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-0e12e052-01654))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Generating Iterables / state machines

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
