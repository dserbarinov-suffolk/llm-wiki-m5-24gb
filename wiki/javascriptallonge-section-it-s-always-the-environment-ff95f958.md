---
page_id: javascriptallonge-section-it-s-always-the-environment-ff95f958
page_kind: source
summary: it's always the environment: 20 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-it-s-always-the-environment-ff95f958@7a6a506e337f14102eb4ddd8346d5402
---

# it's always the environment

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-if-functions-without-free-variables-are-pure-are-closures-impure-a8b1b370]] - previous source section: if functions without free variables are pure, are closures impure?
- [[javascriptallonge-section-shadowy-variables-from-a-shadowy-planet-ad7f51cc]] - next source section: shadowy variables from a shadowy planet

### Recipes

- [[javascriptallonge-recipe-it-s-always-the-environment]] - recipe pattern: it's always the environment

## Statements

- To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ? Let's fill in the blanks! _(javascriptallonge.pdf (source-range-c98ab3e6-00340))_
- (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20 _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) . _(javascriptallonge.pdf (source-range-c98ab3e6-00350))_
- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-c98ab3e6-00351))_
- As we've said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00340))_
- (x) => (y) => x is called the K Combinator, or Kestrel . _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- (x) => x is called the I Combinator, or the Identity Function . _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3) . _(javascriptallonge.pdf (source-range-c98ab3e6-00350))_
- Calling a curried function with only some of its arguments is sometimes called partial application b . _(javascriptallonge.pdf (source-range-c98ab3e6-00351))_

## Technical atoms

### Technical frame 1: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00343))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00341))_

<a id="atom-technical-atom-7cd2e3295f4d04ba"></a>
> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.
