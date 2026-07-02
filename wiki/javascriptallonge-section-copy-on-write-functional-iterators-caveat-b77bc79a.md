---
page_id: javascriptallonge-section-copy-on-write-functional-iterators-caveat-b77bc79a
page_kind: source
summary: Copy on Write / Functional Iterators / caveat: 5 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-functional-iterators-caveat-b77bc79a@a9b28d2d8161c5873451d0f11f255b0a
---

# Copy on Write / Functional Iterators / caveat

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-copy-on-write-functional-iterators-bonus-164389bb]] - previous source section: Copy on Write / Functional Iterators / bonus

### Source structure

- [[javascriptallonge-section-copy-on-write-functional-iterators-773e8dc1]] - broader source section: Copy on Write / Functional Iterators

## Statements

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you're changing the state of the original! _(javascriptallonge.pdf (source-range-0e12e052-01318))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-0e12e052-01319))_
- Please note that unlike most of the other functions discussed in this book, iterators are stateful . _(javascriptallonge.pdf (source-range-0e12e052-01318))_
