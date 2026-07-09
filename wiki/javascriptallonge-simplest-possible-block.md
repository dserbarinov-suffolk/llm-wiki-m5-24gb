---
page_id: javascriptallonge-simplest-possible-block
page_kind: concept
summary: the simplest possible block: 2 accepted assertion(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_43a5fd19bc0e93a3@1b7d8e90e9f78cb50267e6ecb05cfea2
---

# the simplest possible block

Source: [[javascriptallonge]]

## Statements

- There's another thing we can put to the right of an arrow, a block . (javascriptallonge.pdf p.34)
- It returns the result of evaluating a block that has no statements. (javascriptallonge.pdf p.34)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
() => {}
```

<a id="atom-2"></a>
**Atom:** code block

```
(() => {})()
//=> undefined
```
