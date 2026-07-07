---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterables-94f83dae
page_kind: source
summary: Served by the Pot: Collections / Iteration and Iterables / iterables: 21 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterables-94f83dae@3a632b329f71936f95f9f0823cc27527
---

# Served by the Pot: Collections / Iteration and Iterables / iterables

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-cbbb8baa]] - previous source section: Served by the Pot: Collections / Iteration and Iterables / iterator objects
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterables-out-to-infinity-ae258dd7]] - next source section: Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-98745d63]] - broader source section: Served by the Pot: Collections / Iteration and Iterables

### Recipes

- [[javascriptallonge-recipe-iterables]] - recipe pattern: iterables

### Topics

- [[javascriptallonge-iterable]] - topic hub: opens the topic page for Iterable

## Statements

- People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-c98ab3e6-01524))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn't make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-c98ab3e6-01525))_
- To ensure that the method would not conflict with any existing code, JavaScript provides a symbol . Symbols are unique constants that are guaranteed not to conflict with existing strings. Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols. 88 _(javascriptallonge.pdf (source-range-c98ab3e6-01526))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-c98ab3e6-01527))_
- 88 You can read more about JavaScript symbols in Axel Rauschmayer's Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-c98ab3e6-01528))_
- Our stack does, so instead of binding the existing iterator method to the name iterator , we bind it to the Symbol.iterator . We'll do that using the [ ] syntax for using an expression as an object literal key: _(javascriptallonge.pdf (source-range-c98ab3e6-01529))_
- The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable: _(javascriptallonge.pdf (source-range-c98ab3e6-01532))_
- As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator ( ... ) can spread the elements of an array in an array literal or as parameters in a function invocation. _(javascriptallonge.pdf (source-range-c98ab3e6-01534))_
- Nowis the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal: _(javascriptallonge.pdf (source-range-c98ab3e6-01535))_
- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-c98ab3e6-01540))_
- And if we have an infinite collection, spreading is going to fail outright as we're about to see. _(javascriptallonge.pdf (source-range-c98ab3e6-01541))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-c98ab3e6-01540))_

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
