---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-9c0e63cc
page_kind: source
summary: Write the test first: 5 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-9c0e63cc@7226ab67a04c0620e9858d3757461956
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Arrays have a fi xed capacity which you define when you declare the variable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00282))_
- Here, we are using the %v placeholder to print the "default" format, which works well for arrays. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00285))_
- It is sometimes useful to also print the inputs to the function in the error message. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00285))_

## Technical atoms

```
package main
import "testing"
func TestSum(t *testing.T) {
numbers := [5]int{1, 2, 3, 4, 5}
got := Sum(numbers)
    want := 15
if got != want {
        t.Errorf("got %d want %d given, %v", got, want, numbers)
    }
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00281))_

```
[N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 
3, 4, 5}
[...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2,
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00283))_
