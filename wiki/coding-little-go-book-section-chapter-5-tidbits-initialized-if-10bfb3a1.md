---
page_id: coding-little-go-book-section-chapter-5-tidbits-initialized-if-10bfb3a1
page_kind: source
summary: Chapter 5 - Tidbits / Initialized If: 5 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-5-tidbits-initialized-if-10bfb3a1@cb7deb5b1bc607511d0efc24b1b04560
---

# Chapter 5 - Tidbits / Initialized If

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-5-tidbits-e7a41f7c]] - broader source section: Chapter 5 - Tidbits
- [[coding-little-go-book-section-chapter-5-tidbits-go-fmt-e0b0680f]] - previous source section: Chapter 5 - Tidbits / go fmt
- [[coding-little-go-book-section-chapter-5-tidbits-empty-interface-and-conversions-c4483a93]] - next source section: Chapter 5 - Tidbits / Empty Interface and Conversions

## Statements

- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_
- Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else . _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

## Technical atoms

### Technical frame 1: Chapter 5 - Tidbits / Initialized If

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

> Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00362))_

> Go supports a slightly modified if-statement, one where a value can be initiated prior to the condition being evaluated:

### Technical frame 2: Chapter 5 - Tidbits / Initialized If

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

> Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00363))_

```
if x := 10; count > x {
  ...
}
```

### Technical frame 3: Chapter 5 - Tidbits / Initialized If

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00366))_

> Interestingly, while the values aren't available outside the ifstatement, they are available inside any else if or else .

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00365))_

```
if err := process(); err != nil {
  return err
}
```
