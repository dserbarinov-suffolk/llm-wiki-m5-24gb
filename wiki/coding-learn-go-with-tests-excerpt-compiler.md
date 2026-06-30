---
page_id: coding-learn-go-with-tests-excerpt-compiler
page_kind: concept
summary: Compiler: 6 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-compiler@15f20bebd76a30a6cdf7b1e5247aad13
---

# Compiler

What [[coding-learn-go-with-tests-excerpt]] covers about compiler:

## Statements

### Hello, YOU

- When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so you don't have to. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00051))_

- In this case the compiler is telling you what you need to do to continue. We have to change our function Hello to accept an argument. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00052))_

### Arrays and their type / Write enough code to make it pass

- It turns out that fixing the compiler problems were all we need to do here and the tests pass! _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00323))_

### Maps / Try to run the test

- By running go test the compiler will fail with ./dictionary_test.go:8:9: undefined: Search . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00557))_

### Pointers, copies, et al / Try to run test

- The compiler will fail because we are not returning a value for Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00625))_

### Note on declaring a new error for Update / Try to run test

- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00692))_


## Technical atoms

### Technical frame 1: Hello, YOU

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00055))_

> If you try and run your tests again your hello.go will fail to compile because you're not passing an argument. Send in "world" to make it compile.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00054))_

```
func Hello(name string) string {
    return "Hello, world"
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-code]] - shared statements and technical atoms: Code shares source evidence from Hello, YOU: When using a statically typed language like Go it is important to listen to the compiler . The compiler understands how your code should snap together and work so yo ... [truncated]; Code shares technical record from Hello, YOU: func Hello(name string) string { return "Hello, world" } (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Maps / Try to run the test: By running go test the compiler will fail with ./dictionary_test.go:8:9: undefined: Search .; Test shares technical record from Hello, YOU: func Hello(name string) string { return "Hello, world" } (1 shared statement(s), 1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-try-run-test]] - shared statements: Try and run the test shares source evidence from Pointers, copies, et al / Try to run test: The compiler will fail because we are not returning a value for Add . (2 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
