---
page_id: coding-learn-go-with-tests-excerpt-section-try-to-run-the-test-a83ac29d
page_kind: source
summary: Try to run the test: 6 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-try-to-run-the-test-a83ac29d@c65f5eb014bfab689af7193effec3fa8
---

# Try to run the test

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- If you had initialized go mod with go mod init main you will be presented with an error _testmain.go:13:2: cannot import "main" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00288))_
- This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00288))_
- This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00288))_
- To fix this, you can rename the main module in go.mod to any other name. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00289))_
- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00290))_
- Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00290))_
