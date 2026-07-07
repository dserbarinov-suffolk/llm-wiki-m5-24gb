---
page_id: javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-98745d63
page_kind: source
summary: Served by the Pot: Collections / Iteration and Iterables: 17 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-98745d63@b555dc6b4be1a5267b60606e005bb150
---

# Served by the Pot: Collections / Iteration and Iterables

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-served-by-the-pot-collections-generating-iterables-f68c47a5]] - next source section: Served by the Pot: Collections / Generating Iterables

### Source structure

- [[javascriptallonge-section-served-by-the-pot-collections-e15a3403]] - broader source section: Served by the Pot: Collections
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-a-look-back-at-functional-iterators-57a76f01]] - narrower source section: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterables-94f83dae]] - narrower source section: Served by the Pot: Collections / Iteration and Iterables / iterables
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterables-out-to-infinity-ae258dd7]] - narrower source section: Served by the Pot: Collections / Iteration and Iterables / iterables out to infinity
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-iterator-objects-cbbb8baa]] - narrower source section: Served by the Pot: Collections / Iteration and Iterables / iterator objects
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-operations-on-ordered-collections-ee56851b]] - narrower source section: Served by the Pot: Collections / Iteration and Iterables / operations on ordered collections
- [[javascriptallonge-section-served-by-the-pot-collections-iteration-and-iterables-ordered-collections-16a4ad9f]] - narrower source section: Served by the Pot: Collections / Iteration and Iterables / ordered collections

### Collections

- [[javascriptallonge-collection-served-by-the-pot-collections-iteration-and-iterables-98745d63]] - collection page: Served by the Pot: Collections / Iteration and Iterables

### Recipes

- [[javascriptallonge-recipe-from]] - recipe pattern: from

## Statements

- Many objects in JavaScript can model collections of things. A collection is like a box containing stuff. Sometimes you just want to move the box around. But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-c98ab3e6-01498))_
- All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-c98ab3e6-01500))_
- Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-c98ab3e6-01500))_

## Statements by subsection

### Served by the Pot: Collections / Iteration and Iterables / from

- Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-c98ab3e6-01581))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript's built-in Array class already has one: _(javascriptallonge.pdf (source-range-c98ab3e6-01582))_
- We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method. _(javascriptallonge.pdf (source-range-c98ab3e6-01584))_
- Nowwecan go 'end to end,' If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-c98ab3e6-01587))_

### Served by the Pot: Collections / Iteration and Iterables / summary

- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. Iterable ordered collections can be iterated over or gathered into another collection. _(javascriptallonge.pdf (source-range-c98ab3e6-01590))_
- Separating concerns with iterators speaks to JavaScript's fundamental nature: It's a language that wants to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-c98ab3e6-01591))_
