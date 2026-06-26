---
page_id: coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-cd3fdc89
page_kind: source
summary: Note on declaring a new error for Update: 4 source-backed entries and 0 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-note-on-declaring-a-new-error-for-update-cd3fdc89@ef97acdada8db168f67e46bd83bb16f3
---

# Note on declaring a new error for Update

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We could reuse ErrNotFound and not add a new error. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00671))_
- However, it is often better to have a precise error for when an update fails. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00671))_
- Having specific errors gives you more information about what went wrong. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00672))_
- You can redirect the user when ErrNotFound is encountered, but display an error message when ErrWordDoesNotExist is encountered. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00673))_
