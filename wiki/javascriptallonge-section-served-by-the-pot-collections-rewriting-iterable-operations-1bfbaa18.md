---
page_id: javascriptallonge-section-served-by-the-pot-collections-rewriting-iterable-operations-1bfbaa18
page_kind: source
summary: Served by the Pot: Collections / rewriting iterable operations: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-rewriting-iterable-operations-1bfbaa18@0110a733676d27ccffa586e3e7dabf52
---

# Served by the Pot: Collections / rewriting iterable operations

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-ae881401]] - previous source section: Served by the Pot: Collections / Generating Iterables
- [[javascriptallonge-section-served-by-the-pot-collections-summary-864be0e2]] - next source section: Served by the Pot: Collections / Summary

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-a69ff5a5]] - broader source section: Served by the Pot: Collections

## Statements

- Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of: _(javascriptallonge.pdf (source-range-c98ab3e6-01744))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done. _(javascriptallonge.pdf (source-range-c98ab3e6-01748))_
- We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators: _(javascriptallonge.pdf (source-range-c98ab3e6-01749))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-c98ab3e6-01752))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01748))_

> No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01745))_

<a id="atom-technical-atom-891e48b6a92cbb03"></a>
```
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
```

### Technical frame 2: Served by the Pot: Collections / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01752))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01750))_

<a id="atom-technical-atom-82c7ac5e8c83a303"></a>
```
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
```

### Technical frame 3: Served by the Pot: Collections / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01752))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01751))_

<a id="atom-technical-atom-b2df1dd8afbd6931"></a>
```
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
```
