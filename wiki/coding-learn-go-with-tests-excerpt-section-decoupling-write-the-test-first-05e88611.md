---
page_id: coding-learn-go-with-tests-excerpt-section-decoupling-write-the-test-first-05e88611
page_kind: source
summary: Decoupling / Write the test first: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-decoupling-write-the-test-first-05e88611@debec1c8fc1aad480e5af60e8df94198
---

# Decoupling / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3]] - broader source section: Decoupling
- [[coding-learn-go-with-tests-excerpt-section-decoupling-further-refactoring-7cd54aa3]] - previous source section: Decoupling / Further refactoring

## Statements

- Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

## Technical atoms

### Technical frame 1: Decoupling / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

> Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00505))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        shape Shape
        want  float64
```

### Technical frame 2: Decoupling / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

> Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00506))_

```
}{
        {Rectangle{12, 6}, 72.0},
        {Circle{10}, 314.1592653589793},
        {Triangle{12, 6}, 36.0},
    }
for _, tt := range areaTests {
        got := tt.shape.Area()
        if got != tt.want {
            t.Errorf("got %g want %g", got, tt.want)
        }
    }
}
```
