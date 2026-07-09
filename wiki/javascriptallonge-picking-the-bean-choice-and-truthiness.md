---
page_id: javascriptallonge-picking-the-bean-choice-and-truthiness
page_kind: concept
summary: topic-concept: 6 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_44f5f9aafe7d6465@4ab27afa8bebf269ec091be407bdc9df
---

# Picking the Bean: Choice and Truthiness

Source: [[javascriptallonge]]

## Statements

- In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. (javascriptallonge.pdf p.94)
- true and false are value types. (javascriptallonge.pdf p.94)
- All values of true are === all other values of true. (javascriptallonge.pdf p.94)
- Now, note well: We have said what happens if you pass boolean values to !. (javascriptallonge.pdf p.95)

## Technical atoms

<a id="atom-1"></a>
**Atom:** code block

```
!true
//=> false
!false
//=> true
```

<a id="atom-2"></a>
**Atom:** code block

```
false && false //=> false
false && true
//=> false
true
&& false //=> false
true
&& true
//=> true
false || false //=> false
false || true
//=> true
true
|| false //=> true
true
|| true
//=> true
```
