---
page_id: javascriptallonge-section-a-rich-aroma-basic-numbers-7443c717
page_kind: source
summary: A Rich Aroma: Basic Numbers: 13 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-rich-aroma-basic-numbers-7443c717@69f7babb2827696c02d30eb8ea0a86bd
---

# A Rich Aroma: Basic Numbers

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-9ed49287]] - previous source section: Prelude: Values and Expressions over Coffee
- [[javascriptallonge-section-the-first-sip-basic-functions-8249ef21]] - next source section: The first sip: Basic Functions

### Source structure

- [[javascriptallonge-section-a-rich-aroma-basic-numbers-floating-1170cd1c]] - narrower source section: A Rich Aroma: Basic Numbers / floating
- [[javascriptallonge-section-a-rich-aroma-basic-numbers-operations-on-numbers-c7608822]] - narrower source section: A Rich Aroma: Basic Numbers / operations on numbers

## Statements

- In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.Wikipedia 12 _(javascriptallonge.pdf (source-range-c98ab3e6-00137))_
- JavaScript, like most languages, has a collection of literals. We saw that an expression consisting solely of numbers, like 42 , is a literal. It represents the number forty-two, which is 42 base 10. Not all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-c98ab3e6-00138))_
- Internally, both 042 and 34 have the same representation, as double-precision floating point 13 numbers. A computer's internal representation for numbers is important to understand. The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.' _(javascriptallonge.pdf (source-range-c98ab3e6-00140))_
- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits. _(javascriptallonge.pdf (source-range-c98ab3e6-00141))_
- Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. _(javascriptallonge.pdf (source-range-c98ab3e6-00137))_
- For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . _(javascriptallonge.pdf (source-range-c98ab3e6-00141))_

## Technical atoms

### Technical frame 1: A Rich Aroma: Basic Numbers / floating

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00151))_

> But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 . Professional programmers almost never use floating point numbers to represent monetary amounts. For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . In this book, we need not think about such details, but outside of this book, we must.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00148))_

<a id="atom-technical-atom-aee77d48a5615cc7"></a>
```text
13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format
14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 13 | http://en.wikipedia.org/wiki/Double-precision_floating-point_format |
| 14 | Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. |

</details>
