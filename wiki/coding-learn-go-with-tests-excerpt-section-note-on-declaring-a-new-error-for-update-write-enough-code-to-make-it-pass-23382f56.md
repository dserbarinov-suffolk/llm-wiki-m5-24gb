---
page_id: coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-23382f56
page_kind: source
summary: Note on declaring a new error for Update / Write enough code to make it pass: 4 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-23382f56@971ee5cd48c753519a2c4fba29669ae7
---

# Note on declaring a new error for Update / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-a49f3aa6]] - broader source section: Note on declaring a new error for Update
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-the-minimal-amount-of-code-for-the-test-to-run-an-d4474d40]] - previous source section: Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-refactor-6eade47d]] - next source section: Note on declaring a new error for Update / Refactor

## Statements

- Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

## Technical atoms

### Technical frame 1: Note on declaring a new error for Update / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

> Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00685))_

```
func (d Dictionary) Delete(word string) {
    delete(d, word)
```

### Technical frame 2: Note on declaring a new error for Update / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

> Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00686))_

```
}
```
