---
page_id: javascriptallonge-pure
page_kind: concept
summary: Pure: 4 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-pure@374f6e9ba7df33d57bdb4d49d04f29f5
---

# Pure

What [[javascriptallonge]] covers about pure:

## Statements

### And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

- Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: _(javascriptallonge.pdf (source-range-0e12e052-00342))_

- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-0e12e052-00344))_

- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . _(javascriptallonge.pdf (source-range-0e12e052-00347))_

### And also: / Closures and Scope / which came first, the chicken or the egg?

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-0e12e052-00373))_


## Technical atoms

### Technical frame 1: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00347))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00346))_

> If pure functions can contain closures, can a closure contain a pure function?


## Related pages

- [[javascriptallonge-closure]] - shared statements and technical atoms: Closure shares source evidence from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: From this, we learn something: A pure function can contain a closure.; Closure shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-scope]] - shared technical atoms: Scope shares technical record from And also: / Closures and Scope / if functions without free variables are pure, are closures impure?: If pure functions can contain closures, can a closure contain a pure function? (1 shared atom(s))

## Source

- [[javascriptallonge]]
