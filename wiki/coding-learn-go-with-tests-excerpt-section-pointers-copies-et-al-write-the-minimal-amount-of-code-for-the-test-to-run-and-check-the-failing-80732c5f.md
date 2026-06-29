---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-80732c5f
page_kind: source
summary: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the failing test output: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-80732c5f@20e72e9740237cb3b6cd4f98466f74fb
---

# Pointers, copies, et al / Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - broader source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-and-run-the-test-e2eb73b2]] - previous source section: Pointers, copies, et al / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-e62dfd1d]] - next source section: Pointers, copies, et al / Write enough code to make it pass

## Statements

- We added our own error type and are returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00663))_

## Technical atoms

### Technical frame 1: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00663))_

> We added our own error type and are returning a nil error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00662))_

```
const (
    ErrNotFound         = DictionaryErr("could not find the word you 
were looking for")
ErrWordExists       = DictionaryErr("cannot add word because it 
already exists")
ErrWordDoesNotExist = DictionaryErr("cannot perform operation on 
word because it does not exist")
)
func (d Dictionary) Update(word, definition string) error {
    d[word] = definition
    return nil
}
```

### Technical frame 2: Pointers, copies, et al / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00663))_

> We added our own error type and are returning a nil error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00665))_

```
dictionary_test.go:66: got error '%!q(<nil>)' want 'cannot update 
word because it does not exist'
```
