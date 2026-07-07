---
page_id: javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-1d686fdb
page_kind: source
summary: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring: 7 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-left-variadic-destructuring-1d686fdb@834c4c4790392dddaa4130075207b2fc
---

# Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-overcoming-limitations-885636ba]] - previous source section: Recipes with Basic Functions / Left-Variadic Functions / overcoming limitations

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-574b019e]] - broader source section: Recipes with Basic Functions / Left-Variadic Functions

## Statements

- Gathering arguments for functions is one of the ways JavaScript can destructure arrays. Another way is when assigning variables, like this: _(javascriptallonge.pdf (source-range-c98ab3e6-00724))_
- But we can write our own left-gathering function utility using the same principles without all the tedium: _(javascriptallonge.pdf (source-range-c98ab3e6-00730))_
- With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function. _(javascriptallonge.pdf (source-range-c98ab3e6-00732))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-c98ab3e6-00730))_

> But we can write our own left-gathering function utility using the same principles without all the tedium:

**Atom:** _(javascriptallonge.pdf (source-range-c98ab3e6-00727))_

<a id="atom-technical-atom-258d1986600602c2"></a>
```
const [...butLast, last] = ['why', 'hello', 'there', 'little', 'droid'];
//=> Unexpected token
```
