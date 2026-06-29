---
page_id: coding-little-go-book-section-chapter-2-structures-pointers-versus-values-a51ed683
page_kind: source
summary: Chapter 2 - Structures / Pointers versus Values: 7 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-2-structures-pointers-versus-values-a51ed683@94ab6779a0205059029868f09b62bf17
---

# Chapter 2 - Structures / Pointers versus Values

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - broader source section: Chapter 2 - Structures
- [[coding-little-go-book-section-chapter-2-structures-composition-06f1b349]] - previous source section: Chapter 2 - Structures / Composition
- [[coding-little-go-book-section-chapter-2-structures-before-you-continue-6cf3e09c]] - next source section: Chapter 2 - Structures / Before You Continue

## Statements

- As you write Go code, it's natural to ask yourself should this be a value, or a pointer to a value? There are two pieces of good news. First, the answer is the same regardless of which of the following we're talking about: _(coding_little_go_book.pdf (source-range-23d24eb1-00174))_
- Secondly, if you aren't sure, use a pointer. _(coding_little_go_book.pdf (source-range-23d24eb1-00180))_
- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). Sometimes, this is the behavior that you'll want but sometimes not. _(coding_little_go_book.pdf (source-range-23d24eb1-00181))_
- Again, these are all pretty subtle cases. Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference. _(coding_little_go_book.pdf (source-range-23d24eb1-00185))_
- Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference. _(coding_little_go_book.pdf (source-range-23d24eb1-00185))_

## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Pointers versus Values

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00185))_

> Again, these are all pretty subtle cases. Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00183))_

```
type Point struct {
  X int
  Y int
}
```
