---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e067099b
page_kind: source
summary: Arrays and their type / Write enough code to make it pass: 4 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e067099b@de37b006144c8f74cd62142f3d390eb6
---

# Arrays and their type / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - broader source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-f1b6d194]] - previous source section: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-8b9fe3c9]] - next source section: Arrays and their type / Refactor

## Statements

- You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with = _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00357))_
- The tests should now pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00358))_

## Technical atoms

### Technical frame 1: Arrays and their type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00357))_

> You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with =

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00354))_

```
func SumAll(numbersToSum ...[]int) []int {
    lengthOfNumbers := len(numbersToSum)
    sums := make([]int, lengthOfNumbers)
for i, numbers := range numbersToSum {
        sums[i] = Sum(numbers)
    }
return sums
}
```

### Technical frame 2: Arrays and their type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00357))_

> You can index slices like arrays with mySlice[N] to get the value out or assign it a new value with =

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00356))_

> There's a new way to create a slice. make allows you to create a slice with a starting capacity of the len of the numbersToSum we need to work through. The length of a slice is the number of elements it holds len(mySlice) , while the capacity is the number of elements it can hold in the underlying array cap(mySlice) , e.g., make([]int, 0, 5) creates a slice with length 0 and capacity 5.
