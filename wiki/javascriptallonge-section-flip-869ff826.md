---
page_id: javascriptallonge-section-flip-869ff826
page_kind: source
summary: Flip: 12 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-flip-869ff826@841d89703d2eb5f300cd0c004c440548
---

# Flip

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-mapwith-6b5ac121]] - previous source section: mapWith
- [[javascriptallonge-section-self-currying-flip-afc1011e]] - next source section: self-currying flip

## Statements

- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. So let's call it flipAndCurry : _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_
- What we have now is a function that takes a function and 'flips' the order of arguments around, then curries it. _(javascriptallonge.pdf (source-range-c98ab3e6-01435))_

## Technical atoms

### Technical frame 1: Flip

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

### Technical frame 2: Flip

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
