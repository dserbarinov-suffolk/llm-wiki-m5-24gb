---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-5bb60d7b
page_kind: source
summary: Arrays and their type / Write enough code to make it pass: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-5bb60d7b@9261d45633041a6f8e44387499b608de
---

# Arrays and their type / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - broader source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-682609ea]] - previous source section: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

## Statements

- Slices can be sliced! The syntax is slice[low:high] . If you omit the value on one of the sides of the : it captures everything to that side of it. In our case, we are saying "take from 1 to the end" with numbers[1:] . You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_

## Technical atoms

### Technical frame 1: Arrays and their type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00374))_

> Slices can be sliced! The syntax is slice[low:high] . If you omit the value on one of the sides of the : it captures everything to that side of it. In our case, we are saying "take from 1 to the end" with numbers[1:] . You may wish to spend some time writing other tests around slices and experiment with the slice operator to get more familiar with it.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00373))_

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
