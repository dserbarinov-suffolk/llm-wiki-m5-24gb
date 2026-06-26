---
page_id: javascriptallonge-array-destructuring-argument
page_kind: concept
summary: Arrays and Destructuring Arguments: 112 statement(s) and 144 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-26
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-array-destructuring-argument@ebc1ebd825abbe373c5165a46bc7b29e
---

# Arrays and Destructuring Arguments

What [[javascriptallonge]] covers about arrays and destructuring arguments:

## Statements

- Functions are applied to arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00652))_
- Well for arguments, that is very simple. _(javascriptallonge.pdf (source-range-8eb13d6b-00311))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-8eb13d6b-01021))_
- Specifically, arrays and objects can mutate. _(javascriptallonge.pdf (source-range-8eb13d6b-01134))_
- The array we had in prepend is no longer used. _(javascriptallonge.pdf (source-range-8eb13d6b-01033))_
- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-8eb13d6b-00864))_
- We need something for when the array isn't empty. _(javascriptallonge.pdf (source-range-8eb13d6b-00913))_
- But this is not how JavaScript's built-in arrays work. _(javascriptallonge.pdf (source-range-8eb13d6b-01037))_
- Up to now, we've looked at functions without arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00277))_
- This function has one argument, room , and an empty body. _(javascriptallonge.pdf (source-range-8eb13d6b-00281))_
- Arrays are JavaScript's 'native' representation of lists. _(javascriptallonge.pdf (source-range-8eb13d6b-00829))_
- Like numbers, strings, and arrays, they have a representation. _(javascriptallonge.pdf (source-range-8eb13d6b-00173))_
- Array literals are expressions, and arrays are reference types . _(javascriptallonge.pdf (source-range-8eb13d6b-00842))_
- We've seen how to build lists with arrays and with linked lists. _(javascriptallonge.pdf (source-range-8eb13d6b-01235))_

## Code, rules, and examples

```
for ( int i = 0; i < array.length; ++i) { // ... }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00022))_

```
var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00024))_

```
function foo () { var first = arguments[0], rest = [].slice.call(arguments, 1); // ... }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00029))_

```
for ( let i = 0; i < array.length; ++i) { // ... }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00033))_

> Notice that you are always generating arrays with the same contents.
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00141))_

> Let's put functions to work. The way we use functions is to apply them to zero or more values called arguments . Just as 2 + 2 produces a value (in this case 4 ), applying a function to zero or more arguments produces a value as well.
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00186))_


## Source

- [[javascriptallonge]]
