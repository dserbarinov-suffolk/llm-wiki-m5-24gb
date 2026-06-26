---
page_id: javascriptallonge-mixing-const
page_kind: concept
summary: mixing let and const: 39 statement(s) and 341 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-26
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-mixing-const@37bcb78e88a7e54d985b461100f7200d
---

# mixing let and const

What [[javascriptallonge]] covers about mixing let and const:

## Statements

- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-8eb13d6b-00486))_
- We use the const keyword in a const statement . _(javascriptallonge.pdf (source-range-8eb13d6b-00428))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-8eb13d6b-00425))_
- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-8eb13d6b-00662))_
- JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-8eb13d6b-00659))_
- There's no benefit to constant space if finite space is sufficient. _(javascriptallonge.pdf (source-range-8eb13d6b-01875))_
- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-8eb13d6b-01028))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. _(javascriptallonge.pdf (source-range-8eb13d6b-01760))_
- JavaScript does not permit us to rebind a name that has been bound with const . _(javascriptallonge.pdf (source-range-8eb13d6b-00501))_
- JavaScript does not permit us to rebind a name that has been bound with const . _(javascriptallonge.pdf (source-range-8eb13d6b-01178))_
- But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-8eb13d6b-01211))_
- While we're executing the mapWith function, we're constructing a new linked list. _(javascriptallonge.pdf (source-range-8eb13d6b-01154))_
- It was, 'Write an algorithm to detect a loop in a linked list, in constant space.' _(javascriptallonge.pdf (source-range-8eb13d6b-01268))_
- Shadowing a const with a let does not permit it to be rebound in its original scope. _(javascriptallonge.pdf (source-range-8eb13d6b-01196))_

## Code, rules, and examples

```
const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } });
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00055))_

```
const filterWith = (fn, iterable) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { if (!!fn(element)) yield element; } } });
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00057))_

> As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00252))_

> We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const :
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00425))_

```
(diameter) => { const PI = 3.14159265; return diameter * PI }
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00426))_

> const statements occur inside blocks, we can't use them when we write a fat arrow that has an expression as its body.
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00428))_


## Source

- [[javascriptallonge]]
