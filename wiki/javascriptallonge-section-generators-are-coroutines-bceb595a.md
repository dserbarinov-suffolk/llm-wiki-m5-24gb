---
page_id: javascriptallonge-section-generators-are-coroutines-bceb595a
page_kind: source
summary: generators are coroutines: 27 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-generators-are-coroutines-bceb595a@ce2d387fba4c0cff96016f26d6308450
---

# generators are coroutines

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-javascript-s-generators-34e25b0e]] - previous source section: javascript's generators
- [[javascriptallonge-section-generators-and-iterables-7c8b674f]] - next source section: generators and iterables

## Statements

- This is where generators behave very, very differently from ordinary functions. What happens semantically ? _(javascriptallonge.pdf (source-range-c98ab3e6-01649))_
- The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-c98ab3e6-01651))_
- When we call interator.next() , the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-c98ab3e6-01652))_
- The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1; . _(javascriptallonge.pdf (source-range-c98ab3e6-01653))_
- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-c98ab3e6-01656))_
- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-c98ab3e6-01657))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 2; . _(javascriptallonge.pdf (source-range-c98ab3e6-01658))_
- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-c98ab3e6-01661))_
- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-c98ab3e6-01662))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 3; . _(javascriptallonge.pdf (source-range-c98ab3e6-01663))_
- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-c98ab3e6-01666))_
- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-c98ab3e6-01667))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement. There are no more lines of code, so it ends. _(javascriptallonge.pdf (source-range-c98ab3e6-01668))_
- Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-c98ab3e6-01671))_
- Instead of thinking of there being on execution context, we can imagine that there are two execution contexts. With an iterator, we can call them the producer and the consumer . The iterator is the producer, and the code that iterates over it is the consumer. When the consumer calls .next() , it 'suspends' and the producer starts running. When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next() . _(javascriptallonge.pdf (source-range-c98ab3e6-01672))_
- Of course, generators need not be implemented exactly as coroutines. For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-c98ab3e6-01674))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-c98ab3e6-01676))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-c98ab3e6-01671))_
- For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-c98ab3e6-01674))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-c98ab3e6-01676))_

## Technical atoms

### Technical frame 1: generators are coroutines

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01676))_

> But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01675))_

<a id="atom-technical-atom-c767043771e0fba5"></a>
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
