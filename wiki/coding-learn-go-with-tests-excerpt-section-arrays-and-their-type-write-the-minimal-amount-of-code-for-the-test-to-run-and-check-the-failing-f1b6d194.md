---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-f1b6d194
page_kind: source
summary: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: 11 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-f1b6d194@863381939308d2d811ce9cadb1652dd3
---

# Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - broader source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-501a4c76]] - previous source section: Arrays and their type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e067099b]] - next source section: Arrays and their type / Write enough code to make it pass

## Statements

- We need to define SumAll according to what our test wants. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00342))_
- Go can let you write variadic functions that can take a variable number of arguments. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00343))_
- This is valid, but our tests still won't compile! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00345))_
- Go does not let you use equality operators with slices. You could write a function to iterate over each got and want slice and check their values, but what if we had a more convenient way to do this? _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00347))_
- From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_
- You should have test output like the following: sum_test.go:30: got [] want [3 9] _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00351))_
