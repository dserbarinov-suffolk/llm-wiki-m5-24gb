---
page_id: javascriptallonge-section-void-c67a822d
page_kind: source
summary: void: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-void-c67a822d@3c06bf624ea931f3600850d079d3e212
---

# void

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-undefined-9b5a2e81]] - previous source section: undefined
- [[javascriptallonge-section-back-on-the-block-e8c3dec9]] - next source section: back on the block

## Statements

- By writing undefined ourselves. _(javascriptallonge.pdf (source-range-c98ab3e6-00222))_
- void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 . _(javascriptallonge.pdf (source-range-c98ab3e6-00225))_
- The first form works but it's cumbersome. The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. The third form is guaranteed to always work, so that's what we will use. 20 _(javascriptallonge.pdf (source-range-c98ab3e6-00226))_

## Technical atoms

### Technical frame 1: void

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00225))_

> void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 .

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00224))_

<a id="atom-technical-atom-8b727b2a2eab1b6a"></a>
```
void 0
//=> undefined
void 1
//=> undefined
void (2 + 2)
//=> undefined
```
