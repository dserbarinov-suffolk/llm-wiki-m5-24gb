---
page_id: coding-little-go-book-array
page_kind: concept
summary: Arrays: 9 statement(s) and 3 atom(s) from raw/coding_little_go_book.pdf.
sources: raw/coding_little_go_book.pdf
updated: 2026-06-26
domain: coding-little-go-book
category_path: concepts
projection_coverage: topic-coding-little-go-book-array@c34a5090a655aa9fbd00c361b4af9fe1
---

# Arrays

What [[coding-little-go-book]] covers about arrays:

## Statements

- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- These are arrays that resize themselves as data is added to them. _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- The above array can hold up to 10 scores using indexes scores[0] through scores[9] . _(coding_little_go_book.pdf (source-range-773b6275-00193))_
- Attempts to access an out of range index in the array will result in a compiler or runtime error. _(coding_little_go_book.pdf (source-range-773b6275-00193))_
- We can use len to get the length of the array. _(coding_little_go_book.pdf (source-range-773b6275-00196))_
- We often don't know the number of elements we'll be dealing with upfront. _(coding_little_go_book.pdf (source-range-773b6275-00198))_
- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-773b6275-00198))_

## Technical atoms

> Context: If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . These are arrays that resize themselves as data is added to them. In Go, like many other languages, arrays are fixed. Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: The above array can hold up to 10 scores using indexes scores[0] through scores[9] . Attempts to access an out of range index in the array will result in a compiler or runtime error.
_(context: coding_little_go_book.pdf (source-range-773b6275-00191, source-range-773b6275-00193))_

```
var scores [10]int
scores[0] = 339
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00192))_

> Context: We can initialize the array with values:
_(context: coding_little_go_book.pdf (source-range-773b6275-00194))_

```
scores := [4]int{9001, 9333, 212, 33}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00195))_

> Context: We can use len to get the length of the array. range can be used to iterate over it:
_(context: coding_little_go_book.pdf (source-range-773b6275-00196))_

```
for index, value := range scores {
}
```
_(source: coding_little_go_book.pdf (source-range-773b6275-00197))_


## Source

- [[coding-little-go-book]]
