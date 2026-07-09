---
page_id: javascriptallonge-pure
page_kind: concept
summary: Pure: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-pure@3978d13e214c9589a03e2334d3774796
---

# Pure

What [[javascriptallonge]] covers about pure:

## Statements

### if functions without free variables are pure, are closures impure?

- Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: _(javascriptallonge.pdf (source-range-c98ab3e6-00333))_

- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-c98ab3e6-00335))_

- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . _(javascriptallonge.pdf (source-range-c98ab3e6-00337))_

### which came first, the chicken or the egg?

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-c98ab3e6-00363))_


## Related pages

### Source structure

- [[javascriptallonge-section-if-functions-without-free-variables-are-pure-are-closures-impure-a8b1b370]] - source section: if functions without free variables are pure, are closures impure?

## Source

- [[javascriptallonge]]
