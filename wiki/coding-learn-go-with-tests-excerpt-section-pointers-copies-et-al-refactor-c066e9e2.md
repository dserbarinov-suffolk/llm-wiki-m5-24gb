---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-refactor-c066e9e2
page_kind: source
summary: Pointers, copies, et al / Refactor: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-refactor-c066e9e2@a09d5360886612d56c7ee0e445d0e2a5
---

# Pointers, copies, et al / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - broader source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-6f139db5]] - previous source section: Pointers, copies, et al / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-764407b8]] - next source section: Pointers, copies, et al / Write the test first
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- We don't have too much to refactor, but as our error usage grows we can make a few modifications. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00635))_
- We made the errors constant; this required us to create our own DictionaryErr type which implements the error interface. You can read more about the details in this excellent article by Dave Cheney. Simply put, it makes the errors more reusable and immutable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00637))_

## Technical atoms

### Technical frame 1: Pointers, copies, et al / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00637))_

> We made the errors constant; this required us to create our own DictionaryErr type which implements the error interface. You can read more about the details in this excellent article by Dave Cheney. Simply put, it makes the errors more reusable and immutable.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00636))_

```
const (
    ErrNotFound   = DictionaryErr("could not find the word you were 
looking for")
ErrWordExists = DictionaryErr("cannot add word because it 
already exists")
)
type DictionaryErr string
func (e DictionaryErr) Error() string {
    return string(e)
}
```
