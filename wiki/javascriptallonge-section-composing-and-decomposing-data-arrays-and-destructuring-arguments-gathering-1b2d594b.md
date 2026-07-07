---
page_id: javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-1b2d594b
page_kind: source
summary: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering: 6 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-1b2d594b@c3050c20613293e53cdb9b62b515f950
---

# Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-arrays-327f6ba9]] - previous source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-27d4b226]] - next source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-2a38bfc8]] - broader source section: Composing and Decomposing Data / Arrays and Destructuring Arguments

### Recipes

- [[javascriptallonge-recipe-gathering]] - recipe pattern: gathering

## Statements

- Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-c98ab3e6-00833))_
- car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst , or head and tail . We will use a common convention and call variables we gather rest , but refer to the ... operation as a 'gather,' following Kyle Simpson's example. 58 _(javascriptallonge.pdf (source-range-c98ab3e6-00835))_
- Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write _(javascriptallonge.pdf (source-range-c98ab3e6-00836))_
- to place the elements of an array inside another array. _(javascriptallonge.pdf (source-range-c98ab3e6-00840))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00835))_

> car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst , or head and tail . We will use a common convention and call variables we gather rest , but refer to the ... operation as a 'gather,' following Kyle Simpson's example. 58

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00834))_

<a id="atom-technical-atom-4f82e17fd807ef21"></a>
```
const [car, ...cdr] = [1, 2, 3, 4, 5];
car
//=> 1
cdr
//=> [2, 3, 4, 5]
```
