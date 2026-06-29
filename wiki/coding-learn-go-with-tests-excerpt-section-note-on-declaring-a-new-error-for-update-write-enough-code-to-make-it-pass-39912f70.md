---
page_id: coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-39912f70
page_kind: source
summary: Note on declaring a new error for Update / Write enough code to make it pass: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-39912f70@63c3cec275511dbe0f12221d499fb433
---

# Note on declaring a new error for Update / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-a49f3aa6]] - broader source section: Note on declaring a new error for Update
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-try-to-run-test-a79de4fc]] - previous source section: Note on declaring a new error for Update / Try to run test

## Statements

- We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00696))_

## Technical atoms

### Technical frame 1: Note on declaring a new error for Update / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00696))_

> We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00695))_

```
func (d Dictionary) Delete(word string) error {
    _, err := d.Search(word)
switch err {
    case ErrNotFound:
        return ErrWordDoesNotExist
    case nil:
        delete(d, word)
    default:
        return err
    }
return nil
}
```
