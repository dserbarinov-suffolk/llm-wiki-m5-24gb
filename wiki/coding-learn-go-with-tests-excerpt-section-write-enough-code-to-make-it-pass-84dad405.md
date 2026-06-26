---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-84dad405
page_kind: source
summary: Write enough code to make it pass: 4 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-84dad405@905f90c1cd37a4589d75a44f121a4b11
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with = _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00357))_
- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00358))_

## Technical atoms

```
func SumAll(numbersToSum	...[]int)	[]int	{ lengthOfNumbers	:=	len(numbersToSum) sums	:=	make([]int,	lengthOfNumbers) for i,	numbers	:= range numbersToSum	{ sums[i]	=	Sum(numbers) } return sums }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00354))_

> There's a new way to create a slice. make allows you to create a slice with a starting capacity of the len of the numbersToSum we need to work through. The length of a slice is the number of elements it holds len(mySlice) , while the capacity is the number of elements it can hold in the underlying array cap(mySlice) , e.g., make([]int, 0, 5) creates a slice with length 0 and capacity 5.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00356))_
