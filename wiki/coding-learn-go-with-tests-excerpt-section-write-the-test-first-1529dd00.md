---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-1529dd00
page_kind: source
summary: Write the test first: 3 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-1529dd00@796cf0da2e0db0e84a6089add5df5e55
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

> mySlice := []int{1,2,3}
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00309))_

> myArray := [3]int{1,2,3}
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00311))_

```
func TestSum(t	*testing.T)	{ t.Run("collection	of	5	numbers", func (t	*testing.T)	{ numbers	:=	[5]int{1,	2,	3,	4,	5} got	:=	Sum(numbers) want	:=	15 if got	!=	want	{ t.Errorf("got	%d	want	%d	given,	%v",	got,	want,	numbers) } }) t.Run("collection	of	any	size", func (t	*testing.T)	{ numbers	:=	[]int{1,	2,	3} got	:=	Sum(numbers) want	:=	6 if got	!=	want	{ t.Errorf("got	%d	want	%d	given,	%v",	got,	want,	numbers) } }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00312))_
