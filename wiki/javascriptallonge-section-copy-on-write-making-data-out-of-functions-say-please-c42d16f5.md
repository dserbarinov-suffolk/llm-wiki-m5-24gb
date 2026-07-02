---
page_id: javascriptallonge-section-copy-on-write-making-data-out-of-functions-say-please-c42d16f5
page_kind: source
summary: Copy on Write / Making Data Out Of Functions / say 'please': 11 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-making-data-out-of-functions-say-please-c42d16f5@d1376ed978ee001a2acf8e73c632a577
---

# Copy on Write / Making Data Out Of Functions / say 'please'

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-lists-with-functions-as-data-52fd04fd]] - previous source section: Copy on Write / Making Data Out Of Functions / lists with functions as data
- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-functions-are-not-the-real-point-ee3008de]] - next source section: Copy on Write / Making Data Out Of Functions / functions are not the real point

### Source structure

- [[javascriptallonge-section-copy-on-write-making-data-out-of-functions-12daea71]] - broader source section: Copy on Write / Making Data Out Of Functions

## Statements

- Wekeep using the same pattern in our functions: aPair === EMPTY ? doSomething : doSomethingElse . This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-0e12e052-01384))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here's length again: _(javascriptallonge.pdf (source-range-0e12e052-01385))_
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let's disambiguate our names: _(javascriptallonge.pdf (source-range-0e12e052-01389))_
- We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters: _(javascriptallonge.pdf (source-range-0e12e052-01392))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-0e12e052-01394))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-0e12e052-01385))_
