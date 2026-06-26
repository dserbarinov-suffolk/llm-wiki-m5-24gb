---
page_id: coding-little-go-book-section-function-declarations-592d3e67
page_kind: source
summary: Function Declarations: 10 source-backed entries and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-function-declarations-592d3e67@53dc7285a39cddbb8bfbbf84210aa2c2
---

# Function Declarations

From [[coding-little-go-book]].

## Statements

- This is a good time to point out that functions can return multiple values. _(coding_little_go_book.pdf (source-range-810ce361-00096))_
- Sometimes, you only care about one of the return values. _(coding_little_go_book.pdf (source-range-810ce361-00100))_
- This lets you use _ over and over again regardless of the returned type. _(coding_little_go_book.pdf (source-range-810ce361-00102))_
- This is more than a convention. _(coding_little_go_book.pdf (source-range-810ce361-00102))_
- _ , the blank identifier, is special in that the return value isn't actually assigned. _(coding_little_go_book.pdf (source-range-810ce361-00102))_
- You'll also frequently use _ to discard a value. _(coding_little_go_book.pdf (source-range-810ce361-00105))_

## Technical atoms

```
func log(message	string)	{ } func add(a	int,	b	int)	int	{ } func power(name	string)	(int,	bool)	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00097))_

```
value,	exists	:=	power("goku") if exists	==	false	{ //	handle	this	error	case }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00099))_

```
_,	exists	:=	power("goku") if exists	==	false	{ //	handle	this	error	case }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00101))_

```
func add(a,	b	int)	int	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00104))_
