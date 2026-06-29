---
page_id: coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-0fbec14c
page_kind: source
summary: Using a custom type / Write enough code to make it pass: 4 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-enough-code-to-make-it-pass-0fbec14c@aef4f92a6c7a04698f97d4378e7ffaa0
---

# Using a custom type / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-3f6de7c1]] - broader source section: Using a custom type
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-96d1b867]] - previous source section: Using a custom type / Write the minimal amount of code for the test to run and check the output
- [[coding-learn-go-with-tests-excerpt-section-using-a-custom-type-refactor-862871b5]] - next source section: Using a custom type / Refactor

## Statements

- In order to make this pass, we are using an interesting property of the map lookup. It can return 2 values. The second value is a boolean which indicates if the key was found successfully. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_
- This property allows us to differentiate between a word that doesn't exist and a word that just doesn't have a definition. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00590))_

## Technical atoms

### Technical frame 1: Using a custom type / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00589))_

> In order to make this pass, we are using an interesting property of the map lookup. It can return 2 values. The second value is a boolean which indicates if the key was found successfully.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00588))_

```
func (d Dictionary) Search(word string) (string, error) {
    definition, ok := d[word]
    if !ok {
        return "", errors.New("could not find the word you were 
looking for")
}
return definition, nil
}
```
