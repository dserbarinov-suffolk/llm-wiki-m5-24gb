---
page_id: coding-little-go-book-package-management
page_kind: concept
summary: Package Management: 6 statement(s) and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-package-management@6aae08b0457b88b8885e7373bf209429
---

# Package Management

What [[coding-little-go-book]] covers about package management:

## Statements

- We just talked about how to import packages that live in our workspace. _(coding_little_go_book.pdf (source-range-773b6275-00310))_
- The go command we've been using to run and build has a get subcommand which is used to fetch third-party libraries. _(coding_little_go_book.pdf (source-range-773b6275-00306))_
- go get supports various protocols but for this example, we'll be getting a library from Github, meaning, you'll need git installed on your computer. _(coding_little_go_book.pdf (source-range-773b6275-00306))_
- Assuming you already have git installed, from a shell/command prompt, enter: _(coding_little_go_book.pdf (source-range-773b6275-00307))_
- In addition to the shopping project that we created, you'll now see a github.com folder. _(coding_little_go_book.pdf (source-range-773b6275-00309))_
- Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-773b6275-00309))_

## Technical atoms

> Context: Assuming you already have git installed, from a shell/command prompt, enter:
_(context: coding_little_go_book.pdf (source-range-773b6275-00307))_

```
go get github.com/mattn/go-sqlite3
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00308))_

> Context: We just talked about how to import packages that live in our workspace. To use our newly gotten go-sqlite3 package, we'd import it like so:
_(context: coding_little_go_book.pdf (source-range-773b6275-00310))_

```
import (
  "github.com/mattn/go-sqlite3"
)
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00311))_


## Source

- [[coding-little-go-book]]
