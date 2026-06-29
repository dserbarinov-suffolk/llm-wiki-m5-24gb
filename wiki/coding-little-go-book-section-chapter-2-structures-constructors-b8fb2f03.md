---
page_id: coding-little-go-book-section-chapter-2-structures-constructors-b8fb2f03
page_kind: source
summary: Chapter 2 - Structures / Constructors: 4 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-2-structures-constructors-b8fb2f03@de620a5840b9918ddaa6d5b53e36cb2e
---

# Chapter 2 - Structures / Constructors

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - broader source section: Chapter 2 - Structures
- [[coding-little-go-book-section-chapter-2-structures-functions-on-structures-7fcf1fb2]] - previous source section: Chapter 2 - Structures / Functions on Structures
- [[coding-little-go-book-section-chapter-2-structures-new-824b3ada]] - next source section: Chapter 2 - Structures / New

## Statements

- Structures don't have constructors. Instead, you create a function that returns an instance of the desired type (like a factory): _(coding_little_go_book.pdf (source-range-23d24eb1-00145))_
- This pattern rubs a lot of developers the wrong way. On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized. _(coding_little_go_book.pdf (source-range-23d24eb1-00147))_

## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Constructors

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00147))_

> This pattern rubs a lot of developers the wrong way. On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00146))_

```
func NewSaiyan(name string, power int) *Saiyan {
  return &Saiyan{
    Name: name,
    Power: power,
  }
}
```

### Technical frame 2: Chapter 2 - Structures / Constructors

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00147))_

> This pattern rubs a lot of developers the wrong way. On the one hand, it's a pretty slight syntactical change; on the other, it does feel a little less compartmentalized.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00149))_

```
func NewSaiyan(name string, power int) Saiyan {
  return Saiyan{
    Name: name,
    Power: power,
  }
}
```
