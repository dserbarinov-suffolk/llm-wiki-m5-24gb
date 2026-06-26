---
page_id: coding-little-go-book-section-dependency-management-ee040459
page_kind: source
summary: Dependency Management: 9 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-dependency-management-ee040459@e6de3cafb405bb15d08b391d2a522a44
---

# Dependency Management

From [[coding-little-go-book]].

## Statements

- In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-810ce361-00314))_
- go get has a couple of other tricks up its sleeve. _(coding_little_go_book.pdf (source-range-810ce361-00314))_
- If you call go get -u it'll update the packages (or you can update a specific package via go get -u FULL_PACKAGE_NAME ). _(coding_little_go_book.pdf (source-range-810ce361-00315))_
- This is an even larger problem if you have two projects needing different versions of the same library. _(coding_little_go_book.pdf (source-range-810ce361-00316))_
- Eventually, you might find go get inadequate. _(coding_little_go_book.pdf (source-range-810ce361-00316))_
- They are still young, but two promising ones are goop and godep. _(coding_little_go_book.pdf (source-range-810ce361-00317))_
- To solve this, you can use a third-party dependency management tool. _(coding_little_go_book.pdf (source-range-810ce361-00317))_
- A more complete list is available at the go-wiki. _(coding_little_go_book.pdf (source-range-810ce361-00317))_

## Technical atoms

> For one thing, there's no way to specify a revision, it always points to the master/head/trunk/default.
_(source: coding_little_go_book.pdf (source-range-810ce361-00316))_
