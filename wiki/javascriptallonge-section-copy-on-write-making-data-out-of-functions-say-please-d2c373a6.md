---
page_id: javascriptallonge-section-copy-on-write-making-data-out-of-functions-say-please-d2c373a6
page_kind: source
summary: Copy on Write / Making Data Out Of Functions / say 'please': 11 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-making-data-out-of-functions-say-please-d2c373a6@3994ef63ce8fca16673331605cc39488
---

# Copy on Write / Making Data Out Of Functions / say 'please'

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-lists-with-functions-as-data-5664b947]] - previous source section: Copy on Write / Making Data Out Of Functions / lists with functions as data
- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-functions-are-not-the-real-point-ffd66dc9]] - next source section: Copy on Write / Making Data Out Of Functions / functions are not the real point

### Source structure

- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-bbf4cfc0]] - broader source section: Copy on Write / Making Data Out Of Functions

## Statements

- Wekeep using the same pattern in our functions: aPair === EMPTY ? doSomething : doSomethingElse . This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-c98ab3e6-01384))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here's length again: _(javascriptallonge.pdf (source-range-c98ab3e6-01385))_
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names: _(javascriptallonge.pdf (source-range-c98ab3e6-01389))_
- We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters: _(javascriptallonge.pdf (source-range-c98ab3e6-01392))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-c98ab3e6-01394))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-c98ab3e6-01385))_
