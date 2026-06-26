---
page_id: coding-little-go-book-section-function-type-0c505106
page_kind: source
summary: Function Type: 5 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-function-type-0c505106@8b8ad7f65731f24bcb896b039d0eb916
---

# Function Type

From [[coding-little-go-book]].

## Statements

- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-810ce361-00389))_
- which can then be used anywhere -- as a field type, as a parameter, as a return value. _(coding_little_go_book.pdf (source-range-810ce361-00389))_

## Technical atoms

```
type Add func (a	int,	b	int)	int
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00388))_

```
package main import ( "fmt" )
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00390))_

```
type Add func (a	int,	b	int)	int func main()	{ fmt.Println(process( func (a	int,	b	int)	int{ return a	+	b })) } func process(adder	Add)	int	{ return adder(1,	2) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00391))_
