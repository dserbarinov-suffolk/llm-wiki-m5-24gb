---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-c3c2298d
page_kind: source
summary: Refactor: 10 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-c3c2298d@012e83ff796341eb21fea9f02969c0b6
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- An unwary developer might try to supply the width and height of a triangle to these functions without realising they will return the wrong answer. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00426))_
- Our code does the job, but it doesn't contain anything explicit about rectangles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00426))_
- A neater solution is to define our own type called Rectangle which encapsulates this concept for us. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00427))_
- We could just give the functions more specific names like RectangleArea . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00427))_
- We can create a simple type using a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00428))_
- A struct is just a named collection of fields where you can store data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00428))_
- Our next requirement is to write an Area function for circles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00435))_

## Technical atoms

```
type Rectangle struct {
    Width  float64
    Height float64
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00430))_

```
func TestPerimeter(t *testing.T) {
    rectangle := Rectangle{10.0, 10.0}
    got := Perimeter(rectangle)
    want := 40.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
func TestArea(t *testing.T) {
    rectangle := Rectangle{12.0, 6.0}
    got := Area(rectangle)
    want := 72.0
if got != want {
        t.Errorf("got %.2f want %.2f", got, want)
    }
}
Remember to run your tests before attempting to ﬁx. The tests should
show a helpful error like
./shapes_test.go:7:18: not enough arguments in call to Perimeter
have (Rectangle)
   want (float64, float64)
You can access the ﬁelds of a struct with the syntax of myStruct.field.
Change the two functions to ﬁx the test.
func Perimeter(rectangle Rectangle) float64 {
    return 2 * (rectangle.Width + rectangle.Height)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00432))_

```
func Perimeter(rectangle Rectangle) float64 {
    return 2 * (rectangle.Width + rectangle.He
}
func Area(rectangle Rectangle) float64 {
    return rectangle.Width * rectangle.Height
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00433))_
