---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-outpu-15292236
page_kind: source
summary: Write the minimal amount of code for the test to run and check the output: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-outpu-15292236@bbcbf6e9bf4848d2bb6b119fa03542ad
---

# Write the minimal amount of code for the test to run and check the output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- dictionary_test.go:22: expected to get an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00586))_

## Technical atoms

```
func (d	Dictionary)	Search(word	string)	(string,	error)	{ return d[word],	nil }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00584))_

> Your test should now fail with a much clearer error message.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00585))_
