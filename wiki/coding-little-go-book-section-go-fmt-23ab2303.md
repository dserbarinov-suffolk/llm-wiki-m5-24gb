---
page_id: coding-little-go-book-section-go-fmt-23ab2303
page_kind: source
summary: go fmt: 8 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-go-fmt-23ab2303@bc842e2f853238fede5799174e972c34
---

# go fmt

From [[coding-little-go-book]].

## Statements

- Most programs written in Go follow the same formatting rules, namely, a tab is used to indent and braces go on the same line as their statement. _(coding_little_go_book.pdf (source-range-773b6275-00356))_
- That's what I did for a long time, but I'm glad I eventually gave in. _(coding_little_go_book.pdf (source-range-773b6275-00357))_
- It's easy to use and authoritative (so no one argues over meaningless preferences). _(coding_little_go_book.pdf (source-range-773b6275-00357))_
- A big reason for this is the go fmt command. _(coding_little_go_book.pdf (source-range-773b6275-00357))_
- I know, you have your own style and you want to stick to it. _(coding_little_go_book.pdf (source-range-773b6275-00357))_
- It does more than indent your code; it also aligns field declarations and alphabetically orders imports. _(coding_little_go_book.pdf (source-range-773b6275-00360))_

## Technical atoms

> When you're inside a project, you can apply the formatting rule to it and all sub-projects via:
_(source: coding_little_go_book.pdf (source-range-773b6275-00358))_

```
go fmt ./...
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00359))_
