---
page_id: coding-learn-go-with-tests-excerpt-array
page_kind: concept
summary: Array: 14 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-array@a2677e19981a180832c82c39e06d2023
---

# Array

What [[coding-learn-go-with-tests-excerpt]] covers about array:

## Statements

- Sum will take an array of numbers and return the total. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00277))_
- When you have arrays, it is very common to have to iterate over them. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00277))_
- An interesting property of arrays is that the size is encoded in its type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00303))_
- Arrays have a fi xed capacity which you define when you declare the variable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00282))_
- Getting a value out of a Map is the same as getting a value out of Array map[key] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00562))_
- To get the value out of an array at a particular index, just use array[index] syntax. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00297))_
- Arrays allow you to store multiple elements of the same type in a variable in a particular order. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00276))_
- Here, we are using the %v placeholder to print the "default" format, which works well for arrays. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00285))_
- You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with = _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00357))_
- In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00297))_
- We've used slices and arrays with integers but they work with any other type too, including arrays/slices themselves. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00404))_
- You may be thinking it's quite cumbersome that arrays have a fixed length, and most of the time you probably won't be using them! _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00304))_
- If you try to run the tests they will still not compile, you will have to change the first test to pass in a slice rather than an array. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00321))_
- Here is an example of slicing an array and how changing the slice affects the original array; but a "copy" of the slice will not affect the original array. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00407))_

## Technical atoms

> We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00325))_

> There's a new way to create a slice. make allows you to create a slice with a starting capacity of the len of the numbersToSum we need to work through. The length of a slice is the number of elements it holds len(mySlice) , while the capacity is the number of elements it can hold in the underlying array cap(mySlice) , e.g., make([]int, 0, 5) creates a slice with length 0 and capacity 5.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00356))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
