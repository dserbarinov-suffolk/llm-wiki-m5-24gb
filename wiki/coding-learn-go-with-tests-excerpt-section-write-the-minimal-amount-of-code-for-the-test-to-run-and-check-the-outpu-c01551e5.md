---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-outpu-c01551e5
page_kind: source
summary: Write the minimal amount of code for the test to run and check the output: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-outpu-c01551e5@56ed68e004eda082797332695f408b65
---

# Write the minimal amount of code for the test to run and check the output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We are still modifying the value, and returning a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00629))_

## Technical atoms

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
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00628))_

```
dictionary_test.go:43: got error '%!q(<nil>)' want 'cannot add word 
because it already exists'
dictionary_test.go:44: got 'new test' want 'this is just a test'
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00630))_
