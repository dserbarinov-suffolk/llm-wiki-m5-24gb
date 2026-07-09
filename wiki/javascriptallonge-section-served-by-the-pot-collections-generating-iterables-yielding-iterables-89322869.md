---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-yielding-iterables-89322869
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables / yielding iterables: 15 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-yielding-iterables-89322869@cb23273b6a24d37fb4fa058f5ebf0342
---

# Served by the Pot: Collections / Generating Iterables / yielding iterables

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-more-generators-30279cb0]] - previous source section: Served by the Pot: Collections / Generating Iterables / more generators

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-f68c47a5]] - broader source section: Served by the Pot: Collections / Generating Iterables

### Recipes

- [[javascriptallonge-recipe-yielding-iterables]] - recipe pattern: yielding iterables

## Statements

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-c98ab3e6-01701))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. But if you can write it as a simple generator, write it as a simple generator. _(javascriptallonge.pdf (source-range-c98ab3e6-01702))_
- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-c98ab3e6-01705))_
- append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results. _(javascriptallonge.pdf (source-range-c98ab3e6-01710))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-c98ab3e6-01702))_
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable. _(javascriptallonge.pdf (source-range-c98ab3e6-01711))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Generating Iterables / yielding iterables

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

### Technical frame 2: Served by the Pot: Collections / Generating Iterables / yielding iterables

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

### Technical frame 3: Served by the Pot: Collections / Generating Iterables / yielding iterables

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
