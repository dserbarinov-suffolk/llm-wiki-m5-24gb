---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-8b9fe3c9
page_kind: source
summary: Arrays and their type / Refactor: 10 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-8b9fe3c9@746ae966aad34d0fa6a9bd65a7f7f6a9
---

# Arrays and their type / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - broader source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e067099b]] - previous source section: Arrays and their type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-6cd5dd08]] - next source section: Arrays and their type / Write the test first

## Statements

- As mentioned, slices have a capacity. If you have a slice with a capacity of 2 and try to do mySlice[10] = 1 you will get a runtime error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00360))_
- However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00361))_
- In this implementation, we are worrying less about capacity. We start with an empty slice sums and append to it the result of Sum as we work through the varargs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00364))_
- Our next requirement is to change SumAll to SumAllTails , where it will calculate the totals of the "tails" of each slice. The tail of a collection is all items in the collection except the first one (the "head"). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00365))_
- However, you can use the append function which takes a slice and a new value, then returns a new slice with all the items in it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00361))_
- The tail of a collection is all items in the collection except the first one (the "head"). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00365))_
