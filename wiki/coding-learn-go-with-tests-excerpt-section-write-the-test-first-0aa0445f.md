---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-0aa0445f
page_kind: source
summary: Write the test first: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-0aa0445f@f4f4e67ca234abca731023e8c682d647
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- However, we have no way to add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00596))_
- We have a great way to search the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00596))_
- In this test, we are utilizing our Search function to make the validation of the dictionary a little easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00598))_

## Technical atoms

```
func TestAdd(t *testing.T) {
    dictionary := Dictionary{}
    dictionary.Add("test", "this is just a test")
want := "this is just a test"
    got, err := dictionary.Search("test")
    if err != nil {
        t.Fatal("should find added word:", err)
    }
assertStrings(t, got, want)
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00597))_
