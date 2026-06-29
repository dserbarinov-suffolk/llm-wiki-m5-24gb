---
page_id: coding-little-go-book-section-chapter-1-the-basics-garbage-collected-538d2af8
page_kind: source
summary: Chapter 1 - The Basics / Garbage Collected: 5 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-1-the-basics-garbage-collected-538d2af8@1ba42b755ea8108e0749f502ccf543ab
---

# Chapter 1 - The Basics / Garbage Collected

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-1-the-basics-45e21143]] - broader source section: Chapter 1 - The Basics
- [[coding-little-go-book-section-chapter-1-the-basics-c-like-syntax-4fda7deb]] - previous source section: Chapter 1 - The Basics / C-Like Syntax
- [[coding-little-go-book-section-chapter-1-the-basics-running-go-code-f8398d4c]] - next source section: Chapter 1 - The Basics / Running Go Code

## Statements

- Some variables, when created, have an easy-to-define life. A variable local to a function, for example, disappears when the function exits. In other cases, it isn't so obvious -- at least to a compiler. For example, the lifetime of a variable returned by a function or referenced by other variables and objects can be tricky to determine. Without garbage collection, it's up to developers to free the memory associated with such variables at a point where the developer knows the variable isn't needed. How? In C, you'd literally free(str); the variable. _(coding_little_go_book.pdf (source-range-23d24eb1-00046))_
- Languages with garbage collectors (e.g., Ruby, Python, Java, JavaScript, C#, Go) are able to keep track of these and free them when they're no longer used. Garbage collection adds overhead, but it also eliminates a number of devastating bugs. _(coding_little_go_book.pdf (source-range-23d24eb1-00047))_
- A variable local to a function, for example, disappears when the function exits. _(coding_little_go_book.pdf (source-range-23d24eb1-00046))_
