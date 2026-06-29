---
page_id: coding-learn-go-with-tests-excerpt-section-iteration-write-enough-code-to-make-it-pass-82c13f0e
page_kind: source
summary: Iteration / Write enough code to make it pass: 11 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-iteration-write-enough-code-to-make-it-pass-82c13f0e@105664f11faf31076a5da247f78a7dc4
---

# Iteration / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-iteration-9b1d79ea]] - broader source section: Iteration
- [[coding-learn-go-with-tests-excerpt-section-iteration-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-output-0144fa59]] - previous source section: Iteration / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-iteration-refactor-5810cb18]] - next source section: Iteration / Refactor

## Statements

- The for syntax is very unremarkable and follows most C-like languages. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00232))_
- as we've been using := so far to declare and initializing variables. However, := is simply short hand for both steps. Here we are declaring a string variable only. Hence, the explicit version. We can also use var to declare functions, as we'll see later on. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_
- Run the test and it should pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00237))_
- Additional variants of the for loop are described here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00238))_
- Here we are declaring a string variable only. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_
- Hence, the explicit version. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_

## Technical atoms

### Technical frame 1: Iteration / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_

> as we've been using := so far to declare and initializing variables. However, := is simply short hand for both steps. Here we are declaring a string variable only. Hence, the explicit version. We can also use var to declare functions, as we'll see later on.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00233))_

```
func Repeat(character string) string {
    var repeated string
    for i := 0; i < 5; i++ {
        repeated = repeated + character
    }
    return repeated
}
```

### Technical frame 2: Iteration / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00236))_

> as we've been using := so far to declare and initializing variables. However, := is simply short hand for both steps. Here we are declaring a string variable only. Hence, the explicit version. We can also use var to declare functions, as we'll see later on.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00235))_

```
var repeated string
```
