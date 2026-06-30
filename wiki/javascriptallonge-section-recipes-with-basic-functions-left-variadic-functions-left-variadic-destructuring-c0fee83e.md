---
page_id: javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-c0fee83e
page_kind: source
summary: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: 7 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-c0fee83e@3266d7def6cbcd2a0e29e4a33efeb0db
---

# Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-c0cc9e6b]] - broader source section: Recipes with Basic Functions / Left-Variadic Functions
- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-overcoming-limitations-ba6c5a7e]] - previous source section: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

## Statements

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-0e12e052-00736))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-0e12e052-00742))_
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-0e12e052-00744))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-0e12e052-00742))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-0e12e052-00739))_

```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```
