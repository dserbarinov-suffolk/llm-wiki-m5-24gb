---
page_id: javascriptallonge-section-left-variadic-destructuring-5db72b5e
page_kind: source
summary: left-variadic destructuring: 7 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-left-variadic-destructuring-5db72b5e@c53abc729e055d5105555af8a55ad76a
---

# left-variadic destructuring

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-overcoming-limitations-b5da4c36]] - previous source section: overcoming limitations
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d2a76f30]] - next source section: Picking the Bean: Choice and Truthiness

## Statements

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00724))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-c98ab3e6-00730))_
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00732))_

## Technical atoms

### Technical frame 1: left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00730))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00727))_

<a id="atom-technical-atom-258d1986600602c2"></a>
```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```
