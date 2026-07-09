---
page_id: javascriptallonge-yielding-iterables
page_kind: concept
summary: topic-concept: 9 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_f0b0e2f96119b05d@ccb61b574f952acb8aefcfc74447daaf
---

# yielding iterables

Source: [[javascriptallonge]]

## Procedure

- It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93. (javascriptallonge.pdf p.240)
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. (javascriptallonge.pdf p.240)
- If e is not an iterable, yield e . (javascriptallonge.pdf p.241)
- Wetake advantage of the for..of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. (javascriptallonge.pdf p.241)
- Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results. (javascriptallonge.pdf p.242)

## Required tables and formulas

<a id="atom-1"></a>
**Atom:** table

```text
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
yield* is handy when writing generator functions that operate on or create iterables.
rewriting iterable operations
Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of:
Served by the Pot: Collections
221
const mapWith = (fn, iterable) =>
({
[Symbol.iterator]: () => {
const iterator = iterable[Symbol.iterator]();
return {
next: () => {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
We can write:
function * mapWith (fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return
an object with a .next() method. No need to fool around with {done} or {value}, just yield values
until we’re done.
We can do the same thing with our other operations like filterWith and untilWith. Here’re our
iterable methods rewritten as generators:
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
Served by the Pot: Collections
222
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```


## Rules and exceptions

- It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93. (javascriptallonge.pdf p.240)
- Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results. (javascriptallonge.pdf p.242)

## Related pages

- [[javascriptallonge-more-generators]] - contextualizes: source-supported topic dependency
