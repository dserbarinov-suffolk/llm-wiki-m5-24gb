---
page_id: coding-little-go-book-section-package-management-3e50ca61
page_kind: source
summary: Package Management: 9 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-package-management-3e50ca61@d7fd4dd806a570da1d4797fc26957960
---

# Package Management

From [[coding-little-go-book]].

## Statements

- The go command we've been using to run and build has a get subcommand which is used to fetch third-party libraries. _(coding_little_go_book.pdf (source-range-773b6275-00306))_
- go get supports various protocols but for this example, we'll be getting a library from Github, meaning, you'll need git installed on your computer. _(coding_little_go_book.pdf (source-range-773b6275-00306))_
- Assuming you already have git installed, from a shell/command prompt, enter: _(coding_little_go_book.pdf (source-range-773b6275-00307))_
- In addition to the shopping project that we created, you'll now see a github.com folder. _(coding_little_go_book.pdf (source-range-773b6275-00309))_
- Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-773b6275-00309))_
- Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-773b6275-00309))_
- We just talked about how to import packages that live in our workspace. _(coding_little_go_book.pdf (source-range-773b6275-00310))_

## Technical atoms

```
go get github.com/mattn/go-sqlite3
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00308))_

```
import (
  "github.com/mattn/go-sqlite3"
)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00311))_
