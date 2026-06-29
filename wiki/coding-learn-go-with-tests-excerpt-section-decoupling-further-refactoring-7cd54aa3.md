---
page_id: coding-learn-go-with-tests-excerpt-section-decoupling-further-refactoring-7cd54aa3
page_kind: source
summary: Decoupling / Further refactoring: 14 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-decoupling-further-refactoring-7cd54aa3@0d78473f8b0b4e56978931069ce9dac0
---

# Decoupling / Further refactoring

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-decoupling-1c6183b3]] - broader source section: Decoupling
- [[coding-learn-go-with-tests-excerpt-section-decoupling-write-the-test-first-05e88611]] - next source section: Decoupling / Write the test first
- [[coding-learn-go-with-tests-excerpt-further-refactoring]] - topic hub: opens the topic page for Further Refactoring

## Statements

- Now that you have some understanding of structs we can introduce "table driven tests". _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00495))_
- The only new syntax here is creating an "anonymous struct", areaTests . We are declaring a slice of structs by using []struct with two fields, the shape and the want . Then we fill the slice with cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- Table driven tests can be a great item in your toolbox, but be sure that you have a need for the extra noise in the tests. They are a great fit when you wish to test various implementations of an interface, or if the data being passed in to a function has lots of different requirements that need testing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00501))_
- The only new syntax here is creating an "anonymous struct", areaTests . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- Then we fill the slice with cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00498))_
- We then iterate over them just like we do any other slice, using the struct fields to run our tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00499))_
- In addition, if a bug is found with Area it is very easy to add a new test case to exercise it before fixing it. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_
- You can see how it would be very easy for a developer to introduce a new shape, implement Area and then add it to the test cases. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00500))_

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
