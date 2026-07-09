---
page_id: javascriptallonge-section-bonus-e75a0dd9
page_kind: source
summary: bonus: 10 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-bonus-e75a0dd9@168603f43eecbf05e6aab5103cd31c0a
---

# bonus

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-unfolding-and-laziness-b92d6532]] - previous source section: unfolding and laziness

### Recipes

- [[javascriptallonge-recipe-bonus]] - recipe pattern: bonus

## Statements

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-c98ab3e6-01291))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: _(javascriptallonge.pdf (source-range-c98ab3e6-01294))_
- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-c98ab3e6-01296))_
- In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-c98ab3e6-01291))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-c98ab3e6-01294))_
