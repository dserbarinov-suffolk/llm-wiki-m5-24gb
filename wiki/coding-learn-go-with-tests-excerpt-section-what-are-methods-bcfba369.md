---
page_id: coding-learn-go-with-tests-excerpt-section-what-are-methods-bcfba369
page_kind: source
summary: What are methods?: 8 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-what-are-methods-bcfba369@9ea49d84a2243d336ea7b83135101f69
---

# What are methods?

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- When we call t.Errorf we are calling the method Errorf on the instance of our t ( testing.T ). _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00448))_
- So far we have only been writing functions but we have been using some methods. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00448))_
- So far we have only been writing functions but we have been using some methods. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00448))_
- Where you can just call functions wherever you like, such as Area(rectangle) you can only call methods on "things". _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00450))_
- Where you can just call functions wherever you like, such as Area(rectangle) you can only call methods on "things". _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00450))_
- It is so important to take the time to slowly read the error messages you get, it will help you in the long run. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00453))_
- I would like to reiterate how great the compiler is here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00453))_

## Technical atoms

```
func TestArea(t *testing.T) {
t.Run("rectangles", func(t *testing.T) {
        rectangle := Rectangle{12, 6}
        got := rectangle.Area()
        want := 72.0
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
t.Run("circles", func(t *testing.T) {
        circle := Circle{10}
        got := circle.Area()
        want := 314.1592653589793
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
}
If we try to run the tests, we get
./shapes_test.go:19:19: rectangle.Area undefined (type Rectangle has 
no field or method Area)
./shapes_test.go:29:16: circle.Area undefined (type Circle has no 
field or method Area)
type Circle has no ﬁeld or method Area
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00452))_
