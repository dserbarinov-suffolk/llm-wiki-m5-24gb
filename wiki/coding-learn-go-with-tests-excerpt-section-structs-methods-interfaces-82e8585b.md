---
page_id: coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b
page_kind: source
summary: Structs, methods & interfaces: 28 source-backed entries and 13 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b@a7ec76ee4b31a7dc927f6d635534fa3b
---

# Structs, methods & interfaces

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-cbb1567f]] - narrower source section: Structs, methods & interfaces / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-try-to-run-the-test-45f95e1a]] - narrower source section: Structs, methods & interfaces / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-fa-e190e01d]] - narrower source section: Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-enough-code-to-make-it-pass-075da993]] - narrower source section: Structs, methods & interfaces / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-refactor-d4181327]] - narrower source section: Structs, methods & interfaces / Refactor
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-test-first-5ffd50f2]] - narrower source section: Structs, methods & interfaces / Write the test first
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-try-to-run-the-test-fadb70be]] - narrower source section: Structs, methods & interfaces / Try to run the test
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-fa-44e30158]] - narrower source section: Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - previous source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-997bc0f7]] - next source section: What are methods?
- [[coding-learn-go-with-tests-excerpt-struct-method-interface]] - topic hub: opens the topic page for Struct Method Interface

## Statements

- Suppose that we need some geometry code to calculate the perimeter of a rectangle given a height and width. We can write a Perimeter(width float64, height float64) function, where float64 is for floating-point numbers like 123.45 . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00410))_

## Statements by subsection

### Structs, methods & interfaces / Write the test first

- Notice the new format string? The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_
- The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00414))_

### Structs, methods & interfaces / Write enough code to make it pass

- Try to do it yourself, following the TDD cycle. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

### Structs, methods & interfaces / Refactor

- Our code does the job, but it doesn't contain anything explicit about rectangles. An unwary developer might try to supply the width and height of a triangle to these functions without realising they will return the wrong answer. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00426))_
- We could just give the functions more specific names like RectangleArea . A neater solution is to define our own type called Rectangle which encapsulates this concept for us. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00427))_
- We can create a simple type using a struct . A struct is just a named collection of fields where you can store data. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00428))_
- Our next requirement is to write an Area function for circles. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00435))_

### Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output

- You can have functions with the same name declared in different packages . So we could create our Area(Circle) in a new package, but that feels overkill here. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00445))_
- We can define methods on our newly defined types instead. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00446))_

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

### Technical frame 2: Structs, methods & interfaces / Try to run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00416))_

```
./shapes_test.go:6:9: undefined: Perimeter
```

### Technical frame 3: Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00418))_

```
func Perimeter(width float64, height float64) float64 {
    return 0
}
Results in shapes_test.go:10: got 0.00 want 40.00.
```

### Technical frame 4: Structs, methods & interfaces / Write enough code to make it pass

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00422))_

> Try to do it yourself, following the TDD cycle.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00420))_

```
func Perimeter(width float64, height float64) float64 {
    return 2 * (width + height)
}
```

### Technical frame 5: Structs, methods & interfaces / Write enough code to make it pass

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

### Technical frame 6: Structs, methods & interfaces / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00435))_

> Our next requirement is to write an Area function for circles.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00430))_

```
type Rectangle struct {
    Width  float64
    Height float64
}
```

### Technical frame 7: Structs, methods & interfaces / Refactor

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

### Technical frame 8: Structs, methods & interfaces / Refactor

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

### Technical frame 9: Structs, methods & interfaces / Write the test first

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

### Technical frame 10: Structs, methods & interfaces / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00438))_

```
if got != want {
            t.Errorf("got %g want %g", got, want)
        }
    })
}
```

### Technical frame 11: Structs, methods & interfaces / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00439))_

> As you can see, the f has been replaced by g , with good reason. Use of g will print a more precise decimal number in the error message (fmt options). For example, using a radius of 1.5 in a circle area calculation, f would show 7.068583 whereas g would show 7.0685834705770345 .

### Technical frame 12: Structs, methods & interfaces / Try to run the test

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00441))_

```
./shapes_test.go:28:13: undefined: Circle
```

### Technical frame 13: Structs, methods & interfaces / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00445))_

> You can have functions with the same name declared in different packages . So we could create our Area(Circle) in a new package, but that feels overkill here.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00443))_

```
We need to deﬁne our Circle type.
type Circle struct {
    Radius float64
}
Now try to run the tests again
./shapes_test.go:29:14: cannot use circle (type Circle) as type 
Rectangle in argument to Area
Some programming languages allow you to do something like this:
func Area(circle Circle) float64       {}
func Area(rectangle Rectangle) float64 {}
But you cannot in Go
./shapes.go:20:32: Area redeclared in this block
```
