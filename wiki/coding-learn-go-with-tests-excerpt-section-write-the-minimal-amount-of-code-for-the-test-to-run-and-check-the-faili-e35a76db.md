---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-e35a76db
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-e35a76db@f3e71e9a6ac76d7143a82184ab070106
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00682))_
- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00682))_
- dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00683))_

## Technical atoms

```
func (d Dictionary) Delete(word string) {
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00681))_
