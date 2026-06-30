---
page_id: javascriptallonge-section-copy-on-write-functional-iterators-bonus-164389bb
page_kind: source
summary: Copy on Write / Functional Iterators / bonus: 10 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
page_family: section-reference
sources: raw/javascriptallonge.pdf
updated: 2026-06-30
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-functional-iterators-bonus-164389bb@2eaed1f05769ff8fb80786c98af18263
---

# Copy on Write / Functional Iterators / bonus

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-copy-on-write-functional-iterators-773e8dc1]] - broader source section: Copy on Write / Functional Iterators
- [[javascriptallonge-section-copy-on-write-functional-iterators-unfolding-and-laziness-34b94643]] - previous source section: Copy on Write / Functional Iterators / unfolding and laziness
- [[javascriptallonge-section-copy-on-write-functional-iterators-caveat-b77bc79a]] - next source section: Copy on Write / Functional Iterators / caveat

## Statements

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-0e12e052-01311))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: _(javascriptallonge.pdf (source-range-0e12e052-01314))_
- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-0e12e052-01316))_
- In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-0e12e052-01311))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-0e12e052-01314))_
