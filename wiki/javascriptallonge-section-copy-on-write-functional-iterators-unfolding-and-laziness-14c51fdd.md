---
page_id: javascriptallonge-section-copy-on-write-functional-iterators-unfolding-and-laziness-14c51fdd
page_kind: source
summary: Copy on Write / Functional Iterators / unfolding and laziness: 16 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-06
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-functional-iterators-unfolding-and-laziness-14c51fdd@10050f81fca5007643f113c5d684020a
---

# Copy on Write / Functional Iterators / unfolding and laziness

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-functional-iterators-iterating-60eb2c86]] - previous source section: Copy on Write / Functional Iterators / iterating
- [[javascriptallonge-section-copy-on-write-functional-iterators-bonus-9d9a69d5]] - next source section: Copy on Write / Functional Iterators / bonus

### Source structure

- [[javascriptallonge-section-copy-on-write-functional-iterators-ef79a70c]] - broader source section: Copy on Write / Functional Iterators

## Statements

- Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let's consider the simplest example: _(javascriptallonge.pdf (source-range-c98ab3e6-01294))_
- A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-c98ab3e6-01298))_
- This business of going on forever has some drawbacks. Let's introduce an idea: A function that takes an iterator and returns another iterator. We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-c98ab3e6-01302))_
- How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly: _(javascriptallonge.pdf (source-range-c98ab3e6-01304))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-c98ab3e6-01309))_
- A function that starts with a seed and expands it into a data structure is called an unfold . _(javascriptallonge.pdf (source-range-c98ab3e6-01298))_
- We can start with take , an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-c98ab3e6-01302))_
