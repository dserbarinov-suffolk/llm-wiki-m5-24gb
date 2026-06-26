---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-aebd5907
page_kind: source
summary: Refactor: 8 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-aebd5907@6015d2e04d2538118dee0cead4476cdc
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- We could've created a new function checkSums like we normally do, but in this case, we're showing a new technique, assigning a function to a variable. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00389))_
- It might look strange but, it's no different to assigning a variable to a string , or an int , functions in effect are values too. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00389))_
- It also allows you to reduce the surface area of your API. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00390))_
- Hiding variables and functions that don't need to be exported is an important design consideration. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00391))_
- A handy side-effect of this is this adds a little type-safety to our code. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00392))_
- If a developer mistakenly adds a new test with checkSums(t, got, "dave") the compiler will stop them in their tracks. _(coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00392))_

## Technical atoms

```
func TestSumAllTails(t *testing.T) {
checkSums := func(t testing.TB, got, want []int) {
        t.Helper()
        if !reflect.DeepEqual(got, want) {
            t.Errorf("got %v want %v", got, want)
        }
    }
t.Run("make the sums of tails of", func(t *testing.T) {
        got := SumAllTails([]int{1, 2}, []int{0, 9})
        want := []int{2, 9}
        checkSums(t, got, want)
    })
t.Run("safely sum empty slices", func(t *testing.T) {
        got := SumAllTails([]int{}, []int{3, 4, 5})
        want := []int{0, 9}
        checkSums(t, got, want)
    })
}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00388))_

```
$ go test
./sum_test.go:52:21: cannot use "dave" (type string) as type []int 
in argument to checkSums
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-f4b7154d-00393))_
