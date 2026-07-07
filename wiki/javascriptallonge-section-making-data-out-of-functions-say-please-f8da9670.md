---
page_id: javascriptallonge-section-making-data-out-of-functions-say-please-f8da9670
page_kind: source
summary: Making Data Out Of Functions / say 'please': 10 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-making-data-out-of-functions-say-please-f8da9670@26bfc5c94e275c1df9831faad9ee0b40
---

# Making Data Out Of Functions / say 'please'

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-making-data-out-of-functions-lists-with-functions-as-data-e74e34a2]] - previous source section: Making Data Out Of Functions / lists with functions as data
- [[javascriptallonge-section-making-data-out-of-functions-functions-are-not-the-real-point-0ee51da0]] - next source section: Making Data Out Of Functions / functions are not the real point

### Source structure

- [[javascriptallonge-section-making-data-out-of-functions-182a6c8b]] - broader source section: Making Data Out Of Functions

### Recipes

- [[javascriptallonge-recipe-say-please]] - recipe pattern: say 'please'

## Statements

- Wekeep using the same pattern in our functions: aPair === EMPTY ? doSomething : doSomethingElse . This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-c98ab3e6-01363))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here's length again: _(javascriptallonge.pdf (source-range-c98ab3e6-01364))_
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names: _(javascriptallonge.pdf (source-range-c98ab3e6-01368))_
- We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters: _(javascriptallonge.pdf (source-range-c98ab3e6-01371))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-c98ab3e6-01373))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-c98ab3e6-01364))_
