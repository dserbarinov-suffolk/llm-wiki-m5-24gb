---
page_id: coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-the-minimal-amount-of-code-for-the-test-to-run-an-d4474d40
page_kind: source
summary: Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-the-minimal-amount-of-code-for-the-test-to-run-an-d4474d40@7c77f6362271a673668bef9175c420b0
---

# Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-a49f3aa6]] - broader source section: Note on declaring a new error for Update
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-try-to-run-the-test-8cf14f42]] - previous source section: Note on declaring a new error for Update / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-23382f56]] - next source section: Note on declaring a new error for Update / Write enough code to make it pass

## Statements

- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00682))_
- dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00683))_
- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00682))_

## Technical atoms

### Technical frame 1: Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00682))_

> After we add this, the test tells us we are not deleting the word.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00681))_

```
func (d Dictionary) Delete(word string) {
}
```
