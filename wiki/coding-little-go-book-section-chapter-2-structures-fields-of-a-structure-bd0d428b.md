---
page_id: coding-little-go-book-section-chapter-2-structures-fields-of-a-structure-bd0d428b
page_kind: source
summary: Chapter 2 - Structures / Fields of a Structure: 4 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-2-structures-fields-of-a-structure-bd0d428b@204b462de6c93f55231e996a261b93c7
---

# Chapter 2 - Structures / Fields of a Structure

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - broader source section: Chapter 2 - Structures
- [[coding-little-go-book-section-chapter-2-structures-new-824b3ada]] - previous source section: Chapter 2 - Structures / New
- [[coding-little-go-book-section-chapter-2-structures-composition-06f1b349]] - next source section: Chapter 2 - Structures / Composition

## Statements

- In the example that we've seen so far, Saiyan has two fields Name and Power of types string and int , respectively. Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions. _(coding_little_go_book.pdf (source-range-23d24eb1-00157))_
- Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions. _(coding_little_go_book.pdf (source-range-23d24eb1-00157))_

## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Fields of a Structure

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00157))_

> In the example that we've seen so far, Saiyan has two fields Name and Power of types string and int , respectively. Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00158))_

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
