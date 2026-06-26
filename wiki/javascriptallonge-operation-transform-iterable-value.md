---
page_id: javascriptallonge-operation-transform-iterable-value
page_kind: concept
summary: operations that transform an iterable into a value: 134 statement(s) and 174 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-26
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-operation-transform-iterable-value@eacac087872df5c6f1baa724de66646e
---

# operations that transform an iterable into a value

What [[javascriptallonge]] covers about operations that transform an iterable into a value:

## Statements

- Ground coffee is a value. _(javascriptallonge.pdf (source-range-8eb13d6b-00116))_
- All values are expressions. _(javascriptallonge.pdf (source-range-8eb13d6b-00108))_
- All values are expressions. _(javascriptallonge.pdf (source-range-8eb13d6b-00114))_
- 11 Boiling water is a value. _(javascriptallonge.pdf (source-range-8eb13d6b-00116))_
- true and false are value types. _(javascriptallonge.pdf (source-range-8eb13d6b-00771))_
- Functions are reference values . _(javascriptallonge.pdf (source-range-8eb13d6b-00651))_
- If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-8eb13d6b-01742))_
- This is especially useful for making iterables. _(javascriptallonge.pdf (source-range-8eb13d6b-01768))_
- Iterables needn't represent ordered collections. _(javascriptallonge.pdf (source-range-8eb13d6b-01591))_
- So now we have a value representing that function. _(javascriptallonge.pdf (source-range-8eb13d6b-00342))_
- Here are the operations we've defined on Iterables. _(javascriptallonge.pdf (source-range-8eb13d6b-01939))_
- All values of true are === all other values of true. _(javascriptallonge.pdf (source-range-8eb13d6b-00771))_
- It presumes there is one canonical empty list value. _(javascriptallonge.pdf (source-range-8eb13d6b-01431))_
- The answer is, this is both an expression and a value. _(javascriptallonge.pdf (source-range-8eb13d6b-00112))_

## Code, rules, and examples

```
const mapWith = (iterable, fn) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { yield fn(element); } } });
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00055))_

```
const filterWith = (fn, iterable) => ({ [Symbol.iterator]: function * () { for ( let element of iterable) { if (!!fn(element)) yield element; } } });
```
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00057))_

> Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista).
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00108))_

> 11 In some languages, expressions are a kind of value unto themselves and can be manipulated.
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00120))_

> Nowwesee that 'strings' are values, and you can make an expression out of strings and an operator + .
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00121))_

> Nowwesee that 'strings' are values, and you can make an expression out of strings and an operator + . Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our 'coffee grounds plus hot water' example. The coffee grounds were a value, the boiling hot water was a value, and the 'plus' operator between them made the whole thing an expression that was not a value.
_(source: javascriptallonge.pdf (source-range-8eb13d6b-00121))_


## Source

- [[javascriptallonge]]
