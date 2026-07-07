---
page_id: javascriptallonge-section-caveat-bb564290
page_kind: source
summary: caveat: 5 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-07-07
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-caveat-bb564290@e0ee4e391eee5d76ca8aa4616de497ae
---

# caveat

From [[javascriptallonge]].

## Related pages

### Source order

- [[javascriptallonge-section-bonus-01586812]] - previous source section: bonus
- [[javascriptallonge-section-making-data-out-of-functions-c168d1cb]] - next source section: Making Data Out Of Functions

## Statements

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you're changing the state of the original! _(javascriptallonge.pdf (source-range-c98ab3e6-01298))_
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-c98ab3e6-01299))_
- Please note that unlike most of the other functions discussed in this book, iterators are stateful . _(javascriptallonge.pdf (source-range-c98ab3e6-01298))_
