---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-3aa3907e
page_kind: source
summary: Refactor: 17 source-backed entries and 7 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-3aa3907e@a68d78b87bafc8e34f71f566a2a843f9
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Remember that we must not neglect our test code in the refactoring stage - we can further improve our Sum tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00325))_
- Having too many tests can turn in to a real problem and it just adds more overhead in maintenance. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00327))_
- It is important to question the value of your tests. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00327))_
- Every test has a cost . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00327))_
- In our case, you can see that having two tests for this function is redundant. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00328))_
- If it works for a slice of one size it's very likely it'll work for a slice of any size (within reason). _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00328))_
- If you have been strict with TDD, it's quite likely you'll have close to 100% coverage anyway. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00329))_
- Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00333))_
- Now that we are happy we have a well-tested function you should commit your great work before taking on the next challenge. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00333))_
- We need a new function called SumAll which will take a varying number of slices, returning a new slice containing the totals for each slice passed in. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00334))_

## Technical atoms

> We already refactored Sum - all we did was replace arrays with slices, so no extra changes are required.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00325))_

```
func TestSum(t	*testing.T)	{ t.Run("collection	of	5	numbers", func (t	*testing.T)	{ numbers	:=	[]int{1,	2,	3,	4,	5} got	:=	Sum(numbers) want	:=	15 if got	!=	want	{ t.Errorf("got	%d	want	%d	given,	%v",	got,	want,	numbers) } }) t.Run("collection	of	any	size", func (t	*testing.T)	{ numbers	:=	[]int{1,	2,	3} got	:=	Sum(numbers) want	:=	6 if got	!=	want	{ t.Errorf("got	%d	want	%d	given,	%v",	got,	want,	numbers) } }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00326))_

> It should not be a goal to have as many tests as possible, but rather to have as much confidence as possible in your code base.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00327))_

> Whilst striving for 100% coverage should not be your end goal, the coverage tool can help identify areas of your code not covered by tests.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00329))_

```
Try	running go	test	-cover You	should	see
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00330))_

```
PASS coverage:	100.0%	of	statements
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00331))_

```
SumAll([]int{1,2},	[]int{0,9}) would	return []int{3,	9} or SumAll([]int{1,1,1}) would	return []int{3}
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00336))_
