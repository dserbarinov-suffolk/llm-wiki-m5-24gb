---
page_id: coding-little-go-book-slice
page_kind: concept
summary: Slices: 25 statement(s) and 5 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-slice@77de48c8cde60009c25a0634fcabbe2d
---

# Slices

What [[coding-little-go-book]] covers about slices:

## Statements

- Instead, you use slices. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-810ce361-00209))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-810ce361-00230))_
- Maps, like slices, are created with the make function. _(coding_little_go_book.pdf (source-range-810ce361-00249))_
- Appending to a slice of length 0 will set the first element. _(coding_little_go_book.pdf (source-range-810ce361-00211))_
- This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-810ce361-00234))_
- Where you will see a difference is when you modify the values of a slice or map. _(coding_little_go_book.pdf (source-range-810ce361-00268))_
- The second one is useful when you'll be writing into specific indexes of a slice. _(coding_little_go_book.pdf (source-range-810ce361-00224))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00244))_
- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- There are a few ways to create a slice, and we'll go over when to use which later on. _(coding_little_go_book.pdf (source-range-810ce361-00200))_
- The length is the size of the slice, the capacity is the size of the underlying array. _(coding_little_go_book.pdf (source-range-810ce361-00204))_
- To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-810ce361-00220))_

## Technical atoms

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

> If we want all of the values of a slice except the last, we do:
_(source: coding_little_go_book.pdf (source-range-810ce361-00239))_


## Source

- [[coding-little-go-book]]
