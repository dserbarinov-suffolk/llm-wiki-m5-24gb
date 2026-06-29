---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-tes-a24fad7d
page_kind: source
summary: Arrays and slices / Write the minimal amount of code for the test to run and check the failing test output: 2 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-tes-a24fad7d@2025318b8f2489524109f85f91c77fac
---

# Arrays and slices / Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c]] - broader source section: Arrays and slices
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-try-to-run-the-test-781534ae]] - previous source section: Arrays and slices / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-enough-code-to-make-it-pass-52249515]] - next source section: Arrays and slices / Write enough code to make it pass

## Technical atoms

### Technical frame 1: Arrays and slices / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00292))_

```
package main
func Sum(numbers [5]int) int {
    return 0
}
```

### Technical frame 2: Arrays and slices / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00294))_

```
sum_test.go:13: got 0 want 15 given, [1 2 3 4 5]
```
