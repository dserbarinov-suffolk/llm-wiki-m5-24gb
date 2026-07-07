---
page_id: javascriptallonge-section-recipes-with-data-flip-b1a8ea8d
page_kind: source
summary: Recipes with Data / Flip: 12 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-data-flip-b1a8ea8d@f3ed057e99a5a0befd3b124ce475da3d
---

# Recipes with Data / Flip

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-data-mapwith-202c0d4f]] - previous source section: Recipes with Data / mapWith
- [[javascriptallonge-section-recipes-with-data-object-assign-8d8e0e13]] - next source section: Recipes with Data / Object.assign

### Source structure

- [[javascriptallonge-section-recipes-with-data-4b3e2c99]] - broader source section: Recipes with Data
- [[javascriptallonge-section-recipes-with-data-flip-flipping-methods-852e9417]] - narrower source section: Recipes with Data / Flip / flipping methods
- [[javascriptallonge-section-recipes-with-data-flip-self-currying-flip-2cc96222]] - narrower source section: Recipes with Data / Flip / self-currying flip

## Statements

- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry : _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_
- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_

## Technical atoms

### Technical frame 1: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01436))_

<a id="atom-technical-atom-890a831292ffdfc1"></a>
```text
84 https://github.com/raganwald/allong.es
85 http://underscorejs.org
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 84 | https://github.com/raganwald/allong.es |
| 85 | http://underscorejs.org |

</details>

### Technical frame 2: Recipes with Data / Flip

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_

> What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry :

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01437))_

<a id="atom-technical-atom-da5a0e5d6c0212ea"></a>
```
const flipAndCurry = (fn) =>
(first) => (second) => fn(second, first);
Sometimes you want to flip, but not curry:
const flip = (fn) =>
(first, second) => fn(second, first);
This is gold. Consider how we define mapWith now:
var mapWith = flipAndCurry(map);
Much nicer!
```
