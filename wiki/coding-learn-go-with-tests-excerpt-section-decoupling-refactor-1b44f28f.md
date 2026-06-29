---
page_id: coding-learn-go-with-tests-excerpt-section-decoupling-refactor-1b44f28f
page_kind: source
summary: Decoupling / Refactor: 5 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-decoupling-refactor-1b44f28f@7b82efdd746def86c0432a4886c4c9f4
---

# Decoupling / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3]] - broader source section: Decoupling
- [[coding-learn-go-with-tests-excerpt-section-decoupling-write-enough-code-to-make-it-pass-9ad411ad]] - previous source section: Decoupling / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-decoupling-make-sure-your-test-output-is-helpful-e3d11678]] - next source section: Decoupling / Make sure your test output is helpful
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- Again, the implementation is fine but our tests could do with some improvement. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00514))_
- It's not immediately clear what all the numbers represent and you should be aiming for your tests to be easily understood. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00517))_
- Now our tests - rather, the list of test cases - make assertions of truth about shapes and their areas. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00524))_

## Technical atoms

### Technical frame 1: Decoupling / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00517))_

> It's not immediately clear what all the numbers represent and you should be aiming for your tests to be easily understood.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00516))_

```
{Rectangle{12, 6}, 72.0},
{Circle{10}, 314.1592653589793},
{Triangle{12, 6}, 36.0},
```

### Technical frame 2: Decoupling / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00524))_

> Now our tests - rather, the list of test cases - make assertions of truth about shapes and their areas.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00520))_

```
{shape: Rectangle{Width: 12, Height: 6}, want: 72.0},
       {shape: Circle{Radius: 10}, want: 314.1592653589793},
       {shape: Triangle{Base: 12, Height: 6}, want: 36.0},
```
