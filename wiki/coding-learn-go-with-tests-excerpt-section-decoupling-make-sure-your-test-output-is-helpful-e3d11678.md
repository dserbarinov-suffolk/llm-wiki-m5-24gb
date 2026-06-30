---
page_id: coding-learn-go-with-tests-excerpt-section-decoupling-make-sure-your-test-output-is-helpful-e3d11678
page_kind: source
summary: Decoupling / Make sure your test output is helpful: 13 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-decoupling-make-sure-your-test-output-is-helpful-e3d11678@e7a3cda515c26cfee755db6ff2a18e21
---

# Decoupling / Make sure your test output is helpful

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3]] - broader source section: Decoupling
- [[coding-learn-go-with-tests-excerpt-section-decoupling-refactor-1b44f28f]] - previous source section: Decoupling / Refactor
- [[coding-learn-go-with-tests-excerpt-section-decoupling-wrapping-up-c20c66cc]] - next source section: Decoupling / Wrapping up

## Statements

- Remember earlier when we were implementing Triangle and we had the failing test? It printed shapes_test.go:31: got 0.00 want 36.00 . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00526))_
- We knew this was in relation to Triangle because we were just working with it. But what if a bug slipped in to the system in one of 20 cases in the table? How would a developer know which case failed? This is not a great experience for the developer, they will have to manually look through the cases to find out which case actually failed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00527))_
- We can change our error message into %#v got %g want %g . The %#v format string will print out our struct with the values in its field, so the developer can see at a glance the properties that are being tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00528))_
- To increase the readability of our test cases further, we can rename the want field into something more descriptive like hasArea . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00529))_
- One final tip with table driven tests is to use t.Run and to name the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00530))_
- By wrapping each case in a t.Run you will have clearer test output on failures as it will print the name of the case _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00531))_
- And you can run specific tests within your table with go test -run TestArea/Rectangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_
- We knew this was in relation to Triangle because we were just working with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00527))_
- And you can run specific tests within your table with go test -run TestArea/Rectangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_
