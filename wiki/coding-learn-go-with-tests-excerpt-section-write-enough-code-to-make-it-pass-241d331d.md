---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-241d331d
page_kind: source
summary: Write enough code to make it pass: 5 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-241d331d@5a25b5b50b93c47ef283a3000c6712b2
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We already saw how to do this when we fixed the issue with Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00651))_
- There is no refactoring we need to do on this since it was a simple change. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00653))_
- If we pass in a new word, Update will add it to the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00653))_
- However, we now have the same issue as with Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00653))_

## Technical atoms

```
func (d	Dictionary)	Update(word,	definition	string)	{ d[word]	=	definition }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00652))_
