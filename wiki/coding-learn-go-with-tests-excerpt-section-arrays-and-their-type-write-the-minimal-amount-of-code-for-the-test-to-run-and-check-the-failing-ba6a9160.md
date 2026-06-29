---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-ba6a9160
page_kind: source
summary: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output: 2 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-ba6a9160@3e4fa232ab227edc64a8e28ee2bb7036
---

# Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - broader source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-19f0372e]] - previous source section: Arrays and their type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-b28de2ad]] - next source section: Arrays and their type / Write enough code to make it pass

## Technical atoms

### Technical frame 1: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00320))_

```
func Sum(numbers []int) int {
    sum := 0
    for _, number := range numbers {
        sum += number
    }
    return sum
}
```

### Technical frame 2: Arrays and their type / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00321))_

> If you try to run the tests they will still not compile, you will have to change the first test to pass in a slice rather than an array.
