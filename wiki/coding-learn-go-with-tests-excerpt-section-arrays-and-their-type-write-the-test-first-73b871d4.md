---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-73b871d4
page_kind: source
summary: Arrays and their type / Write the test first: 3 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-73b871d4@6a99fc4386957f4f99309ef8fb11542a
---

# Arrays and their type / Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - broader source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-try-and-run-the-test-19f0372e]] - next source section: Arrays and their type / Try and run the test

## Technical atoms

### Technical frame 1: Arrays and their type / Write the test first

**Atoms:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00309, source-range-cb73a893-00311))_

> mySlice := []int{1,2,3}

> myArray := [3]int{1,2,3}

### Technical frame 2: Arrays and their type / Write the test first

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00312))_

```
func TestSum(t *testing.T) {
t.Run("collection of 5 numbers", func(t *testing.T) {
        numbers := [5]int{1, 2, 3, 4, 5}
got := Sum(numbers)
        want := 15
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
t.Run("collection of any size", func(t *testing.T) {
        numbers := []int{1, 2, 3}
got := Sum(numbers)
        want := 6
if got != want {
            t.Errorf("got %d want %d given, %v", got, want, numbers)
        }
    })
}
```
