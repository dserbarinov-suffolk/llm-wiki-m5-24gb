---
page_id: coding-learn-go-with-tests-excerpt-note-declaring-error-update
page_kind: concept
summary: Note on declaring a new error for Update: 3 statement(s) and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-note-declaring-error-update@41bfb57480bee4f44dc4b43b2730ccc8
---

# Note on declaring a new error for Update

What [[coding-learn-go-with-tests-excerpt]] covers about note on declaring a new error for update:

## Statements

- Having specific errors gives you more information about what went wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00672))_
- However, it is often better to have a precise error for when an update fails. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00671))_
- We could reuse ErrNotFound and not add a new error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00671))_

## Technical atoms

> Context: Having specific errors gives you more information about what went wrong. Here is an example in a web app:
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00672))_

> You can redirect the user when ErrNotFound is encountered, but display an error message when ErrWordDoesNotExist is encountered.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00673))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
