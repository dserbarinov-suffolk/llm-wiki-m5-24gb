---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-16363708
page_kind: source
summary: Refactor: 10 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-16363708@173f3171cfff3e7d77bca7684fd2ebe5
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- As mentioned, slices have a capacity. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00360))_
- If you have a slice with a capacity of 2 and try to do mySlice[10] = 1 you will get a runtime error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00360))_
- However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00361))_
- However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00361))_
- In this implementation, we are worrying less about capacity. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00364))_
- Our next requirement is to change SumAll to SumAllTails , where it will calculate the totals of the "tails" of each slice. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00365))_
- The tail of a collection is all items in the collection except the first one (the "head"). _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00365))_
- The tail of a collection is all items in the collection except the first one (the "head"). _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00365))_

## Technical atoms

```
func SumAll(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        sums = append(sums, Sum(numbers))
    }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00362))_

```
return sums
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00363))_
