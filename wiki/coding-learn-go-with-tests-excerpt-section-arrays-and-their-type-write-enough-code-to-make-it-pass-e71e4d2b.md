---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e71e4d2b
page_kind: source
summary: Arrays and their type / Write enough code to make it pass: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e71e4d2b@74594cf3b6e8b7cbc47a3547e3906e9b
---

# Arrays and their type / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - broader source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-dbff4772]] - previous source section: Arrays and their type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-1446fc86]] - next source section: Arrays and their type / Refactor

## Technical atoms

### Technical frame 1: Arrays and their type / Write enough code to make it pass

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00385))_

```
func SumAllTails(numbersToSum ...[]int) []int {
    var sums []int
    for _, numbers := range numbersToSum {
        if len(numbers) == 0 {
            sums = append(sums, 0)
        } else {
            tail := numbers[1:]
            sums = append(sums, Sum(tail))
        }
    }
return sums
}
```
