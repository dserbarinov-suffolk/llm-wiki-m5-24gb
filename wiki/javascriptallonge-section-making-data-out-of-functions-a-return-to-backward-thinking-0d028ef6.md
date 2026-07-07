---
page_id: javascriptallonge-section-making-data-out-of-functions-a-return-to-backward-thinking-0d028ef6
page_kind: source
summary: Making Data Out Of Functions / a return to backward thinking: 20 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-making-data-out-of-functions-a-return-to-backward-thinking-0d028ef6@05d6d55b688f88e835904699423913a6
---

# Making Data Out Of Functions / a return to backward thinking

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-making-data-out-of-functions-functions-are-not-the-real-point-0ee51da0]] - previous source section: Making Data Out Of Functions / functions are not the real point

### Source structure

- [[javascriptallonge-section-making-data-out-of-functions-182a6c8b]] - broader source section: Making Data Out Of Functions

### Recipes

- [[javascriptallonge-recipe-a-return-to-backward-thinking]] - recipe pattern: a return to backward thinking

## Statements

- To make pairs work, we did things backwards , we passed the first and rest functions to the pair, and the pair called our function. As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y) . _(javascriptallonge.pdf (source-range-c98ab3e6-01383))_
- But we could have done something completely different. We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-c98ab3e6-01384))_
- The exact implementation of a pair is hidden from the code that uses a pair. Here, we'll prove it: _(javascriptallonge.pdf (source-range-c98ab3e6-01385))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-c98ab3e6-01387))_
- We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-c98ab3e6-01390))_
- The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-c98ab3e6-01393))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. This is a fundamental principle of good design. It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-c98ab3e6-01394))_
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns: _(javascriptallonge.pdf (source-range-c98ab3e6-01395))_
- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-c98ab3e6-01396))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-c98ab3e6-01390))_
