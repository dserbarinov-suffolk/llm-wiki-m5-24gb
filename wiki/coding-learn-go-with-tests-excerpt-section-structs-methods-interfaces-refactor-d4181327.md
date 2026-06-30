---
page_id: coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-refactor-d4181327
page_kind: source
summary: Structs, methods & interfaces / Refactor: 10 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-refactor-d4181327@2a2561b1ddfd5058e974a99d0cb97eea
---

# Structs, methods & interfaces / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b]] - broader source section: Structs, methods & interfaces
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-enough-code-to-make-it-pass-075da993]] - previous source section: Structs, methods & interfaces / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-5ffd50f2]] - next source section: Structs, methods & interfaces / Write the test first
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- Our code does the job, but it doesn't contain anything explicit about rectangles. An unwary developer might try to supply the width and height of a triangle to these functions without realising they will return the wrong answer. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00426))_
- We could just give the functions more specific names like RectangleArea . A neater solution is to define our own type called Rectangle which encapsulates this concept for us. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00427))_
- We can create a simple type using a struct . A struct is just a named collection of fields where you can store data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00428))_
- Our next requirement is to write an Area function for circles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00435))_

## Technical atoms

### Technical frame 1: Structs, methods & interfaces / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00435))_

> Our next requirement is to write an Area function for circles.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00432))_

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

### Technical frame 2: Structs, methods & interfaces / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00435))_

> Our next requirement is to write an Area function for circles.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00433))_

```
func Perimeter(rectangle Rectangle) float64 {
    return 2 * (rectangle.Width + rectangle.He
}
func Area(rectangle Rectangle) float64 {
    return rectangle.Width * rectangle.Height
}
```
