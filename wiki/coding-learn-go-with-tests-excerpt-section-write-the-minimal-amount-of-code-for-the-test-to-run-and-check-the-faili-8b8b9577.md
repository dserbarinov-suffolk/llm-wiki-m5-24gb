---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-8b8b9577
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 7 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-8b8b9577@7ab84ac112ff7fc3b693ab1f647e6375
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Now run the tests, and we should be happy that the test is correctly reporting what is wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00178))_
- It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00180))_
- If you have noticed we learnt about named return value in the last section but aren't using the same here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00180))_
- You can refer this wiki for more details. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00180))_

## Technical atoms

```
package integers
func Add(x, y int) int {
    return 0
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00176))_

> Remember, when you have more than one argument of the same type (in our case two integers) rather than having (x int, y int) you can shorten it to (x, y int) .
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00177))_

```
adder_test.go:10: expected '4' but got '0'
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00179))_
