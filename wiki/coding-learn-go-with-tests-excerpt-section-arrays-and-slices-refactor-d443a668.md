---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-slices-refactor-d443a668
page_kind: source
summary: Arrays and slices / Refactor: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-slices-refactor-d443a668@babb2d5da0af89668180d629bec8c959
---

# Arrays and slices / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c]] - broader source section: Arrays and slices
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-enough-code-to-make-it-pass-52249515]] - previous source section: Arrays and slices / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Technical atoms

### Technical frame 1: Arrays and slices / Refactor

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00300))_

```
func Sum(numbers [5]int) int {
    sum := 0
    for _, number := range numbers {
        sum += number
    }
    return sum
}
```
