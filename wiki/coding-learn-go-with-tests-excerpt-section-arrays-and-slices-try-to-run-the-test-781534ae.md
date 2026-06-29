---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-slices-try-to-run-the-test-781534ae
page_kind: source
summary: Arrays and slices / Try to run the test: 6 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-slices-try-to-run-the-test-781534ae@08653327128bf3338a457661702a5a8d
---

# Arrays and slices / Try to run the test

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c]] - broader source section: Arrays and slices
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-test-first-0df2234d]] - previous source section: Arrays and slices / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-tes-a24fad7d]] - next source section: Arrays and slices / Write the minimal amount of code for the test to run and check the failing test output

## Statements

- If you had initialized go mod with go mod init main you will be presented with an error _testmain.go:13:2: cannot import "main" . This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00288))_
- To fix this, you can rename the main module in go.mod to any other name. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00289))_
- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00290))_
- This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00288))_
