---
page_id: coding-little-go-book-section-pointers-versus-values-6ef8a5bb
page_kind: source
summary: Pointers versus Values: 7 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-pointers-versus-values-6ef8a5bb@67c6be32a2e2ee4606260aed427e8ac8
---

# Pointers versus Values

From [[coding-little-go-book]].

## Statements

- There are two pieces of good news. _(coding_little_go_book.pdf (source-range-773b6275-00174))_
- Secondly, if you aren't sure, use a pointer. _(coding_little_go_book.pdf (source-range-773b6275-00180))_
- Sometimes, this is the behavior that you'll want but sometimes not. _(coding_little_go_book.pdf (source-range-773b6275-00181))_
- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). _(coding_little_go_book.pdf (source-range-773b6275-00181))_
- Again, these are all pretty subtle cases. _(coding_little_go_book.pdf (source-range-773b6275-00185))_
- Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference. _(coding_little_go_book.pdf (source-range-773b6275-00185))_

## Technical atoms

```
type Point struct {
  X int
  Y int
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00183))_
