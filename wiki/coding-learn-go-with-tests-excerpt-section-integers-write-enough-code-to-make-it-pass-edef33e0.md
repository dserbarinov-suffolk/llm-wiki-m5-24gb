---
page_id: coding-learn-go-with-tests-excerpt-section-integers-write-enough-code-to-make-it-pass-edef33e0
page_kind: source
summary: Integers / Write enough code to make it pass: 5 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-integers-write-enough-code-to-make-it-pass-edef33e0@2a541c30d5f47ea9c1f415eade577cdf
---

# Integers / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-integers-771ce4c7]] - broader source section: Integers
- [[coding-learn-go-with-tests-excerpt-section-integers-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-output-4c223d77]] - previous source section: Integers / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-integers-refactor-acc9e7fe]] - next source section: Integers / Refactor

## Statements

- In the strictest sense of TDD we should now write the minimal amount of code to make the test pass . A pedantic programmer may do this _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00182))_
- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

## Technical atoms

### Technical frame 1: Integers / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

> Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00183))_

```
func Add(x, y int) int {
    return 4
}
```

### Technical frame 2: Integers / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

> Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00188))_

```
func Add(x, y int) int {
    return x + y
}
```

### Technical frame 3: Integers / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00186))_

> Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00189))_

> If you re-run the tests they should pass.
