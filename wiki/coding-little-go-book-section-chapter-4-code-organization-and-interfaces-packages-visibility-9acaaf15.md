---
page_id: coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-visibility-9acaaf15
page_kind: source
summary: Chapter 4 - Code Organization and Interfaces / Packages / Visibility: 7 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-visibility-9acaaf15@2bb4fcf496625e07a9c4f82062b3cf17
---

# Chapter 4 - Code Organization and Interfaces / Packages / Visibility

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-57d2c239]] - broader source section: Chapter 4 - Code Organization and Interfaces / Packages
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-cyclical-imports-bbcc282e]] - previous source section: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-package-management-ac6e6900]] - next source section: Chapter 4 - Code Organization and Interfaces / Packages / Package Management

## Statements

- Go uses a simple rule to define what types and functions are visible outside of a package. If the name of the type or function starts with an uppercase letter, it's visible. If it starts with a lowercase letter, it isn't. _(coding_little_go_book.pdf (source-range-23d24eb1-00299))_
- This also applies to structure fields. If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_
- it could be called via models.NewItem() . But if the function was named newItem , we wouldn't be able to access it from a different package. _(coding_little_go_book.pdf (source-range-23d24eb1-00303))_
- If a structure field name starts with a lowercase letter, only code within the same package will be able to access them. _(coding_little_go_book.pdf (source-range-23d24eb1-00300))_

## Technical atoms

### Technical frame 1: Chapter 4 - Code Organization and Interfaces / Packages / Visibility

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00303))_

> it could be called via models.NewItem() . But if the function was named newItem , we wouldn't be able to access it from a different package.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00302))_

```
func NewItem() *Item {
  // ...
}
```

### Technical frame 2: Chapter 4 - Code Organization and Interfaces / Packages / Visibility

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00303))_

> it could be called via models.NewItem() . But if the function was named newItem , we wouldn't be able to access it from a different package.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00304))_

> For example, if you rename the Item's Price field to price , you should get an error.
