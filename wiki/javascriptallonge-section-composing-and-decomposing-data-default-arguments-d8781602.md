---
page_id: javascriptallonge-section-composing-and-decomposing-data-default-arguments-d8781602
page_kind: source
summary: Composing and Decomposing Data / default arguments: 9 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-default-arguments-d8781602@d32f149ef3fb23900459ab525ab81fe6
---

# Composing and Decomposing Data / default arguments

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-composing-and-decomposing-data-factorials-f9cc315b]] - previous source section: Composing and Decomposing Data / factorials
- [[javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-3d9ba8f9]] - next source section: Composing and Decomposing Data / defaults and destructuring

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-d80dc70f]] - broader source section: Composing and Decomposing Data

## Statements

- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . _(javascriptallonge.pdf (source-range-c98ab3e6-00999))_
- By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . We can do similar things with our other tail-recursive functions: _(javascriptallonge.pdf (source-range-c98ab3e6-01002))_
- Now we don't need to use two functions. A default argument is concise and readable. _(javascriptallonge.pdf (source-range-c98ab3e6-01004))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / default arguments

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-01002))_

> By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . We can do similar things with our other tail-recursive functions:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-01001))_

<a id="atom-technical-atom-68080487c6d3c933"></a>
```
const factorial = (n, work = 1) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1)
//=> 1
factorial(6)
//=> 720
```
