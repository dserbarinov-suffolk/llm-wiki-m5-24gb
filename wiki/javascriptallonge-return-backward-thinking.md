---
page_id: javascriptallonge-return-backward-thinking
page_kind: concept
summary: a return to backward thinking: 44 statement(s) and 187 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-26
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-return-backward-thinking@6e3cc8ce8ea9ef9dd9ad780ca484915c
---

# a return to backward thinking

What [[javascriptallonge]] covers about a return to backward thinking:

## Statements

- There are three places it returns. _(javascriptallonge.pdf (source-range-8eb13d6b-00982))_
- No need to return an object with a .next() method. _(javascriptallonge.pdf (source-range-8eb13d6b-01760))_
- Now our .iterator() method is returning an iterator object. _(javascriptallonge.pdf (source-range-8eb13d6b-01561))_
- We know that (() => 0)() returns 0 , and this is unsurprising. _(javascriptallonge.pdf (source-range-8eb13d6b-00193))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-8eb13d6b-00201))_
- This is a function that is applied to no values and returns 0 . _(javascriptallonge.pdf (source-range-8eb13d6b-00175))_
- One of the important possible statements is a return statement. _(javascriptallonge.pdf (source-range-8eb13d6b-00294))_
- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-8eb13d6b-00218))_
- So we have a function, that returns a function, that returns zero . _(javascriptallonge.pdf (source-range-8eb13d6b-00268))_
- There are ifs, fors, returns, everything thrown higgledy piggledy together. _(javascriptallonge.pdf (source-range-8eb13d6b-00591))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-8eb13d6b-00982))_
- This expression, when evaluated, returns a function that calculates circumferences. _(javascriptallonge.pdf (source-range-8eb13d6b-00397))_
- We've writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-8eb13d6b-01733))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-8eb13d6b-00608))_

## Code, rules, and examples

> Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00195))_

```
(() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World'
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00256))_

> The return keyword creates a return statement that immediately terminates the function application and returns the result of evaluating its expression. For example:
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00257))_

```
(() => { 1 + 1; return 2 + 2 })() //=> 4
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00258))_

```
(() => { return 1 + 1; 2 + 2 })() //=> 2
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00260))_

> The return statement is the first statement we've seen, and it behaves differently than an expression. For example, you can't use one as the expression in a simple function, because it isn't an expression:
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00261))_


## Source

- [[javascriptallonge]]
