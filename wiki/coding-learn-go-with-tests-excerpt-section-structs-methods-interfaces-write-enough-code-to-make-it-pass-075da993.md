---
page_id: coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-enough-code-to-make-it-pass-075da993
page_kind: source
summary: Structs, methods & interfaces / Write enough code to make it pass: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-enough-code-to-make-it-pass-075da993@ba174841cb28bc03e926513a41b96062
---

# Structs, methods & interfaces / Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b]] - broader source section: Structs, methods & interfaces
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-fa-e190e01d]] - previous source section: Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-refactor-d4181327]] - next source section: Structs, methods & interfaces / Refactor

## Statements

- Try to do it yourself, following the TDD cycle. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

## Technical atoms

### Technical frame 1: Structs, methods & interfaces / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

> Try to do it yourself, following the TDD cycle.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00420))_

```
func Perimeter(width float64, height float64) float64 {
    return 2 * (width + height)
}
```

### Technical frame 2: Structs, methods & interfaces / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

> Try to do it yourself, following the TDD cycle.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00424))_

```
func TestPerimeter(t *testing.T) {
    got := Perimeter(10.0, 10.0)
    want := 40.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
func TestArea(t *testing.T) {
    got := Area(12.0, 6.0)
    want := 72.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
And code like this
func Perimeter(width float64, height float64) float64 {
    return 2 * (width + height)
}
func Area(width float64, height float64) float64 {
    return width * height
}
```
