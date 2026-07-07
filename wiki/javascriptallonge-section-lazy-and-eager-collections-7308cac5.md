---
page_id: javascriptallonge-section-lazy-and-eager-collections-7308cac5
page_kind: source
summary: Lazy and Eager Collections: 12 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lazy-and-eager-collections-7308cac5@2c254c8804b526438f2648b5976bd819
---

# Lazy and Eager Collections

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-e15a3403]] - previous source section: Served by the Pot: Collections
- [[javascriptallonge-section-interlude-the-carpenter-interviews-for-a-job-9cc5ffd7]] - next source section: Interlude: The Carpenter Interviews for a Job

### Source structure

- [[javascriptallonge-section-lazy-and-eager-collections-eager-collections-527b72b9]] - narrower source section: Lazy and Eager Collections / eager collections
- [[javascriptallonge-section-lazy-and-eager-collections-implementing-methods-with-iteration-e67a1913]] - narrower source section: Lazy and Eager Collections / implementing methods with iteration
- [[javascriptallonge-section-lazy-and-eager-collections-lazy-collection-operations-0de83c02]] - narrower source section: Lazy and Eager Collections / lazy collection operations

### Collections

- [[javascriptallonge-collection-lazy-and-eager-collections-7308cac5]] - collection page: Lazy and Eager Collections

## Statements

- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack _(javascriptallonge.pdf (source-range-c98ab3e6-01733))_
- in the older style of object-oriented programming, we built 'fat' objects. Each collection knew how to map itself ( .map ), how to fold itself ( .reduce ), how to filter itself ( .filter ) and how to find one element within itself ( .find ). If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01734))_
- Over time, this informal 'interface' for collections grows by accretion. Some methods are only added to a few collections, some are added to all. But our objects grow fatter and fatter. We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-c98ab3e6-01735))_
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. Each one has its own variation, but the overall form is identical. That's a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. _(javascriptallonge.pdf (source-range-c98ab3e6-01736))_
- This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail. That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-c98ab3e6-01737))_
- Each collection knew how to map itself ( .map ), how to fold itself ( .reduce ), how to filter itself ( .filter ) and how to find one element within itself ( .find ). _(javascriptallonge.pdf (source-range-c98ab3e6-01734))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-c98ab3e6-01735))_
