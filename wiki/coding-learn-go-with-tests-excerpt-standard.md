---
page_id: coding-learn-go-with-tests-excerpt-standard
page_kind: concept
summary: Standard: 5 statement(s) and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: topic-concept
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-standard@3bd5b31e85ad5291980216db15c55c8d
---

# Standard

What [[coding-learn-go-with-tests-excerpt]] covers about standard:

## Statements

### Go's documentation

- The vast majority of the standard library has excellent documentation with examples. Navigating to http://localhost:8080/testing would be worthwhile to see what's available to you. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00041))_

### Testable Examples

- To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . , which should open a web browser for you, pointing to http://localhost:8080 . Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example documentation for github.com/quii/learn-go-with-tests . Follow that link, and then look under Integers , then under func Add , then expand Example and you should see the example you added for sum := Add(1, 5) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_

### Benchmarking

- The standard library provides the strings.Builder stringsBuilder type which minimizes memory copying. It implements a WriteString method which we can use to concatenate strings: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00257))_

### Benchmarking / Practice exercises

- Have a look through the strings package. Find functions you think could be useful and experiment with them by writing tests like we have here. Investing time learning the standard library will really pay off over time. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00269))_

### Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

- From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. Note that this function expects the elements to be comparable. So, it can't be applied to slices with non-comparable elements like 2D slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00348))_


## Technical atoms

### Technical frame 1: Testable Examples

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00208))_

> To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running the following command: go install golang.org/x/pkgsite/cmd/pkgsite@latest , then run pkgsite -open . , which should open a web browser for you, pointing to http://localhost:8080 . Inside here you'll see a list of all of Go's Standard Library packages, plus Third Party packages you have installed, under which you should see your example

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00209))_

> If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev.

### Technical frame 2: Benchmarking

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

### Technical frame 3: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00347))_

> Go does not let you use equality operators with slices. You could write a function to iterate over each got and want slice and check their values, but what if we had a more convenient way to do this?

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00346))_

```
./sum_test.go:26:9: invalid operation: got != want (slice can only 
be compared to nil)
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-library]] - shared statements and technical atoms: Library shares source evidence from Go's documentation: The vast majority of the standard library has excellent documentation with examples. Navigating to http://localhost:8080/testing would be worthwhile to see what's available to you.; Library shares technical record from Testable Examples: If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev. (4 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-package]] - shared statements and technical atoms: Package shares source evidence from Testable Examples: To view example documentation, let's take a quick look at pkgsite . Before navigating to your project's directory, make sure you have installed pkgsite by running th ... [truncated]; Package shares technical record from Testable Examples: If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev. (2 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-note]] - shared technical atoms: Note shares technical record from Benchmarking: const repeatCount = 5 func Repeat(character string) string { var repeated strings.Builder for i := 0; i < repeatCount; i++ { repeated.WriteString(character) } return ... [truncated] (2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-function]] - shared technical atoms: Function shares technical record from Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: ./sum_test.go:26:9: invalid operation: got != want (slice can only be compared to nil) (1 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test]] - shared technical atoms: Test shares technical record from Testable Examples: If you publish your code with examples to a public URL, you can share the documentation of your code at pkg.go.dev. (1 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
