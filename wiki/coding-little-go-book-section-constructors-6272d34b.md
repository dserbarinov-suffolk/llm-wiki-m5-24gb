---
page_id: coding-little-go-book-section-constructors-6272d34b
page_kind: source
summary: Constructors: 4 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-constructors-6272d34b@e1c480550d475ec94c4fac95c1d39384
---

# Constructors

From [[coding-little-go-book]].

## Statements

- Structures don't have constructors. _(coding_little_go_book.pdf (source-range-773b6275-00145))_
- On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized. _(coding_little_go_book.pdf (source-range-773b6275-00147))_

## Technical atoms

```
func NewSaiyan(name string, power int) *Saiyan {
  return &Saiyan{
    Name: name,
    Power: power,
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00146))_

```
func NewSaiyan(name string, power int) Saiyan {
  return Saiyan{
    Name: name,
    Power: power,
  }
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00149))_
