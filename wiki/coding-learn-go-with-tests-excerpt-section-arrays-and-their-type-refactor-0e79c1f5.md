---
page_id: coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-0e79c1f5
page_kind: source
summary: Arrays and their type / Refactor: 17 source-backed entries and 4 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-29
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-refactor-0e79c1f5@f5b512fcd6320a7127675e5f318ef62b
---

# Arrays and their type / Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Related pages

- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-0c35221e]] - broader source section: Arrays and their type
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-enough-code-to-make-it-pass-b28de2ad]] - previous source section: Arrays and their type / Write enough code to make it pass
- [[coding-learn-go-with-tests-excerpt-section-arrays-and-their-type-write-the-test-first-08e30bdd]] - next source section: Arrays and their type / Write the test first
- [[coding-learn-go-with-tests-excerpt-refactor]] - topic hub: opens the topic page for Refactor

## Statements

- We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required. Remember that we must not neglect our test code in the refactoring stage - we can further improve our Sum tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00325))_
- It is important to question the value of your tests. It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in your code base. Having too many tests can turn in to a real problem and it just adds more overhead in maintenance. Every test has a cost . _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_
- In our case, you can see that having two tests for this function is redundant. If it works for a slice of one size it's very likely it'll work for a slice of any size (within reason). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00328))_
- Go's built-in testing toolkit features a coverage tool. Whilst striving for 100% coverage should not be your end goal, the coverage tool can help identify areas of your code not covered by tests. If you have been strict with TDD, it's quite likely you'll have close to 100% coverage anyway. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00329))_
- Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_
- We need a new function called SumAll which will take a varying number of slices, returning a new slice containing the totals for each slice passed in. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00334))_
- If it works for a slice of one size it's very likely it'll work for a slice of any size (within reason). _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00328))_
- Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge. _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_

## Technical atoms

### Technical frame 1: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00327))_

> It is important to question the value of your tests. It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in your code base. Having too many tests can turn in to a real problem and it just adds more overhead in maintenance. Every test has a cost .

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00326))_

```
func TestSum(t *testing.T) {
t.Run("collection of 5 numbers", func(t *testing.T) {
        numbers := []int{1, 2, 3, 4, 5}
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

### Technical frame 2: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_

> Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00330))_

```
Try running
go test -cover
You should see
```

### Technical frame 3: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00333))_

> Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00331))_

```
PASS
coverage: 100.0% of statements
```

### Technical frame 4: Arrays and their type / Refactor

**Context:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00334))_

> We need a new function called SumAll which will take a varying number of slices, returning a new slice containing the totals for each slice passed in.

**Atom:** _(coding_learn_go_with_tests_excerpt.pdf (source-range-cb73a893-00336))_

```
SumAll([]int{1,2}, []int{0,9}) would return []int{3, 9}
or
SumAll([]int{1,1,1}) would return []int{3}
```
