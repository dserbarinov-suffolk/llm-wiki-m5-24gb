---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-9d6f8acb
page_kind: source
summary: Pointers, copies, et al / Write the test first: 4 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-9d6f8acb@ce06fc5b7c12a06e593f021c80ed49f9
---

# Pointers, copies, et al / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - broader source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-618028a3]] - previous source section: Pointers, copies, et al / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-try-and-run-the-test-e2eb73b2]] - next source section: Pointers, copies, et al / Try and run the test

## Statements

- We added yet another error type for when the word does not exist. We also modified Update to return an error value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00657))_

## Technical atoms

### Technical frame 1: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00657))_

> We added yet another error type for when the word does not exist. We also modified Update to return an error value.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00655))_

```
t.Run("existing word", func(t *testing.T) {
    word := "test"
    definition := "this is just a test"
    dictionary := Dictionary{word: definition}
    newDefinition := "new definition"
err := dictionary.Update(word, newDefinition)
assertError(t, err, nil)
    assertDefinition(t, dictionary, word, newDefinition)
})
t.Run("new word", func(t *testing.T) {
    word := "test"
    definition := "this is just a test"
    dictionary := Dictionary{}
```

### Technical frame 2: Pointers, copies, et al / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00657))_

> We added yet another error type for when the word does not exist. We also modified Update to return an error value.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00656))_

```
err := dictionary.Update(word, definition)
assertError(t, err, ErrWordDoesNotExist)
})
```
