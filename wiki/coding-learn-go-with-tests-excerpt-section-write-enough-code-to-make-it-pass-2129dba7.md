---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-2129dba7
page_kind: source
summary: Write enough code to make it pass: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-2129dba7@39674a75469ffb3e0e230543168c66fd
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- To get the value out of an array at a particular index, just use array[index] syntax. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00297))_
- In this case, we are using for to iterate 5 times to work through the array and add each item onto sum . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00297))_

## Technical atoms

```
func Sum(numbers	[5]int)	int	{ sum	:=	0 for i	:=	0;	i	<	5;	i++	{ sum	+=	numbers[i] } return sum }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00296))_
