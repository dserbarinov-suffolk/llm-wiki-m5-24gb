---
page_id: javascriptallonge-section-copy-on-write-d081f846
page_kind: source
summary: Copy on Write: 11 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-d081f846@82c2d7434f31f745bf8cc97288384dba
---

# Copy on Write

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-yes-consider-this-variation-af64fdfd]] - previous source section: Yes. Consider this variation:
- [[javascriptallonge-section-recipes-with-data-4b3e2c99]] - next source section: Recipes with Data

### Source structure

- [[javascriptallonge-section-copy-on-write-a-few-utilities-7b82367a]] - narrower source section: Copy on Write / a few utilities
- [[javascriptallonge-section-copy-on-write-functional-iterators-74724e0a]] - narrower source section: Copy on Write / Functional Iterators
- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-182a6c8b]] - narrower source section: Copy on Write / Making Data Out Of Functions
- [[javascriptallonge-section-copy-on-write-tortoises-hares-and-teleporting-turtles-3a4746f2]] - narrower source section: Copy on Write / Tortoises, Hares, and Teleporting Turtles

### Topics

- [[javascriptallonge-copy-write]] - topic hub: opens the topic page for Copy Write

## Statements

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-c98ab3e6-01200))_
- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-c98ab3e6-01201))_
- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-c98ab3e6-01202))_
- The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-c98ab3e6-01203))_
- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01207))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-c98ab3e6-01203))_
- And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent. _(javascriptallonge.pdf (source-range-c98ab3e6-01204))_

## Technical atoms

### Technical frame 1: Copy on Write / Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01305))_

> They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. We can model lists just using functions.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01309))_

<a id="atom-technical-atom-268f5812c47797c2"></a>
```text
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

</details>

### Technical frame 2: Copy on Write / Making Data Out Of Functions / functions are not the real point

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01379))_

> Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons 81 of the electromagnetic force. It's the QED of physics that underpins the Maxwell's Equations of programming. Deeply important, but not practical when you're building a bridge.

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01380))_

<a id="atom-technical-atom-f2ed9b6962a2b6bc"></a>
```text
79 https://en.wikipedia.org/wiki/Church_encoding
81 https://en.wikipedia.org/wiki/Gauge_boson
80 https://en.wikipedia.org/wiki/Surreal_number
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 79 | https://en.wikipedia.org/wiki/Church_encoding |
| 81 | https://en.wikipedia.org/wiki/Gauge_boson |
| 80 | https://en.wikipedia.org/wiki/Surreal_number |

</details>
