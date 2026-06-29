---
page_id: coding-learn-go-with-tests-excerpt-section-decoupling-write-enough-code-to-make-it-pass-9ad411ad
page_kind: source
summary: Decoupling / Write enough code to make it pass: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-decoupling-write-enough-code-to-make-it-pass-9ad411ad@5e7cc2df99a0aba5fc8bf918fc749eb3
---

# Decoupling / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3]] - broader source section: Decoupling
- [[coding-learn-go-with-tests-excerpt-section-decoupling-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-outpu-cfea595a]] - previous source section: Decoupling / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-decoupling-refactor-1b44f28f]] - next source section: Decoupling / Refactor

## Technical atoms

### Technical frame 1: Decoupling / Write enough code to make it pass

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00512))_

```
func (t Triangle) Area() float64 {
    return (t.Base * t.Height) * 0.5
}
And our tests pass!
```
