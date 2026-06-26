---
page_id: coding-little-go-book-maps-array-slice
page_kind: concept
summary: Maps, Arrays and Slices: 46 statement(s) and 7 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-maps-array-slice@51562bfe4b4abe64a2c5ee3da584ed6f
---

# Maps, Arrays and Slices

What [[coding-little-go-book]] covers about maps, arrays and slices:

## Statements

- Instead, you use slices. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-810ce361-00198))_
- Iteration over maps isn't ordered. _(coding_little_go_book.pdf (source-range-810ce361-00264))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-810ce361-00209))_
- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-810ce361-00378))_
- We can use len to get the length of the array. _(coding_little_go_book.pdf (source-range-810ce361-00196))_
- In Go, you rarely, if ever, use arrays directly. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-810ce361-00191))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Maps, like slices, are created with the make function. _(coding_little_go_book.pdf (source-range-810ce361-00249))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-810ce361-00260))_
- Appending to a slice of length 0 will set the first element. _(coding_little_go_book.pdf (source-range-810ce361-00211))_

## Technical atoms

> Declaring an array requires that we specify the size, and once the size is specified, it cannot grow:
_(source: coding_little_go_book.pdf (source-range-810ce361-00191))_

```
c	:=	cap(scores) fmt.Println(c) for i	:=	0;	i	<	25;	i++	{ scores	=	append(scores,	i) //	if	our	capacity	has	changed, //	Go	had	to	grow	our	array	to	accommodate	the	new	data if cap(scores)	!=	c	{ c	=	cap(scores) fmt.Println(c) } } }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00216))_

```
scores = [ 1,2,3,4,5 ] slice = scores [ 2 .. 4 ] slice [ 0 ] = 999 puts	scores
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00231))_

> The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(source: coding_little_go_book.pdf (source-range-810ce361-00232))_

```
scores	:=	[]int{1,2,3,4,5} slice	:=	scores[2:4] slice[0]	=	999 fmt.Println(scores)
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00233))_

> This changes how you code. For example, a number of functions take a position parameter. In JavaScript, if we want to find the first space in a string (yes, slices work on strings too!) after the first five characters, we'd write:
_(source: coding_little_go_book.pdf (source-range-810ce361-00235))_


## Source

- [[coding-little-go-book]]
