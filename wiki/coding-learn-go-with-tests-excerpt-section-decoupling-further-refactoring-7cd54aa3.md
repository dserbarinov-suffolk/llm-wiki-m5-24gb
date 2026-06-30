---
page_id: coding-learn-go-with-tests-excerpt-section-decoupling-further-refactoring-7cd54aa3
page_kind: source
summary: Decoupling / Further refactoring: 14 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-decoupling-further-refactoring-7cd54aa3@fd949b65d06e98f3c31f3ff6253e6bb3
---

# Decoupling / Further refactoring

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3]] - broader source section: Decoupling
- [[coding-learn-go-with-tests-excerpt-section-decoupling-write-the-test-first-05e88611]] - next source section: Decoupling / Write the test first

## Statements

- Now that you have some understanding of structs we can introduce "table driven tests". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00495))_
- The only new syntax here is creating an "anonymous struct", areaTests . We are declaring a slice of structs by using []struct with two fields, the shape and the want . Then we fill the slice with cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- Table driven tests can be a great item in your toolbox, but be sure that you have a need for the extra noise in the tests. They are a great fit when you wish to test various implementations of an interface, or if the data being passed in to a function has lots of different requirements that need testing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00501))_
- The only new syntax here is creating an "anonymous struct", areaTests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- Then we fill the slice with cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_
- In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
