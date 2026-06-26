---
page_id: coding-learn-go-with-tests-excerpt-compiler
page_kind: concept
summary: Compiler: 6 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-compiler@b27edb3a21147b8e2f6947b9f5223c09
---

# Compiler

What [[coding-learn-go-with-tests-excerpt]] covers about compiler:

## Statements

- The compiler understands how your code should snap together and work so you don't have to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00051))_
- In this case the compiler is telling you what you need to do to continue. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00052))_
- It turns out that fixing the compiler problems were all we need to do here and the tests pass! _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00323))_
- By running go test the compiler will fail with ./dictionary_test.go:8:9: undefined: Search . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00557))_
- The compiler will fail because we are not returning a value for Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00625))_
- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00692))_

## Technical atoms

> Context: When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00051, source-range-559be4b1-00055))_

```
func Hello(name	string)	string	{ return "Hello,	world" }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00054))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
