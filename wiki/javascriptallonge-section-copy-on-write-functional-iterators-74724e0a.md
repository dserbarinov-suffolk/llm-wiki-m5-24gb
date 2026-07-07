---
page_id: javascriptallonge-section-copy-on-write-functional-iterators-74724e0a
page_kind: source
summary: Copy on Write / Functional Iterators: 12 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-functional-iterators-74724e0a@ee371f4b6305c037ed2bc5eac527b10a
---

# Copy on Write / Functional Iterators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-tortoises-hares-and-teleporting-turtles-3a4746f2]] - previous source section: Copy on Write / Tortoises, Hares, and Teleporting Turtles

### Source structure

- [[javascriptallonge-section-copy-on-write-d081f846]] - broader source section: Copy on Write

### Recipes

- [[javascriptallonge-recipe-functional-iterators]] - recipe pattern: Functional Iterators

### Topics

- [[javascriptallonge-functional-iterator]] - topic hub: opens the topic page for Functional Iterator

## Statements

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-c98ab3e6-01251))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-c98ab3e6-01253))_
- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-c98ab3e6-01255))_
- We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-c98ab3e6-01258))_
- But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-c98ab3e6-01251))_
