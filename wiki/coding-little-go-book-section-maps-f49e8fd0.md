---
page_id: coding-little-go-book-section-maps-f49e8fd0
page_kind: source
summary: Maps: 15 source-backed entries and 7 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-maps-f49e8fd0@1953469bf5d39cd7d8a8ff26d0c1c019
---

# Maps

From [[coding-little-go-book]].

## Statements

- They work as you expect: you define a key and value, and can get, set and delete values from it. _(coding_little_go_book.pdf (source-range-810ce361-00248))_
- Maps in Go are what other languages call hashtables or dictionaries. _(coding_little_go_book.pdf (source-range-810ce361-00248))_
- Maps, like slices, are created with the make function. _(coding_little_go_book.pdf (source-range-810ce361-00249))_
- To get the number of keys, we use len . _(coding_little_go_book.pdf (source-range-810ce361-00251))_
- If you have some idea of how many keys your map will have, defining an initial size can help with performance. _(coding_little_go_book.pdf (source-range-810ce361-00255))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-810ce361-00260))_
- Iteration over maps isn't ordered. _(coding_little_go_book.pdf (source-range-810ce361-00264))_
- Each iteration over a lookup will return the key value pair in a random order. _(coding_little_go_book.pdf (source-range-810ce361-00264))_

## Technical atoms

```
func main()	{ lookup	:=	make( map [string]int) lookup["goku"]	=	9001 power,	exists	:=	lookup["vegeta"] //	prints	0,	false //	0	is	the	default	value	for	an	integer fmt.Println(power,	exists) }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00250))_

```
//	returns	1 total	:=	len(lookup) //	has	no	return,	can	be	called	on	a	non-existing	key delete(lookup,	"goku")
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00252))_

```
lookup	:=	make( map [string]int,	100)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00254))_

```
type Saiyan struct { Name	string Friends map [string]*Saiyan }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00257))_

```
goku	:=	&Saiyan{ Name:	"Goku", Friends:	make( map [string]*Saiyan), } goku.Friends["krillin"]	=	... //todo	load	or	create	Krillin
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00259))_

```
lookup	:= map [string]int{ "goku":	9001, "gohan":	2044, }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00261))_

```
for key,	value	:= range lookup	{ ... }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00263))_
