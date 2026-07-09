---
page_id: javascriptallonge-generators-are-coroutines
page_kind: concept
summary: topic-concept: 27 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_32b2ca36b9ae1930@7298a1d94106a17af3539491ae1798fa
---

# generators are coroutines

Source: [[javascriptallonge]]

## Statements

- This is where generators behave very, very differently from ordinary functions. (javascriptallonge.pdf p.232)
- The iterator is in a nascent or 'newborn' state. (javascriptallonge.pdf p.232)
- When we call interator.next() , the body of our generator begins to be evaluated. (javascriptallonge.pdf p.232)
- The body of our generator runs until it returns, ends , or encounters a yield statement, which is yield 1; . (javascriptallonge.pdf p.233)
- The rest of the program continues along its way until it makes another call to iterator.next() . (javascriptallonge.pdf p.233)
- The iterator resumes execution from the point where it yielded the last value. (javascriptallonge.pdf p.233)
- The body of our generator runs until it returns, ends , or encounters the next yield statement, which is yield 2; . (javascriptallonge.pdf p.233)
- The rest of the program continues along its way until it makes another call to iterator.next() . (javascriptallonge.pdf p.233)
- The iterator resumes execution from the point where it yielded the last value. (javascriptallonge.pdf p.233)
- The body of our generator runs until it returns, ends , or encounters the next yield statement, which is yield 3; . (javascriptallonge.pdf p.233)
- The rest of the program continues along its way until it makes another call to iterator.next() . (javascriptallonge.pdf p.233)
- The iterator resumes execution from the point where it yielded the last value. (javascriptallonge.pdf p.233)
- The body of our generator runs until it returns, ends , or encounters the next yield statement. (javascriptallonge.pdf p.233)
- There are no more lines of code, so it ends. (javascriptallonge.pdf p.233)
- Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. (javascriptallonge.pdf p.233)
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. (javascriptallonge.pdf p.233)
- With an iterator, we can call them the producer and the consumer . (javascriptallonge.pdf p.233-234)
- The iterator is the producer, and the code that iterates over it is the consumer. (javascriptallonge.pdf p.233-234)
- Of course, generators need not be implemented exactly as coroutines. (javascriptallonge.pdf p.234)
- For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later):. (javascriptallonge.pdf p.234)
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. (javascriptallonge.pdf p.234)
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. (javascriptallonge.pdf p.234)

## Rules

- With an iterator, we can call them the producer and the consumer . (javascriptallonge.pdf p.233-234)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const oneTwoThree = function * () {
yield 1;
yield 2;
yield 3;
};
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
const iterator = oneTwoThree();
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

<a id="atom-2"></a>
**Atom:** code block

```
const oneTwoThree = function () {
let state = 'newborn';
return {
next () {
switch (state) {
case 'newborn':
state = 1;
return {value: 1};
case 1:
state = 2;
return {value: 2}
case 2:
state = 3;
return {value: 3}
case 3:
return {done: true};
}
}
}
};
```


## Related pages

- [[javascriptallonge-javascript-s-generators]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-generators-and-iterables]] - contextualizes: source-supported topic dependency
