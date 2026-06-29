---
page_id: coding-little-go-book-section-chapter-2-structures-functions-on-structures-7fcf1fb2
page_kind: source
summary: Chapter 2 - Structures / Functions on Structures: 3 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-2-structures-functions-on-structures-7fcf1fb2@2b6e91a42a326e52a59bdbda1f1df056
---

# Chapter 2 - Structures / Functions on Structures

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-2-structures-59a89c52]] - broader source section: Chapter 2 - Structures
- [[coding-little-go-book-section-chapter-2-structures-declarations-and-initializations-aa4f849c]] - previous source section: Chapter 2 - Structures / Declarations and Initializations
- [[coding-little-go-book-section-chapter-2-structures-constructors-b8fb2f03]] - next source section: Chapter 2 - Structures / Constructors

## Statements

- In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so: _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

## Technical atoms

### Technical frame 1: Chapter 2 - Structures / Functions on Structures

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

> In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00141))_

```
type Saiyan struct {
  Name string
  Power int
}
func (s *Saiyan) Super() {
  s.Power += 10000
}
```

### Technical frame 2: Chapter 2 - Structures / Functions on Structures

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00142))_

> In the above code, we say that the type *Saiyan is the receiver of the Super method. We call Super like so:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00143))_

```
goku := &Saiyan{"Goku", 9001}
goku.Super()
fmt.Println(goku.Power) // will print 19001
```
