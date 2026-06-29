---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-1446fc86
page_kind: source
summary: Arrays and their type / Refactor: 8 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-1446fc86@38dda7f5563d0e7bc1f64cd4f6386eaf
---

# Arrays and their type / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - broader source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-e71e4d2b]] - previous source section: Arrays and their type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-wrapping-up-53597979]] - next source section: Arrays and their type / Wrapping up
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- We could've created a new function checkSums like we normally do, but in this case, we're showing a new technique, assigning a function to a variable. It might look strange but, it's no different to assigning a variable to a string , or an int , functions in effect are values too. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00389))_
- It's not shown here, but this technique can be useful when you want to bind a function to other local variables in "scope" (e.g between some {} ). It also allows you to reduce the surface area of your API. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00390))_
- By defining this function inside the test, it cannot be used by other functions in this package. Hiding variables and functions that don't need to be exported is an important design consideration. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00391))_
- A handy side-effect of this is this adds a little type-safety to our code. If a developer mistakenly adds a new test with checkSums(t, got, "dave") the compiler will stop them in their tracks. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00392))_

## Technical atoms

### Technical frame 1: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00389))_

> We could've created a new function checkSums like we normally do, but in this case, we're showing a new technique, assigning a function to a variable. It might look strange but, it's no different to assigning a variable to a string , or an int , functions in effect are values too.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00388))_

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

### Technical frame 2: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00392))_

> A handy side-effect of this is this adds a little type-safety to our code. If a developer mistakenly adds a new test with checkSums(t, got, "dave") the compiler will stop them in their tracks.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00393))_

```
$ go test
./sum_test.go:52:21: cannot use "dave" (type string) as type []int 
in argument to checkSums
```
