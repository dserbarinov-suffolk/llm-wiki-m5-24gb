---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-0f97ef75
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 2 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-0f97ef75@5f7e14c10f08681d9ead5efe19e63d44
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

```
package main
func Sum(numbers [5]int) int {
    return 0
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00292))_

```
sum_test.go:13: got 0 want 15 given, [1 2 3 4 5]
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00294))_
