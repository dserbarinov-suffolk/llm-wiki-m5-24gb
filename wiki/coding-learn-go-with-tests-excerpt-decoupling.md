---
page_id: coding-learn-go-with-tests-excerpt-decoupling
page_kind: concept
summary: Decoupling: 33 statement(s) and 10 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-decoupling@42d36d340531dc80f04b263712eab2e9
---

# Decoupling

What [[coding-learn-go-with-tests-excerpt]] covers about decoupling:

## Statements

### Decoupling

- Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . By declaring an interface, the helper is decoupled from the concrete types and only has the method it needs to do its job. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00492))_

- This kind of approach of using interfaces to declare only what you need is very important in software design and will be covered in more detail in later sections. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00493))_

### Decoupling / Further refactoring

- Now that you have some understanding of structs we can introduce "table driven tests". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00495))_

- The only new syntax here is creating an "anonymous struct", areaTests . We are declaring a slice of structs by using []struct with two fields, the shape and the want . Then we fill the slice with cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_

- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_

- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_

- Table driven tests can be a great item in your toolbox, but be sure that you have a need for the extra noise in the tests. They are a great fit when you wish to test various implementations of an interface, or if the data being passed in to a function has lots of different requirements that need testing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00501))_

### Decoupling / Write the test first

- Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

### Decoupling / Refactor

- Again, the implementation is fine but our tests could do with some improvement. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00514))_

- It's not immediately clear what all the numbers represent and you should be aiming for your tests to be easily understood. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00517))_

- Now our tests - rather, the list of test cases - make assertions of truth about shapes and their areas. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00524))_

### Decoupling / Make sure your test output is helpful

- Remember earlier when we were implementing Triangle and we had the failing test? It printed shapes_test.go:31: got 0.00 want 36.00 . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00526))_

- We knew this was in relation to Triangle because we were just working with it. But what if a bug slipped in to the system in one of 20 cases in the table? How would a developer know which case failed? This is not a great experience for the developer, they will have to manually look through the cases to find out which case actually failed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00527))_

- We can change our error message into %#v got %g want %g . The %#v format string will print out our struct with the values in its field, so the developer can see at a glance the properties that are being tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00528))_

- To increase the readability of our test cases further, we can rename the want field into something more descriptive like hasArea . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00529))_

- One final tip with table driven tests is to use t.Run and to name the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00530))_

- By wrapping each case in a t.Run you will have clearer test output on failures as it will print the name of the case _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00531))_

- And you can run specific tests within your table with go test -run TestArea/Rectangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_

### Decoupling / Wrapping up

- This was more TDD practice, iterating over our solutions to basic mathematic problems and learning new language features motivated by our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00537))_

- Declaring structs to create your own data types which lets you bundle related data together and make the intent of your code clearer _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00538))_

- Adding methods so you can add functionality to your data types and so you can implement interfaces _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00540))_

- Table driven tests to make your assertions clearer and your test suites easier to extend & maintain _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00541))_

- This was an important chapter because we are now starting to define our own types. In statically typed languages like Go, being able to design your own types is essential for building software that is easy to understand, to piece together and to test. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00542))_

- Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was asserting on, only how to "ask" for its area. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00543))_

- As you become more familiar with Go you will start to see the real strength of interfaces and the standard library. You'll learn about interfaces defined in the standard library that are used everywhere and by implementing them against your own types, you can very quickly re-use a lot of great functionality. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00544))_


## Technical atoms

### Technical frame 1: Decoupling / Further refactoring

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_

> The only new syntax here is creating an "anonymous struct", areaTests . We are declaring a slice of structs by using []struct with two fields, the shape and the want . Then we fill the slice with cases.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00496))_

> Table driven tests are useful when you want to build a list of test cases that can be tested in the same manner.

### Technical frame 2: Decoupling / Further refactoring

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_

> The only new syntax here is creating an "anonymous struct", areaTests . We are declaring a slice of structs by using []struct with two fields, the shape and the want . Then we fill the slice with cases.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00497))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        shape Shape
        want  float64
    }{
        {Rectangle{12, 6}, 72.0},
        {Circle{10}, 314.1592653589793},
    }
for _, tt := range areaTests {
        got := tt.shape.Area()
        if got != tt.want {
            t.Errorf("got %g want %g", got, tt.want)
        }
    }
}
```

### Technical frame 3: Decoupling / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00504))_

> Adding a new test for our new shape is very easy. Just add {Triangle{12, 6}, 36.0}, to our list.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00505))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        shape Shape
        want  float64
```

### Technical frame 4: Decoupling / Write the test first

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

### Technical frame 5: Decoupling / Write the minimal amount of code for the test to run and check the failing test output

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00510))_

