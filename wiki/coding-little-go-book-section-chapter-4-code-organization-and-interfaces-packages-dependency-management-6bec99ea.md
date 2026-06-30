---
page_id: coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-dependency-management-6bec99ea
page_kind: source
summary: Chapter 4 - Code Organization and Interfaces / Packages / Dependency Management: 8 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-dependency-management-6bec99ea@cd0e6297877b9bd1a40e7e17a0643efe
---

# Chapter 4 - Code Organization and Interfaces / Packages / Dependency Management

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-57d2c239]] - broader source section: Chapter 4 - Code Organization and Interfaces / Packages
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-package-management-ac6e6900]] - previous source section: Chapter 4 - Code Organization and Interfaces / Packages / Package Management

## Statements

- go get has a couple of other tricks up its sleeve. If we go get within a project, it'll scan all the files, looking for imports to third-party libraries and will download them. In a way, our own source code becomes a Gemfile or package.json . _(coding_little_go_book.pdf (source-range-23d24eb1-00314))_
- Eventually, you might find go get inadequate. For one thing, there's no way to specify a revision, it always points to the master/head/trunk/default. This is an even larger problem if you have two projects needing different versions of the same library. _(coding_little_go_book.pdf (source-range-23d24eb1-00316))_
- To solve this, you can use a third-party dependency management tool. They are still young, but two promising ones are goop and godep. A more complete list is available at the go-wiki. _(coding_little_go_book.pdf (source-range-23d24eb1-00317))_
