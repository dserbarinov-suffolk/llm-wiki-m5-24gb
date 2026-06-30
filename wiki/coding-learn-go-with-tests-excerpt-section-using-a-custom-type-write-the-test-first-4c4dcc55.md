---
page_id: coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-4c4dcc55
page_kind: source
summary: Using a custom type / Write the test first: 9 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-4c4dcc55@499d615da72984db7cb1f09a44f0ba1a
---

# Using a custom type / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1]] - broader source section: Using a custom type
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-try-and-run-the-test-ebf022ab]] - next source section: Using a custom type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-write-test]] - topic hub: opens the topic page for Write Test

## Statements

- We actually get nothing back. This is good because the program can continue to run, but there is a better approach. The function can report that the word is not in the dictionary. This way, the user isn't left wondering if the word doesn't exist or if there is just no definition (this might not seem very useful for a dictionary. However, it's a scenario that could be key in other usecases). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- The way to handle this scenario in Go is to return a second argument which is an Error type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00579))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_
- This is good because the program can continue to run, but there is a better approach. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00577))_
- Notice that as we've seen in the pointers and error section here in order to assert the error message we first check that the error is not nil and then use .Error() method to get the string which we can then pass to the assertion. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00580))_
