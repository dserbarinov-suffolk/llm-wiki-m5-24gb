---
page_id: coding-little-go-book-array
page_kind: concept
summary: Arrays: 23 statement(s) and 11 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-array@7ff0f892328b1d23846b763660160891
---

# Arrays

What [[coding-little-go-book]] covers about arrays:

## Statements

- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-810ce361-00197))_
- Strings and byte arrays are closely related. _(coding_little_go_book.pdf (source-range-810ce361-00377))_
- In Go, you rarely, if ever, use arrays directly. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-810ce361-00190))_
- Slices as wrappers to arrays is a powerful concept. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Many languages have the concept of slicing an array. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Both JavaScript and Ruby arrays have a slice method. _(coding_little_go_book.pdf (source-range-810ce361-00229))_
- Like make , this approach is specific to maps and arrays. _(coding_little_go_book.pdf (source-range-810ce361-00259))_
- These are arrays that resize themselves as data is added to them. _(coding_little_go_book.pdf (source-range-810ce361-00190))_
- We'll now have this same conversation with respect to array and map values. _(coding_little_go_book.pdf (source-range-810ce361-00265))_
- You use this when you know the values that you want in the array ahead of time. _(coding_little_go_book.pdf (source-range-810ce361-00222))_
- A slice is a lightweight structure that wraps and represents a portion of an array. _(coding_little_go_book.pdf (source-range-810ce361-00199))_
- You might be thinking this doesn't actually solve the fixed-length issue of arrays. _(coding_little_go_book.pdf (source-range-810ce361-00212))_
- The length is the size of the slice, the capacity is the size of the underlying array. _(coding_little_go_book.pdf (source-range-810ce361-00203))_

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
