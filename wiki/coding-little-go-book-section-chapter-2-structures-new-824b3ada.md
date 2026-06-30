---
page_id: coding-little-go-book-section-chapter-2-structures-new-824b3ada
page_kind: source
summary: Chapter 2 - Structures / New: 4 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-2-structures-new-824b3ada@cf409654c7f792738b5fda95e5fc2d2c
---

# Chapter 2 - Structures / New

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - broader source section: Chapter 2 - Structures
- [[coding-little-go-book-section-chapter-2-structures-constructors-b8fb2f03]] - previous source section: Chapter 2 - Structures / Constructors
- [[coding-little-go-book-section-chapter-2-structures-fields-of-a-structure-bd0d428b]] - next source section: Chapter 2 - Structures / Fields of a Structure

## Statements

- Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read: _(coding_little_go_book.pdf (source-range-23d24eb1-00153))_

## Technical atoms

### Technical frame 1: Chapter 2 - Structures / New

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00153))_

> Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00152))_

```
goku := new(Saiyan)
// same as
goku := &Saiyan{}
```

### Technical frame 2: Chapter 2 - Structures / New

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00153))_

> Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00154))_

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

### Technical frame 3: Chapter 2 - Structures / New

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00153))_

> Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00155))_

> Whichever approach you choose, if you follow the factory pattern above, you can shield the rest of your code from knowing and worrying about any of the allocation details.
