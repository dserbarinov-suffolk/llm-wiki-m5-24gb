---
page_id: coding-learn-go-with-tests-excerpt-section-refactor-a767c259
page_kind: source
summary: Refactor: 2 source-backed entries and 1 atom(s) from raw/coding_learn_go_with_tests_excerpt.pdf.
sources: raw/coding_learn_go_with_tests_excerpt.pdf
updated: 2026-06-26
domain: coding-learn-go-with-tests-excerpt
category_path: sources/coding-learn-go-with-tests-excerpt/sections
source_id: coding_learn_go_with_tests_excerpt.pdf
projection_coverage: section-coding-learn-go-with-tests-excerpt-section-refactor-a767c259@fca965afafc115ec1b3a1916b24c248e
---

# Refactor

From [[coding-learn-go-with-tests-excerpt]].

## Statements

- I decided to create an assertStrings helper to make the implementation more general. _(coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00565))_

## Technical atoms

```
func TestSearch(t	*testing.T)	{ dictionary	:= map [string]string{"test":	"this	is	just	a	test"} got	:=	Search(dictionary,	"test") want	:=	"this	is	just	a	test" assertStrings(t,	got,	want) } func assertStrings(t	testing.TB,	got,	want	string)	{ t.Helper() if got	!=	want	{ t.Errorf("got	%q	want	%q",	got,	want) } }
```
_(source: coding_learn_go_with_tests_excerpt.pdf (source-range-559be4b1-00564))_
