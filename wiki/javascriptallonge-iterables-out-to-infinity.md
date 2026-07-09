---
page_id: javascriptallonge-iterables-out-to-infinity
page_kind: concept
summary: topic-concept: 7 supported fragment(s) and 2 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_1361023c7abb6d47@5e1b4667aff54fa9d5d9a020b06b16a5
---

# iterables out to infinity

Source: [[javascriptallonge]]

## Statements

- There are useful things we can do with iterables representing an infinitely large collection. (javascriptallonge.pdf p.215)
- Attempting to spread an infinite iterable into an array is always going to fail. (javascriptallonge.pdf p.216)

## Rules

- There are useful things we can do with iterables representing an infinitely large collection. (javascriptallonge.pdf p.215)

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


## Related pages

- [[javascriptallonge-iterable]] - contextualizes: source-supported topic dependency
- [[javascriptallonge-ordered-collections]] - contextualizes: source-supported topic dependency
