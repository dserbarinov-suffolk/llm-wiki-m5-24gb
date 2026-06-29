---
page_id: coding-little-go-book-section-chapter-2-structures-composition-overloading-8c373927
page_kind: source
summary: Chapter 2 - Structures / Composition / Overloading: 3 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-2-structures-composition-overloading-8c373927@ebe740590348f861c6830f50573f6bed
---

# Chapter 2 - Structures / Composition / Overloading

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-2-structures-composition-06f1b349]] - broader source section: Chapter 2 - Structures / Composition

## Statements

- The composed version is always available via s.Person.Introduce() . _(coding_little_go_book.pdf (source-range-23d24eb1-00172))_

## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Composition / Overloading

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00172))_

> The composed version is always available via s.Person.Introduce() .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00170))_

> However, because implicit composition is really just a compiler trick, we can "overwrite" the functions of a composed type. For example, our Saiyan structure can have its own Introduce function:

### Technical frame 2: Chapter 2 - Structures / Composition / Overloading

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00172))_

> The composed version is always available via s.Person.Introduce() .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00171))_

```
func (s *Saiyan) Introduce() {
  fmt.Printf("Hi, I'm %s. Ya!\n", s.Name)
}
```
