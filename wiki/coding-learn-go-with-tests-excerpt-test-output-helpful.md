---
page_id: coding-learn-go-with-tests-excerpt-test-output-helpful
page_kind: concept
summary: Make sure your test output is helpful: 9 statement(s) and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: concepts
projection_coverage: topic-coding-learn-go-with-tests-excerpt-test-output-helpful@88b8f649cfa810d6017e6eff125c5c9b
---

# Make sure your test output is helpful

What [[coding-learn-go-with-tests-excerpt]] covers about make sure your test output is helpful:

## Statements

- It printed shapes_test.go:31: got 0.00 want 36.00 . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00526))_
- We knew this was in relation to Triangle because we were just working with it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00527))_
- This is not a great experience for the developer, they will have to manually look through the cases to find out which case actually failed. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00527))_
- The %#v format string will print out our struct with the values in its field, so the developer can see at a glance the properties that are being tested. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00528))_
- We can change our error message into %#v got %g want %g . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00528))_
- To increase the readability of our test cases further, we can rename the want field into something more descriptive like hasArea . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00529))_
- One final tip with table driven tests is to use t.Run and to name the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00530))_
- By wrapping each case in a t.Run you will have clearer test output on failures as it will print the name of the case _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00531))_
- And you can run specific tests within your table with go test -run TestArea/Rectangle . _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00533))_

## Technical atoms

> Context: One final tip with table driven tests is to use t.Run and to name the test cases.
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00530))_

```
--- FAIL: TestArea (0.00s)
--- FAIL: TestArea/Rectangle (0.00s)
       shapes_test.go:33: main.Rectangle{Width:12, Height:6} got 
72.00 want 72.10
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00532))_

> Context: And you can run specific tests within your table with go test -run TestArea/Rectangle .
_(context: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00533))_

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
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00535))_


## Source

- [[coding-learn-go-with-tests-excerpt]]
