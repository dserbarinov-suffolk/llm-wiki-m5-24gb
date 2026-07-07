---
page_id: javascriptallonge-section-yielding-iterables-117bbefd
page_kind: source
summary: yielding iterables: 17 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yielding-iterables-117bbefd@215e53c810ad58489b1f4fb8922069a2
---

# yielding iterables

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-more-generators-8710183f]] - previous source section: more generators
- [[javascriptallonge-section-rewriting-iterable-operations-af476334]] - next source section: rewriting iterable operations

## Statements

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-c98ab3e6-01701))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. But if you can write it as a simple generator, write it as a simple generator. _(javascriptallonge.pdf (source-range-c98ab3e6-01702))_
- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-c98ab3e6-01705))_
- append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results. _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-c98ab3e6-01702))_
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable. _(javascriptallonge.pdf (source-range-c98ab3e6-01711))_

## Technical atoms

### Technical frame 1: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_

> append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01712))_

<a id="atom-technical-atom-d77f5e63d004d0aa"></a>
```
function * append (...iterables) {
for (const iterable of iterables) {
yield * iterable;
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
```

### Technical frame 2: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_

> append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01713))_

<a id="atom-technical-atom-4f414c5b2051fa87"></a>
```
//=>
a
b
c
one
two
thre
do
re
```

### Technical frame 3: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_

> append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01714))_

<a id="atom-technical-atom-61b4cb84b60ebc91"></a>
```
const isIterable = (something) =>
!!something[Symbol.iterator];
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
yield * tree(e);
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 4: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_

> append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01716))_

<a id="atom-technical-atom-973b2255b0347893"></a>
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

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 5 | yield* is handy when writing generator functions that operate on or create iterables. rewriting iterable operations Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of: |
| 221 | Served by the Pot: Collections const mapWith = (fn, iterable) => [Symbol.iterator]: () => { const iterator = iterable[Symbol.iterator](); return { next: () => { const {done, value} = iterator.next(); return ({done, value: done? undefined: fn(value)}); We can write: function * mapWith (fn, iterable) { for (const element of iterable) { yield fn(element); No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a.next() method. No need to fool around with {done} or {value}, just yield values until we’re done. We can do the same thing with our other operations like filterWith and untilWith. Here’re our iterable methods rewritten as generators: function * mapWith(fn, iterable) { for (const element of iterable) { yield fn(element); function * filterWith (fn, iterable) { for (const element of iterable) { if (!!fn(element)) yield element; |
| 222 | Served by the Pot: Collections function * untilWith (fn, iterable) { for (const element of iterable) { if (fn(element)) break; yield fn(element); first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: const first = (iterable) => iterable[Symbol.iterator]().next().value; function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next(); yield * iterator; |

</details>
