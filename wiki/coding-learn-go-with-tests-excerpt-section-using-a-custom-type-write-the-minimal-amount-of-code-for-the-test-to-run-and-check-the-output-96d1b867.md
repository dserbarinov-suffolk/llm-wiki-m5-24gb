---
page_id: coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-96d1b867
page_kind: source
summary: Using a custom type / Write the minimal amount of code for the test to run and check the output: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-96d1b867@fde79ea2e986af7c96daa33969294f65
---

# Using a custom type / Write the minimal amount of code for the test to run and check the output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1]] - broader source section: Using a custom type
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-try-and-run-the-test-ebf022ab]] - previous source section: Using a custom type / Try and run the test
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-0fbec14c]] - next source section: Using a custom type / Write enough code to make it pass

## Statements

- Your test should now fail with a much clearer error message. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00585))_
- dictionary_test.go:22: expected to get an error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00586))_

## Technical atoms

### Technical frame 1: Using a custom type / Write the minimal amount of code for the test to run and check the output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00585))_

> Your test should now fail with a much clearer error message.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00584))_

```
func (d Dictionary) Search(word string) (string, error) {
    return d[word], nil
}
```
