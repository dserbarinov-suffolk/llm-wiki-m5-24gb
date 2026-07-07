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
projection_coverage: section-javascriptallonge-section-lazy-and-eager-collections-7308cac5@e1fd8ea1b04420c3d66363e84fba92a1
---

# Lazy and Eager Collections

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-summary-551391b0]] - previous source section: Summary
- [[javascriptallonge-section-implementing-methods-with-iteration-d176c6c9]] - next source section: implementing methods with iteration

## Statements

- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack _(javascriptallonge.pdf (source-range-c98ab3e6-01733))_
- in the older style of object-oriented programming, we built 'fat' objects. Each collection knew how to map itself ( .map ), how to fold itself ( .reduce ), how to filter itself ( .filter ) and how to find one element within itself ( .find ). If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01734))_
- Over time, this informal 'interface' for collections grows by accretion. Some methods are only added to a few collections, some are added to all. But our objects grow fatter and fatter. We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-c98ab3e6-01735))_
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. Each one has its own variation, but the overall form is identical. That's a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. _(javascriptallonge.pdf (source-range-c98ab3e6-01736))_
- This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail. That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-c98ab3e6-01737))_
- Each collection knew how to map itself ( .map ), how to fold itself ( .reduce ), how to filter itself ( .filter ) and how to find one element within itself ( .find ). _(javascriptallonge.pdf (source-range-c98ab3e6-01734))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-c98ab3e6-01735))_
