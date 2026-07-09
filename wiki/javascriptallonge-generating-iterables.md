---
page_id: javascriptallonge-generating-iterables
page_kind: concept
summary: Generating Iterables: 8 accepted assertion(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_b2ef6728ef0cd7cf@75ae0603b3611cba27df5bec939b3748
---

# Generating Iterables

Source: [[javascriptallonge]]

## Statements

- Iterables look cool, but then again, everything looks amazing when you're given cherry- picked examples. (javascriptallonge.pdf p.224)
- Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. (javascriptallonge.pdf p.224)
- This seems blindingly obvious and simple. (javascriptallonge.pdf p.224)
- There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers. (javascriptallonge.pdf p.225)
- Of course, when we have some code that makes a bunch of something, we don't usually write it like that. (javascriptallonge.pdf p.225)
- And magically, the numbers would pour forth. (javascriptallonge.pdf p.225)
- We would generate numbers. (javascriptallonge.pdf p.225)
- Well, there are some collections that are much easier to generate than to iterate over. (javascriptallonge.pdf p.226)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
Iterators have to arrange its own state such that when you call them, they compute and return the next item.
```

<a id="atom-2"></a>
**Atom:** code block

```
const Numbers = {
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
};
```

<a id="atom-3"></a>
**Atom:** code block

```
let n = 0;
while (true) {
console.log(n++)
}
```

<a id="atom-4"></a>
**Atom:** code block

```
// Iteration
let n = 0;
() =>
({done: false, value: n++})
// Generation
let n = 0;
while (true) {
console.log(n++)
}
```
