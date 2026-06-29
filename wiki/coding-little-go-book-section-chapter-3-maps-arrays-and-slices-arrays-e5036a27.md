---
page_id: coding-little-go-book-section-chapter-3-maps-arrays-and-slices-arrays-e5036a27
page_kind: source
summary: Chapter 3 - Maps, Arrays and Slices / Arrays: 12 source-backed entries and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-29
domain: coding-little-go-book
category_path: sources/coding-little-go-book/sections
source_id: coding_little_go_book.pdf
projection_coverage: section-coding-little-go-book-section-chapter-3-maps-arrays-and-slices-arrays-e5036a27@6f1018d4463048ebb6f39e47e41e99fb
---

# Chapter 3 - Maps, Arrays and Slices / Arrays

From [[coding-little-go-book]].

## Related pages

- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-4800f0d1]] - broader source section: Chapter 3 - Maps, Arrays and Slices
- [[coding-little-go-book-section-chapter-3-maps-arrays-and-slices-slices-7f1a7b05]] - next source section: Chapter 3 - Maps, Arrays and Slices / Slices
- [[coding-little-go-book-array]] - topic hub: opens the topic page for Array

## Statements

- If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves as data is added to them. In Go, like many other languages, arrays are fixed. Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: _(coding_little_go_book.pdf (source-range-23d24eb1-00191))_
- The above array can hold up to 10 scores using indexes scores[0] through scores[9] . Attempts to access an out of range index in the array will result in a compiler or runtime error. _(coding_little_go_book.pdf (source-range-23d24eb1-00193))_
- We can use len to get the length of the array. range can be used to iterate over it: _(coding_little_go_book.pdf (source-range-23d24eb1-00196))_
- Arrays are efficient but rigid. We often don't know the number of elements we'll be dealing with upfront. For this, we turn to slices. _(coding_little_go_book.pdf (source-range-23d24eb1-00198))_

## Technical atoms

### Technical frame 1: Chapter 3 - Maps, Arrays and Slices / Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00193))_

> The above array can hold up to 10 scores using indexes scores[0] through scores[9] . Attempts to access an out of range index in the array will result in a compiler or runtime error.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00192))_

```
var scores [10]int
scores[0] = 339
```

### Technical frame 2: Chapter 3 - Maps, Arrays and Slices / Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00196))_

> We can use len to get the length of the array. range can be used to iterate over it:

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00195))_

```
scores := [4]int{9001, 9333, 212, 33}
```

### Technical frame 3: Chapter 3 - Maps, Arrays and Slices / Arrays

**Context:** _(coding_little_go_book.pdf (source-range-23d24eb1-00198))_

> Arrays are efficient but rigid. We often don't know the number of elements we'll be dealing with upfront. For this, we turn to slices.

**Atom:** _(coding_little_go_book.pdf (source-range-23d24eb1-00197))_

```
for index, value := range scores {
}
```
