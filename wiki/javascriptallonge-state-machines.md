---
page_id: javascriptallonge-state-machines
page_kind: concept
summary: state machines: 6 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_226693a04fa98b5d@d68997a56a0f39e79a7243d30a284d3b
---

# state machines

Source: [[javascriptallonge]]

## Statements

- Some iterables can be modelled as state machines. (javascriptallonge.pdf p.228)
- The first element of the fibonacci sequence is zero. (javascriptallonge.pdf p.228)
- The second element of the fibonacci sequence is one. (javascriptallonge.pdf p.228)
- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. (javascriptallonge.pdf p.228)
- This isn't a good fit for an iterator, because iterators have one functional entry point and therefore, we'd have to represent our three states explicitly, perhaps using a state pattern 90 :. (javascriptallonge.pdf p.229)
- The thing to note here is that our fibonacci generator has three states: generating 0 , generating 1 , and generating everything after that. (javascriptallonge.pdf p.229)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** table

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
