---
page_id: javascriptallonge-recipe-rewriting-iterable-operations
page_kind: recipe
summary: rewriting iterable operations: reusable source-backed pattern with 5 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
page_family: recipe-pattern
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: rewriting-iterable-operations
projection_coverage: recipe-javascriptallonge-recipe-rewriting-iterable-operations@a07fb0e2f247fabed834bba171347e0f
---

# rewriting iterable operations

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-served-by-the-pot-collections-rewriting-iterable-operations-588fbe28]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- Now that we know about iterables, we can rewrite our iterable operations as generators. _(javascriptallonge.pdf (source-range-0e12e052-01744))_
- No need to return an object with a .next() method. _(javascriptallonge.pdf (source-range-0e12e052-01748))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. _(javascriptallonge.pdf (source-range-0e12e052-01748))_
- We can do the same thing with our other operations like filterWith and untilWith . _(javascriptallonge.pdf (source-range-0e12e052-01749))_
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: _(javascriptallonge.pdf (source-range-0e12e052-01752))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01745)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01747)_

```
function * mapWith (fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01750)_

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

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01751)_

```
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-0e12e052-01753)_

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-served-by-the-pot-collections-rewriting-iterable-operations-588fbe28]]
