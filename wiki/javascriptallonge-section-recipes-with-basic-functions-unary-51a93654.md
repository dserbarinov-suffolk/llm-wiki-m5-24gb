---
page_id: javascriptallonge-section-recipes-with-basic-functions-unary-51a93654
page_kind: source
summary: Recipes with Basic Functions / Unary: 15 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-unary-51a93654@a96853911320b5e8224ee2ad446cba51
---

# Recipes with Basic Functions / Unary

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-basic-functions-partial-application-576f87fc]] - previous source section: Recipes with Basic Functions / Partial Application
- [[javascriptallonge-section-recipes-with-basic-functions-tap-7702e150]] - next source section: Recipes with Basic Functions / Tap

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-8e785fac]] - broader source section: Recipes with Basic Functions

## Statements

- The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action: _(javascriptallonge.pdf (source-range-c98ab3e6-00664))_
- If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: _(javascriptallonge.pdf (source-range-c98ab3e6-00669))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00671))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00671))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . _(javascriptallonge.pdf (source-range-c98ab3e6-00671))_
