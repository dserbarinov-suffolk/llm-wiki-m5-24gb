---
page_id: coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-5ffd50f2
page_kind: source
summary: Structs, methods & interfaces / Write the test first: 3 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-5ffd50f2@0c6de3e374701680cd3e7467a20f0145
---

# Structs, methods & interfaces / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b]] - broader source section: Structs, methods & interfaces
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-refactor-d4181327]] - previous source section: Structs, methods & interfaces / Refactor
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-try-to-run-the-test-fadb70be]] - next source section: Structs, methods & interfaces / Try to run the test

## Technical atoms

### Technical frame 1: Structs, methods & interfaces / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00437))_

```
func TestArea(t *testing.T) {
t.Run("rectangles", func(t *testing.T) {
        rectangle := Rectangle{12, 6}
        got := Area(rectangle)
        want := 72.0
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
t.Run("circles", func(t *testing.T) {
        circle := Circle{10}
        got := Area(circle)
        want := 314.1592653589793
```

### Technical frame 2: Structs, methods & interfaces / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00438))_

```
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
}
```

### Technical frame 3: Structs, methods & interfaces / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00439))_

> As you can see, the f has been replaced by g , with good reason. Use of g will print a more precise decimal number in the error message (fmt options). For example, using a radius of 1.5 in a circle area calculation, f would show 7.068583 whereas g would show 7.0685834705770345 .
