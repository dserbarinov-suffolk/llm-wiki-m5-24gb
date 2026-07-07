---
page_id: javascriptallonge-section-gathering-5b2815df
page_kind: source
summary: gathering: 9 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-gathering-5b2815df@3020064452f761f41f8e6878093241b1
---

# gathering

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-destructuring-arrays-70fdfed7]] - previous source section: destructuring arrays
- [[javascriptallonge-section-destructuring-is-not-pattern-matching-385525f3]] - next source section: destructuring is not pattern matching

## Statements

- Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-c98ab3e6-00833))_
- car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst , or head and tail . We will use a common convention and call variables we gather rest , but refer to the ... operation as a 'gather,' following Kyle Simpson's example. 58 _(javascriptallonge.pdf (source-range-c98ab3e6-00835))_
- Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write _(javascriptallonge.pdf (source-range-c98ab3e6-00836))_
- to place the elements of an array inside another array. _(javascriptallonge.pdf (source-range-c98ab3e6-00840))_

## Technical atoms

### Technical frame 1: gathering

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

### Technical frame 2: gathering

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00833))_

> Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00837))_

<a id="atom-technical-atom-5337ddc45c7cfcfe"></a>
```text
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 57 | https://en.wikipedia.org/wiki/CAR_and_CDR |
| 58 | Kyle Simpson is the author of You Don't Know JS, available here |

</details>
