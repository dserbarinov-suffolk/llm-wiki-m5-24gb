---
page_id: javascriptallonge-section-recipes-with-basic-functions-unary-d494fe78
page_kind: source
summary: Recipes with Basic Functions / Unary: 15 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-unary-d494fe78@5c37261485c9a9d66e71fcc4b15ba8ad
---

# Recipes with Basic Functions / Unary

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-recipes-with-basic-functions-partial-application-70ce84b0]] - previous source section: Recipes with Basic Functions / Partial Application
- [[javascriptallonge-section-recipes-with-basic-functions-tap-51486e75]] - next source section: Recipes with Basic Functions / Tap

### Source structure

- [[javascriptallonge-section-recipes-with-basic-functions-d7445960]] - broader source section: Recipes with Basic Functions

## Statements

- The most common use case is to fix a problem. JavaScript has a .map method for arrays, and many libraries offer a map function with the same semantics. Here it is in action: _(javascriptallonge.pdf (source-range-c98ab3e6-00652))_
- If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example: _(javascriptallonge.pdf (source-range-c98ab3e6-00657))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00659))_
- Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us: _(javascriptallonge.pdf (source-range-c98ab3e6-00660))_
- What we want is to convert parseInt into a function taking only one argument. _(javascriptallonge.pdf (source-range-c98ab3e6-00659))_
- This doesn't work because parseInt is defined as parseInt(string[, radix]) . _(javascriptallonge.pdf (source-range-c98ab3e6-00659))_
