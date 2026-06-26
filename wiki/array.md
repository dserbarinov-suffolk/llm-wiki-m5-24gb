---
page_id: array
page_kind: concept
summary: Canonical concept 'Array': 2 source(s), 13 statement(s), 3 atom(s), 0 relation(s).
sources: raw/coding_learn_go_with_tests_excerpt.pdf, raw/coding_little_go_book.pdf
updated: 2026-06-26
category_path: concepts
projection_coverage: canonical-concept-array@94ee3746406841d3f2a844b62624d7b6
---

# Array

Compiled concept page from 2 source(s), 13 statement(s), and 3 technical atom(s).

## Source Evidence

### [[coding-learn-go-with-tests-excerpt]]

Source topic: [[coding-learn-go-with-tests-excerpt-array]]

#### Statements

- Arrays allow you to store multiple elements of the same type in a variable in a particular order. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00276))_
- An interesting property of arrays is that the size is encoded in its type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00303))_
- Sum will take an array of numbers and return the total. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00277))_
- You may be thinking it's quite cumbersome that arrays have a fixed length, and most of the time you probably won't be using them! _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00304))_

### [[coding-little-go-book]]

Source topic: [[coding-little-go-book-array]]

#### Statements

- In Go, like many other languages, arrays are fixed. _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- Declaring an array requires that we specify the size, and once the size is specified, it cannot grow: _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- The above array can hold up to 10 scores using indexes scores[0] through scores[9] . _(coding_little_go_book.pdf (source-range-773b6275-00193))_
- Attempts to access an out of range index in the array will result in a compiler or runtime error. _(coding_little_go_book.pdf (source-range-773b6275-00193))_
- Arrays are efficient but rigid. _(coding_little_go_book.pdf (source-range-773b6275-00198))_
- These are arrays that resize themselves as data is added to them. _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- If you come from Python, Ruby, Perl, JavaScript or PHP (and more), you're probably used to programming with dynamic arrays . _(coding_little_go_book.pdf (source-range-773b6275-00191))_
- We can use len to get the length of the array. _(coding_little_go_book.pdf (source-range-773b6275-00196))_
- We often don't know the number of elements we'll be dealing with upfront. _(coding_little_go_book.pdf (source-range-773b6275-00198))_

#### Technical atoms

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


## Cross-Source Comparison

- No typed cross-source relationships detected yet.
