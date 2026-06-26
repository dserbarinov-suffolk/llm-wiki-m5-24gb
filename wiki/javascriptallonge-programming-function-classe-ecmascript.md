---
page_id: javascriptallonge-programming-function-classe-ecmascript
page_kind: concept
summary: Programming from Functions to Classes in ECMAScript 2015: 243 statement(s) and 254 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-26
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-programming-function-classe-ecmascript@d6a6d57301e65f9a281246e47009a1dd
---

# Programming from Functions to Classes in ECMAScript 2015

What [[javascriptallonge]] covers about programming from functions to classes in ecmascript 2015:

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

> ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs.
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00019))_

> Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features.
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00020))_

```
var i; for (i = 0; i < array.length; ++i) { ( function (i) { // ... })(i) }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00024))_

```
function foo () { var first = arguments[0], rest = [].slice.call(arguments, 1); // ... }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00029))_

> With ECMASCript 2015, we can write:
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00032))_

```
function foo (first, ...rest) { // ... }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00035))_


## Source

- [[javascriptallonge]]
