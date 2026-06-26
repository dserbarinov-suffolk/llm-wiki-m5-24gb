---
page_id: coding-little-go-book-array
page_kind: concept
summary: Arrays: 28 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-array@91efa29cb3ace3c54a1c490125b46fd3
---

# Arrays

What [[coding-little-go-book]] covers about arrays:

## Statements

- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-810ce361-00198))_
- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-810ce361-00378))_
- We can use len to get the length of the array. _(coding_little_go_book.pdf (source-range-810ce361-00196))_
- In Go, you rarely, if ever, use arrays directly. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-810ce361-00191))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-810ce361-00260))_
- These are arrays that resize themselves as data is added to them. _(coding_little_go_book.pdf (source-range-810ce361-00191))_
- We'll now have this same conversation with respect to array and map values. _(coding_little_go_book.pdf (source-range-810ce361-00266))_
- You use this when you know the values that you want in the array ahead of time. _(coding_little_go_book.pdf (source-range-810ce361-00223))_
- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- You might be thinking this doesn't actually solve the fixed-length issue of arrays. _(coding_little_go_book.pdf (source-range-810ce361-00213))_

## Technical atoms

> Declaring an array requires that we specify the size, and once the size is specified, it cannot grow:
_(source: coding_little_go_book.pdf (source-range-810ce361-00191))_

```
c	:=	cap(scores) fmt.Println(c) for i	:=	0;	i	<	25;	i++	{ scores	=	append(scores,	i) //	if	our	capacity	has	changed, //	Go	had	to	grow	our	array	to	accommodate	the	new	data if cap(scores)	!=	c	{ c	=	cap(scores) fmt.Println(c) } } }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00216))_

> The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(source: coding_little_go_book.pdf (source-range-810ce361-00232))_


## Source

- [[coding-little-go-book]]
