---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-1c8e9d48
page_kind: source
summary: Refactor: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-1c8e9d48@3ca070d9c49a8983e0c834a37c9e05fc
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- += called "the Add AND assignment operator" , adds the right operand to the left operand and assigns the result to left operand. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00242))_

## Technical atoms

```
const repeatCount = 5
func Repeat(character string) string {
    var repeated string
    for i := 0; i < repeatCount; i++ {
        repeated += character
    }
    return repeated
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00241))_
