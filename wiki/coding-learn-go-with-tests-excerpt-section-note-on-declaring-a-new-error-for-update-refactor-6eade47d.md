---
page_id: coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-refactor-6eade47d
page_kind: source
summary: Note on declaring a new error for Update / Refactor: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-refactor-6eade47d@77c0c434999481d59dbd3255a62cb60f
---

# Note on declaring a new error for Update / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-a49f3aa6]] - broader source section: Note on declaring a new error for Update
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-23382f56]] - previous source section: Note on declaring a new error for Update / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-try-to-run-test-a79de4fc]] - next source section: Note on declaring a new error for Update / Try to run test
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00689))_

## Technical atoms

### Technical frame 1: Note on declaring a new error for Update / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00689))_

> There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00690))_

```
func TestDelete(t *testing.T) {
    t.Run("existing word", func(t *testing.T) {
        word := "test"
        dictionary := Dictionary{word: "test definition"}
err := dictionary.Delete(word)
assertError(t, err, nil)
_, err = dictionary.Search(word)
assertError(t, err, ErrNotFound)
    })
t.Run("non-existing word", func(t *testing.T) {
        word := "test"
        dictionary := Dictionary{}
err := dictionary.Delete(word)
assertError(t, err, ErrWordDoesNotExist)
    })
}
```
