---
page_id: coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-7b766fd4
page_kind: source
summary: Using a custom type / Write enough code to make it pass: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-7b766fd4@8ff820135efad5b6614b3e23dc1b688c
---

# Using a custom type / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1]] - broader source section: Using a custom type
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-output-ef8ec6d6]] - previous source section: Using a custom type / Write the minimal amount of code for the test to run and check output

## Statements

- Adding to a map is also similar to an array. You just need to specify a key and set it equal to a value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00603))_

## Technical atoms

### Technical frame 1: Using a custom type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00603))_

> Adding to a map is also similar to an array. You just need to specify a key and set it equal to a value.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00602))_

```
func (d Dictionary) Add(word, definition string) {
    d[word] = definition
}
```
