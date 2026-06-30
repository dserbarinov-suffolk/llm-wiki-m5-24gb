---
page_id: coding-little-go-book-section-chapter-6-concurrency-before-you-continue-a4098176
page_kind: source
summary: Chapter 6 - Concurrency / Before You Continue: 6 source-backed entries and 0 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-6-concurrency-before-you-continue-a4098176@4730115a82c5dcc60fbf690963a7448e
---

# Chapter 6 - Concurrency / Before You Continue

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-6-concurrency-55851f5e]] - broader source section: Chapter 6 - Concurrency
- [[coding-little-go-book-section-chapter-6-concurrency-channels-5666c1f3]] - previous source section: Chapter 6 - Concurrency / Channels
- [[coding-little-go-book-you-continue]] - topic hub: opens the topic page for You Continue

## Statements

- If you're new to the world of concurrent programming, it might all seem rather overwhelming. It categorically demands considerably more attention and care. Go aims to make it easier. _(coding_little_go_book.pdf (source-range-23d24eb1-00467))_
- Goroutines effectively abstract what's needed to run concurrent code. Channels help eliminate some serious bugs that can happen when data is shared by eliminating the sharing of data. This doesn't just eliminate bugs, but it changes how one approaches concurrent programming. You start to think about concurrency with respect to message passing, rather than dangerous areas of code. _(coding_little_go_book.pdf (source-range-23d24eb1-00468))_
- Having said that, I still make extensive use of the various synchronization primitives found in the sync and sync/atomic packages. I think it's important to be comfortable with both. I encourage you to first focus on channels, but when you see a simple example that needs a short-lived lock, consider using a mutex or readwrite mutex. _(coding_little_go_book.pdf (source-range-23d24eb1-00469))_
