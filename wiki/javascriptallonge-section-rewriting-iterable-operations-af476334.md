---
page_id: javascriptallonge-section-rewriting-iterable-operations-af476334
page_kind: source
summary: rewriting iterable operations: 10 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-rewriting-iterable-operations-af476334@6dcab9b14cbae84b74a8e04676e4b22f
---

# rewriting iterable operations

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-yielding-iterables-117bbefd]] - previous source section: yielding iterables
- [[javascriptallonge-section-summary-551391b0]] - next source section: Summary

## Statements

- Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of: _(javascriptallonge.pdf (source-range-c98ab3e6-01718))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done. _(javascriptallonge.pdf (source-range-c98ab3e6-01722))_
- We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators: _(javascriptallonge.pdf (source-range-c98ab3e6-01723))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-c98ab3e6-01726))_

## Technical atoms

### Technical frame 1: rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01722))_

> No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01719))_

<a id="atom-technical-atom-25d3587ef9f9a48b"></a>
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

### Technical frame 2: rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01726))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01724))_

<a id="atom-technical-atom-8baf6cf9e1639464"></a>
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

### Technical frame 3: rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01726))_

> first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01725))_

<a id="atom-technical-atom-59ca762afc40d860"></a>
```
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
```
