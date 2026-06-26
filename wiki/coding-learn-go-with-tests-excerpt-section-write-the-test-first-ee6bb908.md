---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-ee6bb908
page_kind: source
summary: Write the test first: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-ee6bb908@0911776b6e6af9c21f9d80034220f7a3
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

```
func TestSumAllTails(t	*testing.T)	{ t.Run("make	the	sums	of	some	slices", func (t	*testing.T)	{ got	:=	SumAllTails([]int{1,	2},	[]int{0,	9}) want	:=	[]int{2,	9} if !reflect.DeepEqual(got,	want)	{ t.Errorf("got	%v	want	%v",	got,	want) } }) t.Run("safely	sum	empty	slices", func (t	*testing.T)	{ got	:=	SumAllTails([]int{},	[]int{3,	4,	5}) want	:=	[]int{0,	9} if !reflect.DeepEqual(got,	want)	{ t.Errorf("got	%v	want	%v",	got,	want) } }) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00379))_
