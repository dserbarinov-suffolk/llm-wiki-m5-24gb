---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-16d67d9f
page_kind: source
summary: Write enough code to make it pass: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-16d67d9f@98b147689864ac18217d8e55d3a9918a
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- If you re-run the tests the rectangle tests should be passing but circle should still be failing. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00466))_

## Technical atoms

```
func (r	Rectangle)	Area()	float64	{ return r.Width	*	r.Height }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00465))_

```
func (c	Circle)	Area()	float64	{ return math.Pi	*	c.Radius	*	c.Radius }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00468))_
