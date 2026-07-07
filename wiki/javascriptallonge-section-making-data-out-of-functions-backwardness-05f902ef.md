---
page_id: javascriptallonge-section-making-data-out-of-functions-backwardness-05f902ef
page_kind: source
summary: Making Data Out Of Functions / backwardness: 7 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-making-data-out-of-functions-backwardness-05f902ef@fa8c5180ff3f094ec1f8abdd20dceb6a
---

# Making Data Out Of Functions / backwardness

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-making-data-out-of-functions-the-kestrel-and-the-idiot-203dea45]] - previous source section: Making Data Out Of Functions / the kestrel and the idiot
- [[javascriptallonge-section-making-data-out-of-functions-the-vireo-1b2dccd1]] - next source section: Making Data Out Of Functions / the vireo

### Source structure

- [[javascriptallonge-section-making-data-out-of-functions-182a6c8b]] - broader source section: Making Data Out Of Functions

### Recipes

- [[javascriptallonge-recipe-backwardness]] - recipe pattern: backwardness

## Statements

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we'd write them like this: _(javascriptallonge.pdf (source-range-c98ab3e6-01328))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-c98ab3e6-01332))_
- But the first and second we built out of K and I don't work that way. You call them and pass them the bits, and they choose what to return. So if we wanted to use them with a two-element array, we'd need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-c98ab3e6-01333))_
- Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data. _(javascriptallonge.pdf (source-range-c98ab3e6-01336))_
