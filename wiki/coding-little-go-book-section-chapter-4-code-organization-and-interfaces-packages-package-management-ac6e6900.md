---
page_id: coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-package-management-ac6e6900
page_kind: source
summary: Chapter 4 - Code Organization and Interfaces / Packages / Package Management: 9 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-package-management-ac6e6900@f8b23a42ce8d3341c03d7acdc259b94d
---

# Chapter 4 - Code Organization and Interfaces / Packages / Package Management

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-57d2c239]] - broader source section: Chapter 4 - Code Organization and Interfaces / Packages
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-visibility-9acaaf15]] - previous source section: Chapter 4 - Code Organization and Interfaces / Packages / Visibility
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-dependency-management-6bec99ea]] - next source section: Chapter 4 - Code Organization and Interfaces / Packages / Dependency Management

## Statements

- The go command we've been using to run and build has a get subcommand which is used to fetch third-party libraries. go get supports various protocols but for this example, we'll be getting a library from Github, meaning, you'll need git installed on your computer. _(coding_little_go_book.pdf (source-range-23d24eb1-00306))_
- Assuming you already have git installed, from a shell/command prompt, enter: _(coding_little_go_book.pdf (source-range-23d24eb1-00307))_
- go get fetches the remote files and stores them in your workspace. Go ahead and check your $GOPATH/src . In addition to the shopping project that we created, you'll now see a github.com folder. Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00309))_
- We just talked about how to import packages that live in our workspace. To use our newly gotten go-sqlite3 package, we'd import it like so: _(coding_little_go_book.pdf (source-range-23d24eb1-00310))_
- Within, you'll see a mattn folder which contains a go-sqlite3 folder. _(coding_little_go_book.pdf (source-range-23d24eb1-00309))_

## Technical atoms

### Technical frame 1: Chapter 4 - Code Organization and Interfaces / Packages / Package Management

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00309))_

> go get fetches the remote files and stores them in your workspace. Go ahead and check your $GOPATH/src . In addition to the shopping project that we created, you'll now see a github.com folder. Within, you'll see a mattn folder which contains a go-sqlite3 folder.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00308))_

```
go get github.com/mattn/go-sqlite3
```

### Technical frame 2: Chapter 4 - Code Organization and Interfaces / Packages / Package Management

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00310))_

> We just talked about how to import packages that live in our workspace. To use our newly gotten go-sqlite3 package, we'd import it like so:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00311))_

```
import (
  "github.com/mattn/go-sqlite3"
)
```
