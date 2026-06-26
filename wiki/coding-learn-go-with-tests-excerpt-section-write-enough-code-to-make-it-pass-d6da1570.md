---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-d6da1570
page_kind: source
summary: Write enough code to make it pass: 4 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-d6da1570@96263753bd1e6b8a8b570ceb5321ed27
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- The first argument is the map and the second is the key to be removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00687))_
- Go has a built-in function delete that works on maps. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00687))_

## Technical atoms

```
func (d Dictionary) Delete(word string) {
    delete(d, word)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00685))_

```
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00686))_
