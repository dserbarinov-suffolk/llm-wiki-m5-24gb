---
page_id: coding-little-go-book-section-pointers-versus-values-3792b243
page_kind: source
summary: Pointers versus Values: 8 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-pointers-versus-values-3792b243@be081b7d4d59fb9df8063fdefdd2ad6b
---

# Pointers versus Values

From [[coding-little-go-book]].

## Statements

- There are two pieces of good news. _(coding_little_go_book.pdf (source-range-810ce361-00174))_
- Secondly, if you aren't sure, use a pointer. _(coding_little_go_book.pdf (source-range-810ce361-00180))_
- As we already saw, passing values is a great way to make data immutable (changes that a function makes to it won't be reflected in the calling code). _(coding_little_go_book.pdf (source-range-810ce361-00181))_
- Sometimes, this is the behavior that you'll want but sometimes not. _(coding_little_go_book.pdf (source-range-810ce361-00181))_
- Again, these are all pretty subtle cases. _(coding_little_go_book.pdf (source-range-810ce361-00185))_

## Technical atoms

> As you write Go code, it's natural to ask yourself should this be a value, or a pointer to a value?
_(source: coding_little_go_book.pdf (source-range-810ce361-00174))_

```
type Point struct { X	int Y	int }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00183))_

> Unless you're iterating over thousands or possibly tens of thousands of such points, you wouldn't notice a difference.
_(source: coding_little_go_book.pdf (source-range-810ce361-00185))_
