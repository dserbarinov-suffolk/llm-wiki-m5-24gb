---
page_id: coding-little-go-book-section-chapter-5-tidbits-error-handling-c2084411
page_kind: source
summary: Chapter 5 - Tidbits / Error Handling: 14 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-5-tidbits-error-handling-c2084411@8623b41a934ecf2ba3e44262fe975019
---

# Chapter 5 - Tidbits / Error Handling

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-5-tidbits-e7a41f7c]] - broader source section: Chapter 5 - Tidbits
- [[coding-little-go-book-section-chapter-5-tidbits-defer-9e77b4c5]] - next source section: Chapter 5 - Tidbits / Defer

## Statements

- Go's preferred way to deal with errors is through return values, not exceptions. Consider the strconv.Atoi function which takes a string and tries to convert it to an integer: _(coding_little_go_book.pdf (source-range-23d24eb1-00339))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-23d24eb1-00341))_
- This is a package variable (it's defined outside of a function) which is publicly accessible (upper-case first letter). Various functions can return this error, say when we're reading from a file or STDIN. If it makes contextual sense, you should use this error, too. As consumers, we can use this singleton: _(coding_little_go_book.pdf (source-range-23d24eb1-00348))_
- As a final note, Go does have panic and recover functions. panic is like throwing an exception while recover is like catch ; they are rarely used. _(coding_little_go_book.pdf (source-range-23d24eb1-00350))_
- You can create your own error type; the only requirement is that it fulfills the contract of the built-in error interface, which is: _(coding_little_go_book.pdf (source-range-23d24eb1-00341))_
