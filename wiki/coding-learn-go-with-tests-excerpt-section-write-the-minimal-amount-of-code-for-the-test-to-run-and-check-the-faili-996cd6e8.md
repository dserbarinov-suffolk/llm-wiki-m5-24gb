---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-996cd6e8
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-996cd6e8@9250fd051c49e21061c93debef08805f
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- If you try to run the tests they will still not compile, you will have to change the first test to pass in a slice rather than an array. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00321))_

## Technical atoms

```
func Sum(numbers	[]int)	int	{ sum	:=	0 for _,	number	:= range numbers	{ sum	+=	number } return sum }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00320))_
