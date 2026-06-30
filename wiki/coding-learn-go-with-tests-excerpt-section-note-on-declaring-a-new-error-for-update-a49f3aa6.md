---
page_id: coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-a49f3aa6
page_kind: source
summary: Note on declaring a new error for Update: 23 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-a49f3aa6@3bb55f245174b7657c6731033ac4214b
---

# Note on declaring a new error for Update

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-the-test-first-601be12a]] - narrower source section: Note on declaring a new error for Update / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-try-to-run-the-test-8cf14f42]] - narrower source section: Note on declaring a new error for Update / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-the-minimal-amount-of-code-for-the-test-to-run-an-d4474d40]] - narrower source section: Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-23382f56]] - narrower source section: Note on declaring a new error for Update / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-refactor-6eade47d]] - narrower source section: Note on declaring a new error for Update / Refactor
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-try-to-run-test-a79de4fc]] - narrower source section: Note on declaring a new error for Update / Try to run test
- [[coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-write-enough-code-to-make-it-pass-39912f70]] - narrower source section: Note on declaring a new error for Update / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - previous source section: Pointers, copies, et al

## Statements

- We could reuse ErrNotFound and not add a new error. However, it is often better to have a precise error for when an update fails. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00671))_
- Having specific errors gives you more information about what went wrong. Here is an example in a web app: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00672))_

## Statements by subsection

### Note on declaring a new error for Update / Write the test first

- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_
- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00677))_

### Note on declaring a new error for Update / Write the minimal amount of code for the test to run and check the failing test output

- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00682))_
- dictionary_test.go:78: got error '%!q(<nil>)' want 'could not find the word you were looking for' _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00683))_
- After we add this, the test tells us we are not deleting the word. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00682))_

### Note on declaring a new error for Update / Write enough code to make it pass

- Go has a built-in function delete that works on maps. It takes two arguments and returns nothing. The first argument is the map and the second is the key to be removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00687))_

### Note on declaring a new error for Update / Refactor

- There isn't much to refactor, but we can implement the same logic from Update to handle cases where word doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00689))_

### Note on declaring a new error for Update / Try to run test

- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00692))_
- The compiler will fail because we are not returning a value for Delete . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00692))_

### Note on declaring a new error for Update / Write enough code to make it pass

- We are again using a switch statement to match on the error when we attempt to delete a word that doesn't exist. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00696))_
