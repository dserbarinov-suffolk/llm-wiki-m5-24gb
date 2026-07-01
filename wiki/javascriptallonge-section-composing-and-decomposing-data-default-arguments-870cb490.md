---
page_id: javascriptallonge-section-composing-and-decomposing-data-default-arguments-870cb490
page_kind: source
summary: Composing and Decomposing Data / default arguments: 9 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-default-arguments-870cb490@c1e61b74789545b66cb64c9ef5514b47
---

# Composing and Decomposing Data / default arguments

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-58c1e32b]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-factorials-48d5d159]] - previous source section: Composing and Decomposing Data / factorials
- [[javascriptallonge-section-composing-and-decomposing-data-defaults-and-destructuring-cd5ea708]] - next source section: Composing and Decomposing Data / defaults and destructuring

## Statements

- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . _(javascriptallonge.pdf (source-range-0e12e052-00999))_
- By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . We can do similar things with our other tail-recursive functions: _(javascriptallonge.pdf (source-range-0e12e052-01002))_
- Now we don't need to use two functions. A default argument is concise and readable. _(javascriptallonge.pdf (source-range-0e12e052-01004))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / default arguments

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-01002))_

> By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . We can do similar things with our other tail-recursive functions:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-01001))_

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
