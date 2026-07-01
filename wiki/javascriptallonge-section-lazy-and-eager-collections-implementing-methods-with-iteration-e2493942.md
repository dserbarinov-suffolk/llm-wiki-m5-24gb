---
page_id: javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e2493942
page_kind: source
summary: Lazy and Eager Collections / implementing methods with iteration: 14 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-01
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e2493942@da24e553d4834e473f8bcae6bf307327
---

# Lazy and Eager Collections / implementing methods with iteration

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-lazy-and-eager-collections-60e3645a]] - broader source section: Lazy and Eager Collections
- [[javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-358e58c2]] - next source section: Lazy and Eager Collections / lazy collection operations

## Statements

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-0e12e052-01765))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-0e12e052-01766))_
- To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs: _(javascriptallonge.pdf (source-range-0e12e052-01772))_
