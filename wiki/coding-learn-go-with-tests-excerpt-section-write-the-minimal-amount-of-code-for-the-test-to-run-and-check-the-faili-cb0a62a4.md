---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-cb0a62a4
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 6 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-cb0a62a4@66347539fe04a13c6c84e7cea54e34ad
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- You don't need to know anything new right now to make the test fail properly. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00226))_
- All you need to do right now is enough to make it compile so you can check your test is written well. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00227))_
- This means you can now play with the production code as much as you like and know it's behaving as you'd hope. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00229))_
- This means you can now play with the production code as much as you like and know it's behaving as you'd hope. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00229))_

## Technical atoms

```
package iteration func Repeat(character	string)	string	{ return "" }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00228))_

```
repeat_test.go:10:	expected	'aaaaa'	but	got	''
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00230))_
