---
page_id: coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-the-test-first-601be12a
page_kind: source
summary: Note on declaring a new error for Update / Write the test first: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-the-test-first-601be12a@bd7edd61c0bf009f3e5d583607166a63
---

# Note on declaring a new error for Update / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-a49f3aa6]] - broader source section: Note on declaring a new error for Update
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-try-to-run-the-test-8cf14f42]] - next source section: Note on declaring a new error for Update / Try to run the test

## Statements

- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_
- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_

## Technical atoms

### Technical frame 1: Note on declaring a new error for Update / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_

> Our test creates a Dictionary with a word and then checks if the word has been removed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00676))_

```
func TestDelete(t *testing.T) {
    word := "test"
    dictionary := Dictionary{word: "test definition"}
dictionary.Delete(word)
_, err := dictionary.Search(word)
    assertError(t, err, ErrNotFound)
}
```
