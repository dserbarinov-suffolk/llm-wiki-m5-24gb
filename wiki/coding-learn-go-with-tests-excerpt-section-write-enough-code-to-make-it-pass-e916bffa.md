---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-e916bffa
page_kind: source
summary: Write enough code to make it pass: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-e916bffa@5b1521f41154a2ee233872be5c8a1d51
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- In our case, we are saying "take from 1 to the end" with numbers[1:] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00374))_
- You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00374))_
- The syntax is slice[low:high] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00374))_

## Technical atoms

```
func SumAllTails(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        tail := numbers[1:]
        sums = append(sums, Sum(tail))
    }
return sums
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00373))_
