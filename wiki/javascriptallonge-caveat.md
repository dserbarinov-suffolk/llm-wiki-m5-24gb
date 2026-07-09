---
page_id: javascriptallonge-caveat
page_kind: concept
summary: caveat: 4 accepted assertion(s) and 0 technical atom(s) from raw/javascriptallonge.pdf.
page_family: topic-concept
sources: raw/javascriptallonge.pdf
updated: 2026-07-09
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-state-tps_352f2a4653bd7a75@94db101223089af7f92be52463f15b94
---

# caveat

Source: [[javascriptallonge]]

## Statements

- Please note that unlike most of the other functions discussed in this book, iterators are stateful . (javascriptallonge.pdf p.176)
- There are some important implications of stateful functions. (javascriptallonge.pdf p.176)
- One is that while functions like take(..) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. (javascriptallonge.pdf p.176)
- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. (javascriptallonge.pdf p.176)
