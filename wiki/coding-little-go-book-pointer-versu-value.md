---
page_id: coding-little-go-book-pointer-versu-value
page_kind: concept
summary: Pointers versus Values: 35 statement(s) and 24 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-pointer-versu-value@02242af384603f067eda3287de6a01a4
---

# Pointers versus Values

What [[coding-little-go-book]] covers about pointers versus values:

## Statements

- Secondly, if you aren't sure, use a pointer. _(coding_little_go_book.pdf (source-range-810ce361-00179))_
- You'll also frequently use _ to discard a value. _(coding_little_go_book.pdf (source-range-810ce361-00104))_
- On a 64-bit machine, a pointer is 64 bits large. _(coding_little_go_book.pdf (source-range-810ce361-00136))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-810ce361-00122))_
- The real value of pointers though is that they let you share values. _(coding_little_go_book.pdf (source-range-810ce361-00136))_
- We'll now have this same conversation with respect to array and map values. _(coding_little_go_book.pdf (source-range-810ce361-00265))_
- Each iteration over a lookup will return the key value pair in a random order. _(coding_little_go_book.pdf (source-range-810ce361-00263))_
- You use this when you know the values that you want in the array ahead of time. _(coding_little_go_book.pdf (source-range-810ce361-00222))_
- In the above example, we simply discard the value that was sent to the channel. _(coding_little_go_book.pdf (source-range-810ce361-00456))_
- Where you will see a difference is when you modify the values of a slice or map. _(coding_little_go_book.pdf (source-range-810ce361-00267))_
- To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-810ce361-00129))_
- A pointer is a memory address; it's the location of where to find the actual value. _(coding_little_go_book.pdf (source-range-810ce361-00126))_
- _ , the blank identifier, is special in that the return value isn't actually assigned. _(coding_little_go_book.pdf (source-range-810ce361-00101))_
- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00125))_

## Code, rules, and examples

> There's more to learn about declaration and assignments. For now, remember that you'll use var NAME TYPE when declaring a variable to its zero value, NAME := VALUE when declaring and assigning a value, and NAME = VALUE when assigning to a previously declared variable.
_(source: coding_little_go_book.pdf (source-range-810ce361-00093))_

> This is a good time to point out that functions can return multiple values.
_(source: coding_little_go_book.pdf (source-range-810ce361-00095))_

```
value,	exists	:=	power("goku") if exists	==	false	{ //	handle	this	error	case }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00098))_

> Sometimes, you only care about one of the return values.
_(source: coding_little_go_book.pdf (source-range-810ce361-00099))_

> It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure.
_(source: coding_little_go_book.pdf (source-range-810ce361-00136))_

> All this isn't to say that you'll always want a pointer.
_(source: coding_little_go_book.pdf (source-range-810ce361-00137))_


## Source

- [[coding-little-go-book]]
