---
page_id: coding-learn-go-with-tests-excerpt-section-what-are-methods-997bc0f7
page_kind: source
summary: What are methods?: 37 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
page_family: section-reference
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-30
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-what-are-methods-997bc0f7@a51ad88597f8e53c737748562a44d7c0
---

# What are methods?

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-failing-test-ace3f374]] - narrower source section: What are methods? / Write the minimal amount of code for the test to run and check the failing test output
- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-write-enough-code-to-make-it-pass-43d2ca7f]] - narrower source section: What are methods? / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-what-are-methods-refactor-1d16bf7b]] - narrower source section: What are methods? / Refactor
- [[coding-learn-go-with-tests-excerpt-section-structs-methods-interfaces-82e8585b]] - previous source section: Structs, methods & interfaces
- [[coding-learn-go-with-tests-excerpt-section-wait-what-eaeaeb8b]] - next source section: Wait, what?

## Statements

- So far we have only been writing functions but we have been using some methods. When we call t.Errorf we are calling the method Errorf on the instance of our t ( testing.T ). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00448))_
- Methods are very similar to functions but they are called by invoking them on an instance of a particular type. Where you can just call functions wherever you like, such as Area(rectangle) you can only call methods on "things". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00450))_
- I would like to reiterate how great the compiler is here. It is so important to take the time to slowly read the error messages you get, it will help you in the long run. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00453))_
- So far we have only been writing functions but we have been using some methods. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00448))_
- Where you can just call functions wherever you like, such as Area(rectangle) you can only call methods on "things". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00450))_

## Statements by subsection

### What are methods? / Write the minimal amount of code for the test to run and check the failing test output

- The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_
- When your method is called on a variable of that type, you get your reference to its data via the receiverName variable. In many other programming languages this is done implicitly and you access the receiver via this . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00459))_
- It is a convention in Go to have the receiver variable be the first letter of the type. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00460))_
- The syntax for declaring methods is almost the same as functions and that's because they're so similar. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_
- The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_

### What are methods? / Write enough code to make it pass

- If you re-run the tests the rectangle tests should be passing but circle should still be failing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00466))_

### What are methods? / Refactor

- There is some duplication in our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00470))_
- All we want to do is take a collection of shapes , call the Area() method on them and then check the result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00471))_
- We want to be able to write some kind of checkArea function that we can pass both Rectangle s and Circle s to, but fail to compile if we try to pass in something that isn't a shape. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00472))_
- With Go, we can codify this intent with interfaces . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00473))_
- Interfaces are a very powerful concept in statically typed languages like Go because they allow you to make functions that can be used with different types and create highly-decoupled code whilst still maintaining type-safety. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00474))_
- We are creating a helper function like we have in other exercises but this time we are asking for a Shape to be passed in. If we try to call this with something that isn't a shape, then it will not compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00478))_
- We're creating a new type just like we did with Rectangle and Circle but this time it is an interface rather than a struct . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00481))_
- Once you add this to the code, the tests will pass. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00482))_
- All we want to do is take a collection of shapes , call the Area() method on them and then check the result. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00471))_
- Interfaces are a very powerful concept in statically typed languages like Go because they allow you to make functions that can be used with different types and create highly-decoupled code whilst still maintaining type-safety. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00474))_
- If we try to call this with something that isn't a shape, then it will not compile. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00478))_

## Technical atoms

### Technical frame 1: What are methods?

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00453))_

> I would like to reiterate how great the compiler is here. It is so important to take the time to slowly read the error messages you get, it will help you in the long run.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00452))_

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

### Technical frame 2: What are methods? / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_

> The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00456))_

```
type Rectangle struct {
    Width  float64
    Height float64
}
func (r Rectangle) Area() float64 {
    return 0
}
type Circle struct {
    Radius float64
```

### Technical frame 3: What are methods? / Write the minimal amount of code for the test to run and check the failing test output

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00458))_

> The syntax for declaring methods is almost the same as functions and that's because they're so similar. The only difference is the syntax of the method receiver func (receiverName ReceiverType) MethodName(args) .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00457))_

```
}
func (c Circle) Area() float64 {
    return 0
}
```
