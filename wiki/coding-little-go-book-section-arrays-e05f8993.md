---
page_id: coding-little-go-book-section-arrays-e05f8993
page_kind: source
summary: Arrays: 12 source-backed entries and 4 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-arrays-e05f8993@f4cb14a479b5ff2206eb4ef49b520e54
---

# Arrays

From [[coding-little-go-book]].

## Statements

- If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . _(coding_little_go_book.pdf (source-range-810ce361-00191))_
- These are arrays that resize themselves as data is added to them. _(coding_little_go_book.pdf (source-range-810ce361-00191))_
- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-810ce361-00191))_
- Attempts to access an out of range index in the array will result in a compiler or runtime error. _(coding_little_go_book.pdf (source-range-810ce361-00193))_
- The above array can hold up to 10 scores using indexes scores[0] through scores[9] . _(coding_little_go_book.pdf (source-range-810ce361-00193))_
- We can use len to get the length of the array. _(coding_little_go_book.pdf (source-range-810ce361-00196))_
- We often don't know the number of elements we'll be dealing with upfront. _(coding_little_go_book.pdf (source-range-810ce361-00198))_
- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-810ce361-00198))_

## Technical atoms

> Declaring an array requires that we specify the size, and once the size is specified, it cannot grow:
_(source: coding_little_go_book.pdf (source-range-810ce361-00191))_

```
var scores	[10]int scores[0]	=	339
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00192))_

```
scores	:=	[4]int{9001,	9333,	212,	33}
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00195))_

```
for index,	value	:= range scores	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00197))_
