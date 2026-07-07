---
page_id: javascriptallonge-section-copy-on-write-functional-iterators-74724e0a
page_kind: source
summary: Copy on Write / Functional Iterators: 17 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-functional-iterators-74724e0a@2943d741bdaed6f57bfe969013c59d13
---

# Copy on Write / Functional Iterators

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-tortoises-hares-and-teleporting-turtles-3a4746f2]] - previous source section: Copy on Write / Tortoises, Hares, and Teleporting Turtles
- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-182a6c8b]] - next source section: Copy on Write / Making Data Out Of Functions

### Source structure

- [[javascriptallonge-section-copy-on-write-d081f846]] - broader source section: Copy on Write
- [[javascriptallonge-section-copy-on-write-functional-iterators-bonus-e75a0dd9]] - narrower source section: Copy on Write / Functional Iterators / bonus
- [[javascriptallonge-section-copy-on-write-functional-iterators-iterating-155e14c1]] - narrower source section: Copy on Write / Functional Iterators / iterating
- [[javascriptallonge-section-copy-on-write-functional-iterators-unfolding-and-laziness-b92d6532]] - narrower source section: Copy on Write / Functional Iterators / unfolding and laziness

### Topics

- [[javascriptallonge-functional-iterator]] - topic hub: opens the topic page for Functional Iterator

## Statements

- The nice thing about this is that the definition for arraySum mostly concerns itself with summing, and not with traversing over a collection of data. But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-c98ab3e6-01251))_
- Well, we call arraySum with an array, and it has baked into it a method for traversing the array. Perhaps we could extract both of those things. Let's rearrange our code a bit: _(javascriptallonge.pdf (source-range-c98ab3e6-01253))_
- What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function doesn't care what kind of data structure we have, as long as it's foldable. _(javascriptallonge.pdf (source-range-c98ab3e6-01255))_
- We've found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we've completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-c98ab3e6-01258))_
- But it still relies on foldArrayWith , so it can only sum arrays. _(javascriptallonge.pdf (source-range-c98ab3e6-01251))_

## Statements by subsection

### Copy on Write / Functional Iterators / caveat

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you're changing the state of the original! _(javascriptallonge.pdf (source-range-c98ab3e6-01298))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-c98ab3e6-01299))_
- Please note that unlike most of the other functions discussed in this book, iterators are stateful . _(javascriptallonge.pdf (source-range-c98ab3e6-01298))_
