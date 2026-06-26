---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-12e9642e
page_kind: source
summary: Write enough code to make it pass: 5 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-12e9642e@b335f162dc916c6a0abf7e4e9ce4c8e8
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- In the strictest sense of TDD we should now write the minimal amount of code to make the test pass . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00182))_
- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00186))_

## Technical atoms

```
func Add(x, y int) int {
    return 4
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00183))_

```
func Add(x, y int) int {
    return x + y
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00188))_

> If you re-run the tests they should pass.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00189))_
