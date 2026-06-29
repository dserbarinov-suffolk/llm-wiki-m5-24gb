---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-7f59b214
page_kind: source
summary: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the output: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-7f59b214@af5bddb9bf08502c84f3c0c5f00ce534
---

# Pointers, copies, et al / Write the minimal amount of code for the test to run and check the output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - broader source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-to-run-test-66becf89]] - previous source section: Pointers, copies, et al / Try to run test
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-6f139db5]] - next source section: Pointers, copies, et al / Write enough code to make it pass

## Statements

- Now we get two more errors. We are still modifying the value, and returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00629))_

## Technical atoms

### Technical frame 1: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00629))_

> Now we get two more errors. We are still modifying the value, and returning a nil error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00628))_

```
In dictionary.go
var (
    ErrNotFound   = errors.New("could not find the word you were 
looking for")
ErrWordExists = errors.New("cannot add word because it already 
exists")
)
func (d Dictionary) Add(word, definition string) error {
    d[word] = definition
    return nil
}
```

### Technical frame 2: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00629))_

> Now we get two more errors. We are still modifying the value, and returning a nil error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00630))_

```
dictionary_test.go:43: got error '%!q(<nil>)' want 'cannot add word 
because it already exists'
dictionary_test.go:44: got 'new test' want 'this is just a test'
```
