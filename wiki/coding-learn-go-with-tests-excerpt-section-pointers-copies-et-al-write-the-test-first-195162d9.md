---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-195162d9
page_kind: source
summary: Pointers, copies, et al / Write the test first: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-195162d9@2f11e6d7eda13d4ead7fcfe20b2b8b3b
---

# Pointers, copies, et al / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - broader source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-refactor-5d607a3f]] - previous source section: Pointers, copies, et al / Refactor
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-to-run-test-66becf89]] - next source section: Pointers, copies, et al / Try to run test

## Statements

- For this test, we modified Add to return an error, which we are validating against a new error variable, ErrWordExists . We also modified the previous test to check for a nil error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00623))_

## Technical atoms

### Technical frame 1: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00623))_

> For this test, we modified Add to return an error, which we are validating against a new error variable, ErrWordExists . We also modified the previous test to check for a nil error.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00622))_

```
func TestAdd(t *testing.T) {
    t.Run("new word", func(t *testing.T) {
        dictionary := Dictionary{}
        word := "test"
        definition := "this is just a test"
err := dictionary.Add(word, definition)
assertError(t, err, nil)
        assertDefinition(t, dictionary, word, definition)
    })
t.Run("existing word", func(t *testing.T) {
        word := "test"
        definition := "this is just a test"
        dictionary := Dictionary{word: definition}
        err := dictionary.Add(word, "new test")
assertError(t, err, ErrWordExists)
        assertDefinition(t, dictionary, word, definition)
    })
}
```
