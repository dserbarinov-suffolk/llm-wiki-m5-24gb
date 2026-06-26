---
page_id: coding-little-go-book-maps-array-slice
page_kind: concept
summary: Maps, Arrays and Slices: 37 statement(s) and 21 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-maps-array-slice@d01d4ec736d9c916f8bb79a6cb249683
---

# Maps, Arrays and Slices

What [[coding-little-go-book]] covers about maps, arrays and slices:

## Statements

- Instead, you use slices. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-810ce361-00197))_
- Iteration over maps isn't ordered. _(coding_little_go_book.pdf (source-range-810ce361-00263))_
- Because our slice has a length of 0. _(coding_little_go_book.pdf (source-range-810ce361-00208))_
- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-810ce361-00377))_
- In Go, you rarely, if ever, use arrays directly. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-810ce361-00190))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-810ce361-00259))_
- Appending to a slice of length 0 will set the first element. _(coding_little_go_book.pdf (source-range-810ce361-00210))_
- This is because our slice is really just a window into scores . _(coding_little_go_book.pdf (source-range-810ce361-00233))_
- These are arrays that resize themselves as data is added to them. _(coding_little_go_book.pdf (source-range-810ce361-00190))_

## Code, rules, and examples

> Saying that a language has a C-like syntax means that if you're used to any other C-like languages such as C, C++, Java, JavaScript and C#, then you're going to find Go familiar -- superficially, at least. For example, it means && is used as a boolean AND, == is used to compare equality, { and } start and end a scope, and array indexes start at 0.
_(source: coding_little_go_book.pdf (source-range-810ce361-00039))_

> Fields can be of any type -including other structures and types that we haven't explored yet such as arrays, maps, interfaces and functions.
_(source: coding_little_go_book.pdf (source-range-810ce361-00156))_

> Declaring an array requires that we specify the size, and once the size is specified, it cannot grow:
_(source: coding_little_go_book.pdf (source-range-810ce361-00190))_

> The above array can hold up to 10 scores using indexes scores[0] through scores[9] .
_(source: coding_little_go_book.pdf (source-range-810ce361-00192))_

> We can initialize the array with values:
_(source: coding_little_go_book.pdf (source-range-810ce361-00193))_

> We can use len to get the length of the array.
_(source: coding_little_go_book.pdf (source-range-810ce361-00195))_


## Source

- [[coding-little-go-book]]
