---
page_id: coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-618028a3
page_kind: source
summary: Pointers, copies, et al / Write enough code to make it pass: 5 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-enough-code-to-make-it-pass-618028a3@fb77a3a185603444e8fd26d6091aadb0
---

# Pointers, copies, et al / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-36483230]] - broader source section: Pointers, copies, et al
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-tes-7802db7d]] - previous source section: Pointers, copies, et al / Write minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-pointers-copies-et-al-write-the-test-first-9d6f8acb]] - next source section: Pointers, copies, et al / Write the test first

## Statements

- We already saw how to do this when we fixed the issue with Add . So let's implement something really similar to Add . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00651))_
- There is no refactoring we need to do on this since it was a simple change. However, we now have the same issue as with Add . If we pass in a new word, Update will add it to the dictionary. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_

## Technical atoms

### Technical frame 1: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_

> There is no refactoring we need to do on this since it was a simple change. However, we now have the same issue as with Add . If we pass in a new word, Update will add it to the dictionary.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00652))_

```
func (d Dictionary) Update(word, definition string) {
    d[word] = definition
}
```

### Technical frame 2: Pointers, copies, et al / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00651))_

> We already saw how to do this when we fixed the issue with Add . So let's implement something really similar to Add .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00653))_

> If we pass in a new word, Update will add it to the dictionary.
