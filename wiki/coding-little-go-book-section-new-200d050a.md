---
page_id: coding-little-go-book-section-new-200d050a
page_kind: source
summary: New: 4 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-new-200d050a@6647d0b64ff48fd0e8cc9ac5b811ae04
---

# New

From [[coding-little-go-book]].

## Statements

- Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read: _(coding_little_go_book.pdf (source-range-773b6275-00153))_

## Technical atoms

```
goku := new(Saiyan)
// same as
goku := &Saiyan{}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00152))_

```
goku := new(Saiyan)
goku.Name = "goku"
goku.Power = 9001
//vs
goku := &Saiyan {
  Name: "goku",
  Power: 9000,
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00154))_

> Whichever approach you choose, if you follow the factory pattern above, you can shield the rest of your code from knowing and worrying about any of the allocation details.
_(source: coding_little_go_book.pdf (source-range-773b6275-00155))_
