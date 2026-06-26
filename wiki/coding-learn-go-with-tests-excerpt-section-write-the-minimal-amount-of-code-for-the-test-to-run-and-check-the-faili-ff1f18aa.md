---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-ff1f18aa
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 7 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-ff1f18aa@ff75e6aab05163b4f5a0e3f9847f6fd8
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Remember, when you have more than one argument of the same type (in our case two integers) rather than having (x int, y int) you can shorten it to (x, y int) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00177))_
- Now run the tests, and we should be happy that the test is correctly reporting what is wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00178))_
- You can refer this wiki for more details. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00180))_
- If you have noticed we learnt about named return value in the last section but aren't using the same here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00180))_

## Technical atoms

```
package integers func Add(x,	y	int)	int	{ return 0 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00176))_

```
adder_test.go:10:	expected	'4'	but	got	'0'
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00179))_

> It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00180))_
