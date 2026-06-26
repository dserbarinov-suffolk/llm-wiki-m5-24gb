---
page_id: coding-little-go-book-section-new-9210a34b
page_kind: source
summary: New: 5 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-new-9210a34b@56e9a20f5df4fe91ba2918bf3dab825a
---

# New

From [[coding-little-go-book]].

## Statements

- Which you use is up to you, but you'll find that most people prefer the latter whenever they have fields to initialize, since it tends to be easier to read: _(coding_little_go_book.pdf (source-range-810ce361-00153))_
- Whichever approach you choose, if you follow the factory pattern above, you can shield the rest of your code from knowing and worrying about any of the allocation details. _(coding_little_go_book.pdf (source-range-810ce361-00155))_

## Technical atoms

> Despite the lack of constructors, Go does have a built-in new function which is used to allocate the memory required by a type.
_(source: coding_little_go_book.pdf (source-range-810ce361-00151))_

```
goku	:=	new(Saiyan) //	same	as goku	:=	&Saiyan{}
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00152))_

```
goku	:=	new(Saiyan) goku.Name	=	"goku" goku.Power	=	9001 //vs goku	:=	&Saiyan	{ Name:	"goku", Power:	9000, }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00154))_
