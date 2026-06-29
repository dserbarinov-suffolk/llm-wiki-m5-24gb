---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-enough-code-to-make-it-pass-52249515
page_kind: source
summary: Arrays and slices / Write enough code to make it pass: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-enough-code-to-make-it-pass-52249515@3a9d07b074c10d74a7c0c61a74f190b1
---

# Arrays and slices / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c]] - broader source section: Arrays and slices
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-tes-a24fad7d]] - previous source section: Arrays and slices / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-refactor-d443a668]] - next source section: Arrays and slices / Refactor

## Statements

- To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_

## Technical atoms

### Technical frame 1: Arrays and slices / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00297))_

> To get the value out of an array at a particular index, just use array[index] syntax. In this case, we are using for to iterate 5 times to work through the array and add each item onto sum .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00296))_

```
func Sum(numbers [5]int) int {
    sum := 0
    for i := 0; i < 5; i++ {
        sum += numbers[i]
    }
    return sum
}
```
