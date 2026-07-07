---
page_id: javascriptallonge-section-shadowy-variables-from-a-shadowy-planet-55213f04
page_kind: source
summary: shadowy variables from a shadowy planet: 11 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-shadowy-variables-from-a-shadowy-planet-55213f04@dfe768b269114437ba4baa3ff5da652f
---

# shadowy variables from a shadowy planet

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-it-s-always-the-environment-e193eb5b]] - previous source section: it's always the environment
- [[javascriptallonge-section-which-came-first-the-chicken-or-the-egg-a12b4efa]] - next source section: which came first, the chicken or the egg?

## Statements

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. Consider: _(javascriptallonge.pdf (source-range-c98ab3e6-00356))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: _(javascriptallonge.pdf (source-range-c98ab3e6-00358))_
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-c98ab3e6-00360))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-c98ab3e6-00361))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. _(javascriptallonge.pdf (source-range-c98ab3e6-00358))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. _(javascriptallonge.pdf (source-range-c98ab3e6-00358))_
