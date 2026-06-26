---
page_id: coding-little-go-book-section-package-main-1f3863cd
page_kind: source
summary: package main: 8 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-package-main-1f3863cd@5a069c819706f5b9ed8834bbebea1c1c
---

# package main

From [[coding-little-go-book]].

## Statements

- This distinction allows multiple simultaneous readers while ensuring that writing is exclusive. _(coding_little_go_book.pdf (source-range-810ce361-00423))_
- While read-write mutexes are commonly used, they place an additional burden on developers: we must now pay attention to not only when we're accessing data, but also how. _(coding_little_go_book.pdf (source-range-810ce361-00423))_
- For one thing, there's another common mutex called a read-write mutex. _(coding_little_go_book.pdf (source-range-810ce361-00423))_
- In Go, sync.RWMutex is such a lock. _(coding_little_go_book.pdf (source-range-810ce361-00423))_
- While read-write mutexes are commonly used, they place an additional burden on developers: we must now pay attention to not only when we're accessing data, but also how. _(coding_little_go_book.pdf (source-range-810ce361-00423))_
- For example, sleeping for 10 milliseconds isn't a particularly elegant solution. _(coding_little_go_book.pdf (source-range-810ce361-00424))_
- These are all things that are doable without channels . _(coding_little_go_book.pdf (source-range-810ce361-00425))_

## Technical atoms

```
import ( "time" "sync" ) var ( lock	sync.Mutex ) func main()	{ go func ()	{	lock.Lock()	}() time.Sleep(time.Millisecond	*	10) lock.Lock() }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00422))_
