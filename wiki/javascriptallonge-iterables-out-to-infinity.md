---
page_id: javascriptallonge-iterables-out-to-infinity
page_kind: concept
summary: iterables out to infinity: 2 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_ea948b61577ad335@9c3324735ca863395d473e0957929974
---

# iterables out to infinity

Source: [[javascriptallonge]]

## Statements

- There are useful things we can do with iterables representing an infinitely large collection. (javascriptallonge.pdf p.215)
- Attempting to spread an infinite iterable into an array is always going to fail. (javascriptallonge.pdf p.216)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
const Numbers = {
[Symbol.iterator] () {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}
```

<a id="atom-2"></a>
**Atom:** code block

```
['all the numbers', ...Numbers]
//=> infinite loop!
firstAndSecondElement(...Numbers)
//=> infinite loop!
```
