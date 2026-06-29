---
page_id: coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-cbb1567f
page_kind: source
summary: Structs, methods & interfaces / Write the test first: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-cbb1567f@249eb051e5eeaec1a9cf5215ed9ee9ef
---

# Structs, methods & interfaces / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b]] - broader source section: Structs, methods & interfaces
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-try-to-run-the-test-45f95e1a]] - next source section: Structs, methods & interfaces / Try to run the test

## Statements

- Notice the new format string? The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_
- The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_

## Technical atoms

### Technical frame 1: Structs, methods & interfaces / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_

> Notice the new format string? The f is for our float64 and the .2 means print 2 decimal places.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00413))_

```
func TestPerimeter(t *testing.T) {
    got := Perimeter(10.0, 10.0)
    want := 40.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
```
