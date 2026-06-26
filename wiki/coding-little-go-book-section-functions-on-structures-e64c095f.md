---
page_id: coding-little-go-book-section-functions-on-structures-e64c095f
page_kind: source
summary: Functions on Structures: 3 source-backed entries and 2 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-functions-on-structures-e64c095f@0e10b22dfa87ac168a59393ba062f083
---

# Functions on Structures

From [[coding-little-go-book]].

## Statements

- In the above code, we say that the type *Saiyan is the receiver of the Super method. _(coding_little_go_book.pdf (source-range-810ce361-00142))_

## Technical atoms

```
type Saiyan struct { Name	string Power	int } func (s	*Saiyan)	Super()	{ s.Power	+=	10000 }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00141))_

```
goku	:=	&Saiyan{"Goku",	9001} goku.Super() fmt.Println(goku.Power) //	will	print	19001
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00143))_
