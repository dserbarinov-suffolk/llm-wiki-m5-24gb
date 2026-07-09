---
page_id: javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e67a1913
page_kind: source
summary: Lazy and Eager Collections / implementing methods with iteration: 11 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e67a1913@6c036be5a4e2f2ef027eb550b4e6dd55
---

# Lazy and Eager Collections / implementing methods with iteration

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-0de83c02]] - next source section: Lazy and Eager Collections / lazy collection operations

### Source structure

- [[javascriptallonge-section-lazy-and-eager-collections-7308cac5]] - broader source section: Lazy and Eager Collections

### Recipes

- [[javascriptallonge-recipe-implementing-methods-with-iteration]] - recipe pattern: implementing methods with iteration

## Statements

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-c98ab3e6-01739))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-c98ab3e6-01740))_
- To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs: _(javascriptallonge.pdf (source-range-c98ab3e6-01746))_
