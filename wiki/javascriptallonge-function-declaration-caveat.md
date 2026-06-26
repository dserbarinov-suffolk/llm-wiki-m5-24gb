---
page_id: javascriptallonge-function-declaration-caveat
page_kind: concept
summary: function declaration caveats 34: 215 statement(s) and 239 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-26
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-declaration-caveat@f7f248dbc2bc3d61cd8ba338c8504f47
---

# function declaration caveats 34

What [[javascriptallonge]] covers about function declaration caveats 34:

## Statements

- Functions are reference values . _(javascriptallonge.pdf (source-range-8eb13d6b-00651))_
- Functions are applied to arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00652))_
- All of our 'functions' are expressions. _(javascriptallonge.pdf (source-range-8eb13d6b-00397))_
- Now we don't need to use two functions. _(javascriptallonge.pdf (source-range-8eb13d6b-01021))_
- Pure functions are easiest to understand. _(javascriptallonge.pdf (source-range-8eb13d6b-00353))_
- In that case, we need a stateful function. _(javascriptallonge.pdf (source-range-8eb13d6b-01913))_
- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-8eb13d6b-01213))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-8eb13d6b-01623))_
- Function bodies have zero or more statements. _(javascriptallonge.pdf (source-range-8eb13d6b-00656))_
- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-8eb13d6b-00173))_
- You can apply a function to one or more functions. _(javascriptallonge.pdf (source-range-8eb13d6b-00310))_
- So now we have a value representing that function. _(javascriptallonge.pdf (source-range-8eb13d6b-00342))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-8eb13d6b-01623))_
- Our length function is recursive , it calls itself. _(javascriptallonge.pdf (source-range-8eb13d6b-00916))_

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
