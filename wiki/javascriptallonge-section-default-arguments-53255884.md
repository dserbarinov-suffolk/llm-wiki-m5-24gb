---
page_id: javascriptallonge-section-default-arguments-53255884
page_kind: source
summary: default arguments: 9 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-default-arguments-53255884@155b5a9189ea6d5dbbc4fc83e3a33f24
---

# default arguments

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-factorials-92a030b5]] - previous source section: factorials
- [[javascriptallonge-section-defaults-and-destructuring-ba72f0fa]] - next source section: defaults and destructuring

## Statements

- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . _(javascriptallonge.pdf (source-range-c98ab3e6-00985))_
- By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . We can do similar things with our other tail-recursive functions: _(javascriptallonge.pdf (source-range-c98ab3e6-00988))_
- Now we don't need to use two functions. A default argument is concise and readable. _(javascriptallonge.pdf (source-range-c98ab3e6-00990))_

## Technical atoms

### Technical frame 1: default arguments

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00988))_

> By writing our parameter list as (n, work = 1) => , we're stating that if a second parameter is not provided, work is to be bound to 1 . We can do similar things with our other tail-recursive functions:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00987))_

<a id="atom-technical-atom-241cc7d206541ba4"></a>
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
