---
page_id: javascriptallonge-list-function-data
page_kind: concept
summary: lists with functions as data: 277 statement(s) and 292 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-26
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-list-function-data@4b557ddcb8eed4b842ce9daa98c6f54b
---

# lists with functions as data

What [[javascriptallonge]] covers about lists with functions as data:

## Statements

- Functions are reference values . _(javascriptallonge.pdf (source-range-8eb13d6b-00651))_
- Functions are applied to arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00652))_
- We have unwittingly reversed the list. _(javascriptallonge.pdf (source-range-8eb13d6b-01128))_
- The state is encoded entirely in data. _(javascriptallonge.pdf (source-range-8eb13d6b-01919))_
- All of our 'functions' are expressions. _(javascriptallonge.pdf (source-range-8eb13d6b-00397))_
- The first rule is simple: [] is a list. _(javascriptallonge.pdf (source-range-8eb13d6b-00902))_
- Now we don't need to use two functions. _(javascriptallonge.pdf (source-range-8eb13d6b-01021))_
- Pure functions are easiest to understand. _(javascriptallonge.pdf (source-range-8eb13d6b-00353))_
- In that case, we need a stateful function. _(javascriptallonge.pdf (source-range-8eb13d6b-01913))_
- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-8eb13d6b-01213))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-8eb13d6b-01623))_
- Function bodies have zero or more statements. _(javascriptallonge.pdf (source-range-8eb13d6b-00656))_
- Here's another look at linked lists using POJOs. _(javascriptallonge.pdf (source-range-8eb13d6b-01387))_
- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-8eb13d6b-00173))_

## Code, rules, and examples

```
var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00024))_

```
function foo () { var first = arguments[0], rest = [].slice.call(arguments, 1); // ... }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00029))_

```
function foo (first, ...rest) { // ... }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00035))_

> But the common thread that runs through all these things is that since they are all simple objects and simple functions, we can use the same set of 'programming with functions' techniques to build programs by composing small, flexible, and decoupled entities.
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00044))_

> Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this:
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00054))_

```
const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } });
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00055))_


## Source

- [[javascriptallonge]]
