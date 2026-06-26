---
page_id: coding-little-go-book-section-visibility-de11476d
page_kind: source
summary: Visibility: 7 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-visibility-de11476d@f8f9a09ea2931f89cec35672e17c13f7
---

# Visibility

From [[coding-little-go-book]].

## Statements

- Go uses a simple rule to define what types and functions are visible outside of a package. _(coding_little_go_book.pdf (source-range-810ce361-00299))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-810ce361-00300))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-810ce361-00300))_
- But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-810ce361-00303))_
- it could be called via models.NewItem() . _(coding_little_go_book.pdf (source-range-810ce361-00303))_

## Technical atoms

```
func NewItem()	*Item	{ //	... }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00302))_

> For example, if you rename the Item's Price field to price , you should get an error.
_(source: coding_little_go_book.pdf (source-range-810ce361-00304))_
