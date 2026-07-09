---
page_id: javascriptallonge-rewriting-iterable-operations
page_kind: concept
summary: topic-concept: 14 supported fragment(s) and 1 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_ff9c58cd44d565ad@32b5e3f3cb74d8c51c313ca6adbde165
---

# rewriting iterable operations

Source: [[javascriptallonge]]

## Statements

- Now that we know about iterables, we can rewrite our iterable operations as generators. (javascriptallonge.pdf p.243)
- No need to explicitly construct an object that has a [Symbol.iterator] method. (javascriptallonge.pdf p.244)
- No need to return an object with a .next() method. (javascriptallonge.pdf p.244)
- We can do the same thing with our other operations like filterWith and untilWith . (javascriptallonge.pdf p.244)
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:. (javascriptallonge.pdf p.245)

## Rules

- Now that we know about iterables, we can rewrite our iterable operations as generators. (javascriptallonge.pdf p.243)
- We can do the same thing with our other operations like filterWith and untilWith . (javascriptallonge.pdf p.244)
- first works directly with iterators and remains unchanged, but rest can be rewritten as a generator:. (javascriptallonge.pdf p.245)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

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

<a id="atom-2"></a>
**Atom:** code block

```
function * mapWith (fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
```

<a id="atom-3"></a>
**Atom:** code block

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

<a id="atom-4"></a>
**Atom:** code block

```
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
```

<a id="atom-5"></a>
**Atom:** code block

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```


## Related pages

- [[javascriptallonge-generating-iterables]] - contextualizes: source-supported topic dependency
