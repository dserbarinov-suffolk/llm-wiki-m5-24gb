---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-b13c8f45
page_kind: source
summary: Refactor: 15 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-b13c8f45@3b3afeee741ccde6060681a6be1139a0
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- There is some duplication in our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00470))_
- All we want to do is take a collection of shapes , call the Area() method on them and then check the result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00471))_
- All we want to do is take a collection of shapes , call the Area() method on them and then check the result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00471))_
- We want to be able to write some kind of checkArea function that we can pass both Rectangle s and Circle s to, but fail to compile if we try to pass in something that isn't a shape. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00472))_
- With Go, we can codify this intent with interfaces . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00473))_
- Interfaces are a very powerful concept in statically typed languages like Go because they allow you to make functions that can be used with different types and create highly-decoupled code whilst still maintaining type-safety. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00474))_
- Interfaces are a very powerful concept in statically typed languages like Go because they allow you to make functions that can be used with different types and create highly-decoupled code whilst still maintaining type-safety. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00474))_
- We are creating a helper function like we have in other exercises but this time we are asking for a Shape to be passed in. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00478))_
- If we try to call this with something that isn't a shape, then it will not compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00478))_
- If we try to call this with something that isn't a shape, then it will not compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00478))_
- We're creating a new type just like we did with Rectangle and Circle but this time it is an interface rather than a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00481))_
- Once you add this to the code, the tests will pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00482))_

## Technical atoms

```
func TestArea(t *testing.T) {
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00476))_

```
checkArea := func(t testing.TB, shape Shape, want float64) {
        t.Helper()
        got := shape.Area()
        if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    }
t.Run("rectangles", func(t *testing.T) {
        rectangle := Rectangle{12, 6}
        checkArea(t, rectangle, 72.0)
    })
t.Run("circles", func(t *testing.T) {
        circle := Circle{10}
        checkArea(t, circle, 314.1592653589793)
    })
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00477))_

```
type Shape interface {
    Area() float64
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00480))_
