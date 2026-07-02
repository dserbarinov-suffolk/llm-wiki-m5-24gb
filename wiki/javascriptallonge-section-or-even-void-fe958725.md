---
page_id: javascriptallonge-section-or-even-void-fe958725
page_kind: source
summary: Or even: / void: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-or-even-void-fe958725@50cb5af3992418dab8a096cabe999f1c
---

# Or even: / void

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-or-even-the-simplest-possible-block-fbb6a26c]] - previous source section: Or even: / the simplest possible block
- [[javascriptallonge-section-or-even-back-on-the-block-b65a6ef3]] - next source section: Or even: / back on the block

### Source structure

- [[javascriptallonge-section-or-even-bc497226]] - broader source section: Or even:

## Statements

- void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 . _(javascriptallonge.pdf (source-range-0e12e052-00233))_
- The first form works but it's cumbersome. The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. The third form is guaranteed to always work, so that's what we will use. 20 _(javascriptallonge.pdf (source-range-0e12e052-00234))_

## Technical atoms

### Technical frame 1: Or even: / void

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00233))_

> void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00232))_

<a id="atom-technical-atom-8540685666108da1"></a>
```
void 0
//=> undefined
void 1
//=> undefined
void (2 + 2)
//=> undefined
```
