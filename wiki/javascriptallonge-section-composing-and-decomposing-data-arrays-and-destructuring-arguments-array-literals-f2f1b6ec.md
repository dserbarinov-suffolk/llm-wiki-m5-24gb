---
page_id: javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-array-literals-f2f1b6ec
page_kind: source
summary: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: 12 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-array-literals-f2f1b6ec@89d591fd1200bc55d65e716c7a9993b4
---

# Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-75756e27]] - next source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-2a38bfc8]] - broader source section: Composing and Decomposing Data / Arrays and Destructuring Arguments

### Recipes

- [[javascriptallonge-recipe-array-literals]] - recipe pattern: array literals

## Statements

- JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: _(javascriptallonge.pdf (source-range-c98ab3e6-00800))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-c98ab3e6-00808))_
- Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-c98ab3e6-00811))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-c98ab3e6-00808))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00808))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00801))_

<a id="atom-technical-atom-abf332c98aac0fdf"></a>
```
[]
//=> []
```

### Technical frame 2: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00811))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00812))_

<a id="atom-technical-atom-7deb364f150a5072"></a>
```
[] === []
//=> false
[2 + 2] === [2 + 2]
//=> false
const array_of_one = () => [1];
array_of_one() === array_of_one()
//=> false
```
