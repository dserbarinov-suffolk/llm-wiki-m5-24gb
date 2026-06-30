---
page_id: coding-learn-go-with-tests-excerpt-note
page_kind: concept
summary: Note: 5 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-note@6636470cf1d12242cad04f2af74dfbd0
---

# Note

What [[coding-learn-go-with-tests-excerpt]] covers about note:

## Statements

### Integers

- Note: Go source files can only have one package per directory. Make sure that your files are organised into their own packages. Here is a good explanation on this. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00165))_

### Integers / Write the test first

- Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working with integers such as Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00171))_

### Benchmarking

- Note : We have to call the String method to retrieve the final result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00259))_

### Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

- From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_

### Arrays and their type / Try and run the test

- Oh no! It's important to note that while the test has compiled , it has a runtime error . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00382))_


## Technical atoms

### Technical frame 1: Benchmarking

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00259))_

> Note : We have to call the String method to retrieve the final result.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00258))_

```
const repeatCount = 5
func Repeat(character string) string {
    var repeated strings.Builder
    for i := 0; i < repeatCount; i++ {
        repeated.WriteString(character)
    }
    return repeated.String()
}
```

### Technical frame 2: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00347))_

> Go does not let you use equality operators with slices. You could write a function to iterate over each got and want slice and check their values, but what if we had a more convenient way to do this?

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00346))_

```
./sum_test.go:26:9: invalid operation: got != want (slice can only 
be compared to nil)
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements: Test shares source evidence from Arrays and their type / Try and run the test: Oh no! It's important to note that while the test has compiled , it has a runtime error . (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-try-run-test]] - shared statements: Try and run the test shares source evidence from Arrays and their type / Try and run the test: Oh no! It's important to note that while the test has compiled , it has a runtime error . (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-write-test]] - shared statements: Write the test first shares source evidence from Integers / Write the test first: Also note that we are no longer using the main package, instead we've defined a package named integers , as the name suggests this will group functions for working w ... [truncated] (1 shared statement(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
