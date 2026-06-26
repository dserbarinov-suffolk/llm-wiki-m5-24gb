---
page_id: coding-little-go-book-section-gopath-src-9d97ecd2
page_kind: source
summary: $GOPATH/src: 8 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-gopath-src-9d97ecd2@110dbf6afe84004b821c4ebf36533088
---

# $GOPATH/src

From [[coding-little-go-book]].

## Statements

- Since we moved the shared Item structure to shopping/models/item.go , we need to change shopping/db/db.go to reference the Item structure from models package: _(coding_little_go_book.pdf (source-range-810ce361-00295))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. _(coding_little_go_book.pdf (source-range-810ce361-00295))_
- pricecheck.go will still import shopping/db , but db.go will now import shopping/models instead of shopping , thus breaking the cycle. _(coding_little_go_book.pdf (source-range-810ce361-00295))_
- The important rule about these shared packages is that they shouldn't import anything from the shopping package or any sub-packages. _(coding_little_go_book.pdf (source-range-810ce361-00297))_
- You'll often need to share more than just models , so you might have other similar folders named utilities and such. _(coding_little_go_book.pdf (source-range-810ce361-00297))_
- In a few sections, we'll look at interfaces which can help us untangle these types of dependencies. _(coding_little_go_book.pdf (source-range-810ce361-00297))_

## Technical atoms

```
-	shopping pricecheck.go -	db db.go -	models item.go -	main main.go
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00294))_

```
package db import ( "shopping/models" ) func LoadItem(id	int)	*models.Item	{ return &models.Item{ Price:	9.001, } }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00296))_
