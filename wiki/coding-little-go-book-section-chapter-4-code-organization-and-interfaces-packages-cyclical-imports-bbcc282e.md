---
page_id: coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-cyclical-imports-bbcc282e
page_kind: source
summary: Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports: 14 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-cyclical-imports-bbcc282e@d5abcfcbac3f370eaa882a665dd31315
---

# Chapter 4 - Code Organization and Interfaces / Packages / Cyclical Imports

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-57d2c239]] - broader source section: Chapter 4 - Code Organization and Interfaces / Packages
- [[coding-little-go-book-section-chapter-4-code-organization-and-interfaces-packages-visibility-9acaaf15]] - next source section: Chapter 4 - Code Organization and Interfaces / Packages / Visibility

## Statements

- As you start writing more complex systems, you're bound to run into cyclical imports. This happens when package A imports package B but package B imports package A (either directly or indirectly through another package). This is something the compiler won't allow. _(coding_little_go_book.pdf (source-range-23d24eb1-00286))_
- If you try to run the code, you'll get a couple of errors from db/db.go about Item being undefined. This makes sense. Item no longer exists in the db package; it's been moved to the shopping package. We need to change shopping/db/db.go to: _(coding_little_go_book.pdf (source-range-23d24eb1-00290))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package: _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_
- You'll often need to share more than just models , so you might have other similar folders named utilities and such. The important rule about these shared packages is that they shouldn't import anything from the shopping package or any sub-packages. In a few sections, we'll look at interfaces which can help us untangle these types of dependencies. _(coding_little_go_book.pdf (source-range-23d24eb1-00297))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. _(coding_little_go_book.pdf (source-range-23d24eb1-00295))_
