---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-cf9e3e10
page_kind: source
summary: Write the test first: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-cf9e3e10@656bd00d24e90b57b5b3b76c19bbaa99
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00677))_
- Our test creates a Dictionary with a word and then checks if the word has been removed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00677))_

## Technical atoms

```
func TestDelete(t *testing.T) {
    word := "test"
    dictionary := Dictionary{word: "test definition"}
dictionary.Delete(word)
_, err := dictionary.Search(word)
    assertError(t, err, ErrNotFound)
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00676))_
