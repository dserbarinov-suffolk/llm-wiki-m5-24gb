---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-test-first-0df2234d
page_kind: source
summary: Arrays and slices / Write the test first: 5 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-slices-write-the-test-first-0df2234d@bec42402b8207085f69d3c6cfa0039c0
---

# Arrays and slices / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-648d683c]] - broader source section: Arrays and slices
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-slices-try-to-run-the-test-781534ae]] - next source section: Arrays and slices / Try to run the test

## Statements

- Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways: _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_
- It is sometimes useful to also print the inputs to the function in the error message. Here, we are using the %v placeholder to print the "default" format, which works well for arrays. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

## Technical atoms

### Technical frame 1: Arrays and slices / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00282))_

> Arrays have a fi xed capacity which you define when you declare the variable. We can initialize an array in two ways:

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00281))_

```
package main
import "testing"
func TestSum(t *testing.T) {
numbers := [5]int{1, 2, 3, 4, 5}
got := Sum(numbers)
    want := 15
if got != want {
        t.Errorf("got %d want %d given, %v", got, want, numbers)
    }
}
```

### Technical frame 2: Arrays and slices / Write the test first

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00285))_

> It is sometimes useful to also print the inputs to the function in the error message. Here, we are using the %v placeholder to print the "default" format, which works well for arrays.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00283))_

```
[N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 
3, 4, 5}
[...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2,
```
