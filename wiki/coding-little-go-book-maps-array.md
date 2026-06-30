---
page_id: coding-little-go-book-maps-array
page_kind: concept
summary: Maps Array: 1 statement(s) and 1 atom(s) from raw/coding_little_go_book.pdf.
page_family: topic-concept
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-maps-array@b6cc4030e0053c836520d5d9069ce7c5
---

# Maps Array

What [[coding-little-go-book]] covers about maps array:

## Statements

### Chapter 3 - Maps, Arrays and Slices / Maps

- There's yet another way to declare and initialize values in Go. Like make , this approach is specific to maps and arrays. We can declare as a composite literal: _(coding_little_go_book.pdf (source-range-23d24eb1-00260))_


## Technical atoms

### Technical frame 1: Chapter 3 - Maps, Arrays and Slices / Maps

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00264))_

> Iteration over maps isn't ordered. Each iteration over a lookup will return the key value pair in a random order.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00261))_

```
lookup := map[string]int{
  "goku": 9001,
  "gohan": 2044,
}
```


## Source

- [[coding-little-go-book]]
