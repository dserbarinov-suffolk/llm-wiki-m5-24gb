---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-f8ea95a0
page_kind: source
summary: Refactor: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-f8ea95a0@ba12fd64c6c136ecf44617dcb5e9a69b
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

```
func Sum(numbers [5]int) int {
    sum := 0
    for _, number := range numbers {
        sum += number
    }
    return sum
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00300))_
