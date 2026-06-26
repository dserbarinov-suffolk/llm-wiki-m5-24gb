---
page_id: coding-little-go-book-section-package-db-daa35d4e
page_kind: source
summary: package db: 13 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-package-db-daa35d4e@545014aaa3462ed1d7bbf10dd875f4a6
---

# package db

From [[coding-little-go-book]].

## Statements

- We're just using this as an example to show how to organize code. _(coding_little_go_book.pdf (source-range-810ce361-00277))_
- Notice that the name of the package is the same as the name of the folder. _(coding_little_go_book.pdf (source-range-810ce361-00277))_
- Now, create a file called pricecheck.go inside of the main shopping folder. _(coding_little_go_book.pdf (source-range-810ce361-00278))_
- Now, create a file called pricecheck.go inside of the main shopping folder. _(coding_little_go_book.pdf (source-range-810ce361-00278))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. _(coding_little_go_book.pdf (source-range-810ce361-00280))_
- It's tempting to think that importing shopping/db is somehow special because we're inside the shopping package/folder already. _(coding_little_go_book.pdf (source-range-810ce361-00280))_
- To build an executable, you still need a main . _(coding_little_go_book.pdf (source-range-810ce361-00281))_
- The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-810ce361-00281))_
- If you're building a package, you don't need anything more than what we've seen. _(coding_little_go_book.pdf (source-range-810ce361-00281))_
- The way I prefer to do this is to create a subfolder called main inside of shopping with a file called main.go and the following content: _(coding_little_go_book.pdf (source-range-810ce361-00281))_

## Technical atoms

```
type Item struct { Price	float64 } func LoadItem(id	int)	*Item	{ return &Item{ Price:	9.001, } }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00276))_

```
package shopping import ( "shopping/db" ) func PriceCheck(itemId	int)	(float64,	bool)	{ item	:=	db.LoadItem(itemId) if item	==	nil	{ return 0,	false } return item.Price,	true }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00279))_

```
package main import ( "shopping" "fmt" ) func main()	{ fmt.Println(shopping.PriceCheck(4343)) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00282))_
