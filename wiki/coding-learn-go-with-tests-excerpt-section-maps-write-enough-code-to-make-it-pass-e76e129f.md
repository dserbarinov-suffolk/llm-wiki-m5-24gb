---
page_id: coding-learn-go-with-tests-excerpt-section-maps-write-enough-code-to-make-it-pass-e76e129f
page_kind: source
summary: Maps / Write enough code to make it pass: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-maps-write-enough-code-to-make-it-pass-e76e129f@ad49ff84405018d10686953db11cf507
---

# Maps / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-maps-198341ba]] - broader source section: Maps
- [[coding-learn-go-with-tests-excerpt-section-maps-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-output-dbf2203c]] - previous source section: Maps / Write the minimal amount of code for the test to run and check the output
- [[coding-learn-go-with-tests-excerpt-section-maps-refactor-a6824beb]] - next source section: Maps / Refactor

## Statements

- Getting a value out of a Map is the same as getting a value out of Array map[key] . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00562))_

## Technical atoms

### Technical frame 1: Maps / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00562))_

> Getting a value out of a Map is the same as getting a value out of Array map[key] .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00561))_

```
func Search(dictionary map[string]string, word string) string {
    return dictionary[word]
}
```
