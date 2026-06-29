---
page_id: coding-learn-go-with-tests-excerpt-section-maps-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-dbf2203c
page_kind: source
summary: Maps / Write the minimal amount of code for the test to run and check the output: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-maps-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-dbf2203c@81a1421d9681fa6fd365128fc21295e1
---

# Maps / Write the minimal amount of code for the test to run and check the output

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-maps-198341ba]] - broader source section: Maps
- [[coding-learn-go-with-tests-excerpt-section-maps-try-to-run-the-test-74951c57]] - previous source section: Maps / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-maps-write-enough-code-to-make-it-pass-e76e129f]] - next source section: Maps / Write enough code to make it pass

## Technical atoms

### Technical frame 1: Maps / Write the minimal amount of code for the test to run and check the output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00559))_

```
In dictionary.go
package main
func Search(dictionary map[string]string, word string) string {
    return ""
}
Your test should now fail with a clear error message
dictionary_test.go:12: got '' want 'this is just a test' given, 
'test'.
```
