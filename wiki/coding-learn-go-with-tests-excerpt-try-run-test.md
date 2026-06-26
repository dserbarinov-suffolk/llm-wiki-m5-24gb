---
page_id: coding-learn-go-with-tests-excerpt-try-run-test
page_kind: concept
summary: Try to run the test: 5 statement(s) and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-try-run-test@6262af8dbead1951e0a5d4945d719b73
---

# Try to run the test

What [[coding-learn-go-with-tests-excerpt]] covers about try to run the test:

## Statements

- This is because according to common practice, package main will only contain integration of other packages and not unit-testable code and hence Go will not allow you to import a package with name main . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00288))_
- Now we can proceed with writing the actual method to be tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00290))_
- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00290))_
- If you had initialized go mod with go mod init main you will be presented with an error _testmain.go:13:2: cannot import "main" . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00288))_
- To fix this, you can rename the main module in go.mod to any other name. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00289))_

## Source

- [[coding-learn-go-with-tests-excerpt]]
