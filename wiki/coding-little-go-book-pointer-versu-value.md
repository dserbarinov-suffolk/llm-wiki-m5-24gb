---
page_id: coding-little-go-book-pointer-versu-value
page_kind: concept
summary: Pointers versus Values: 44 statement(s) and 12 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-pointer-versu-value@0b4116a559a4d93f0e41aa8565fb747f
---

# Pointers versus Values

What [[coding-little-go-book]] covers about pointers versus values:

## Statements

- Secondly, if you aren't sure, use a pointer. _(coding_little_go_book.pdf (source-range-810ce361-00180))_
- You'll also frequently use _ to discard a value. _(coding_little_go_book.pdf (source-range-810ce361-00105))_
- On a 64-bit machine, a pointer is 64 bits large. _(coding_little_go_book.pdf (source-range-810ce361-00137))_
- Just like unassigned variables have a zero value, so do fields. _(coding_little_go_book.pdf (source-range-810ce361-00123))_
- The real value of pointers though is that they let you share values. _(coding_little_go_book.pdf (source-range-810ce361-00137))_
- This is a good time to point out that functions can return multiple values. _(coding_little_go_book.pdf (source-range-810ce361-00096))_
- We'll now have this same conversation with respect to array and map values. _(coding_little_go_book.pdf (source-range-810ce361-00266))_
- Each iteration over a lookup will return the key value pair in a random order. _(coding_little_go_book.pdf (source-range-810ce361-00264))_
- You use this when you know the values that you want in the array ahead of time. _(coding_little_go_book.pdf (source-range-810ce361-00223))_
- In the above example, we simply discard the value that was sent to the channel. _(coding_little_go_book.pdf (source-range-810ce361-00457))_
- Where you will see a difference is when you modify the values of a slice or map. _(coding_little_go_book.pdf (source-range-810ce361-00268))_
- Go's preferred way to deal with errors is through return values, not exceptions. _(coding_little_go_book.pdf (source-range-810ce361-00339))_
- To make this work as you probably expect, we need to pass a pointer to our value: _(coding_little_go_book.pdf (source-range-810ce361-00130))_
- A pointer is a memory address; it's the location of where to find the actual value. _(coding_little_go_book.pdf (source-range-810ce361-00127))_

## Technical atoms

```
value,	exists	:=	power("goku") if exists	==	false	{ //	handle	this	error	case }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00099))_

> It should also be obvious that copying a pointer is going to be cheaper than copying a complex structure.
_(source: coding_little_go_book.pdf (source-range-810ce361-00137))_

> All this isn't to say that you'll always want a pointer.
_(source: coding_little_go_book.pdf (source-range-810ce361-00138))_

> As you write Go code, it's natural to ask yourself should this be a value, or a pointer to a value?
_(source: coding_little_go_book.pdf (source-range-810ce361-00174))_

```
for index,	value	:= range scores	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00197))_

> The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(source: coding_little_go_book.pdf (source-range-810ce361-00232))_


## Source

- [[coding-little-go-book]]
