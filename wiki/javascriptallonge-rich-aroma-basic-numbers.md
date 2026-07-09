---
page_id: javascriptallonge-rich-aroma-basic-numbers
page_kind: concept
summary: topic-concept: 12 supported fragment(s) and 0 related link(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: page-projection-pgp_c8621afad6764e3d@f2cd548e33dca440bd4e910a8eb7d502
---

# A Rich Aroma: Basic Numbers

Source: [[javascriptallonge]]

## Statements

- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. (javascriptallonge.pdf p.24)
- In computer science, a literal is a notation for representing a fixed value in source code. (javascriptallonge.pdf p.24)
- We saw that an expression consisting solely of numbers, like 42 , is a literal. (javascriptallonge.pdf p.24-25)
- Not all numbers are base ten. (javascriptallonge.pdf p.24-25)
- If we start a literal with a zero, it is an octal literal. (javascriptallonge.pdf p.24-25)
- It represents the number forty-two, which is 42 base 10. (javascriptallonge.pdf p.24-25)
- So the literal 042 is 42 base 8, which is actually 34 base 10. (javascriptallonge.pdf p.24-25)
- A computer's internal representation for numbers is important to understand. (javascriptallonge.pdf p.25)
- Internally, both 042 and 34 have the same representation, as double-precision floating point 13 numbers. (javascriptallonge.pdf p.25)
- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . (javascriptallonge.pdf p.25)

## Rules

- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . (javascriptallonge.pdf p.25)

## Technical atoms

<a id="atom-1"></a>
**Atom:** rule

```
The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.'
```
