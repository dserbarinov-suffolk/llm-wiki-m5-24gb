---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-458aa742
page_kind: source
summary: Write enough code to make it pass: 5 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-458aa742@c8fe2f7ed1441e0fa81b4a4bee1079cb
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We already saw how to do this when we fixed the issue with Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00651))_
- There is no refactoring we need to do on this since it was a simple change. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00653))_
- However, we now have the same issue as with Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00653))_

## Technical atoms

```
func (d Dictionary) Update(word, definition string) {
    d[word] = definition
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00652))_

> If we pass in a new word, Update will add it to the dictionary.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00653))_
