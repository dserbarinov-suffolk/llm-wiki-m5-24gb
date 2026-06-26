---
page_id: coding-learn-go-with-tests-excerpt-further-refactoring
page_kind: concept
summary: Further refactoring: 7 statement(s) and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-further-refactoring@8d117385098b87170c3c353ac157aa01
---

# Further refactoring

What [[coding-learn-go-with-tests-excerpt]] covers about further refactoring:

## Statements

- Now that you have some understanding of structs we can introduce "table driven tests". _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00495))_
- The only new syntax here is creating an "anonymous struct", areaTests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00498))_
- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00499))_
- In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00500))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00500))_
- They are a great fit when you wish to test various implementations of an interface, or if the data being passed in to a function has lots of different requirements that need testing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00501))_
- Table driven tests can be a great item in your toolbox, but be sure that you have a need for the extra noise in the tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00501))_

## Source

- [[coding-learn-go-with-tests-excerpt]]
