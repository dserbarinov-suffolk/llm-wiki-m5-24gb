---
page_id: coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-d5397d92
page_kind: source
summary: Using a custom type / Write the test first: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-test-first-d5397d92@75e6a27e11d365bd6f87cf64dc73f09e
---

# Using a custom type / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1]] - broader source section: Using a custom type
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-refactor-862871b5]] - previous source section: Using a custom type / Refactor
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-output-ef8ec6d6]] - next source section: Using a custom type / Write the minimal amount of code for the test to run and check output

## Statements

- We have a great way to search the dictionary. However, we have no way to add new words to our dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00596))_
- In this test, we are utilizing our Search function to make the validation of the dictionary a little easier. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00598))_

## Technical atoms

### Technical frame 1: Using a custom type / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00598))_

> In this test, we are utilizing our Search function to make the validation of the dictionary a little easier.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00597))_

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
