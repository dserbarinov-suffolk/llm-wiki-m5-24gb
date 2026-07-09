---
page_id: javascriptallonge-lazy-and-eager-collections
page_kind: concept
summary: Lazy and Eager Collections: 10 accepted assertion(s) and 0 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_3d5da3ef34482e27@70e5a434101a8923d57256c8fd9cc368
---

# Lazy and Eager Collections

Source: [[javascriptallonge]]

## Statements

- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. (javascriptallonge.pdf p.246)
- in the older style of object- oriented programming, we built 'fat' objects. (javascriptallonge.pdf p.246)
- If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. (javascriptallonge.pdf p.246)
- We tell ourselves that, well, a collection ought to know how to map itself. (javascriptallonge.pdf p.246)
- Some methods are only added to a few collections, some are added to all. (javascriptallonge.pdf p.246)
- That's a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. (javascriptallonge.pdf p.246)
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. (javascriptallonge.pdf p.246)
- Each one has its own variation, but the overall form is identical. (javascriptallonge.pdf p.246)
- That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. (javascriptallonge.pdf p.246)
- This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail. (javascriptallonge.pdf p.246)
