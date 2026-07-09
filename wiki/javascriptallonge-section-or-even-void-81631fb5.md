---
page_id: javascriptallonge-section-or-even-void-81631fb5
page_kind: source
summary: Or even: / void: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-or-even-void-81631fb5@ba16d84f6bcaa4f063ce9d9f6768540a
---

# Or even: / void

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-or-even-the-simplest-possible-block-e2f3f94d]] - previous source section: Or even: / the simplest possible block
- [[javascriptallonge-section-or-even-back-on-the-block-ffc7c96a]] - next source section: Or even: / back on the block

### Recipes

- [[javascriptallonge-recipe-void]] - recipe pattern: void

## Statements

- By writing undefined ourselves. _(javascriptallonge.pdf (source-range-c98ab3e6-00222))_
- void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 . _(javascriptallonge.pdf (source-range-c98ab3e6-00225))_
- The first form works but it's cumbersome. The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we'll discuss in Reassignment and Mutation. The third form is guaranteed to always work, so that's what we will use. 20 _(javascriptallonge.pdf (source-range-c98ab3e6-00226))_

## Technical atoms

### Technical frame 1: Or even: / void

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
