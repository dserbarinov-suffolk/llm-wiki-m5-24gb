---
page_id: coding-little-go-book-section-fields-of-a-structure-eaf15bfa
page_kind: source
summary: Fields of a Structure: 4 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-fields-of-a-structure-eaf15bfa@81a418d000016328a59e29a2ce5db652
---

# Fields of a Structure

From [[coding-little-go-book]].

## Statements

- In the example that we've seen so far, Saiyan has two fields Name and Power of types string and int , respectively. _(coding_little_go_book.pdf (source-range-773b6275-00157))_
- Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions. _(coding_little_go_book.pdf (source-range-773b6275-00157))_
- Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions. _(coding_little_go_book.pdf (source-range-773b6275-00157))_

## Technical atoms

```
For example, we could expand our deﬁnition of Saiyan:
type Saiyan struct {
  Name string
  Power int
  Father *Saiyan
}
which we'd initialize via:
gohan := &Saiyan{
  Name: "Gohan",
  Power: 1000,
  Father: &Saiyan {
    Name: "Goku",
    Power: 9001,
    Father: nil,
  },
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00158))_
