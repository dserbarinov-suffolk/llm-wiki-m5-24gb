---
page_id: coding-learn-go-with-tests-excerpt-section-what-are-methods-write-enough-code-to-make-it-pass-43d2ca7f
page_kind: source
summary: What are methods? / Write enough code to make it pass: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-what-are-methods-write-enough-code-to-make-it-pass-43d2ca7f@1970f509a314c97394c29c753b798e7c
---

# What are methods? / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-997bc0f7]] - broader source section: What are methods?
- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-ace3f374]] - previous source section: What are methods? / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-refactor-1d16bf7b]] - next source section: What are methods? / Refactor

## Statements

- If you re-run the tests the rectangle tests should be passing but circle should still be failing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

## Technical atoms

### Technical frame 1: What are methods? / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

> If you re-run the tests the rectangle tests should be passing but circle should still be failing.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00465))_

```
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}
```

### Technical frame 2: What are methods? / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

> If you re-run the tests the rectangle tests should be passing but circle should still be failing.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00468))_

```
func (c Circle) Area() float64 {
    return math.Pi * c.Radius * c.Radius
}
```
