---
page_id: javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-and-iterables-adba5c82
page_kind: source
summary: Served by the Pot: Collections / Generating Iterables / generators and iterables: 11 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-and-iterables-adba5c82@8d5e1840fe61b8052b9282b89d25b972
---

# Served by the Pot: Collections / Generating Iterables / generators and iterables

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-generators-are-coroutines-d0fde127]] - previous source section: Served by the Pot: Collections / Generating Iterables / generators are coroutines
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-more-generators-30279cb0]] - next source section: Served by the Pot: Collections / Generating Iterables / more generators

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-f68c47a5]] - broader source section: Served by the Pot: Collections / Generating Iterables

### Recipes

- [[javascriptallonge-recipe-generators-and-iterables]] - recipe pattern: generators and iterables

## Statements

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-c98ab3e6-01678))_
- If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-c98ab3e6-01679))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-c98ab3e6-01682))_
- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_
- Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / Generating Iterables / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01684))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01683))_

<a id="atom-technical-atom-54530c82c657b597"></a>
```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```
