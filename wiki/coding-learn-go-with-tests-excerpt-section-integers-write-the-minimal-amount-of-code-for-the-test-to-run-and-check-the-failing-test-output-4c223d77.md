---
page_id: coding-learn-go-with-tests-excerpt-section-integers-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-output-4c223d77
page_kind: source
summary: Integers / Write the minimal amount of code for the test to run and check the failing test output: 7 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-integers-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-output-4c223d77@aec77d185e9be90c000691d69001f5fa
---

# Integers / Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-integers-771ce4c7]] - broader source section: Integers
- [[coding-learn-go-with-tests-excerpt-section-integers-try-and-run-the-test-ce54b37e]] - previous source section: Integers / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-integers-write-enough-code-to-make-it-pass-edef33e0]] - next source section: Integers / Write enough code to make it pass

## Statements

- Now run the tests, and we should be happy that the test is correctly reporting what is wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_
- If you have noticed we learnt about named return value in the last section but aren't using the same here. It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters. You can refer this wiki for more details. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00180))_

## Technical atoms

### Technical frame 1: Integers / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_

> Now run the tests, and we should be happy that the test is correctly reporting what is wrong.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00176))_

```
package integers
func Add(x, y int) int {
    return 0
}
```

### Technical frame 2: Integers / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00178))_

> Now run the tests, and we should be happy that the test is correctly reporting what is wrong.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00177))_

> Remember, when you have more than one argument of the same type (in our case two integers) rather than having (x int, y int) you can shorten it to (x, y int) .

### Technical frame 3: Integers / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00180))_

> If you have noticed we learnt about named return value in the last section but aren't using the same here. It should generally be used when the meaning of the result isn't clear from context, in our case it's pretty much clear that Add function will add the parameters. You can refer this wiki for more details.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00179))_

```
adder_test.go:10: expected '4' but got '0'
```
