---
page_id: coding-little-go-book-slice
page_kind: concept
summary: Slices: 20 statement(s) and 12 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-slice@bca496227b6466f16acfcc024a5af488
---

# Slices

What [[coding-little-go-book]] covers about slices:

## Statements

- Instead, you use slices. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-810ce361-00208))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Appending to a slice of length 0 will set the first element. _(coding_little_go_book.pdf (source-range-810ce361-00210))_
- This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-810ce361-00233))_
- Where you will see a difference is when you modify the values of a slice or map. _(coding_little_go_book.pdf (source-range-810ce361-00267))_
- copy is one of those functions that highlights how slices change the way we code. _(coding_little_go_book.pdf (source-range-810ce361-00243))_
- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- There are a few ways to create a slice, and we'll go over when to use which later on. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- The length is the size of the slice, the capacity is the size of the underlying array. _(coding_little_go_book.pdf (source-range-810ce361-00203))_
- To a compiler, you're telling it to append a value to a slice that already holds 5 values. _(coding_little_go_book.pdf (source-range-810ce361-00219))_
- However, what's being passed/returned is a copy of the slice, which itself is a reference. _(coding_little_go_book.pdf (source-range-810ce361-00267))_
- Slices are powerful and they have a surprisingly large impact on the clarity of your code. _(coding_little_go_book.pdf (source-range-810ce361-00269))_

## Code, rules, and examples

> Specifically, we have to allocate the memory for the underlying array and also initialize the slice.
_(source: coding_little_go_book.pdf (source-range-810ce361-00203))_

> To do this, we can re-slice our slice:
_(source: coding_little_go_book.pdf (source-range-810ce361-00210))_

> How large can we resize a slice?
_(source: coding_little_go_book.pdf (source-range-810ce361-00212))_

> The second one is useful when you'll be writing into specific indexes of a slice. For example:
_(source: coding_little_go_book.pdf (source-range-810ce361-00223))_

> You can also get a slice in Ruby by using [START..END] or in Python via [START:END] .
_(source: coding_little_go_book.pdf (source-range-810ce361-00229))_

```
scores = [ 1,2,3,4,5 ] slice = scores [ 2 .. 4 ] slice [ 0 ] = 999 puts	scores
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00230))_


## Source

- [[coding-little-go-book]]
