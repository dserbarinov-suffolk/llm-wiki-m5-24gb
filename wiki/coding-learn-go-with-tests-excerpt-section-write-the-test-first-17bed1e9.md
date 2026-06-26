---
page_id: coding-learn-go-with-tests-excerpt-section-write-the-test-first-17bed1e9
page_kind: source
summary: Write the test first: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-the-test-first-17bed1e9@1a5983f541fe0d16db9b739df7b71000
---

# Write the test first

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Adding a new test for our new shape is very easy. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00504))_

## Technical atoms

```
func TestArea(t	*testing.T)	{ areaTests	:=	[] struct { shape	Shape want		float64
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00505))_

```
}{ {Rectangle{12,	6},	72.0}, {Circle{10},	314.1592653589793}, {Triangle{12,	6},	36.0}, } for _,	tt	:= range areaTests	{ got	:=	tt.shape.Area() if got	!=	tt.want	{ t.Errorf("got	%g	want	%g",	got,	tt.want) } } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00506))_
