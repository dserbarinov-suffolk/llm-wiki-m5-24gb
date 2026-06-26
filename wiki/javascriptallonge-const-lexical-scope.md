---
page_id: javascriptallonge-const-lexical-scope
page_kind: concept
summary: const and lexical scope: 55 statement(s) and 345 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-26
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-const-lexical-scope@b3087dfa4e89ede5c245ea7ec08040df
---

# const and lexical scope

What [[javascriptallonge]] covers about const and lexical scope:

## Statements

- And i is scoped to the for loop. _(javascriptallonge.pdf (source-range-8eb13d6b-00034))_
- However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-8eb13d6b-01213))_
- But const statements can appear inside blocks. _(javascriptallonge.pdf (source-range-8eb13d6b-00486))_
- We use the const keyword in a const statement . _(javascriptallonge.pdf (source-range-8eb13d6b-00428))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-8eb13d6b-00425))_
- Scopes are nested and free variable references closed over. _(javascriptallonge.pdf (source-range-8eb13d6b-00663))_
- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-8eb13d6b-00662))_
- And the variable i is scoped locally to the code within the braces. _(javascriptallonge.pdf (source-range-8eb13d6b-00023))_
- JavaScript uses const to bind values to names within block scope. _(javascriptallonge.pdf (source-range-8eb13d6b-00659))_
- There's no benefit to constant space if finite space is sufficient. _(javascriptallonge.pdf (source-range-8eb13d6b-01875))_
- The x in the great-great-grandparent scope is ignored, as are both w s. _(javascriptallonge.pdf (source-range-8eb13d6b-00380))_
- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-8eb13d6b-01028))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. _(javascriptallonge.pdf (source-range-8eb13d6b-01760))_
- JavaScript does not permit us to rebind a name that has been bound with const . _(javascriptallonge.pdf (source-range-8eb13d6b-00501))_

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
