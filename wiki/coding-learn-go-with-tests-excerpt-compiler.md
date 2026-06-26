---
page_id: coding-learn-go-with-tests-excerpt-compiler
page_kind: concept
summary: Compiler: 10 statement(s) and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-compiler@562a8b52ae4d011237bddb65c61f193b
---

# Compiler

What [[coding-learn-go-with-tests-excerpt]] covers about compiler:

## Statements

- I would like to reiterate how great the compiler is here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00453))_
- The compiler will fail because we are not returning a value for Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00625))_
- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00692))_
- In this case the compiler is telling you what you need to do to continue. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00052))_
- When using a statically typed language like Go it is important to listen to the compiler . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00051))_
- By running go test the compiler will fail with ./dictionary_test.go:8:9: undefined: Search . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00557))_
- It turns out that fixing the compiler problems were all we need to do here and the tests pass! _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00323))_
- If a developer mistakenly adds a new test with checkSums(t, got, "dave") the compiler will stop them in their tracks. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00392))_
- Once the above error is fixed, if you run go test the compiler will fail with the familiar ./sum_test.go:10:15: undefined: Sum error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00290))_
- Comments in Go are a great way to add additional information to your code, or in this case, a quick way to tell the compiler to ignore a line. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00088))_

## Technical atoms

> The compiler understands how your code should snap together and work so you don't have to.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00051))_

> When you try to run the test, the compiler should complain because you are calling Hello with two arguments rather than one.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00109))_

> Because such examples are validated by the Go compiler, you can be confident your documentation's examples always reflect current code behavior.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00199))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
