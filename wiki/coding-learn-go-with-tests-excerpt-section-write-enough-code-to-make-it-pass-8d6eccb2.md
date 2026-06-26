---
page_id: coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-8d6eccb2
page_kind: source
summary: Write enough code to make it pass: 3 source-backed entries and 2 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-write-enough-code-to-make-it-pass-8d6eccb2@4bba79f7333a93059060c88c3a50e579
---

# Write enough code to make it pass

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- Try to do it yourself, following the TDD cycle. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00422))_

## Technical atoms

```
func Perimeter(width	float64,	height	float64)	float64	{ return 2	*	(width	+	height) }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00420))_

```
And	code	like	this func TestPerimeter(t	*testing.T)	{ got	:=	Perimeter(10.0,	10.0) want	:=	40.0 if got	!=	want	{ t.Errorf("got	%.2f	want	%.2f",	got,	want) } } func TestArea(t	*testing.T)	{ got	:=	Area(12.0,	6.0) want	:=	72.0 if got	!=	want	{ t.Errorf("got	%.2f	want	%.2f",	got,	want) } } func Perimeter(width	float64,	height	float64)	float64	{ return 2	*	(width	+	height) } func Area(width	float64,	height	float64)	float64	{ return width	*	height }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00424))_
