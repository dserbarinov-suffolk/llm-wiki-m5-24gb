---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-98b684c9
page_kind: source
summary: Write the test first: 3 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-98b684c9@b0afe07521b3303731f9e086829df706
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

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
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00437))_

```
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00438))_

> As you can see, the f has been replaced by g , with good reason. Use of g will print a more precise decimal number in the error message (fmt options). For example, using a radius of 1.5 in a circle area calculation, f would show 7.068583 whereas g would show 7.0685834705770345 .
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00439))_
