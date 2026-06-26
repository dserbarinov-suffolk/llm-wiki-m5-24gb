---
page_id: coding-little-go-book-section-dependency-management-e63019ff
page_kind: source
summary: Dependency Management: 8 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-dependency-management-e63019ff@3a6fbefaf405d511aaff6af89d8fbdd4
---

# Dependency Management

From [[coding-little-go-book]].

## Statements

- go get has a couple of other tricks up its sleeve. _(coding_little_go_book.pdf (source-range-773b6275-00314))_
- In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-773b6275-00314))_
- This is an even larger problem if you have two projects needing different versions of the same library. _(coding_little_go_book.pdf (source-range-773b6275-00316))_
- Eventually, you might find go get inadequate. _(coding_little_go_book.pdf (source-range-773b6275-00316))_
- To solve this, you can use a third-party dependency management tool. _(coding_little_go_book.pdf (source-range-773b6275-00317))_
- A more complete list is available at the go-wiki. _(coding_little_go_book.pdf (source-range-773b6275-00317))_
- They are still young, but two promising ones are goop and godep. _(coding_little_go_book.pdf (source-range-773b6275-00317))_

## Technical atoms

> If you call go get -u it'll update the packages (or you can update a specific package via go get -u FULL_PACKAGE_NAME ).
_(source: coding_little_go_book.pdf (source-range-773b6275-00315))_
