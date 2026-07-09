---
page_id: javascriptallonge-undefined
page_kind: concept
summary: topic-concept: 14 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_75002af35576692b@2c336af2d74eb61fc87334917b2ae06d
---

# undefined

Source: [[javascriptallonge]]

## Statements

- In JavaScript, the absence of a value is written undefined , and it means there is no value. (javascriptallonge.pdf p.34)
- It will crop up again. (javascriptallonge.pdf p.34)
- Like numbers, booleans and strings, JavaScript can print out the value undefined . (javascriptallonge.pdf p.34)
- No matter how you evaluate undefined , you get an identical value back. (javascriptallonge.pdf p.34)
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. (javascriptallonge.pdf p.34)
- You might think that undefined in JavaScript is equivalent to NULL in SQL. (javascriptallonge.pdf p.35)
- In JavaScript, every undefined is identical to every other undefined . (javascriptallonge.pdf p.35)
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. (javascriptallonge.pdf p.35)

## Rules

- Like numbers, booleans and strings, JavaScript can print out the value undefined . (javascriptallonge.pdf p.34)
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. (javascriptallonge.pdf p.34)
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can't be equal. (javascriptallonge.pdf p.35)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
undefined
```

<a id="atom-2"></a>
**Atom:** code block

```
//=> undefined
```

<a id="atom-3"></a>
**Atom:** code block

```
undefined === undefined
//=> true
(() => {})() === (() => {})()
//=> true
(() => {})() === undefined
//=> true
```
