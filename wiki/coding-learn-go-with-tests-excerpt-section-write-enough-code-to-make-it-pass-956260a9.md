---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-956260a9
page_kind: source
summary: Write enough code to make it pass: 1 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-956260a9@2c37f369d2d555eccc5b6880a0451896
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Technical atoms

```
func SumAllTails(numbersToSum	...[]int)	[]int	{ var sums	[]int for _,	numbers	:= range numbersToSum	{ if len(numbers)	==	0	{ sums	=	append(sums,	0) } else { tail	:=	numbers[1:] sums	=	append(sums,	Sum(tail)) } } return sums }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00385))_
