---
page_id: javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-71d66043
page_kind: source
summary: And also: / Closures and Scope / shadowy variables from a shadowy planet: 11 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-closures-and-scope-shadowy-variables-from-a-shadowy-planet-71d66043@64121ab4a5917ea8acbbc02192db8d5f
---

# And also: / Closures and Scope / shadowy variables from a shadowy planet

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-closures-and-scope-ff45d11c]] - broader source section: And also: / Closures and Scope
- [[javascriptallonge-section-and-also-closures-and-scope-it-s-always-the-environment-3905285c]] - previous source section: And also: / Closures and Scope / it's always the environment
- [[javascriptallonge-section-and-also-closures-and-scope-which-came-first-the-chicken-or-the-egg-66a98800]] - next source section: And also: / Closures and Scope / which came first, the chicken or the egg?

## Statements

- An interesting thing happens when a variable has the same name as an ancestor environment's variable. Consider: _(javascriptallonge.pdf (source-range-0e12e052-00366))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x , it is ignored when evaluating x + y . JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- When evaluating x + y + z , JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both w s. When a variable has the same name as an ancestor environment's binding, it is said to shadow the ancestor. _(javascriptallonge.pdf (source-range-0e12e052-00370))_
- This is often a good thing. _(javascriptallonge.pdf (source-range-0e12e052-00371))_
- JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. _(javascriptallonge.pdf (source-range-0e12e052-00368))_
- The function (x, y) => x + y is a pure function, because its x is defined within its own environment. _(javascriptallonge.pdf (source-range-0e12e052-00368))_
