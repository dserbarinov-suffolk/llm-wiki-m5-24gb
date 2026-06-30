---
page_id: coding-little-go-book-section-chapter-3-maps-arrays-and-slices-pointers-versus-values-61a54414
page_kind: source
summary: Chapter 3 - Maps, Arrays and Slices / Pointers versus Values: 6 source-backed entries and 1 atom(s) from raw/coding_little_go_book.pdf.
page_family: section-reference
sources: raw/coding_little_go_book.pdf
updated: 2026-06-30
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-3-maps-arrays-and-slices-pointers-versus-values-61a54414@505008424e45a6cab4c07e32222ee205
---

# Chapter 3 - Maps, Arrays and Slices / Pointers versus Values

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-4800f0d1]] - broader source section: Chapter 3 - Maps, Arrays and Slices
- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-maps-cf61ad17]] - previous source section: Chapter 3 - Maps, Arrays and Slices / Maps
- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-before-you-continue-97563f70]] - next source section: Chapter 3 - Maps, Arrays and Slices / Before You Continue
- [[coding-little-go-book-pointer-versus-value]] - topic hub: opens the topic page for Pointer Versus Value

## Statements

- We finished Chapter 2 by looking at whether you should assign and pass pointers or values. We'll now have this same conversation with respect to array and map values. Which of these should you use? _(coding_little_go_book.pdf (source-range-23d24eb1-00266))_
- Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice, which itself is a reference. So with respect to passing/returning the slice itself, there's no difference. Where you will see a difference is when you modify the values of a slice or map. At this point, the same logic that we saw in Chapter 2 applies. So the decision on whether to define an array of pointers versus an array of values comes down to how you use the individual values, not how you use the array or map itself. _(coding_little_go_book.pdf (source-range-23d24eb1-00268))_

## Technical atoms

### Technical frame 1: Chapter 3 - Maps, Arrays and Slices / Pointers versus Values

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00268))_

> Many developers think that passing b to, or returning it from, a function is going to be more efficient. However, what's being passed/returned is a copy of the slice, which itself is a reference. So with respect to passing/returning the slice itself, there's no difference. Where you will see a difference is when you modify the values of a slice or map. At this point, the same logic that we saw in Chapter 2 applies. So the decision on whether to define an array of pointers versus an array of valu

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00267))_

```
a := make([]Saiyan, 10)
//or
b := make([]*Saiyan, 10)
```
