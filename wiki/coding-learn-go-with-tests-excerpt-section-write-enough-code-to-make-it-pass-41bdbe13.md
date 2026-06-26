---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-41bdbe13
page_kind: source
summary: Write enough code to make it pass: 5 source-backed entries and 3 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-41bdbe13@9bb28a9065fbdbe92869e78b7f2b24a8
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- In the strictest sense of TDD we should now write the minimal amount of code to make the test pass . _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00182))_
- Once we're more familiar with Go's syntax I will introduce a technique called "Property Based Testing" , which would stop annoying developers and help you find bugs. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00186))_

## Technical atoms

```
func Add(x,	y	int)	int	{ return 4 }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00183))_

```
func Add(x,	y	int)	int	{ return x	+	y }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00188))_

> If you re-run the tests they should pass.
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00189))_
