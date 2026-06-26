---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-8416a524
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-8416a524@599841826d5b64374a67023c978eb491
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

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
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00510))_
