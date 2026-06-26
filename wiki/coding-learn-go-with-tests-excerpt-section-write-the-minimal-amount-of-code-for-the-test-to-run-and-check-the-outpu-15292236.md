---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-outpu-15292236
page_kind: source
summary: Write the minimal amount of code for the test to run and check the output: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-outpu-15292236@705d0b3be5f67f2c96ab99b863964e4c
---

# Write the minimal amount of code for the test to run and check the output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Your test should now fail with a much clearer error message. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00585))_
- dictionary_test.go:22: expected to get an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00586))_

## Technical atoms

```
func (d	Dictionary)	Search(word	string)	(string,	error)	{ return d[word],	nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00584))_
