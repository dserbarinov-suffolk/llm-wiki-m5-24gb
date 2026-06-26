---
page_id: coding-little-go-book-section-pointers-versus-values-51d1e0ae
page_kind: source
summary: Pointers versus Values: 6 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-pointers-versus-values-51d1e0ae@b56f894ad51b068c7e9766231f1ecff3
---

# Pointers versus Values

From [[coding-little-go-book]].

## Statements

- We'll now have this same conversation with respect to array and map values. _(coding_little_go_book.pdf (source-range-773b6275-00266))_
- So the decision on whether to define an array of pointers versus an array of values comes down to how you use the individual values, not how you use the array or map itself. _(coding_little_go_book.pdf (source-range-773b6275-00268))_
- Many developers think that passing b to, or returning it from, a function is going to be more efficient. _(coding_little_go_book.pdf (source-range-773b6275-00268))_
- Where you will see a difference is when you modify the values of a slice or map. _(coding_little_go_book.pdf (source-range-773b6275-00268))_
- However, what's being passed/returned is a copy of the slice, which itself is a reference. _(coding_little_go_book.pdf (source-range-773b6275-00268))_

## Technical atoms

```
a := make([]Saiyan, 10)
//or
b := make([]*Saiyan, 10)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00267))_