```
./shapes_test.go:25:4: undefined: Triangle
We have not deﬁned Triangle yet
type Triangle struct {
    Base   float64
    Height float64
}
Try again
./shapes_test.go:25:8: cannot use Triangle literal (type Triangle) 
as type Shape in field value:
Triangle does not implement Shape (missing Area method)
It's telling us we cannot use a Triangle as a shape because it does not
have an Area() method, so add an empty implementation to get the
test working
func (t Triangle) Area() float64 {
    return 0
}
Finally the code compiles and we get our error
shapes_test.go:31: got 0.00 want 36.00
```

### Technical frame 6: Decoupling / Write enough code to make it pass

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00512))_

```
func (t Triangle) Area() float64 {
    return (t.Base * t.Height) * 0.5
}
And our tests pass!
```

### Technical frame 7: Decoupling / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00517))_

> It's not immediately clear what all the numbers represent and you should be aiming for your tests to be easily understood.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00516))_

```
{Rectangle{12, 6}, 72.0},
{Circle{10}, 314.1592653589793},
{Triangle{12, 6}, 36.0},
```

### Technical frame 8: Decoupling / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00524))_

> Now our tests - rather, the list of test cases - make assertions of truth about shapes and their areas.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00520))_

```
{shape: Rectangle{Width: 12, Height: 6}, want: 72.0},
       {shape: Circle{Radius: 10}, want: 314.1592653589793},
       {shape: Triangle{Base: 12, Height: 6}, want: 36.0},
```

### Technical frame 9: Decoupling / Make sure your test output is helpful

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_

> And you can run specific tests within your table with go test -run TestArea/Rectangle .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00532))_

```
--- FAIL: TestArea (0.00s)
--- FAIL: TestArea/Rectangle (0.00s)
       shapes_test.go:33: main.Rectangle{Width:12, Height:6} got 
72.00 want 72.10
```

### Technical frame 10: Decoupling / Make sure your test output is helpful

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00533))_

> And you can run specific tests within your table with go test -run TestArea/Rectangle .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00535))_

```
func TestArea(t *testing.T) {
areaTests := []struct {
        name    string
        shape   Shape
        hasArea float64
    }{
        {name: "Rectangle", shape: Rectangle{Width: 12, Height: 6}, 
hasArea: 72.0},
{name: "Circle", shape: Circle{Radius: 10}, hasArea: 
314.1592653589793},
{name: "Triangle", shape: Triangle{Base: 12, Height: 6}, 
hasArea: 36.0},
}
for _, tt := range areaTests {
        // using tt.name from the case to use it as the `t.Run` test 
name
t.Run(tt.name, func(t *testing.T) {
            got := tt.shape.Area()
            if got != tt.hasArea {
                t.Errorf("%#v got %g want %g", tt.shape, got, 
tt.hasArea)
}
        })
}
}
```


## Related pages

- [[coding-learn-go-with-tests-excerpt-test]] - shared statements and technical atoms: Test shares source evidence from Decoupling / Further refactoring: Table driven tests can be a great item in your toolbox, but be sure that you have a need for the extra noise in the tests. They are a great fit when you wish to test ... [truncated]; Test shares technical record from Decoupling / Further refactoring: Table driven tests are useful when you want to build a list of test cases that can be tested in the same manner. (7 shared statement(s), 6 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-test-output-helpful]] - shared statements and technical atoms: Make sure your test output is helpful shares source evidence from Decoupling / Make sure your test output is helpful: Remember earlier when we were implementing Triangle and we had the failing test? It printed shapes_test.go:31: got 0.00 want 36.00 .; Make sure your test output is helpful shares technical record from Decoupling / Make sure your test output is helpful: --- FAIL: TestArea (0.00s) --- FAIL: TestArea/Rectangle (0.00s) shapes_test.go:33: main.Rectangle{Width:12, Height:6} got 72.00 want 72.10 (9 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-further-refactoring]] - shared statements and technical atoms: Further refactoring shares source evidence from Decoupling / Further refactoring: Now that you have some understanding of structs we can introduce "table driven tests".; Further refactoring shares technical record from Decoupling / Further refactoring: Table driven tests are useful when you want to build a list of test cases that can be tested in the same manner. (7 shared statement(s), 2 shared atom(s))
- [[coding-learn-go-with-tests-excerpt-code]] - shared statements: Code shares source evidence from Decoupling / Wrapping up: Interfaces are a great tool for hiding complexity away from other parts of the system. In our case our test helper code did not need to know the exact shape it was a ... [truncated] (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-type]] - shared statements: Type shares source evidence from Decoupling / Wrapping up: Declaring structs to create your own data types which lets you bundle related data together and make the intent of your code clearer (1 shared statement(s))
- [[coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3]] - source section: Decoupling shares source evidence from Decoupling: Notice how our helper does not need to concern itself with whether the shape is a Rectangle or a Circle or a Triangle . By declaring an interface, the helper is deco ... [truncated]; Decoupling shares technical record from Decoupling / Further refactoring: Table driven tests are useful when you want to build a list of test cases that can be tested in the same manner. (33 shared statement(s), 10 shared atom(s))

## Source

- [[coding-learn-go-with-tests-excerpt]]
