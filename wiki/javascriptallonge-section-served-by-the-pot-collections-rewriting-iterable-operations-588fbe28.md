---
page_id: javascriptallonge-section-served-by-the-pot-collections-rewriting-iterable-operations-588fbe28
page_kind: source
summary: Served by the Pot: Collections / rewriting iterable operations: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-rewriting-iterable-operations-588fbe28@011d53ee60c69943a0d76e4cc2483106
---

# Served by the Pot: Collections / rewriting iterable operations

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-served-by-the-pot-collections-14399de3]] - broader source section: Served by the Pot: Collections
- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-8c929c4d]] - previous source section: Served by the Pot: Collections / Generating Iterables
- [[javascriptallonge-section-served-by-the-pot-collections-summary-bda1f2d6]] - next source section: Served by the Pot: Collections / Summary

## Statements

- Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of: _(javascriptallonge.pdf (source-range-0e12e052-01744))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done. _(javascriptallonge.pdf (source-range-0e12e052-01748))_
- We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators: _(javascriptallonge.pdf (source-range-0e12e052-01749))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-0e12e052-01752))_

## Technical atoms

### Technical frame 1: Served by the Pot: Collections / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01748))_

> No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done.

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01745))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01752))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01750))_

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

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01752))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01751))_

```
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
```
