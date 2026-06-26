---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-a3663517
page_kind: source
summary: Refactor: 11 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-a3663517@8c6dea6eda49b97c4f2eab9136e2a7a0
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- There isn't much to refactor in our implementation but the test could use a little simplification. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00616))_
- We made variables for word and definition, and moved the definition assertion into its own helper function. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00618))_
- Our Add is looking good. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00619))_
- Except, we didn't consider what happens when the value we are trying to add already exists! _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00619))_
- Except, we didn't consider what happens when the value we are trying to add already exists! _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00619))_
- Map will not throw an error if the value already exists. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00620))_
- It should only add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00620))_
- Instead, they will go ahead and overwrite the value with the newly provided value. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00620))_
- This can be convenient in practice, but makes our function name less than accurate. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00620))_
- It should only add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00620))_

## Technical atoms

```
func TestAdd(t *testing.T) {
    dictionary := Dictionary{}
    word := "test"
    definition := "this is just a test"
dictionary.Add(word, definition)
assertDefinition(t, dictionary, word, definition)
}
func assertDefinition(t testing.TB, dictionary Dictionary, word, 
definition string) {
t.Helper()
got, err := dictionary.Search(word)
    if err != nil {
        t.Fatal("should find added word:", err)
    }
    assertStrings(t, got, definition)
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00617))_
