---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-ba4b7ae7
page_kind: source
summary: Write the minimal amount of code for the test to run and check the failing test output: 11 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-minimal-amount-of-code-for-the-test-to-run-and-check-the-faili-ba4b7ae7@c7086caf11db99f619c768f8d7a3dd7a
---

# Write the minimal amount of code for the test to run and check the failing test output

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We need to define SumAll according to what our test wants. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00342))_
- Go can let you write variadic functions that can take a variable number of arguments. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00343))_
- This is valid, but our tests still won't compile! _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00345))_
- Go does not let you use equality operators with slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00347))_
- Note that this function expects the elements to be comparable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00348))_
- From Go 1.21, slices standard package is available, which has slices.Equal function to do a simple shallow compare on slices, where you don't need to worry about the types like the above case. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00348))_
- So, it can't be applied to slices with non-comparable elements like 2D slices. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00348))_
- You should have test output like the following: sum_test.go:30: got [] want [3 9] _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00351))_

## Technical atoms

```
func SumAll(numbersToSum ...[]int) []int {
    return nil
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00344))_

```
./sum_test.go:26:9: invalid operation: got != want (slice can only 
be compared to nil)
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00346))_

```
func TestSumAll(t *testing.T) {
got := SumAll([]int{1, 2}, []int{0, 9})
    want := []int{3, 9}
if !slices.Equal(got, want) {
        t.Errorf("got %v want %v", got, want)
    }
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00350))_
