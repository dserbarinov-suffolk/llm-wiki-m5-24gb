---
page_id: javascriptallonge-section-backwardness-6e5a7d1d
page_kind: source
summary: backwardness: 7 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-backwardness-6e5a7d1d@2ff1eca60e5bb1c22b4b8a684bd44357
---

# backwardness

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-the-kestrel-and-the-idiot-de84450c]] - previous source section: the kestrel and the idiot
- [[javascriptallonge-section-the-vireo-15cde3c9]] - next source section: the vireo

## Statements

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we'd write them like this: _(javascriptallonge.pdf (source-range-c98ab3e6-01328))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it. _(javascriptallonge.pdf (source-range-c98ab3e6-01332))_
- But the first and second we built out of K and I don't work that way. You call them and pass them the bits, and they choose what to return. So if we wanted to use them with a two-element array, we'd need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-c98ab3e6-01333))_
- Our latin data structure is no longer a dumb data structure, it's a function. And instead of passing latin to first or second , we pass first or second to latin . It's exactly backwards of the way we write functions that operate on data. _(javascriptallonge.pdf (source-range-c98ab3e6-01336))_
