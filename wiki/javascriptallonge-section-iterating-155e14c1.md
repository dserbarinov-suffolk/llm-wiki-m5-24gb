---
page_id: javascriptallonge-section-iterating-155e14c1
page_kind: source
summary: iterating: 15 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iterating-155e14c1@a8db3c64893b954fe94fdcff2c032f13
---

# iterating

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-d081f846]] - previous source section: Copy on Write
- [[javascriptallonge-section-unfolding-and-laziness-b92d6532]] - next source section: unfolding and laziness

### Recipes

- [[javascriptallonge-recipe-iterating]] - recipe pattern: iterating

## Statements

- Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration. _(javascriptallonge.pdf (source-range-c98ab3e6-01260))_
- JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: _(javascriptallonge.pdf (source-range-c98ab3e6-01261))_
- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-c98ab3e6-01263))_
- Notice that buried inside our loop, we have bound the names done and value . We can put those into a POJO (a Plain Old JavaScript Object). It'll be a little awkward, but we'll be patient: _(javascriptallonge.pdf (source-range-c98ab3e6-01266))_
- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-c98ab3e6-01269))_
- We can write a different iterator for a different data structure. Here's one for linked lists: _(javascriptallonge.pdf (source-range-c98ab3e6-01270))_
- Notice that buried inside our loop, we have bound the names done and value . _(javascriptallonge.pdf (source-range-c98ab3e6-01266))_
