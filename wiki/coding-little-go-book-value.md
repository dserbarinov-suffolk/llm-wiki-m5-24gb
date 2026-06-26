---
page_id: coding-little-go-book-value
page_kind: concept
summary: Value: 39 statement(s) and 10 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-value@c54b55e55b7c594761986b396abb4bcf
---

# Value

What [[coding-little-go-book]] covers about value:

## Statements

- You'll also frequently use _ to discard a value. _(coding_little_go_book.pdf (source-range-810ce361-00105))_
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
- _ , the blank identifier, is special in that the return value isn't actually assigned. _(coding_little_go_book.pdf (source-range-810ce361-00102))_
- What all of the above examples do is declare a variable goku and assign a value to it. _(coding_little_go_book.pdf (source-range-810ce361-00126))_

## Technical atoms

```
value,	exists	:=	power("goku") if exists	==	false	{ //	handle	this	error	case }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00099))_

> As you write Go code, it's natural to ask yourself should this be a value, or a pointer to a value?
_(source: coding_little_go_book.pdf (source-range-810ce361-00174))_

```
for index,	value	:= range scores	{ }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00197))_

> The answer is [1, 2, 3, 4, 5] . That's because slice is a completely new array with copies of values. Now, consider the Go equivalent:
_(source: coding_little_go_book.pdf (source-range-810ce361-00232))_

> If we want all of the values of a slice except the last, we do:
_(source: coding_little_go_book.pdf (source-range-810ce361-00239))_

```
//	won't	preserve	order func removeAtIndex(source	[]int,	index	int)	[]int	{ lastIndex	:=	len(source)	-	1 //swap	the	last	value	and	the	value	we	want	to	remove source[index],	source[lastIndex]	=	source[lastIndex], source[index] return source[:lastIndex] }
```
_(source: coding_little_go_book.pdf (source-range-810ce361-00243))_


## Source

- [[coding-little-go-book]]
