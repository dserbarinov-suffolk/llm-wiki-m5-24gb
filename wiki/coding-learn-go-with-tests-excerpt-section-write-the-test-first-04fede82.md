---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-04fede82
page_kind: source
summary: Write the test first: 3 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-04fede82@b9468224ff1841226c90f56dd0fc3f0e
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00414))_
- The f is for our float64 and the .2 means print 2 decimal places. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00414))_

## Technical atoms

```
func TestPerimeter(t	*testing.T)	{ got	:=	Perimeter(10.0,	10.0) want	:=	40.0 if got	!=	want	{ t.Errorf("got	%.2f	want	%.2f",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00413))_
